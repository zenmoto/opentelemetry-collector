# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opentelemetry/proto/logs/v1/logs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opentelemetry.proto.common.v1 import common_pb2 as opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2
from opentelemetry.proto.resource.v1 import resource_pb2 as opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='opentelemetry/proto/logs/v1/logs.proto',
  package='opentelemetry.proto.logs.v1',
  syntax='proto3',
  serialized_options=b'\n\036io.opentelemetry.proto.logs.v1B\tLogsProtoP\001Z<github.com/open-telemetry/opentelemetry-proto/gen/go/logs/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&opentelemetry/proto/logs/v1/logs.proto\x12\x1bopentelemetry.proto.logs.v1\x1a*opentelemetry/proto/common/v1/common.proto\x1a.opentelemetry/proto/resource/v1/resource.proto\"L\n\x08LogsData\x12@\n\rresource_logs\x18\x01 \x03(\x0b\x32).opentelemetry.proto.logs.v1.ResourceLogs\"\xbe\x01\n\x0cResourceLogs\x12;\n\x08resource\x18\x01 \x01(\x0b\x32).opentelemetry.proto.resource.v1.Resource\x12]\n\x1cinstrumentation_library_logs\x18\x02 \x03(\x0b\x32\x37.opentelemetry.proto.logs.v1.InstrumentationLibraryLogs\x12\x12\n\nschema_url\x18\x03 \x01(\t\"\xbe\x01\n\x1aInstrumentationLibraryLogs\x12V\n\x17instrumentation_library\x18\x01 \x01(\x0b\x32\x35.opentelemetry.proto.common.v1.InstrumentationLibrary\x12\x34\n\x04logs\x18\x02 \x03(\x0b\x32&.opentelemetry.proto.logs.v1.LogRecord\x12\x12\n\nschema_url\x18\x03 \x01(\t\"\xd6\x02\n\tLogRecord\x12\x16\n\x0etime_unix_nano\x18\x01 \x01(\x06\x12\x44\n\x0fseverity_number\x18\x02 \x01(\x0e\x32+.opentelemetry.proto.logs.v1.SeverityNumber\x12\x15\n\rseverity_text\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x35\n\x04\x62ody\x18\x05 \x01(\x0b\x32\'.opentelemetry.proto.common.v1.AnyValue\x12;\n\nattributes\x18\x06 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12 \n\x18\x64ropped_attributes_count\x18\x07 \x01(\r\x12\r\n\x05\x66lags\x18\x08 \x01(\x07\x12\x10\n\x08trace_id\x18\t \x01(\x0c\x12\x0f\n\x07span_id\x18\n \x01(\x0c*\xc3\x05\n\x0eSeverityNumber\x12\x1f\n\x1bSEVERITY_NUMBER_UNSPECIFIED\x10\x00\x12\x19\n\x15SEVERITY_NUMBER_TRACE\x10\x01\x12\x1a\n\x16SEVERITY_NUMBER_TRACE2\x10\x02\x12\x1a\n\x16SEVERITY_NUMBER_TRACE3\x10\x03\x12\x1a\n\x16SEVERITY_NUMBER_TRACE4\x10\x04\x12\x19\n\x15SEVERITY_NUMBER_DEBUG\x10\x05\x12\x1a\n\x16SEVERITY_NUMBER_DEBUG2\x10\x06\x12\x1a\n\x16SEVERITY_NUMBER_DEBUG3\x10\x07\x12\x1a\n\x16SEVERITY_NUMBER_DEBUG4\x10\x08\x12\x18\n\x14SEVERITY_NUMBER_INFO\x10\t\x12\x19\n\x15SEVERITY_NUMBER_INFO2\x10\n\x12\x19\n\x15SEVERITY_NUMBER_INFO3\x10\x0b\x12\x19\n\x15SEVERITY_NUMBER_INFO4\x10\x0c\x12\x18\n\x14SEVERITY_NUMBER_WARN\x10\r\x12\x19\n\x15SEVERITY_NUMBER_WARN2\x10\x0e\x12\x19\n\x15SEVERITY_NUMBER_WARN3\x10\x0f\x12\x19\n\x15SEVERITY_NUMBER_WARN4\x10\x10\x12\x19\n\x15SEVERITY_NUMBER_ERROR\x10\x11\x12\x1a\n\x16SEVERITY_NUMBER_ERROR2\x10\x12\x12\x1a\n\x16SEVERITY_NUMBER_ERROR3\x10\x13\x12\x1a\n\x16SEVERITY_NUMBER_ERROR4\x10\x14\x12\x19\n\x15SEVERITY_NUMBER_FATAL\x10\x15\x12\x1a\n\x16SEVERITY_NUMBER_FATAL2\x10\x16\x12\x1a\n\x16SEVERITY_NUMBER_FATAL3\x10\x17\x12\x1a\n\x16SEVERITY_NUMBER_FATAL4\x10\x18*X\n\x0eLogRecordFlags\x12\x1f\n\x1bLOG_RECORD_FLAG_UNSPECIFIED\x10\x00\x12%\n LOG_RECORD_FLAG_TRACE_FLAGS_MASK\x10\xff\x01\x42k\n\x1eio.opentelemetry.proto.logs.v1B\tLogsProtoP\x01Z<github.com/open-telemetry/opentelemetry-proto/gen/go/logs/v1b\x06proto3'
  ,
  dependencies=[opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2.DESCRIPTOR,opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2.DESCRIPTOR,])

_SEVERITYNUMBER = _descriptor.EnumDescriptor(
  name='SeverityNumber',
  full_name='opentelemetry.proto.logs.v1.SeverityNumber',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_TRACE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_TRACE2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_TRACE3', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_TRACE4', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_DEBUG', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_DEBUG2', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_DEBUG3', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_DEBUG4', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_INFO', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_INFO2', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_INFO3', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_INFO4', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_WARN', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_WARN2', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_WARN3', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_WARN4', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_ERROR', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_ERROR2', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_ERROR3', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_ERROR4', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_FATAL', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_FATAL2', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_FATAL3', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEVERITY_NUMBER_FATAL4', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=973,
  serialized_end=1680,
)
_sym_db.RegisterEnumDescriptor(_SEVERITYNUMBER)

SeverityNumber = enum_type_wrapper.EnumTypeWrapper(_SEVERITYNUMBER)
_LOGRECORDFLAGS = _descriptor.EnumDescriptor(
  name='LogRecordFlags',
  full_name='opentelemetry.proto.logs.v1.LogRecordFlags',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOG_RECORD_FLAG_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOG_RECORD_FLAG_TRACE_FLAGS_MASK', index=1, number=255,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1682,
  serialized_end=1770,
)
_sym_db.RegisterEnumDescriptor(_LOGRECORDFLAGS)

LogRecordFlags = enum_type_wrapper.EnumTypeWrapper(_LOGRECORDFLAGS)
SEVERITY_NUMBER_UNSPECIFIED = 0
SEVERITY_NUMBER_TRACE = 1
SEVERITY_NUMBER_TRACE2 = 2
SEVERITY_NUMBER_TRACE3 = 3
SEVERITY_NUMBER_TRACE4 = 4
SEVERITY_NUMBER_DEBUG = 5
SEVERITY_NUMBER_DEBUG2 = 6
SEVERITY_NUMBER_DEBUG3 = 7
SEVERITY_NUMBER_DEBUG4 = 8
SEVERITY_NUMBER_INFO = 9
SEVERITY_NUMBER_INFO2 = 10
SEVERITY_NUMBER_INFO3 = 11
SEVERITY_NUMBER_INFO4 = 12
SEVERITY_NUMBER_WARN = 13
SEVERITY_NUMBER_WARN2 = 14
SEVERITY_NUMBER_WARN3 = 15
SEVERITY_NUMBER_WARN4 = 16
SEVERITY_NUMBER_ERROR = 17
SEVERITY_NUMBER_ERROR2 = 18
SEVERITY_NUMBER_ERROR3 = 19
SEVERITY_NUMBER_ERROR4 = 20
SEVERITY_NUMBER_FATAL = 21
SEVERITY_NUMBER_FATAL2 = 22
SEVERITY_NUMBER_FATAL3 = 23
SEVERITY_NUMBER_FATAL4 = 24
LOG_RECORD_FLAG_UNSPECIFIED = 0
LOG_RECORD_FLAG_TRACE_FLAGS_MASK = 255



_LOGSDATA = _descriptor.Descriptor(
  name='LogsData',
  full_name='opentelemetry.proto.logs.v1.LogsData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_logs', full_name='opentelemetry.proto.logs.v1.LogsData.resource_logs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=163,
  serialized_end=239,
)


_RESOURCELOGS = _descriptor.Descriptor(
  name='ResourceLogs',
  full_name='opentelemetry.proto.logs.v1.ResourceLogs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource', full_name='opentelemetry.proto.logs.v1.ResourceLogs.resource', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instrumentation_library_logs', full_name='opentelemetry.proto.logs.v1.ResourceLogs.instrumentation_library_logs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema_url', full_name='opentelemetry.proto.logs.v1.ResourceLogs.schema_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=242,
  serialized_end=432,
)


_INSTRUMENTATIONLIBRARYLOGS = _descriptor.Descriptor(
  name='InstrumentationLibraryLogs',
  full_name='opentelemetry.proto.logs.v1.InstrumentationLibraryLogs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrumentation_library', full_name='opentelemetry.proto.logs.v1.InstrumentationLibraryLogs.instrumentation_library', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs', full_name='opentelemetry.proto.logs.v1.InstrumentationLibraryLogs.logs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema_url', full_name='opentelemetry.proto.logs.v1.InstrumentationLibraryLogs.schema_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=435,
  serialized_end=625,
)


_LOGRECORD = _descriptor.Descriptor(
  name='LogRecord',
  full_name='opentelemetry.proto.logs.v1.LogRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_unix_nano', full_name='opentelemetry.proto.logs.v1.LogRecord.time_unix_nano', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='severity_number', full_name='opentelemetry.proto.logs.v1.LogRecord.severity_number', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='severity_text', full_name='opentelemetry.proto.logs.v1.LogRecord.severity_text', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='opentelemetry.proto.logs.v1.LogRecord.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='opentelemetry.proto.logs.v1.LogRecord.body', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='opentelemetry.proto.logs.v1.LogRecord.attributes', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_attributes_count', full_name='opentelemetry.proto.logs.v1.LogRecord.dropped_attributes_count', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flags', full_name='opentelemetry.proto.logs.v1.LogRecord.flags', index=7,
      number=8, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='opentelemetry.proto.logs.v1.LogRecord.trace_id', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='span_id', full_name='opentelemetry.proto.logs.v1.LogRecord.span_id', index=9,
      number=10, type=12, cpp_type=9, label=1,
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
  serialized_start=628,
  serialized_end=970,
)

_LOGSDATA.fields_by_name['resource_logs'].message_type = _RESOURCELOGS
_RESOURCELOGS.fields_by_name['resource'].message_type = opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2._RESOURCE
_RESOURCELOGS.fields_by_name['instrumentation_library_logs'].message_type = _INSTRUMENTATIONLIBRARYLOGS
_INSTRUMENTATIONLIBRARYLOGS.fields_by_name['instrumentation_library'].message_type = opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2._INSTRUMENTATIONLIBRARY
_INSTRUMENTATIONLIBRARYLOGS.fields_by_name['logs'].message_type = _LOGRECORD
_LOGRECORD.fields_by_name['severity_number'].enum_type = _SEVERITYNUMBER
_LOGRECORD.fields_by_name['body'].message_type = opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2._ANYVALUE
_LOGRECORD.fields_by_name['attributes'].message_type = opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2._KEYVALUE
DESCRIPTOR.message_types_by_name['LogsData'] = _LOGSDATA
DESCRIPTOR.message_types_by_name['ResourceLogs'] = _RESOURCELOGS
DESCRIPTOR.message_types_by_name['InstrumentationLibraryLogs'] = _INSTRUMENTATIONLIBRARYLOGS
DESCRIPTOR.message_types_by_name['LogRecord'] = _LOGRECORD
DESCRIPTOR.enum_types_by_name['SeverityNumber'] = _SEVERITYNUMBER
DESCRIPTOR.enum_types_by_name['LogRecordFlags'] = _LOGRECORDFLAGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogsData = _reflection.GeneratedProtocolMessageType('LogsData', (_message.Message,), {
  'DESCRIPTOR' : _LOGSDATA,
  '__module__' : 'opentelemetry.proto.logs.v1.logs_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.logs.v1.LogsData)
  })
_sym_db.RegisterMessage(LogsData)

ResourceLogs = _reflection.GeneratedProtocolMessageType('ResourceLogs', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCELOGS,
  '__module__' : 'opentelemetry.proto.logs.v1.logs_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.logs.v1.ResourceLogs)
  })
_sym_db.RegisterMessage(ResourceLogs)

InstrumentationLibraryLogs = _reflection.GeneratedProtocolMessageType('InstrumentationLibraryLogs', (_message.Message,), {
  'DESCRIPTOR' : _INSTRUMENTATIONLIBRARYLOGS,
  '__module__' : 'opentelemetry.proto.logs.v1.logs_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.logs.v1.InstrumentationLibraryLogs)
  })
_sym_db.RegisterMessage(InstrumentationLibraryLogs)

LogRecord = _reflection.GeneratedProtocolMessageType('LogRecord', (_message.Message,), {
  'DESCRIPTOR' : _LOGRECORD,
  '__module__' : 'opentelemetry.proto.logs.v1.logs_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.logs.v1.LogRecord)
  })
_sym_db.RegisterMessage(LogRecord)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
