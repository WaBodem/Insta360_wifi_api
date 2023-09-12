# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: battery_low.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import battery_pb2 as battery__pb2

from battery_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='battery_low.proto',
  package='insta360.messages',
  syntax='proto3',
  serialized_options=b'\242\002\005INSPB',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x62\x61ttery_low.proto\x12\x11insta360.messages\x1a\rbattery.proto\"R\n\x16NotificationBatteryLow\x12\x38\n\x0e\x62\x61ttery_status\x18\x01 \x01(\x0b\x32 .insta360.messages.BatteryStatusB\x08\xa2\x02\x05INSPBP\x00\x62\x06proto3'
  ,
  dependencies=[battery__pb2.DESCRIPTOR,],
  public_dependencies=[battery__pb2.DESCRIPTOR,])




_NOTIFICATIONBATTERYLOW = _descriptor.Descriptor(
  name='NotificationBatteryLow',
  full_name='insta360.messages.NotificationBatteryLow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='battery_status', full_name='insta360.messages.NotificationBatteryLow.battery_status', index=0,
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
  serialized_start=55,
  serialized_end=137,
)

_NOTIFICATIONBATTERYLOW.fields_by_name['battery_status'].message_type = battery__pb2._BATTERYSTATUS
DESCRIPTOR.message_types_by_name['NotificationBatteryLow'] = _NOTIFICATIONBATTERYLOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotificationBatteryLow = _reflection.GeneratedProtocolMessageType('NotificationBatteryLow', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONBATTERYLOW,
  '__module__' : 'battery_low_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.NotificationBatteryLow)
  })
_sym_db.RegisterMessage(NotificationBatteryLow)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)