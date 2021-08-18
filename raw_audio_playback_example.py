# =========================================================================== #
# gRPC Audio Playback Example
# =========================================================================== #
# Copyright(C) 2021 Reverb Robotics Inc.
# Author: Lukas Grasse
# Email:  lukas@reverbrobotics.ca
# =========================================================================== #

import grpc
import rero_grpc.audio_pb2_grpc as audio_grpc
import rero_grpc.audio_pb2 as audio
import pyaudio

# main method
def run():

    #create channel
    with grpc.insecure_channel('localhost:50052') as channel:
        #audio stub
        audio_stub = audio_grpc.AudioStreamerStub(channel)

        #create audio request object
        request = audio.StreamRequest()

        #set audio params
        request.sample_rate = 16000
        request.num_channels = 1
        request.format = "paInt16"
        request.frames_per_buffer = 1024
        request.bytes_per_sample = 2

        #number of seconds for playback
        num_seconds = 30

        #create pyaudio object
        p = pyaudio.PyAudio()

        #open stream
        stream = p.open(format=pyaudio.paInt16, channels=request.num_channels, rate=request.sample_rate, output=True)

        #play audio stream frames over system audio
        audio_stream = audio_stub.GetStream(request)
        for i, audio_frame in enumerate(audio_stream):

            #break if time limit exceeded
            if i > (num_seconds*request.sample_rate)//request.frames_per_buffer:
                break

            #write frame to stream
            stream.write(audio_frame.raw_data)

        #close stream and pyaudio device
        stream.stop_stream()
        stream.close()
        p.terminate()

# check file is being run directly
if __name__ == '__main__':
    #run audio playback
    run()
