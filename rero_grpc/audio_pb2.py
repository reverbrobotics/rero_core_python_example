# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='audio.proto',
  package='rero',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x61udio.proto\x12\x04rero\"\x7f\n\rStreamRequest\x12\x13\n\x0bsample_rate\x18\x01 \x01(\r\x12\x14\n\x0cnum_channels\x18\x02 \x01(\r\x12\x0e\n\x06\x66ormat\x18\x03 \x01(\t\x12\x19\n\x11\x66rames_per_buffer\x18\x04 \x01(\r\x12\x18\n\x10\x62ytes_per_sample\x18\x05 \x01(\r\"\x8e\x01\n\x05\x41udio\x12\x13\n\x0bnum_samples\x18\x01 \x01(\r\x12\x14\n\x0cnum_channels\x18\x02 \x01(\r\x12\x18\n\x10\x62ytes_per_sample\x18\x03 \x01(\r\x12\x19\n\x11\x66rames_per_buffer\x18\x04 \x01(\r\x12\x13\n\x0bsample_rate\x18\x05 \x01(\r\x12\x10\n\x08raw_data\x18\x06 \x01(\x0c\x32\x42\n\rAudioStreamer\x12\x31\n\tGetStream\x12\x13.rero.StreamRequest\x1a\x0b.rero.Audio\"\x00\x30\x01\x62\x06proto3'
)




_STREAMREQUEST = _descriptor.Descriptor(
  name='StreamRequest',
  full_name='rero.StreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate', full_name='rero.StreamRequest.sample_rate', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_channels', full_name='rero.StreamRequest.num_channels', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format', full_name='rero.StreamRequest.format', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frames_per_buffer', full_name='rero.StreamRequest.frames_per_buffer', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes_per_sample', full_name='rero.StreamRequest.bytes_per_sample', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=21,
  serialized_end=148,
)


_AUDIO = _descriptor.Descriptor(
  name='Audio',
  full_name='rero.Audio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_samples', full_name='rero.Audio.num_samples', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_channels', full_name='rero.Audio.num_channels', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes_per_sample', full_name='rero.Audio.bytes_per_sample', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frames_per_buffer', full_name='rero.Audio.frames_per_buffer', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_rate', full_name='rero.Audio.sample_rate', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='raw_data', full_name='rero.Audio.raw_data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=151,
  serialized_end=293,
)

DESCRIPTOR.message_types_by_name['StreamRequest'] = _STREAMREQUEST
DESCRIPTOR.message_types_by_name['Audio'] = _AUDIO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamRequest = _reflection.GeneratedProtocolMessageType('StreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMREQUEST,
  '__module__' : 'audio_pb2'
  # @@protoc_insertion_point(class_scope:rero.StreamRequest)
  })
_sym_db.RegisterMessage(StreamRequest)

Audio = _reflection.GeneratedProtocolMessageType('Audio', (_message.Message,), {
  'DESCRIPTOR' : _AUDIO,
  '__module__' : 'audio_pb2'
  # @@protoc_insertion_point(class_scope:rero.Audio)
  })
_sym_db.RegisterMessage(Audio)



_AUDIOSTREAMER = _descriptor.ServiceDescriptor(
  name='AudioStreamer',
  full_name='rero.AudioStreamer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=295,
  serialized_end=361,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStream',
    full_name='rero.AudioStreamer.GetStream',
    index=0,
    containing_service=None,
    input_type=_STREAMREQUEST,
    output_type=_AUDIO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUDIOSTREAMER)

DESCRIPTOR.services_by_name['AudioStreamer'] = _AUDIOSTREAMER

# @@protoc_insertion_point(module_scope)
