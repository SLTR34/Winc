# Do not modify these lines
__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

# Add your code after this line

# make a Specialist class.
class Specialist:
     
     def __init__(self, name, price):
          self.name = name
          self.price = price

class Electrician(Specialist):
        pass

class Painter(Specialist):
        pass

class Plumber(Specialist):
        pass

# make a Homeowner class.
class Homeowner:
    """Hold a record of homeowners"""
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs
        self.contracts = []

    def add_contract(self, specialists):
        price = 0
        cheapest_specialist = None
        for specialist in specialists:
            if price == 0:
                price = specialist.price
            if specialist.price <= price:
                cheapest_specialist = specialist

        self.contracts.append(cheapest_specialist)

# Classes are hashable so they can be used as keys in dictionaries
specialists =  {
  Electrician: [
    Electrician("Alice Aliceville", 2500),
    Electrician("Dave Davesville", 1700)
  ],
  Painter: [Painter("Bob Bobsville", 1400),
            Painter("Erik Eriksson", 1000)],
  Plumber:
  [Plumber("Craig Craigsville", 1200),
   Plumber("Fiona Fenderson", 1100)],
}

homeowners = [
  Homeowner("Alfred Alfredson", "Alfredslane 123", [Painter, Plumber]),
  Homeowner("Bert Bertson", "Bertslane 231", [Plumber]),
  Homeowner("Candice Candicedottir", "Candicelane 312",
            [Electrician, Painter]),
]

for homeowner in homeowners:
  for need in homeowner.needs:
    homeowner.add_contract(specialists[need])
  print(f"{homeowner.name}'s contracts:",
        [specialist.name for specialist in homeowner.contracts])

# Homeowners
#alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ["painter", "plumber"])
#bert = Homeowner("Bert Bertson", "Bertslane 231", ["plumber"])
#candice = Homeowner("Candice Candicedottir", "Candicelane 312", ["electrician", "painter"])

# alfred_contracts = []
# for need in alfred_needs:
#     if need == alice_profession:
#         alfred_contracts.append(alice_name)
#     elif need == bob_profession:
#         alfred_contracts.append(bob_name)
#     elif need == craig_profession:
#         alfred_contracts.append(craig_name)

# bert_contracts = []
# for need in bert_needs:
#     if need == alice_profession:
#         bert_contracts.append(alice_name)
#     elif need == bob_profession:
#         bert_contracts.append(bob_name)
#     elif need == craig_profession:
#         bert_contracts.append(craig_name)

# candice_contracts = []
# for need in candice_needs:
#     if need == alice_profession:
#         candice_contracts.append(alice_name)
#     elif need == bob_profession:
#         candice_contracts.append(bob_name)
#     elif need == craig_profession:
#         candice_contracts.append(craig_name)

# print("Alfred's contracts:", alfred_contracts)
# print("Bert's contracts:", bert_contracts)
# print("Candice's contracts:", candice_contracts)
