with open("example.txt") as file:
    lines = file.readlines()
    for elem in lines:
        print(elem)