numbers=[10,20,30,40,50,12,25,50,78,0,34]
numbers.append(60)

numbers.extend([10])
numbers.insert(3,5)
print(numbers)
print(numbers.count(10))
print(numbers.index(50,6,11))
sot=sorted(numbers)
print(sot)