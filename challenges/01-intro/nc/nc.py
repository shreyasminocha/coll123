from random import randrange
from secret import flag

print(
    r"""
       _
      ( \
       \ \
       / /                |\\
      / /     .-`````-.   / ^`-.
      \ \    /         \_/  {|} `o
       \ \  /   .---.   \\ _  ,--'
        \ \/   /     \,  \( `^^^
         \   \/\      (\  )
          \   ) \     ) \ \
      jgs  ) /__ \__  ) (\ \___
          (___)))__))(__))(__)))
  """
)
print()

a, b = randrange(0, 100), randrange(0, 100)
solution = input(f"what is {a} + {b}? ")

if int(solution) == a + b:
    print("yes! here's the flag:", flag)
else:
    print("oops. try again")
