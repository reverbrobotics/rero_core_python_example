# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import audio_pb2 as audio__pb2
from . import speech_recognition_pb2 as speech__recognition__pb2


class SpeechRecognitionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RecognizeSpeech = channel.stream_unary(
                '/rero.SpeechRecognition/RecognizeSpeech',
                request_serializer=audio__pb2.Audio.SerializeToString,
                response_deserializer=speech__recognition__pb2.SpeechRecognitionResult.FromString,
                )


class SpeechRecognitionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RecognizeSpeech(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpeechRecognitionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RecognizeSpeech': grpc.stream_unary_rpc_method_handler(
                    servicer.RecognizeSpeech,
                    request_deserializer=audio__pb2.Audio.FromString,
                    response_serializer=speech__recognition__pb2.SpeechRecognitionResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rero.SpeechRecognition', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SpeechRecognition(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RecognizeSpeech(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/rero.SpeechRecognition/RecognizeSpeech',
            audio__pb2.Audio.SerializeToString,
            speech__recognition__pb2.SpeechRecognitionResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
