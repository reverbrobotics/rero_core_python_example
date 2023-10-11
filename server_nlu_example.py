# =========================================================================== #
# gRPC Natural Language Understanding Example
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
import rero_grpc.nlu_pb2 as nlu
import rero_grpc.nlu_pb2_grpc as nlu_grpc

# main method
def run():

    #create channel
    with grpc.insecure_channel('testserver.reverbrobotics.ca:50052') as channel:

        #nlu stub
        nlu_stub = nlu_grpc.NLUStub(channel)

        nlu_input = input("Please enter a sentence: ")


        #create nlu request object
        nlu_request = nlu.NLURequest()
        nlu_request.request = nlu_input

        #get nlu result
        nlu_result = nlu_stub.GetSpeechIntent(nlu_request)

        #print nlu result
        print("NLU Intent: ", nlu_result.intentName)
        print("NLU Probability: ", nlu_result.probability)
        print(" ")
        for i, slot in enumerate(nlu_result.slots):
            print("NLU Slot {}: ".format(i))
            print("===============")
            print(slot)
            print("")


# check file is being run directly
if __name__ == '__main__':
    #run speech recognition and nlu
    run()
