"""count = 1

while count < 11:
    print(count)
    count = count + 1

if count == 11:
    print("Counting complete.")
    """

evens = [i**2 for i in range(9) if i**2 % 2 == 0]
print(evens)