from enum import Enum

streettypes = Enum('Drive', 'Street', 'Lane', 'Avenue', 'Way')
provinces = Enum('AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT')

class Address():
    def __init__(self, addressee, civicaddress, stype, city, province, pcode):
      self.addressee = addressee
      self.civicaddress = civicaddress
      self.stype = stype
      self.city = city
      self.province = province
      self.pcode = pcode

myaddress = Address('Anthony', '266 Claridge',streettypes.Drive, 'Ottawa', provinces.ON, 'K2J 5B9')

print myaddress.addressee
print myaddress.civicaddress, myaddress.stype
print myaddress.city, myaddress.province, myaddress.pcode
