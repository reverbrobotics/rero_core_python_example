# =========================================================================== #
# gRPC Speech Recognition Example
# =========================================================================== #
# Copyright(C) 2021 Reverb Robotics Inc.
# Author: Lukas Grasse
# Email:  lukas@reverbrobotics.ca
# =========================================================================== #

import json
import grpc
import rero_grpc.audio_pb2_grpc as audio_grpc
import rero_grpc.audio_pb2 as audio
import rero_grpc.speech_recognition_pb2_grpc as sr_grpc

# main method
def run():

    #create channel
    with grpc.insecure_channel('localhost:50052') as channel:
        #audio stub
        audio_stub = audio_grpc.AudioStreamerStub(channel)

        #speech recognition stub
        sr_stub = sr_grpc.SpeechRecognitionStub(channel)

        #create audio request object
        request = audio.StreamRequest()

        #set audio params
        request.sample_rate = 16000
        request.num_channels = 1
        request.format = "paInt16"
        request.frames_per_buffer = 1024
        request.bytes_per_sample = 2

        #get speech recognition result synchronously (call sr_stub.RecognizeSpeech.future for asynchronous object)
        audio_stream = audio_stub.GetStream(request)
        sr_result = sr_stub.RecognizeSpeech(audio_stream)

        #parse json result
        parsed_result = json.loads(sr_result.result)

        #print result
        print("Speech Recognition Result: ", parsed_result['text'])

# check file is being run directly
if __name__ == '__main__':
    #run speech recognition
    run()
