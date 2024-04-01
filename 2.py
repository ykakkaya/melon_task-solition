# enter number
number = int(input("Enter a number: "))

# numbers divisiors sum
sum_of_divisors = sum([i for i in range(1, number) if number % i == 0])

# Result
if sum_of_divisors < number:
    print(f"{number} deficient number")
elif sum_of_divisors == number:
    print(f"{number} perfect number ")
else:
    print(f"{number} abundant number")
