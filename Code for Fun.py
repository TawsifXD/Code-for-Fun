print("\nHello there, This is just simple quiz! just type N or Y\n \nFor your attention N = No and Y = Yes :)")
print("\nLet's Strat\n")
def ask(answer):
    yesorno = input(answer).lower().upper()
    if yesorno == "Y" or yesorno == "N":
        return yesorno
    else:
        print("Please Enter Y or N only")
        return ask
animel_one = ask("Is Riya can fly ? Y/N: ")
if animel_one == "N":
    print("Yes kid. Keep Going :)")
    animel_two = ask("Is rabbit is an animel ? Y/N: ")
    if animel_two == "Y":
        print("Currect Answer kid. Nice one")
        animel_three = ask("Is Man eat grass ? Y/N: ")
        if animel_three == "N":
            print("Yahh.. Man don't eat grass, Cow eat's grass (COW) ")
            animel_four = ask("Is man make money? Y/N: ")
            if animel_four == "Y":
                print("Yahh boy.... Let's Gooooo .")
                animel_five = ask("Is man need women in her life? Y/N: ")
                if animel_five == "Y":
                    print("Yah, Man need women in her life")
                    animel_six = ask("A man need money to servive ? Y/N: ")
                    if animel_six == "Y":
                        print("Yes, You are right, But i have no money! \nPlease bikash me for a coffee. My number is: 01722287869")
                    else:
                        print("You are wrong bro! A man can't servive her life without money broo.")
                elif animel_five == "N":
                    print("Only gay people don't need women in her life.Czz gay like man. Then you are a ...... prove me worng!")
            elif animel_four == "N":
                print("WHf ? Man make money broo .You thing animels make money ? prove me wrong !")
        elif animel_three == "Y":
            print("LOL, You eat grass ! whtf ?")
    elif animel_two == "N":
        print("Ehhh ? wht")
elif animel_one == "Y":
    print("I think your wits are below the knee, Try again")