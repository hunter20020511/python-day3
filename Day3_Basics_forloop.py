numbers=[45,56,36,50,99,20]
for i in numbers:
    print(i) #prints all numbers from list -> numbers
for numbers in range(10):
    print(numbers)
for numbers in range(1, 11):
    print(numbers)

list2=[20,49,49,21,33,559,450,55,49,12,13,16]
for num in list2:
    if num<50:
        print(num)
for num in list2:
    if num % 2==0:
        print("Even number: ", num)
    else:
        print("Odd number: ", num)

