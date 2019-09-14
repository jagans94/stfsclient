# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stfsclient/tensorflow_serving/internal/get_model_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stfsclient.tensorflow_serving.internal import model_pb2 as stfsclient_dot_tensorflow__serving_dot_internal_dot_model__pb2
from stfsclient.tensorflow_serving.internal import status_pb2 as stfsclient_dot_tensorflow__serving_dot_internal_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stfsclient/tensorflow_serving/internal/get_model_status.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\n=stfsclient/tensorflow_serving/internal/get_model_status.proto\x12\x12tensorflow.serving\x1a\x32stfsclient/tensorflow_serving/internal/model.proto\x1a\x33stfsclient/tensorflow_serving/internal/status.proto\"J\n\x15GetModelStatusRequest\x12\x31\n\nmodel_spec\x18\x01 \x01(\x0b\x32\x1d.tensorflow.serving.ModelSpec\"\xe8\x01\n\x12ModelVersionStatus\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12;\n\x05state\x18\x02 \x01(\x0e\x32,.tensorflow.serving.ModelVersionStatus.State\x12/\n\x06status\x18\x03 \x01(\x0b\x32\x1f.tensorflow.serving.StatusProto\"S\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05START\x10\n\x12\x0b\n\x07LOADING\x10\x14\x12\r\n\tAVAILABLE\x10\x1e\x12\r\n\tUNLOADING\x10(\x12\x07\n\x03\x45ND\x10\x32\"t\n\x16GetModelStatusResponse\x12Z\n\x14model_version_status\x18\x01 \x03(\x0b\x32&.tensorflow.serving.ModelVersionStatusR\x14model_version_statusB\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[stfsclient_dot_tensorflow__serving_dot_internal_dot_model__pb2.DESCRIPTOR,stfsclient_dot_tensorflow__serving_dot_internal_dot_status__pb2.DESCRIPTOR,])



_MODELVERSIONSTATUS_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='tensorflow.serving.ModelVersionStatus.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=1, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOADING', index=2, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVAILABLE', index=3, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNLOADING', index=4, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=5, number=50,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=416,
  serialized_end=499,
)
_sym_db.RegisterEnumDescriptor(_MODELVERSIONSTATUS_STATE)


_GETMODELSTATUSREQUEST = _descriptor.Descriptor(
  name='GetModelStatusRequest',
  full_name='tensorflow.serving.GetModelStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_spec', full_name='tensorflow.serving.GetModelStatusRequest.model_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=190,
  serialized_end=264,
)


_MODELVERSIONSTATUS = _descriptor.Descriptor(
  name='ModelVersionStatus',
  full_name='tensorflow.serving.ModelVersionStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorflow.serving.ModelVersionStatus.version', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='tensorflow.serving.ModelVersionStatus.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='tensorflow.serving.ModelVersionStatus.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MODELVERSIONSTATUS_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=499,
)


_GETMODELSTATUSRESPONSE = _descriptor.Descriptor(
  name='GetModelStatusResponse',
  full_name='tensorflow.serving.GetModelStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_version_status', full_name='tensorflow.serving.GetModelStatusResponse.model_version_status', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='model_version_status', file=DESCRIPTOR),
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
  serialized_start=501,
  serialized_end=617,
)

_GETMODELSTATUSREQUEST.fields_by_name['model_spec'].message_type = stfsclient_dot_tensorflow__serving_dot_internal_dot_model__pb2._MODELSPEC
_MODELVERSIONSTATUS.fields_by_name['state'].enum_type = _MODELVERSIONSTATUS_STATE
_MODELVERSIONSTATUS.fields_by_name['status'].message_type = stfsclient_dot_tensorflow__serving_dot_internal_dot_status__pb2._STATUSPROTO
_MODELVERSIONSTATUS_STATE.containing_type = _MODELVERSIONSTATUS
_GETMODELSTATUSRESPONSE.fields_by_name['model_version_status'].message_type = _MODELVERSIONSTATUS
DESCRIPTOR.message_types_by_name['GetModelStatusRequest'] = _GETMODELSTATUSREQUEST
DESCRIPTOR.message_types_by_name['ModelVersionStatus'] = _MODELVERSIONSTATUS
DESCRIPTOR.message_types_by_name['GetModelStatusResponse'] = _GETMODELSTATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetModelStatusRequest = _reflection.GeneratedProtocolMessageType('GetModelStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELSTATUSREQUEST,
  '__module__' : 'stfsclient.tensorflow_serving.internal.get_model_status_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.GetModelStatusRequest)
  })
_sym_db.RegisterMessage(GetModelStatusRequest)

ModelVersionStatus = _reflection.GeneratedProtocolMessageType('ModelVersionStatus', (_message.Message,), {
  'DESCRIPTOR' : _MODELVERSIONSTATUS,
  '__module__' : 'stfsclient.tensorflow_serving.internal.get_model_status_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ModelVersionStatus)
  })
_sym_db.RegisterMessage(ModelVersionStatus)

GetModelStatusResponse = _reflection.GeneratedProtocolMessageType('GetModelStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELSTATUSRESPONSE,
  '__module__' : 'stfsclient.tensorflow_serving.internal.get_model_status_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.GetModelStatusResponse)
  })
_sym_db.RegisterMessage(GetModelStatusResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
