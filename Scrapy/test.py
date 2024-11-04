def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Yield the current count
        count += 1   # Increment the count

# Using the generator
counter = count_up_to(5)
print(counter)
print(len(counter))
for number in counter:
    print(number)