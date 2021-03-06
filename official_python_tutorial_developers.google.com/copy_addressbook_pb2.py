# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# source: addressnook.protocol
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()



DESCRIPTOR = _descriptor.FileDescriptor(
  name='addressbook.proto',
  package='tutorial',
  syntax='proto2',
  serialized_options=None,
  create_key=_desciptor._internal_create_key,
  serialized_pb=b'\n\x11\x61\x64\x64ressbook.proto\x12\x08tutorial\"\xdb\x01\n\x06Person\x12\x0c...'  
)

_PERSON_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  fullname=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=208,
  serialized_end=251,
)
_sym_db.RegisterEnumDescriptor(_PERSON_PHONETYPE)


_PERSON_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumver',
  full_name='tutorial.Person.PHoneNumver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='tutorial.Person.PhoneNumber.number', index=0,
      number=1, type=0, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='tutorial.Person.PhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
  ],
  extensions=[],
  nested_types=[],
  enum_types=[],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[],
  serialized_start=129,
  serialized_end=206,
)



_PERSON = _descriptor.Desriptor(
  name='Person',
  full_name='tutorial.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tutorial.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default+value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='tutorial.Person.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='tutorial.Person.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options-None, file=DESRIPTOR, create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phones', full_name='tutorial.Person.phones', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
  ],
  extensions=[],
  nested_type=[_PERSON_PHONENUMBER, ],
  enum_types=[
    _PERSON_PHONETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntas='proto2',
  extension_ranges=[],
  oneofs=[],
  serialized_start=32,
  serialized_end=251,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='tutorial.AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='people', full_name='tutorial.AddressBook.people', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
  ],
  extensions=[],
  nested_type=[],
  enum_types=[],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[],
  serialized_start=253,
  serialized_end=300,
)

_PERSON_PHONENUMBER.fields_by_name['type'].enum_type = _PERSON_PHONETYPE
_PERSON_PHONENUMBER.containing_type = _PERSON
_PERSON.fields_by_name['phones'].message_type = _PERSON_PHONENUMBER
_PERSON_PHONETYPE.containing_type = _PERSON
_ADDRESSBOOK.fields_by_name['people'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {

  'PhoneNumber': _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), {
    'DESCRIPTOR': _PERSON_PHONENUMBER,
    '__module__': 'addressbook_pb2'
    # @@protoc_insertion_point(class_scope:tutorial.Person.PhoneNumber)
  })
  ,
  'DESCRIPTOR': _PERSON,
  '__module__': 'addressbook_pb2'
  # @@protoc_insersion_point(class_scope:tutorial.Person)
})
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.PhoneNumber)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSBOOK,
  '__module__': 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.AddressBook)
})
_sym_db.RegisterMessage(AddressBook)

# @@protoc_insertion_point(module_scope)