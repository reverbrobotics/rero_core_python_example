# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: text_to_speech.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='text_to_speech.proto',
  package='rero',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14text_to_speech.proto\x12\x04rero\"\x1a\n\nTTSRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1d\n\x0bTTSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32<\n\x0cTextToSpeech\x12,\n\x03TTS\x12\x10.rero.TTSRequest\x1a\x11.rero.TTSResponse\"\x00\x62\x06proto3'
)




_TTSREQUEST = _descriptor.Descriptor(
  name='TTSRequest',
  full_name='rero.TTSRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='rero.TTSRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=56,
)


_TTSRESPONSE = _descriptor.Descriptor(
  name='TTSResponse',
  full_name='rero.TTSResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='rero.TTSResponse.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['TTSRequest'] = _TTSREQUEST
DESCRIPTOR.message_types_by_name['TTSResponse'] = _TTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TTSRequest = _reflection.GeneratedProtocolMessageType('TTSRequest', (_message.Message,), {
  'DESCRIPTOR' : _TTSREQUEST,
  '__module__' : 'text_to_speech_pb2'
  # @@protoc_insertion_point(class_scope:rero.TTSRequest)
  })
_sym_db.RegisterMessage(TTSRequest)

TTSResponse = _reflection.GeneratedProtocolMessageType('TTSResponse', (_message.Message,), {
  'DESCRIPTOR' : _TTSRESPONSE,
  '__module__' : 'text_to_speech_pb2'
  # @@protoc_insertion_point(class_scope:rero.TTSResponse)
  })
_sym_db.RegisterMessage(TTSResponse)



_TEXTTOSPEECH = _descriptor.ServiceDescriptor(
  name='TextToSpeech',
  full_name='rero.TextToSpeech',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=89,
  serialized_end=149,
  methods=[
  _descriptor.MethodDescriptor(
    name='TTS',
    full_name='rero.TextToSpeech.TTS',
    index=0,
    containing_service=None,
    input_type=_TTSREQUEST,
    output_type=_TTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXTTOSPEECH)

DESCRIPTOR.services_by_name['TextToSpeech'] = _TEXTTOSPEECH

# @@protoc_insertion_point(module_scope)
