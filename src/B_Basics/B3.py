for e in range(1,101):
    text = None
    if e % 5 == 0 and e % 3 == 0:
        print("FizzBuzz")
    elif e % 5 == 0:
        print("Buzz")
    elif e % 3 == 0:
        print("Fizz")
    else:
        print(e)