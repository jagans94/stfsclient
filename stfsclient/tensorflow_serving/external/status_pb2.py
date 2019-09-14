# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stfsclient/tensorflow_serving/external/status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.lib.core import error_codes_pb2 as tensorflow_dot_core_dot_lib_dot_core_dot_error__codes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stfsclient/tensorflow_serving/external/status.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\n3stfsclient/tensorflow_serving/external/status.proto\x12\x12tensorflow.serving\x1a*tensorflow/core/lib/core/error_codes.proto\"k\n\x0bStatusProto\x12\x36\n\nerror_code\x18\x01 \x01(\x0e\x32\x16.tensorflow.error.CodeR\nerror_code\x12$\n\rerror_message\x18\x02 \x01(\tR\rerror_messageB\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_lib_dot_core_dot_error__codes__pb2.DESCRIPTOR,])




_STATUSPROTO = _descriptor.Descriptor(
  name='StatusProto',
  full_name='tensorflow.serving.StatusProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='tensorflow.serving.StatusProto.error_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='error_code', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='tensorflow.serving.StatusProto.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='error_message', file=DESCRIPTOR),
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
  serialized_start=119,
  serialized_end=226,
)

_STATUSPROTO.fields_by_name['error_code'].enum_type = tensorflow_dot_core_dot_lib_dot_core_dot_error__codes__pb2._CODE
DESCRIPTOR.message_types_by_name['StatusProto'] = _STATUSPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusProto = _reflection.GeneratedProtocolMessageType('StatusProto', (_message.Message,), {
  'DESCRIPTOR' : _STATUSPROTO,
  '__module__' : 'stfsclient.tensorflow_serving.external.status_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.StatusProto)
  })
_sym_db.RegisterMessage(StatusProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
