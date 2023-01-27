from random import randrange

print("do some arithmetic 🤓")

for _ in range(50):
    a, b = randrange(0, 100), randrange(0, 100)
    solution = input(f"what is {a} + {b}? ")

    if int(solution) == a + b:
        print("correct!")
    else:
        print("oops. start over")
        break
