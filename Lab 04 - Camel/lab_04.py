import random


def print_intro():
    print("Welcome to the Coyote Escape!")
    print("You have stolen a Mizutani Shion 'Coyote' to make your way across the desert and out of Night City.")
    print("The Aldecaldo Nomad family wants their car back and are chasing you down!")
    print("You were wounded in the escape and need to heal throughout the run")
    print("To make matters worse, the gas line is wrecked. You will have to refuel constantly.")
    print("Survive your desert trek and outrun the nomads to cross the border into Arizona.")


def main():
    print_intro()

    miles_traveled = 0
    gas_level = 10  # Starting gas level
    nomads_distance = -20
    health_points = 10
    ambushed = 0
    done = False

    while not done:
        print("\nA. Drive at moderate speed.")
        print("B. Drive at full speed.")
        print("C. Stop to refuel.")
        print("D. Use an airhypo")
        print("E. Status check.")
        print("Q. Quit.")

        choice = input("Your choice: ").upper()

        if choice == "Q":
            print("\nCouldn't handle the pressure I see?")
            done = True
        elif choice == "E":
            print(f"\nMiles traveled: {miles_traveled}")
            print(f"Gas level: {gas_level}")
            print(f"The nomads are {miles_traveled - nomads_distance} miles behind you.")
            print(f"Your biomonitor shows: {health_points}")
        elif choice == "D":
            health_points = 10  # Healing
            print("\nYou inject yourself and get that fuzzy feeling.")
            nomads_distance += random.randint(7, 14)
        elif choice == "C":
            gas_level = 10  # Refuel gas
            print("\nThe Coyote is fueled up and ready to go.")
            nomads_distance += random.randint(7, 14)
            health_points -= random.randint(1, 2)
        elif choice == "B":
            miles = random.randint(15, 20)
            miles_traveled += miles
            gas_level -= random.randint(3, 4)
            nomads_distance += random.randint(7, 14)
            health_points -= random.randint(1, 2)
            print(f"\nYou drove {miles} miles.")
            if miles_traveled >= 100 and ambushed == 0:
                print("\nYou are halfway to Arizona!")
                print("Suddenly, you are ambushed by the Night City Police!")
                print("What will you do?")
                print("\nA. Fight back.")
                print("B. Try to run.")
                ambush_choice = input("Your choice: ").upper()
                if ambush_choice == "A":
                    print("\nYou chose to fight back! A fierce battle ensues.")
                    if health_points >= 4:
                        print("Though injured, you successfully fight off the cops and continue your escape.")
                        ambushed = 1
                    else:
                        print("\nUnfortunately, the cops overpower you. Game over!")
                        done = True
                elif ambush_choice == "B":
                    print("\nYou smash the accelerator to the floor.")
                    if gas_level >= 4:
                        print("You are able to outrun the ambush and continue your escape.")
                        ambushed = 1
                    else:
                        print("You run out of gas and are unable to escape the trap. Game Over!")
                        done = True
                else:
                    print("\nInvalid choice. You hesitate, and the cops capture you. Game over!")
                    done = True
        elif choice == "A":
            miles = random.randint(10, 15)
            miles_traveled += miles
            gas_level -= random.randint(1, 3)
            nomads_distance += random.randint(7, 14)
            health_points -= random.randint(1, 2)
            print(f"\nYou drove {miles} miles.")
            # Check if the player is halfway to Arizona
            if miles_traveled >= 100 and ambushed == 0:
                print("\nYou are halfway to Arizona!")
                print("Suddenly, you are ambushed by the Night City Police!")
                print("What will you do?")
                print("\nA. Fight back.")
                print("B. Try to run.")
                ambush_choice = input("Your choice: ").upper()
                if ambush_choice == "A":
                    print("\nYou choose to fight back! A fierce battle ensues.")
                    if health_points >= 5:
                        print("Though injured, you successfully fight off the cops and continue your escape.")
                        ambushed = 1
                    else:
                        print("Unfortunately, the cops overpower you. Game over!")
                        done = True
                elif ambush_choice == "B":
                    print("\nYou smash the accelerator to the floor")
                    if gas_level >= 5:
                        print("You are able to outrun the ambush and continue your escape")
                        ambushed = 1
                    else:
                        print("You run out of gas and are unable to escape the trap. Game Over!")
                        done = True
                else:
                    print("Invalid choice. You hesitate, and the cops capture you. Game over!")
                    done = True
        else:
            print("Invalid choice. Please enter A, B, C, D, E, or Q.")

        # Check if the player has won or lost
        if nomads_distance >= miles_traveled:
            print("\nThe nomads caught up to you. Your legs are broken and you are left in the desert. Game over!")
            done = True
        elif miles_traveled >= 200:
            print("\nCongratulations! You have successfully crossed the border into Arizona and escaped the nomads!")
            done = True
        elif health_points <= 0:
            print("\nYour escape comes to an end as you bleed out behind the wheel of the stolen 'Coyote'. Game Over!")
            done = True

        if not done and gas_level <= 0:
            print("You damage the car by driving with no gas. The nomads caught up to you. Game over!")
            done = True


if __name__ == "__main__":
    main()
