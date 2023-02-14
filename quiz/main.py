for FizzBuzz in range(101):
    if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
        print("FizzBuzz")
    elif FizzBuzz % 3 == 0:
        print("Fizz")
    elif FizzBuzz % 5 == 0:
        print("Buzz")
        print(FizzBuzz)