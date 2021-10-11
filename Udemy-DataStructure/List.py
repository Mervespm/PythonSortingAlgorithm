
class Employee:
	def __init__(self, firstName, lastName, id):
		self.firstName = firstName
		self.lastName = lastName
		self.id = id

list1 = []
list1.append(Employee('John', 'Jones', 2423))
list1.append(Employee('Mary', 'Smith', 1231))
list1.append(Employee('Mike', 'Wilson', 3242))

for i in list1:
	print(i.firstName)

print(len(list1))
