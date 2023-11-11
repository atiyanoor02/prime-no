def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

print(f"Prime numbers in the range {start_index} to {end_index} are:")

for number in range(start_index, end_index + 1):
    if is_prime(number):
        print(number)