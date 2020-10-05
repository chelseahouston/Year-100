def form():
  name = input("What is your name? ")
  age = input("What is your age? ")
  try:
    age = int(age)
  except ValueError:
    print("Incorrect value. Please enter a number. Restarting...")
    form()
  difference = 100 - age
  year100 = 2020 + difference
  print("Hello, " + name + ".")
  print(f"You will turn 100 years old in the year { year100 } !")
def run():
  runagain = input("Run again? (Y/N): ")
  if runagain == "Y":
    form()
    run()
  elif runagain == "N":
    print("Goodbye. Have a good day.")
  else:
    print("Error: Incorrect Value.")
    run()
form()
run()


