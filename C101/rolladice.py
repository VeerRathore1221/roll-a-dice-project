import random
response = input("Do you want to roll a dice?")
while response == "y":
        no = random.randint(1,6)
        if no == 1:

                print("[-----]")
                print("[     ]")
                print("[  0  ]")
                print("[     ]")
                print("[-----]")
                response = input("press n to exit and y to roll again: ")
                if(response != "y"):
                        print("Successfully exited the program")
        elif no == 2:

                print("[-----]")
                print("[0    ]")
                print("[     ]")
                print("[    0]")
                print("[-----]")
                response = input("Do you want to roll a dice?")
                if(response != "y"):
                        print("Successfully exited the program")
        elif no == 3:

                print("[-----]")
                print("[0    ]")
                print("[  0  ]")
                print("[    0]")
                print("[-----]")
                response = input("Do you want to roll a dice?")
                if(response != "y"):
                        print("Successfully exited the program")
        elif no == 4:

                print("[-----]")
                print("[0   0]")
                print("[     ]")
                print("[0   0]")
                print("[-----]")
                response = input("Do you want to roll a dice?")
                if(response != "y"):
                        print("Successfully exited the program")
        elif no == 5:

                print("[-----]")
                print("[0   0]")
                print("[  0  ]")
                print("[0   0]")
                print("[-----]")
                response = input("Do you want to roll a dice?")
                if(response != "y"):
                        print("Successfully exited the program")
        elif no == 6:

                print("[-----]")
                print("[0   0]")
                print("[0   0]")
                print("[0   0]")
                print("[-----]")
                response = input("Do you want to roll a dice?")
                if(response != "y"):
                        print("Successfully exited the program")
else:
        print("You did not roll a dice")
        