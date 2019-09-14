# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stfsclient/tensorflow_serving/internal/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stfsclient/tensorflow_serving/internal/model.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\n2stfsclient/tensorflow_serving/internal/model.proto\x12\x12tensorflow.serving\x1a\x1egoogle/protobuf/wrappers.proto\"\x8c\x01\n\tModelSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x07version\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueH\x00\x12\x17\n\rversion_label\x18\x04 \x01(\tH\x00\x12\x16\n\x0esignature_name\x18\x03 \x01(\tB\x10\n\x0eversion_choiceB\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_MODELSPEC = _descriptor.Descriptor(
  name='ModelSpec',
  full_name='tensorflow.serving.ModelSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.serving.ModelSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorflow.serving.ModelSpec.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_label', full_name='tensorflow.serving.ModelSpec.version_label', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature_name', full_name='tensorflow.serving.ModelSpec.signature_name', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='version_choice', full_name='tensorflow.serving.ModelSpec.version_choice',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=107,
  serialized_end=247,
)

_MODELSPEC.fields_by_name['version'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_MODELSPEC.oneofs_by_name['version_choice'].fields.append(
  _MODELSPEC.fields_by_name['version'])
_MODELSPEC.fields_by_name['version'].containing_oneof = _MODELSPEC.oneofs_by_name['version_choice']
_MODELSPEC.oneofs_by_name['version_choice'].fields.append(
  _MODELSPEC.fields_by_name['version_label'])
_MODELSPEC.fields_by_name['version_label'].containing_oneof = _MODELSPEC.oneofs_by_name['version_choice']
DESCRIPTOR.message_types_by_name['ModelSpec'] = _MODELSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelSpec = _reflection.GeneratedProtocolMessageType('ModelSpec', (_message.Message,), {
  'DESCRIPTOR' : _MODELSPEC,
  '__module__' : 'stfsclient.tensorflow_serving.internal.model_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ModelSpec)
  })
_sym_db.RegisterMessage(ModelSpec)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
