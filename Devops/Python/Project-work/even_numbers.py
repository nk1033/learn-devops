## write a code to disply even numbers betwenn 1 to 10
count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} Even Numbers between the Range")