# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: libp2p/security/insecure/pb/plaintext.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from libp2p.crypto.pb import crypto_pb2 as libp2p_dot_crypto_dot_pb_dot_crypto__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+libp2p/security/insecure/pb/plaintext.proto\x12\x0cplaintext.pb\x1a\x1dlibp2p/crypto/pb/crypto.proto\"<\n\x08\x45xchange\x12\n\n\x02id\x18\x01 \x01(\x0c\x12$\n\x06pubkey\x18\x02 \x01(\x0b\x32\x14.crypto.pb.PublicKey')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'libp2p.security.insecure.pb.plaintext_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EXCHANGE']._serialized_start=92
  _globals['_EXCHANGE']._serialized_end=152
# @@protoc_insertion_point(module_scope)
