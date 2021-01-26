affirmative_answers = ["yes", "yeah", "sure", "yup", "okay", "of course", "alright", "certainly", "absolutely", "by all means", "yup", "ok", "okie", "yea", "why not", "lets begin"]
negative_answers = ["naw", "never", "absolutly not""no", "nope", "nah","not a chance", "sorry", "never", "no way"] 
print("Welcome to my Text Adventure!")

name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10

if age >= 13:
  print("Hi", name, "you are old enough to play!")
else:
  print("Sorry, you are not old enough to play")
  quit()

wants_to_play = input("Do you want to play? ").lower()
if wants_to_play in affirmative_answers:
  print("You are starting with", health, "health")
  print("Let's play!")
else:
  print("Good bye")
  quit()   
        
left_or_right = input("On your left you see a muddy path and on your right you see a hill. Do you want to go right or left? (left/right)? ")

if left_or_right == "left":
  ans = input("Nice, you follow the path and reach a lake... Do you want to swim across or go around.(across/around)? ")
else:
  print("You fell down and lost...")
  quit()
            

if ans == "around":
 print("You went around and reached the other side of the lake.")
elif ans == "across":
  print("You managed to get across, but were bit by a fish and lost 5 health.")
  health -= 5

ans = input("You notice a house that might have some food and a river that you want to go to for some odd reason. Where do you go? (river/house)? ")

if ans == "house":
  print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
  health -= 5
  
else:
  print("Turns out the river has sharks. You died")

if health <= 0:
  print("You now have 0 health and you lost the game...")


elif health >= 1:
 print("Congrats you have succesfully survived... You win!")



