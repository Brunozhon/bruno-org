import time, ramdom
which = ans = rand = None
dog = cat = hamster = 0

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
  
intro()
