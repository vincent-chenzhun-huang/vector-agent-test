# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vector.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import event_pb2 as event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cvector.proto\x12\x06vector\x1a\x0b\x65vent.proto\"8\n\x11PushEventsRequest\x12#\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x13.event.EventWrapper\"\x14\n\x12PushEventsResponse\"\x14\n\x12HealthCheckRequest\"<\n\x13HealthCheckResponse\x12%\n\x06status\x18\x01 \x01(\x0e\x32\x15.vector.ServingStatus*-\n\rServingStatus\x12\x0b\n\x07SERVING\x10\x00\x12\x0f\n\x0bNOT_SERVING\x10\x01\x32\x97\x01\n\x06Vector\x12\x45\n\nPushEvents\x12\x19.vector.PushEventsRequest\x1a\x1a.vector.PushEventsResponse\"\x00\x12\x46\n\x0bHealthCheck\x12\x1a.vector.HealthCheckRequest\x1a\x1b.vector.HealthCheckResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vector_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SERVINGSTATUS']._serialized_start=201
  _globals['_SERVINGSTATUS']._serialized_end=246
  _globals['_PUSHEVENTSREQUEST']._serialized_start=37
  _globals['_PUSHEVENTSREQUEST']._serialized_end=93
  _globals['_PUSHEVENTSRESPONSE']._serialized_start=95
  _globals['_PUSHEVENTSRESPONSE']._serialized_end=115
  _globals['_HEALTHCHECKREQUEST']._serialized_start=117
  _globals['_HEALTHCHECKREQUEST']._serialized_end=137
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=139
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=199
  _globals['_VECTOR']._serialized_start=249
  _globals['_VECTOR']._serialized_end=400
# @@protoc_insertion_point(module_scope)
