pattern_size = int(input("Enter the size of the pattern:"))
i = 0

while i < pattern_size:
    for x in range(pattern_size):
        print("*", end="")
        x += 1
    print()
    i += 1
