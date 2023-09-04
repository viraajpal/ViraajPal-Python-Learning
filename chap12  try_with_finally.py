try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)


finally:
    print("We had done")

    # finally will run whatever you are doing in except it doesn't matter we cant stop finally....