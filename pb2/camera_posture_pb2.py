# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camera_posture.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='camera_posture.proto',
  package='insta360.messages',
  syntax='proto3',
  serialized_options=b'\242\002\005INSPB',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x63\x61mera_posture.proto\x12\x11insta360.messages\"\xbe\x02\n\x1fNotificationCameraPostureUpdate\x12\\\n\x0e\x63\x61mera_posture\x18\x01 \x01(\x0e\x32\x44.insta360.messages.NotificationCameraPostureUpdate.CameraPostureType\"\xbc\x01\n\x11\x43\x61meraPostureType\x12\x1b\n\x17\x43\x41MERA_POSTURE_ROTATE_0\x10\x00\x12\x1c\n\x18\x43\x41MERA_POSTURE_ROTATE_90\x10\x01\x12\x1d\n\x19\x43\x41MERA_POSTURE_ROTATE_180\x10\x02\x12\x1d\n\x19\x43\x41MERA_POSTURE_ROTATE_270\x10\x03\x12\x15\n\x11\x43\x41MERA_POSTURE_UP\x10\x04\x12\x17\n\x13\x43\x41MERA_POSTURE_DOWN\x10\x05\x42\x08\xa2\x02\x05INSPBb\x06proto3'
)



_NOTIFICATIONCAMERAPOSTUREUPDATE_CAMERAPOSTURETYPE = _descriptor.EnumDescriptor(
  name='CameraPostureType',
  full_name='insta360.messages.NotificationCameraPostureUpdate.CameraPostureType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CAMERA_POSTURE_ROTATE_0', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_POSTURE_ROTATE_90', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_POSTURE_ROTATE_180', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_POSTURE_ROTATE_270', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_POSTURE_UP', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_POSTURE_DOWN', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=174,
  serialized_end=362,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONCAMERAPOSTUREUPDATE_CAMERAPOSTURETYPE)


_NOTIFICATIONCAMERAPOSTUREUPDATE = _descriptor.Descriptor(
  name='NotificationCameraPostureUpdate',
  full_name='insta360.messages.NotificationCameraPostureUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='camera_posture', full_name='insta360.messages.NotificationCameraPostureUpdate.camera_posture', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NOTIFICATIONCAMERAPOSTUREUPDATE_CAMERAPOSTURETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=362,
)

_NOTIFICATIONCAMERAPOSTUREUPDATE.fields_by_name['camera_posture'].enum_type = _NOTIFICATIONCAMERAPOSTUREUPDATE_CAMERAPOSTURETYPE
_NOTIFICATIONCAMERAPOSTUREUPDATE_CAMERAPOSTURETYPE.containing_type = _NOTIFICATIONCAMERAPOSTUREUPDATE
DESCRIPTOR.message_types_by_name['NotificationCameraPostureUpdate'] = _NOTIFICATIONCAMERAPOSTUREUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotificationCameraPostureUpdate = _reflection.GeneratedProtocolMessageType('NotificationCameraPostureUpdate', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONCAMERAPOSTUREUPDATE,
  '__module__' : 'camera_posture_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.NotificationCameraPostureUpdate)
  })
_sym_db.RegisterMessage(NotificationCameraPostureUpdate)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)