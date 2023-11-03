import json
import time
import wave
import rero_grpc.audio_pb2 as audio
import rero_grpc.speech_recognition_pb2_grpc as sr_grpc
import grpc
import numpy as np

class AudioStreamer:
    def __init__(self, wav_filename, buffer_size=1024):
        self.wav_filename = wav_filename
        self.buffer_size = buffer_size
        self.wav_file = None
        self.is_end_of_stream = False

    #open wav file
    def open(self):
        self.wav_file = wave.open(self.wav_filename, 'rb')
        self.is_end_of_stream = False

    #close wav file
    def close(self):
        if self.wav_file:
            self.wav_file.close()

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_end_of_stream:
            raise StopIteration

        # Read and yield the raw audio data in chunks.
        raw_data = self.wav_file.readframes(self.frames_per_buffer)

        if not raw_data:
            raw_data = np.zeros(self.frames_per_buffer, dtype=np.int16).tobytes()

        # Create an Audio message
        audio_message = audio.Audio(
            num_samples=self.num_samples,
            num_channels=self.num_channels,
            bytes_per_sample=self.bytes_per_sample,
            frames_per_buffer=self.frames_per_buffer,
            sample_rate=self.sample_rate,
            raw_data=raw_data
        )

        time.sleep(0.064)

        return audio_message

    def initialize(self):
        # Open the WAV file.
        self.open()
        # Read parameters from the WAV file
        self.num_channels = self.wav_file.getnchannels()
        self.bytes_per_sample = self.wav_file.getsampwidth()
        self.sample_rate = self.wav_file.getframerate()
        self.num_frames = self.wav_file.getnframes()
        # Calculate number of samples
        self.num_samples = self.num_frames * self.num_channels
        # Initialize frames_per_buffer
        self.frames_per_buffer = self.buffer_size // (self.bytes_per_sample * self.num_channels)

    #basically useless as silence is streamed afterwards
    def has_leftover(self):
        return not self.is_end_of_stream

# Usage example:
def recognize_audio(streamer, stub):
    #start streamer
    streamer.initialize()

    # keep looping from where we left off
    while streamer.has_leftover():

        #recognize some text
        response = stub.RecognizeSpeech(streamer)

        #parse json result
        parsed_result = json.loads(response.result)

        # if we get silence as a result we are done
        if 'text' not in parsed_result or parsed_result['text'] == '':
            break

        #print result
        print("Speech Recognition Result: ", parsed_result['text'])

    streamer.close()

# Create a gRPC channel and stub
with grpc.insecure_channel('0.0.0.0:50052') as channel:
    stub = sr_grpc.SpeechRecognitionStub(channel)

    # Create an AudioStreamer instance
    streamer = AudioStreamer('/home/lukas/Desktop/jfk2.wav')

    # Start the recognition process
    recognize_audio(streamer, stub)
