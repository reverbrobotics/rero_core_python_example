# =========================================================================== #
# gRPC Text-to-Speech Example
# =========================================================================== #
# Copyright(C) 2021 Reverb Robotics Inc.
# Author: Lukas Grasse
# Email:  lukas@reverbrobotics.ca
# =========================================================================== #

import grpc
import rero_grpc.text_to_speech_pb2_grpc as tts_grpc
import rero_grpc.text_to_speech_pb2 as tts

# main method
def run():

    #create channel
    with grpc.insecure_channel('localhost:50052') as channel:
        #tts stub
        tts_stub = tts_grpc.TextToSpeechStub(channel)

        text = input("Please enter text to say and press enter: ")

        #create tts request
        tts_request = tts.TTSRequest(text=text)

        #send tts request
        tts_stub.TTS(tts_request)

# check file is being run directly
if __name__ == '__main__':
    #run tts
    run()
