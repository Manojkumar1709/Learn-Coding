
#  Write a Python program that prints the numbers from 1 to 100 and checks their divisibility with all numbers between 2 and 100.
#    a. For each number from 1 to 100, the program should check if the number is divisible by any of the numbers from 2 to 100.
#    b. If a number is divisible by one or more numbers, the program should print the divisors. If it is not divisible by any 
#       of the numbers from 2 to 100, print a message stating that it is not divisible by any of the specified numbers.


print("Number Division")

for i in range(1, 101):
    divisible_by = []      
  
    for divisor in range(2, 101):  
        if i % divisor == 0:
            divisible_by.append(divisor)
    
    if divisible_by:
        print(f"The number {i} is divisible by: {', '.join(map(str, divisible_by))}")
    else:
        print(f"The number {i} is not divisible by any of the specified numbers.")


