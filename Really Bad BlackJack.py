import random


#Set starting cash
cash = 500

while cash > 0:
    #Take bet from player (validate input)
    while True:
        try:
            #Looking for an integer
            print ("Cash: ", cash, "\n")
            bet = int(input("How much will you bet:"))
        except ValueError:
            #Rejects values that aren't integers
            print("Invalid Response")
        else:
            if bet > cash:
                print("You can't afford this")
                continue
            else:
                break
    
    # Make dealer sum of 2 random numbers between 1 and 10
    dealer = random.randint(1,10)
    dealer = dealer + random.randint(1,10)
    # Make player sum of 2 random numbers between 1 and 10
    player = random.randint(1,10)
    player = player + random.randint(1, 10)

    #Print Hand Values
    print ("Dealer's Hand:", dealer, "\n")
    print ("Player's Hand:", player, "\n")
    


    while player < 21:

        #Ask For Player's Action
        action = str(input("Hit, Double, or Stand \n"))
        
        print
        #When Input is Hit, will "draw a card" adding to players total then display the hand totals
        if action == 'Hit':
            player = player + random.randint(1, 10)
            print ("Dealer's Hand:", dealer)
            print ("Player's Hand:", player)
            print ("---------------------------------")
            
            #breaks out of while loop when player total is higher than 21 (this is repeated in other actions and I think I can shorten the code by a few lines if I were to have the checks for bust/blackjacks outside of the IF conditions instead)
            if player > 21:
                print ("Bust")
                cash = cash - bet
                break
            elif player < 21:
                continue
            #If player gets blackjack they get extra money compared to a normal win
            else:
                print ("Blackjack!")
                cash = cash + (bet * 1.5)
                break
       
       #Increases the bet total by *2, less useful than in normal blackjack since all possibilities have the same weight
        elif action == 'Double':
            bet = bet * 2
            player = player + random.randint(1, 10)
            print ("Player's Hand:", player, "\n")
            print ("Dealer's Hand:", dealer, "\n") 
            if player > 21:
                print ("Bust")
                print ("--------------------------------- \n")
                cash = cash - bet
            elif player < 21:
                continue
            else:
                print ("Player Blackjack!")
                print ("--------------------------------- \n")
                cash = cash + (bet * 1.5)
                break
        
        #If Player stands it checks dealers values, dealer essentially "stands" at 17+ otherwise it draws, 
        elif action == 'Stand':
            if dealer > 21:
                print ("Player's Hand:", player, "\n")
                print ("Dealer's Hand:", dealer, "\n") 
                print("Dealer Bust")
                print ("--------------------------------- \n")
                cash = bet * 2
                break
            elif dealer < 21:
                if dealer >= 17:
                    if dealer > player:
                        print ("Player's Hand:", player, "\n")
                        print ("Dealer's Hand:", dealer, "\n")
                        print ("The House Wins")
                        print ("--------------------------------- \n")
                        cash = cash - bet
                        break
                    else:
                        print ("Player's Hand:", player, "\n")
                        print ("Dealer's Hand:", dealer, "\n")
                        print ("Player Win")
                        cash = cash + bet
                        break
                #This shouldn't really loop back to player input and should have dealer continue to draw until they reach 17+ or bust, but for now they just draw and give the player chance to decide if they want to do something else
                elif dealer < 17:
                    dealer = dealer + random.randint(1, 10)
                    print ("Player's Hand:", player, "\n")
                    print ("Dealer's Hand:", dealer, "\n")
                    print ("--------------------------------- \n")
                else:
                    print ("I do not know what just happened")
        #If player enters something that isn't hit double or stand, tells them its invalid and loop continues
        else:
            print ("Invalid Input")
