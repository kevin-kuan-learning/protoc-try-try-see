from google.protobuf.json_format import MessageToDict
import addressbook_pb2

RUNERROR = False

person = addressbook_pb2.Person()
person.id = 34173
if RUNERROR:
    person.id = "34173" # TypeError
    person.address = "YuanTong Rd."  # AttributeError
person.name = "Kevin Kuan"
person.email = "kevin_kuan@trendmicro.com"

phone = person.phones.add()
phone.number = "0919487522"
phone.type = addressbook_pb2.Person.PhoneType.HOME
phone.type = addressbook_pb2.Person.HOME # this works too

print(person)
# name: "Kevin Kuan"
# id: 34173
# email: "kevin_kuan@trendmicro.com"
# phones {
#   number: "0919487522"
#   type: MOBILE
# }

kevin2 = addressbook_pb2.Person()
kevin2.CopyFrom(person)
print(kevin2)
# name: "Kevin Kuan"
# id: 34173
# email: "kevin_kuan@trendmicro.com"
# phones {
#   number: "0919487522"
#   type: MOBILE
# }


person.Clear()
print(person) # None

binary_string = kevin2.SerializeToString()
print(binary_string) 
# b'\n\nKevin Kuan\x10\xfd\x8a\x02\x1a\x19kevin_kuan@trendmicro.com"\x0e\n\n0919487522\x10\x00'
print(type(binary_string))  #binary string indeed

with open('test', 'wb') as f:
    f.write(binary_string)

with open('test', 'rb') as f:
    s = f.read()

person.ParseFromString(s)  # returns bytes parsed, 59.
j = MessageToJson(person)


pass