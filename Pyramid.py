def pyramidPrinter(limit):
    limit += 1
    for line in range(limit):
        for i in range(line):
            print("* ", end="")
        print("\n")


limitInput = int(input("Input your pyramid limit: "))
pyramidPrinter(limitInput)
