# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UsersMicroservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17UsersMicroservice.proto\x12\x11UsersMicroservice\"6\n\tTokenPair\x12\x13\n\x0b\x61\x63\x63\x65ssToken\x18\x01 \x01(\t\x12\x14\n\x0crefreshToken\x18\x02 \x01(\t\"E\n\x04User\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x0f\n\x07isGuest\x18\x03 \x01(\x08\x12\x0e\n\x06rating\x18\x04 \x01(\r\"\x1f\n\x0b\x41uthRequest\x12\x10\n\x08\x61uthCode\x18\x01 \x01(\t\"\xb8\x01\n\x0c\x41uthResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.UsersMicroservice.ExitStatus\x12\x31\n\x06tokens\x18\x02 \x01(\x0b\x32\x1c.UsersMicroservice.TokenPairH\x00\x88\x01\x01\x12.\n\x08userInfo\x18\x03 \x01(\x0b\x32\x17.UsersMicroservice.UserH\x01\x88\x01\x01\x42\t\n\x07_tokensB\x0b\n\t_userInfo\"A\n\x15\x43hangeNicknameRequest\x12\x13\n\x0brequesterID\x18\x01 \x01(\r\x12\x13\n\x0bnewNickname\x18\x03 \x01(\t\"G\n\x16\x43hangeNicknameResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.UsersMicroservice.ExitStatus\"0\n\x19RefreshAccessTokenRequest\x12\x13\n\x0brequesterID\x18\x01 \x01(\r\"u\n\x1aRefreshAccessTokenResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.UsersMicroservice.ExitStatus\x12\x18\n\x0b\x61\x63\x63\x65ssToken\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_accessToken\"5\n\x0eGetInfoRequest\x12\x13\n\x0brequesterID\x18\x01 \x01(\r\x12\x0e\n\x06userID\x18\x02 \x01(\r\"}\n\x0fGetInfoResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.UsersMicroservice.ExitStatus\x12.\n\x08userInfo\x18\x02 \x01(\x0b\x32\x17.UsersMicroservice.UserH\x00\x88\x01\x01\x42\x0b\n\t_userInfo*r\n\nExitStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\x10\n\x0c\x43ODING_ERROR\x10\x01\x12\x12\n\x0e\x44\x45\x43ODING_ERROR\x10\x02\x12\x15\n\x11\x46\x41ILED_DEPENDENCY\x10\x03\x12\x1a\n\x16RESOURCE_NOT_AVAILABLE\x10\x04\x32\xd9\x03\n\x0cUsersService\x12N\n\x0b\x41uthAsGuest\x12\x1e.UsersMicroservice.AuthRequest\x1a\x1f.UsersMicroservice.AuthResponse\x12M\n\nAuthFromVK\x12\x1e.UsersMicroservice.AuthRequest\x1a\x1f.UsersMicroservice.AuthResponse\x12\x65\n\x0e\x43hangeNickname\x12(.UsersMicroservice.ChangeNicknameRequest\x1a).UsersMicroservice.ChangeNicknameResponse\x12q\n\x12RefreshAccessToken\x12,.UsersMicroservice.RefreshAccessTokenRequest\x1a-.UsersMicroservice.RefreshAccessTokenResponse\x12P\n\x07GetInfo\x12!.UsersMicroservice.GetInfoRequest\x1a\".UsersMicroservice.GetInfoResponseB\x0cZ\n./users_pbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'UsersMicroservice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\n./users_pb'
  _EXITSTATUS._serialized_start=884
  _EXITSTATUS._serialized_end=998
  _TOKENPAIR._serialized_start=46
  _TOKENPAIR._serialized_end=100
  _USER._serialized_start=102
  _USER._serialized_end=171
  _AUTHREQUEST._serialized_start=173
  _AUTHREQUEST._serialized_end=204
  _AUTHRESPONSE._serialized_start=207
  _AUTHRESPONSE._serialized_end=391
  _CHANGENICKNAMEREQUEST._serialized_start=393
  _CHANGENICKNAMEREQUEST._serialized_end=458
  _CHANGENICKNAMERESPONSE._serialized_start=460
  _CHANGENICKNAMERESPONSE._serialized_end=531
  _REFRESHACCESSTOKENREQUEST._serialized_start=533
  _REFRESHACCESSTOKENREQUEST._serialized_end=581
  _REFRESHACCESSTOKENRESPONSE._serialized_start=583
  _REFRESHACCESSTOKENRESPONSE._serialized_end=700
  _GETINFOREQUEST._serialized_start=702
  _GETINFOREQUEST._serialized_end=755
  _GETINFORESPONSE._serialized_start=757
  _GETINFORESPONSE._serialized_end=882
  _USERSSERVICE._serialized_start=1001
  _USERSSERVICE._serialized_end=1474
# @@protoc_insertion_point(module_scope)
