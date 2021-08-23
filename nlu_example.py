# =========================================================================== #
# gRPC Speech Recognition with Natural Language Understanding Example
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
    with grpc.insecure_channel('localhost:50052') as channel:
        #audio stub
        audio_stub = audio_grpc.AudioStreamerStub(channel)

        #speech recognition stub
        sr_stub = sr_grpc.SpeechRecognitionStub(channel)

        #nlu stub
        nlu_stub = nlu_grpc.NLUStub(channel)

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

        #print sr result
        print("Speech Recognition Result: ", parsed_result['text'])
        print("")

        if parsed_result['text'] == '':
            return

        #create nlu request object
        nlu_request = nlu.NLURequest()
        nlu_request.request = parsed_result['text']

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
