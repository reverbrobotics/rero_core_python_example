# =========================================================================== #
# gRPC Server Speech Recognition Example
# =========================================================================== #
# Copyright(C) 2023 Reverb Robotics Inc.
# Author: Lukas Grasse
# Email:  lukas@reverbrobotics.ca
# =========================================================================== #

import json
import grpc
import rero_grpc.speech_recognition_pb2_grpc as sr_grpc
import rero_grpc.speech_recognition_pb2 as speech
from util.microphone import MicrophoneStream

# main method
def run():

    #create channel
    with grpc.insecure_channel('testserver.reverbrobotics.ca:50052') as channel:

        #audio settings
        sample_rate = 16000
        num_channels = 1
        frames_per_buffer = 1024
        bytes_per_sample = 2

        #open local microphone straem
        with MicrophoneStream(sample_rate, frames_per_buffer, num_channels, bytes_per_sample) as stream:

            #speech recognition stub
            sr_stub = sr_grpc.SpeechRecognitionStub(channel)

            #instantiate audio object generator
            generator = stream.generator()

            #set vocab to be default (change if using limited vocabulary)
            vocab = speech.Vocab()

            vocab.vocab = ""
            sr_stub.SetVocab(vocab)

            # stream results from generator to Speech Recognition until result is returned
            sr_result = sr_stub.RecognizeSpeech(generator)

            #parse json result
            parsed_result = json.loads(sr_result.result)

            #print result
            if 'text' in parsed_result:
                print("Speech Recognition Result: ", parsed_result['text'])
            else:
                print("Speech Recognition Result: ")

# check file is being run directly
if __name__ == '__main__':
    #run speech recognition
    run()
