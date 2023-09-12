# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stop_hdr.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import video_pb2 as video__pb2
import extra_info_pb2 as extra__info__pb2
try:
  offset__state__pb2 = extra__info__pb2.offset__state__pb2
except AttributeError:
  offset__state__pb2 = extra__info__pb2.offset_state_pb2
try:
  window__crop__info__pb2 = extra__info__pb2.window__crop__info__pb2
except AttributeError:
  window__crop__info__pb2 = extra__info__pb2.window_crop_info_pb2

from video_pb2 import *
from extra_info_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='stop_hdr.proto',
  package='insta360.messages',
  syntax='proto3',
  serialized_options=b'\242\002\005INSPB',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0estop_hdr.proto\x12\x11insta360.messages\x1a\x0bvideo.proto\x1a\x10\x65xtra_info.proto\"C\n\x07StopHdr\x12\x38\n\x0e\x65xtra_metadata\x18\x01 \x01(\x0b\x32 .insta360.messages.ExtraMetadata\"6\n\x0bStopHdrResp\x12\'\n\x05video\x18\x01 \x01(\x0b\x32\x18.insta360.messages.VideoB\x08\xa2\x02\x05INSPBP\x00P\x01\x62\x06proto3'
  ,
  dependencies=[video__pb2.DESCRIPTOR,extra__info__pb2.DESCRIPTOR,],
  public_dependencies=[video__pb2.DESCRIPTOR,extra__info__pb2.DESCRIPTOR,])




_STOPHDR = _descriptor.Descriptor(
  name='StopHdr',
  full_name='insta360.messages.StopHdr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='extra_metadata', full_name='insta360.messages.StopHdr.extra_metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=68,
  serialized_end=135,
)


_STOPHDRRESP = _descriptor.Descriptor(
  name='StopHdrResp',
  full_name='insta360.messages.StopHdrResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='video', full_name='insta360.messages.StopHdrResp.video', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=137,
  serialized_end=191,
)

_STOPHDR.fields_by_name['extra_metadata'].message_type = extra__info__pb2._EXTRAMETADATA
_STOPHDRRESP.fields_by_name['video'].message_type = video__pb2._VIDEO
DESCRIPTOR.message_types_by_name['StopHdr'] = _STOPHDR
DESCRIPTOR.message_types_by_name['StopHdrResp'] = _STOPHDRRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StopHdr = _reflection.GeneratedProtocolMessageType('StopHdr', (_message.Message,), {
  'DESCRIPTOR' : _STOPHDR,
  '__module__' : 'stop_hdr_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.StopHdr)
  })
_sym_db.RegisterMessage(StopHdr)

StopHdrResp = _reflection.GeneratedProtocolMessageType('StopHdrResp', (_message.Message,), {
  'DESCRIPTOR' : _STOPHDRRESP,
  '__module__' : 'stop_hdr_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.StopHdrResp)
  })
_sym_db.RegisterMessage(StopHdrResp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)