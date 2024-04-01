# enter a number
number = int(input("Enter a number: "))

# sum numbers digit
sum_of_digits = sum(int(digit) for digit in str(number))

# result
if number % sum_of_digits == 0:
    print(f"{number}  Harshad .")
else:
    print(f"{number} not Harshad ")
