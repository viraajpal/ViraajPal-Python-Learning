def game():
    return 48
z = game()
     with open("another.txt", "w") as f:
    another = int(f.read())
if another<z:
    with open("another.txt", "w") as f:
        f.write(str(z))
