def text():
    choice_1 = input("""You are in a city, you have to go do the doctor but the hospital feels weird,
    you have a choice, run now, or shrug it off and keep going type 'run' or 'keep going'
    in the terminal.""").strip()
    if choice_1 == 'run' or choice_1 == 'Run':
        print("while running you tripped and died, Game Over")
    elif choice_1 == 'keep going':
        choice_2 = input("You keep exploring and eventually the lights go out, what do you do: "
                         "scream or stay silent").strip()
        print(choice_2)
        if choice_2 == 'scream':
            print('something came from behind and killed you,' + ' '
                  'Game Over')
        elif choice_2 == 'stay silent':
            choice_3 = input("you barely keep going, you use the walls to guide you with your hand, you find a flashlight and a 9mm gun, then you see an exit sign, but something is blocking it, it says its friendly, "
                             "do you shoot it or accept his friendship?(type shoot for shoot and accept"
                             " for accepting)").strip()
            if choice_3 == 'shoot':
                print("YOU WIN, IT WAS HOSTILE, you make it to the exit and survive.")
            elif choice_3 == 'accept':
                print("it says thank you and moves out the wa,signalling you to exit, you get closer and finally exit... right? as soon as you step outisde, it grabs you and you DIE, GAME OVER ")



text()
























