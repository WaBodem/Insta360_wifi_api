# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stop_timelapse.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import video_pb2 as video__pb2
import timelapse_pb2 as timelapse__pb2
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
from timelapse_pb2 import *
from extra_info_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='stop_timelapse.proto',
  package='insta360.messages',
  syntax='proto3',
  serialized_options=b'\242\002\005INSPB',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14stop_timelapse.proto\x12\x11insta360.messages\x1a\x0bvideo.proto\x1a\x0ftimelapse.proto\x1a\x10\x65xtra_info.proto\"y\n\rStopTimelapse\x12.\n\x04mode\x18\x01 \x01(\x0e\x32 .insta360.messages.TimelapseMode\x12\x38\n\x0e\x65xtra_metadata\x18\x02 \x01(\x0b\x32 .insta360.messages.ExtraMetadata\"<\n\x11StopTimelapseResp\x12\'\n\x05video\x18\x01 \x01(\x0b\x32\x18.insta360.messages.VideoB\x08\xa2\x02\x05INSPBP\x00P\x01P\x02\x62\x06proto3'
  ,
  dependencies=[video__pb2.DESCRIPTOR,timelapse__pb2.DESCRIPTOR,extra__info__pb2.DESCRIPTOR,],
  public_dependencies=[video__pb2.DESCRIPTOR,timelapse__pb2.DESCRIPTOR,extra__info__pb2.DESCRIPTOR,])




_STOPTIMELAPSE = _descriptor.Descriptor(
  name='StopTimelapse',
  full_name='insta360.messages.StopTimelapse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='insta360.messages.StopTimelapse.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_metadata', full_name='insta360.messages.StopTimelapse.extra_metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=91,
  serialized_end=212,
)


_STOPTIMELAPSERESP = _descriptor.Descriptor(
  name='StopTimelapseResp',
  full_name='insta360.messages.StopTimelapseResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='video', full_name='insta360.messages.StopTimelapseResp.video', index=0,
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
  serialized_start=214,
  serialized_end=274,
)

_STOPTIMELAPSE.fields_by_name['mode'].enum_type = timelapse__pb2._TIMELAPSEMODE
_STOPTIMELAPSE.fields_by_name['extra_metadata'].message_type = extra__info__pb2._EXTRAMETADATA
_STOPTIMELAPSERESP.fields_by_name['video'].message_type = video__pb2._VIDEO
DESCRIPTOR.message_types_by_name['StopTimelapse'] = _STOPTIMELAPSE
DESCRIPTOR.message_types_by_name['StopTimelapseResp'] = _STOPTIMELAPSERESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StopTimelapse = _reflection.GeneratedProtocolMessageType('StopTimelapse', (_message.Message,), {
  'DESCRIPTOR' : _STOPTIMELAPSE,
  '__module__' : 'stop_timelapse_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.StopTimelapse)
  })
_sym_db.RegisterMessage(StopTimelapse)

StopTimelapseResp = _reflection.GeneratedProtocolMessageType('StopTimelapseResp', (_message.Message,), {
  'DESCRIPTOR' : _STOPTIMELAPSERESP,
  '__module__' : 'stop_timelapse_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.StopTimelapseResp)
  })
_sym_db.RegisterMessage(StopTimelapseResp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)