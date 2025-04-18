# search for a number in a tuple
# tuples = (1,4,9,16,25,36,49,64,81,100)
# index = 0
# while index < len(tuples):
#     if tuples[index] == 36:
#         print("Number found", index)
#         break
#     index += 1
# else:
#     print("Number not found")

#fizzbuzz 

num = int(input("Enter a number: "))
index = 1
while index <= num:
    if index % 3 == 0:
        print("Fizz")
    elif index % 5 == 0:
        print("Buzz")
    elif index % 3 == 0 and index % 5 == 0:
        print("FizzBuzz")
    else:
        print(index)
    index += 1
            
        