numbers=[23,34,60,80]
for num in numbers:
    print(numbers)

print (numbers[0])
print(numbers[2])
print(numbers)
numbers[1]=100
print(numbers)
numbers.remove(100)
print(numbers)
numbers.append(69)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers) # Once there are no elements to remove, it gives an Traceback error
