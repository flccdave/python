words = {
  "hello": "A typical greeting",
  "goodbye": "A typical expression for parting ways",
  "desk": "Furniture for studying or working. One flat surface."
}

warhammer.brand


class Warrior:
  def __init__(self, name, age, weight, rank, weapon):
    self.name = name
    self.age = age
	self.weight = weight
	self.rank = rank
	self.weapon = weapon
	self.health = 100

w1 = Warrior("John", 36, 100, "Lt.", "battle axe")
w2 = Warrior("Dave", 46, 160, "Captain", "bastard sword")


print(w1.weapon)