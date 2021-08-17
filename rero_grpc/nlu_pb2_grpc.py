# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import nlu_pb2 as nlu__pb2


class NLUStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSpeechIntent = channel.unary_unary(
                '/rero.NLU/GetSpeechIntent',
                request_serializer=nlu__pb2.NLURequest.SerializeToString,
                response_deserializer=nlu__pb2.Intent.FromString,
                )


class NLUServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSpeechIntent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NLUServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSpeechIntent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSpeechIntent,
                    request_deserializer=nlu__pb2.NLURequest.FromString,
                    response_serializer=nlu__pb2.Intent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rero.NLU', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NLU(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSpeechIntent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rero.NLU/GetSpeechIntent',
            nlu__pb2.NLURequest.SerializeToString,
            nlu__pb2.Intent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)