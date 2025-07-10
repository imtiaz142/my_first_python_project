i = 0
while True:
    i += 1  # Move this before checking anything

    if i == 3:
        continue  # Skip the print for 3

    print(i)

    if i == 5:
        break
