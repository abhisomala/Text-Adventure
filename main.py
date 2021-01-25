affirmative_answers = ["yes", "yeah", "sure", "yup", "okay", "of course", "alright", "certainly", "absolutely", "by all means", "yup", "ok", "okie", "yea", "why not", "lets begin"]
negative_answers = ["naw", "never", "absolutly not""no", "nope", "nah","not a chance", "sorry", "never", "no way"] 
print("Welcome to my Text Adventure!")

name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10

if age >= 13:
    print("Hi", name, "you are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play in affirmative_answers:

        print("You are starting with", health, "health")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")

        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")

            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("Congrats you have succesfully survived... You win!")

            else:
                print("You fell in the river and lost...")


        else:
            print("You fell down and lost...")

    else:
        print("Good bye")
else:
    print("Sorry, you are not old enough to play")