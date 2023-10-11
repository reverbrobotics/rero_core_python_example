# =========================================================================== #
# gRPC Microphone Stream Class
# =========================================================================== #
# Copyright(C) 2023 Reverb Robotics Inc.
# Author: Lukas Grasse
# Email:  lukas@reverbrobotics.ca
# =========================================================================== #

# Microphone stream class adapted from: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/HEAD/speech/microphone/transcribe_streaming_mic.py
# Copyright 2017 Google LLC

import queue
import rero_grpc.audio_pb2_grpc as audio_grpc
import rero_grpc.audio_pb2 as audio
import pyaudio

class MicrophoneStream:
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self: object, rate: int = 16000, chunk: int = 1024, num_channels=1, bytes_per_sample=2) -> None:
        """The audio -- and generator -- is guaranteed to be on the main thread."""
        self._rate = rate
        self._chunk = chunk
        self._num_channels = num_channels
        self._bytes_per_sample = bytes_per_sample
        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self: object) -> object:
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=self._num_channels,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(
        self: object,
        type: object,
        value: object,
        traceback: object,
    ) -> None:
        """Closes the stream, regardless of whether the connection was lost or not."""
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(
        self: object,
        in_data: object,
        frame_count: int,
        time_info: object,
        status_flags: object,
    ) -> object:
        """Continuously collect data from the audio stream, into the buffer.

        Args:
            in_data: The audio data as a bytes object
            frame_count: The number of frames captured
            time_info: The time information
            status_flags: The status flags

        Returns:
            The audio data as a bytes object
        """
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self: object) -> object:
        """Generates audio chunks from the stream of audio data in chunks.

        Args:
            self: The MicrophoneStream object

        Returns:
            A generator that outputs audio chunks.
        """
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            raw_audio_bytes = b"".join(data)

            audio_object = audio.Audio()
            audio_object.num_samples = self._chunk
            audio_object.num_channels = self._num_channels
            audio_object.bytes_per_sample = self._bytes_per_sample
            audio_object.frames_per_buffer = self._chunk
            audio_object.sample_rate = self._rate
            audio_object.raw_data = raw_audio_bytes

            yield audio_object
