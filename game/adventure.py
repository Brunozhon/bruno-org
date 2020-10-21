import time, ramdom
which = ans = rand = None
dog = cat = hamster = 0
items = []

def intro():
  print('''
  Welcome!
  
  Press 1 to go to Room 1
  ''')
  which = input("Which room?")
  if which == 1:
    room1()
  elif which == 2:
    room2()
  elif which == 3:
    room3()
  elif which == 4:
    room4()
  choice()
  
def room1():
  print("You go to a hall. You go on a train.")
  time.sleep(10)
  print("'Hucton Huc', said the train.")
  ans = input("Do you want to go to Hucton Huc?")
  if ans == "Yes":
    print("You walk to Kro...")
    time.sleep(1)
    print("The lava is rising. Oh no! You died")
  else:
    print("You keep going. Suddenly, the train became...")
    time.sleep(20)
    print("a... a...")
    rand = random.randrange(1,4)
    if rand == 1:
      print("A DOG!")
      dog = dog + 1
    elif rand == 2:
      print("A CAT!")
      cat = cat + 1
    else:
      print("You got a hamster. The end.")
      hamster = hamster + 1
      time.sleep(5)
      print("JUST KIDDING! All of your hamsters ran away.")
      hamster = 0
      
def room2():
  print("You got a bunch of cuddly hamsters, dogs, and cats.")
  dog = dog + 1000
  cat = cat + 1000
  hamster = hamster + 1000
  time.sleep(5)
  print("YOU ARE DOOMED! You stole these from the pet store!")
  ans = input("What are you going to do?")
  if ans == "Escape":
    print("You escape. But you forgot to carry the nice...")
    time.sleep(1)
    print("It turns out the property is yours! The mothers and fathers had bought TOO MUCH cats!")
    time.sleep(10)
    print("You go back to your house.")
  else:
    print("You don't get to get the cats. Such sad.")
   

def room3():
  print('''
    Stats:
    
    Dogs: {dog}
    Cats: {cat}
    Hamsters: {hamster}
  ''')
  
def room4():
  print("You found something on the ground. It is a sword.")
  ans = input("Do you  want to pick it?")
  if ans = "Yes":
    items.append("sword")
    print("You picked it up and you led yourself to a epic life. You survive, fight, and all the other stuff.")
    time.sleep(2)
    print("It comes to an end, where you surpass all levels, and then you got a bow, sheild, and parachute.")
    items.append("bow")
    items.append("sheild")
    items.append("parachute")
  else:
    print("A tiger instantly kills you.")
  
sugar = chocobar = chocosugar = chocosugarproxide = 0 # Chocosugarproxide?
banksugar = bankchocobar = bankchocosugarproxide = 100000000000000
def sugarintro():
  ans = input('''
  What do you want to do?
  
  SC = sugar for chocobar
  CS = chocobar for sugar
  STS = steal sugar from bank
  STC = steal chocobar from bank
  ''')
  if ans == "SC":
    ans = int(input("How much chocobars? 10 sugar = chocobar"))
    sugar = sugar - ans * 10
    chocobar = chocobar + ans
  elif ans = "CS":
    ans = int(input("How much sugar? chocobar = 10 sugar"))
    sugar = sugar + ans
    chocobar = chocobar - ans / 10
  elif ans = "STS":
    #banksugar = 0
    sugar = sugar + banksugar
    print("The bank quickly refils")
  elif ans = "STC":
    chocobar = chocobar + bankchocobar / 4
 
def choice():
  rand = random.randrange(0,1)
  if rand = 0:
    intro()
  else:
    sugarintro()
    
choice()
  
