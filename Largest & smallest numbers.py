numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print("List:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
