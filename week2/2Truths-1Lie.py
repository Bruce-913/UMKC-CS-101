import random

def fact(given_fact):
    if given_fact == 1:
        print ("I enjoy programming a lot more now!")
        return 1
    elif given_fact ==2:
        print ("I am amazing at videogames!")
        return 1
    else:
        print("I love Summer!")
        return 2
    
def game():
    fact_number = [1, 2, 3]
    random.shuffle(fact_number)

    incorrect_guess = 0

    print ("Welcome to 2 TRUTHS AND 1 LIE!")
    print ("Truth or Lie?")

    while incorrect_guess < 2:
        while True:
            random_fact = fact_number.pop(0)
            correct_answer = fact(random_fact)
            try:
                
                answer = int(input("1 - Truth\n2 - Lie\nChoice==>"))
                if answer == 1 or answer == 2:
                    break
                else:
                    print("Invalid entry. Type 1 for true and 2 for lie.")
            except ValueError:
                print("Invalid literal. Type 1 for true or 2 for lie.")

        if answer == correct_answer:
            print("Good Job! You know me well!")
            continue
        else:
            incorrect_guess += 1
            print(f"Incorrect guess!")    
    else:
        incorrect_guess == 2
        print("Oh No! You are out of guesses.")

def game_loop():
    while True:
        game()
        retry = input("Do you wish to retry?(y/n)")
        if retry != "y":
            print("Thanks for playing!")
            break
game_loop()