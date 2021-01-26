affirmative_answers = ["yes", "yeah", "sure", "yup", "okay", "of course", "alright", "certainly", "absolutely", "by all means", "yup", "ok", "okie", "yea", "why not", "lets begin"]
negative_answers = ["naw", "never", "absolutly not""no", "nope", "nah","not a chance", "sorry", "never", "no way"] 
print("Welcome to Text Adventure!")

name = input("\nWhat is your name? ")
age = int(input("\nWhat is your age? "))
health = 15

if age >= 13:
  print("\nHi", name, "you are old enough to play!")
else:
  print("\nSorry, you are not old enough to play")
  quit()

wants_to_play = input("\nDo you want to play? ").lower()
if wants_to_play in affirmative_answers:
  print("\nYou are starting with", health, "health")
  print("\nLet's play!")
else:
  print("\nGood bye")
  quit()   
        
left_or_right = input("\nOn your left you see a muddy path and on your right you see a hill. Do you want to go right or left? (left/right)? ")

if left_or_right == "left":
  ans = input("\nNice, you follow the path and reach a lake... Do you want to swim across or go around.(across/around)? ")
else:
  print("\nYou fell down and lost...")
  quit()
            

if ans == "around":
 print("\nYou went around and reached the other side of the lake.")
elif ans == "across":
  print("\nYou managed to get across, but were bit by a fish and lost 5 health.")
  health -= 5

ans = input("\nYou notice a house that might have some food and a river that you want to go to for some odd reason. Where do you go? (river/house)? ")

if ans == "house":
  print("\nYou go to the house and are greeted by the owner") 
else:
  print("\nTurns out the river has sharks. You lost 5 health")
  health -= 5

ans = input("\nThere is a forest on your right and on your left there is a cave. Which one do you enter. (forest/cave)")

if ans == "forest":
  print("\nYou are now in the forest and see berries. They may recover your health but they may also be poisonous ")
  ans = input("\n Do you want to eat the berry or walk away from it? (eat/ walk away)")
  if ans == "eat":
    print("The berry tasted amazing and you feel energized again! You gained 5 health.")
    health += 5
  
elif ans == "cave":
  print("\nYou enter the cave and presented with 2 pathways.")
  ans = input("\n The left pathway leads deeper into the cave. It may contain treasure. Then the right pathway seems to lead to the exit. Which one will you choose? (Left/Right)")

if health <= 0:
  print("\nYou now have 0 health and you lost the game...")


elif health >= 1:
 print("\nCongrats you have succesfully survived... You win!")



