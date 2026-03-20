"""GAMES"""

# Games
def random_number():
    """Guess the Random Number"""
    import random
    import time
    x = 0
    magic_number = random.randint(1, 100)
    while True:
        guess = int(input("(0-100) Guess the number: "))
        x += 1
        if guess > magic_number:
            print(f"Lower than {guess}")
        if guess < magic_number:
            print(f"Higher than {guess}")
        if guess == magic_number:
            print(f"Horray!\nYou guessed the magic number in {x} tries!")
            x = 0
            time.sleep(3)
            break

def rps():
    """Rock Paper Scissors"""
    import random
    import time
    bot_score  = 0
    player_score = 0
    while True:
        rps_bot = random.randint(1, 3)
        if rps_bot == 1:
            rps_bot = "Rock"
        if rps_bot == 2:
            rps_bot = "Paper"
        if rps_bot == 3:
            rps_bot = "Scissors"
        rps_player = input("(R)ock, (P)aper, (S)cissors (q to quit)\nInput: ").lower().strip()
        time.sleep(0.5)
        if rps_player == "r":
            rps_player = "Rock"
        if rps_player == "p":
            rps_player = "Paper"
        if rps_player == "s":
            rps_player = "Scissors"
        if rps_player == "q":
            break
        print(f"rps_player : {rps_player}")
        time.sleep(0.5)
        print(f"rps_bot : {rps_bot}")
        time.sleep(0.5)
        if rps_player == rps_bot:
            print("TIE!")
        #ROCK
        if rps_player == "Rock" and rps_bot == "Paper":
            print("rps_bot WNS!")
            bot_score += 1
        if rps_player == "Rock" and rps_bot == "Scissors":
            print("rps_player WINS!")
            player_score += 1
        #PAPER
        if rps_player == "Paper" and rps_bot == "Scissors":
            print("rps_bot WNS!")
            bot_score += 1
        if rps_player == "Paper" and rps_bot == "Rock":
            print("rps_player WINS!")
            player_score += 1
        #SCISSORS
        if rps_player == "Scissors" and rps_bot == "Rock":
            print("rps_bot WNS!")
            bot_score += 1
        if rps_player == "Scissors" and rps_bot == "Paper":
            print("rps_player WINS!")
            player_score += 1
        time.sleep(0.5)
        print("------------")
        print(f"PLAYER\tBOT\n  {player_score}\t {bot_score}")
        print("------------")
        time.sleep(1.5)

def diceroll():
    """Rolling Dice"""
    import random
    import time
    amount_dice = int(input("1 or 2 dice? "))
    if amount_dice == 1:
        dice1 = random.randint(1, 6)
        time.sleep(0.5)
        print(f"Dice 1 : {dice1}")
    if amount_dice == 2:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Dice 1: {dice1}")
        time.sleep(0.5)
        print(f"Dice 2: {dice2}")
        time.sleep(0.5)
        print(f"Total: {int(dice1) + int(dice2)}")
    time.sleep(3)

def blackjack(cash_total):
    """Compiles blackjack game"""
    import random
    import time
    dl_streak = 0
    pl_streak = 0
    line = "~" * 40
    if cash_total < 1:
        print("\nYou're broke, go play something else.")
        time.sleep(1.5)
        return cash_total
    
    def create_deck():
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        suits = ["♤", "♡", "♢", "♧"]
        deck = []
        for suit in suits:
            for number in cards:
                deck.append([number, suit])
        return deck

    def deal(deck):
        dl_hand = []
        pl_hand = []
        dl_hand.append(random.choice(deck))
        deck.pop(deck.index(dl_hand[0]))
        dl_hand.append(random.choice(deck))
        deck.pop(deck.index(dl_hand[1]))
        pl_hand.append(random.choice(deck))
        deck.pop(deck.index(pl_hand[0]))
        pl_hand.append(random.choice(deck))
        deck.pop(deck.index(pl_hand[1]))
        
        return dl_hand, pl_hand

    def print_cards(dl_hand=0, pl_hand=0, pl_in=0):
        """PRINTING BLAKCJACK CARDS"""
        l1 = ""
        l2 = ""
        l3 = ""
        l4 = ""
        l5 = ""
        l6 = ""
        l7 = ""
        if len(dl_hand) > 2 or pl_in == "s":
            for card, suit in dl_hand:
                l1 += "_________ "
                l2 += f"|{card:2}     | "
                l3 += "|       | "
                l4 +=f"|   {suit}   | "
                l5 += "|       | "
                l6 +=f"|     {card:2}| "
                l7 +="‾‾‾‾‾‾‾‾‾ "
        else:
            l1 += "_________ _________ "
            l2 += f"|{dl_hand[0][0]:2}     | |{"X":2}     | "
            l3 += "|       | |       | "
            l4 +=f"|   {dl_hand[0][1]}   | |   ?   | "
            l5 += "|       | |       | "
            l6 +=f"|     {dl_hand[0][0]:2}| |     {"X":2}| "
            l7 +="‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ "
        l1 += "|"
        l2 += "|"
        l3 += "|"
        l4 += "|"
        l5 += "|"
        l6 += "|"
        l7 += "|"
        

        for card, suit in pl_hand:
            l1 += " _________ "
            l2 += f" |{card:2}     | "
            l3 += " |       | "
            l4 +=f" |   {suit}   | "
            l5 += " |       | "
            l6 +=f" |     {card:2}| "
            l7 += " ‾‾‾‾‾‾‾‾‾ "
        print(f"{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}\n{l7}")

    def card_logic(pl_hand=0, dl_hand=0, pl_in=0, show_dl_hand=0):
        """CARD LOGIC FOR VALUES"""
        pl_total = [0, 0]
        dl_total = [0, 0]
        if pl_in == "s":
            show_dl_hand = True

        for card in pl_hand:
            if card[0] in ("K", "Q", "J"):
                pl_total[0] += 10
                pl_total[1] += 10
            elif card[0] == "A" and pl_total[0] != pl_total[1]:
                pl_total[0] += 1
                pl_total[1] += 1
            elif card[0] == "A":
                pl_total[0] += 1
                pl_total[1] += 11
            elif card[0] in range(2, 11):
                pl_total[0] += card[0]
                pl_total[1] += card[0]

        if show_dl_hand is True:
            for card in dl_hand:
                if card[0] in ("K", "Q", "J"):
                    dl_total[0] += 10
                    dl_total[1] += 10
                elif card[0] == "A" and dl_total[0] != dl_total[1]:
                    dl_total[0] += 1
                    dl_total[1] += 1
                elif card[0] == "A":
                    dl_total[0] += 1
                    dl_total[1] += 11
                elif card[0] in range(2, 11):
                    dl_total[0] += card[0]
                    dl_total[1] += card[0]
        else:
            if dl_hand[0][0] in ("K", "Q", "J"):
                dl_total[0] += 10
                dl_total[1] += 10
            elif dl_hand[0][0] == "A":
                dl_total[0] += 1
                dl_total[1] += 11
            else:
                dl_total[0] += dl_hand[0][0]
                dl_total[1] += dl_hand[0][0]

        if pl_total[1] > 21:
            pl_total[1] = pl_total[0]

        if dl_total[1] > 21:
            dl_total[1] = dl_total[0]


        if pl_total[0] == pl_total[1] and dl_total[0] == dl_total[1]:
            print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}")

        elif pl_total[0] != pl_total[1] and dl_total[0] != dl_total[1]:
            if pl_total[1] <= 21 and dl_total[1] <= 21:
                print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}/{dl_total[1]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}/{pl_total[1]}")
            elif pl_total[1] > 21:
                print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}/{dl_total[1]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}")
            elif dl_total[1] > 21:
                print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}/{pl_total[1]}")
            else:
                print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}")

        elif pl_total[0] != pl_total[1] and pl_total[1] > 21:
            print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}")
        elif dl_total[0] != dl_total[1] and dl_total[1] > 21:
            print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}")
        elif pl_total[0] != pl_total[1] and pl_total[1] < 21:
            print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}/{pl_total[1]}")
        elif dl_total[0] != dl_total[1] and dl_total[1] < 21:
            print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}/{dl_total[1]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}")

        elif pl_total[1] == 21 and len(pl_total) < 3:
            if dl_total[0] != dl_total[1]:
                print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}/{dl_total[1]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), "PLAYER: Blackjack")
            else:
                print(" " * (len(dl_hand) * 2), f"DEALER: {dl_total[0]}", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), "PLAYER: Blackjack")
        elif dl_total[1] == 21 and len(dl_total) < 3:
            if pl_total[0] != pl_total[1]:
                print(" " * (len(dl_hand) * 2), "DEALER: Blackjack", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}/{pl_total[1]}")
            else:
                print(" " * (len(dl_hand) * 2), "DEALER: Blackjack", " " * (len(dl_hand) * 2 + len(pl_hand) * 4), f"PLAYER: {pl_total[0]}")



        return pl_total, dl_total

    def game(deck, dl_hand, pl_total, dl_total, pl_win, dl_win):
        while dl_total[0] < 17 and dl_total[1] < pl_total[1]:

        
            next_card = random.choice(deck)
            deck.remove(next_card)
            dl_hand.append(next_card)

            print_cards(dl_hand, pl_hand)
            pl_total, dl_total = card_logic(pl_hand, dl_hand, "s", True)
            time.sleep(1)

        if dl_total[1] > 21:
            print("DEALER BUST | PLAYER WINS")
            pl_win = True
            
        elif pl_total[1] > dl_total[1]:
            print("PLAYER WINS")
            pl_win = True
            
        elif pl_total[1] < dl_total[1]:
            print("DEALER WINS")
            dl_win = True
            
        elif pl_total[1] == dl_total[1]:
            print("STANDOFF")
                
            

        return pl_win, dl_win

    #def split():
        #pl_hand
            
    #def double_down():
        #dl_hand

    while True:
        print(line) 
        print(f"  DEALER STREAK\t  PLAYER STREAK\n\t{dl_streak}\t\t{pl_streak}")
        print(line)

        pl_win = False
        dl_win = False

        deck = create_deck()
        while True:
            print(f"Cash: ${cash_total}")
            bet = float(input("($1.00 minimum) Place your bet: $"))
            if bet > cash_total:
                print("Invalid amount.")
            else:
                break
        
        dl_hand, pl_hand = deal(deck)
        print_cards(dl_hand, pl_hand)
        pl_total, dl_total = card_logic(pl_hand, dl_hand, 0)
        
        while True:
            pl_in = input("(S)tand, (H)it\nINPUT: ").lower().strip()
            if pl_in == "s":
                print("DEALER CARD REVEALED")
                print_cards(dl_hand, pl_hand, pl_in)
                pl_total, dl_total = card_logic(pl_hand, dl_hand, pl_in, True)
                time.sleep(1.5)
                pl_win, dl_win = game(deck, dl_hand, pl_total, dl_total, pl_win, dl_win)
                break
                
            if pl_in == "h":
                next_card = random.choice(deck)
                deck.pop(deck.index(next_card))
                pl_hand.append(next_card)
                print_cards(dl_hand, pl_hand)
                pl_total, dl_total = card_logic(pl_hand, dl_hand)
                time.sleep(1)

                if pl_total[0] == pl_total[1] and pl_total[0] > 21:
                    print("PLAYER BUST | DEALER WINS")
                     
                    dl_win = True
                    time.sleep(1)
                    break

                if pl_total[0] != pl_total[1]:
                    if pl_total[0] > 21:
                        print("PLAYER BUST | DEALER WINS")
                        dl_win = True
                        time.sleep(1)
                        break
        if pl_win is True:
            cash_total += bet
            print(f"\nYou won ${bet:2}\nYour new total is ${cash_total:2}")
            pl_streak += 1
            dl_streak = 0
        elif dl_win is True:
            cash_total -= bet
            print(f"\nYou lost ${bet:2}\nYour new total is ${cash_total:2}")
            dl_streak += 1
            pl_streak = 0
        elif dl_win is False and pl_win is False:
            print(f"\nYou get your bet back ${bet:2}\nYour total is still ${cash_total:2}")

        if cash_total < 1:
            print("\nYou're broke, go play something else.")
            time.sleep(1.5)
            return cash_total

        while pl_in not in ("c", "p"):
            pl_in = input("(P)lace a bet|(C)ash out\nEntry: ").lower().strip()
            if pl_in not in ("c", "p"):
                print("Invalid Entry.")

        if pl_in == "c":
            print(f"You cashed out with ${cash_total:2}")
            time.sleep(1)
            return cash_total
        elif pl_in == "p":
            pass

def thirty_one():
    """Thirty one card game"""
    import random

    def deal2(deck):
        pick = random.choice(deck)
        p1c1 = pick
        deck.pop(deck.index(pick))
        pick = random.choice(deck)
        p2c1 = pick
        deck.pop(deck.index(pick))
        pick = random.choice(deck)
        p1c2 = pick
        deck.pop(deck.index(pick))
        pick = random.choice(deck)
        p2c2 = pick
        deck.pop(deck.index(pick))
        pick = random.choice(deck)
        p1c3 = pick
        deck.pop(deck.index(pick))
        pick = random.choice(deck)
        p2c3 = pick
        deck.pop(deck.index(pick))
        return p1c1, p2c1, p1c2, p2c2, p1c3, p2c3

    def deal3(deck):
        pick = random.choice(deck)
        p1c1 = pick
        deck.pop(pick)
        pick = random.choice(deck)
        p2c1 = pick
        deck.pop(pick)
        pick = random.choice(deck)
        p3c1 = pick
        deck.pop(pick)
        pick = random.choice(deck)
        p1c2 = pick
        deck.pop(pick)
        pick = random.choice(deck)
        p2c2 = pick
        deck.pop(pick)
        pick = random.choice(deck)
        p3c2 = pick
        deck.pop(pick)
        pick = random.choice(deck)
        p1c3 = pick
        deck.pop(pick)
        pick = random.choice(deck)
        p2c3 = pick
        deck.pop(pick)
        pick = random.choice(deck)
        p3c3 = pick
        deck.pop(pick)
        return p1c1, p2c1, p3c1, p1c2, p2c2, p3c2, p1c3, p2c3, p3c3

    cards = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
    suits = ("♤", "♡", "♢", "♧")
    deck = []
    end_game = False
    for suit in suits:
        for card in cards:
            deck.append([card, suit])
    face = random.choice(deck)
    deck.pop(deck.index(face))
    players = int(input("How many players?\n(2)(3)(4)(5)\nINPUT: "))
    if players == 2:
        p1c1, p2c1, p1c2, p2c2, p1c3, p2c3 = deal2(deck)
        face = random.choice(deck)
        deck.pop(deck.index(face))
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t   DISCARD\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while end_game == False:
            if input("(Y/N) Player 1? ").lower() in ("y", "yes"):
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t    PILE\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾")
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________\n|{p1c1[0]:2}     | |{p1c2[0]:2}     | |{p1c3[0]:2}     |\n|       | |       | |       |\n|   {p1c1[1]}   | |   {p1c2[1]}   | |   {p1c3[1]}   |\n|       | |       | |       |\n|     {p1c1[0]:2}| |     {p1c2[0]:2}| |     {p1c3[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                cycle = True
                while cycle == True:
                    choice = input("    PICK UP\n(D)eck (P)ile\nor\n(K)nock\nINPUT: ").lower()
                    if choice == "d":
                        pick = random.choice(deck)
                        deck.pop(deck.index(pick))
                        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________ _________\n|{p1c1[0]:2}     | |{p1c2[0]:2}     | |{p1c3[0]:2}     | |{pick[0]:2}     |\n|       | |       | |       | |       |\n|   {p1c1[1]}   | |   {p1c2[1]}   | |   {p1c3[1]}   | |   {pick[1]}   |\n|       | |       | |       | |       |\n|     {p1c1[0]:2}| |     {p1c2[0]:2}| |     {p1c3[0]:2}| |     {pick[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        choice = int(input("DISCARD ONE:\n(1)(2)(3)(4)\nINPUT: "))
                        while True:
                            if choice == 1:
                                face = p1c1
                                p1c1 = p1c2
                                p1c2 = p1c3
                                p1c3 = pick
                                break
                            if choice == 2:
                                face = p1c2
                                p1c2 = p1c3
                                p1c3 = pick
                                break
                            if choice == 3:
                                face = p1c3
                                p1c3 = pick
                                break
                            if choice == 4:
                                face = pick
                                break
                        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t   DISCARD\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        cycle = False
                    if choice == "p":
                        pick = face
                        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________ _________\n|{p1c1[0]:2}     | |{p1c2[0]:2}     | |{p1c3[0]:2}     | |{face[0]:2}     |\n|       | |       | |       | |       |\n|   {p1c1[1]}   | |   {p1c2[1]}   | |   {p1c3[1]}   | |   {face[1]}   |\n|       | |       | |       | |       |\n|     {p1c1[0]:2}| |     {p1c2[0]:2}| |     {p1c3[0]:2}| |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        choice = int(input("DISCARD ONE:\n(1)(2)(3)\nINPUT: "))
                        while True:
                            if choice == 1:
                                face = p1c1
                                p1c1 = p1c2
                                p1c2 = p1c3
                                p1c3 = pick
                                break
                            if choice == 2:
                                face = p1c2
                                p1c2 = p1c3
                                p1c3 = pick
                                break
                            if choice == 3:
                                face = p1c3
                                p1c3 = pick
                                break
                        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t   DISCARD\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        cycle = False

                    if choice == "k":
                        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t   DISCARD\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("PLAYER 1 KNOCKED!")
                        if input("(Y/N) Player 2?\nINPUT: ").lower() in ("y", "yes"):
                            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t    PILE\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾")
                            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________\n|{p2c1[0]:2}     | |{p2c2[0]:2}     | |{p2c3[0]:2}     |\n|       | |       | |       |\n|   {p2c1[1]}   | |   {p2c2[1]}   | |   {p2c3[1]}   |\n|       | |       | |       |\n|     {p2c1[0]:2}| |     {p2c2[0]:2}| |     {p2c3[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            choice = input("    PICK UP\n(D)eck (P)ile\nINPUT: ").lower()
                            cycle = True
                            while cycle == True:
                                if choice == "d":
                                    pick = random.choice(deck)
                                    deck.pop(deck.index(pick))
                                    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________ _________\n|{p2c1[0]:2}     | |{p2c2[0]:2}     | |{p2c3[0]:2}     | |{pick[0]:2}     |\n|       | |       | |       | |       |\n|   {p2c1[1]}   | |   {p2c2[1]}   | |   {p2c3[1]}   | |   {pick[1]}   |\n|       | |       | |       | |       |\n|     {p2c1[0]:2}| |     {p2c2[0]:2}| |     {p2c3[0]:2}| |     {pick[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    choice = int(input("DISCARD ONE:\n(1)(2)(3)(4)\nINPUT: "))
                                    if choice == 1:
                                        face = p1c1
                                        p1c1 = p1c2
                                        p1c2 = p1c3
                                        p1c3 = pick
                                        break
                                    if choice == 2:
                                        face = p1c2
                                        p1c2 = p1c3
                                        p1c3 = pick
                                        break
                                    if choice == 3:
                                        face = p1c3
                                        p1c3 = pick
                                        break
                                    if choice == 4:
                                        face = pick
                                        break
                                print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t   DISCARD\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                cycle = False
                                if choice =="p":
                                    pick = face
                                    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________ _________\n|{p2c1[0]:2}     | |{p2c2[0]:2}     | |{p2c3[0]:2}     | |{face[0]:2}     |\n|       | |       | |       | |       |\n|   {p2c1[1]}   | |   {p2c2[1]}   | |   {p2c3[1]}   | |   {face[1]}   |\n|       | |       | |       | |       |\n|     {p2c1[0]:2}| |     {p2c2[0]:2}| |     {p2c3[0]:2}| |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    choice = int(input("DISCARD ONE:\n(1)(2)(3)\nINPUT: "))
                                    while True:
                                        if choice == 1:
                                            face = p1c1
                                            p1c1 = p1c2
                                            p1c2 = p1c3
                                            p1c3 = pick
                                            break
                                        if choice == 2:
                                            face = p1c2
                                            p1c2 = p1c3
                                            p1c3 = pick
                                            break
                                        if choice == 3:
                                            face = p1c3
                                            p1c3 = pick
                                            break
                                    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t   DISCARD\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                cycle = False
                            
                        print("FINAL DISPLAY")
                        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\tPLAYER 1 CARDS\n_________ _________ _________\n|{p1c1[0]:2}     | |{p1c2[0]:2}     | |{p1c3[0]:2}     |\n|       | |       | |       |\n|   {p1c1[1]}   | |   {p1c2[1]}   | |   {p1c3[1]}   |\n|       | |       | |       |\n|     {p1c1[0]:2}| |     {p1c2[0]:2}| |     {p1c3[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(f"\tPLAYER 2 CARDS\n_________ _________ _________\n|{p2c1[0]:2}     | |{p2c2[0]:2}     | |{p2c3[0]:2}     |\n|       | |       | |       |\n|   {p2c1[1]}   | |   {p2c2[1]}   | |   {p2c3[1]}   |\n|       | |       | |       |\n|     {p2c1[0]:2}| |     {p2c2[0]:2}| |     {p2c3[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
                        return

            if input("(Y/N) Player 2?\nINPUT: ").lower() in ("y", "yes"):
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t    PILE\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾")
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________\n|{p2c1[0]:2}     | |{p2c2[0]:2}     | |{p2c3[0]:2}     |\n|       | |       | |       |\n|   {p2c1[1]}   | |   {p2c2[1]}   | |   {p2c3[1]}   |\n|       | |       | |       |\n|     {p2c1[0]:2}| |     {p2c2[0]:2}| |     {p2c3[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                cycle = True
                while cycle == True:
                    choice = input("    PICK UP\n(D)eck (P)ile\nor\n(K)nock\nINPUT: ").lower()
                    if choice == "d":
                        pick = random.choice(deck)
                        deck.pop(deck.index(pick))
                        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________ _________\n|{p2c1[0]:2}     | |{p2c2[0]:2}     | |{p2c3[0]:2}     | |{pick[0]:2}     |\n|       | |       | |       | |       |\n|   {p2c1[1]}   | |   {p2c2[1]}   | |   {p2c3[1]}   | |   {pick[1]}   |\n|       | |       | |       | |       |\n|     {p2c1[0]:2}| |     {p2c2[0]:2}| |     {p2c3[0]:2}| |     {pick[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        choice = int(input("DISCARD ONE:\n(1)(2)(3)(4)\nINPUT: "))
                        while True:
                            if choice == 1:
                                face = p2c1
                                p2c1 = p2c2
                                p2c2 = p2c3
                                p2c3 = pick
                                break
                            if choice == 2:
                                face = p2c2
                                p2c2 = p2c3
                                p2c3 = pick
                                break
                            if choice == 3:
                                face = p2c3
                                p2c3 = pick
                                break
                            if choice == 4:
                                face = pick
                                break
                        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t   DISCARD\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                        cycle = False
                    if choice =="p":
                        pick = face
                        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________ _________\n|{p2c1[0]:2}     | |{p2c2[0]:2}     | |{p2c3[0]:2}     | |{face[0]:2}     |\n|       | |       | |       | |       |\n|   {p2c1[1]}   | |   {p2c2[1]}   | |   {p2c3[1]}   | |   {face[1]}   |\n|       | |       | |       | |       |\n|     {p2c1[0]:2}| |     {p2c2[0]:2}| |     {p2c3[0]:2}| |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        choice = int(input("DISCARD ONE:\n(1)(2)(3)\nINPUT: "))
                        while True:
                            if choice == 1:
                                face = p2c1
                                p2c1 = p2c2
                                p2c2 = p2c3
                                p2c3 = pick
                                break
                            if choice == 2:
                                face = p2c2
                                p2c2 = p2c3
                                p2c3 = pick
                                break
                            if choice == 3:
                                face = p2c3
                                p2c3 = pick
                                break
                        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t   DISCARD\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                        cycle = False
                        
                    if choice == "k":
                        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t   DISCARD\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("PLAYER 2 KNOCKED!")
                        if input("(Y/N) Player 1?\nINPUT: ").lower() in ("y", "yes"):
                            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  DECK\t    PILE\n_________ _________\n|       | |{face[0]:2}     |\n|  ? ?  | |       |\n|   ?   | |   {face[1]}   |\n|  ? ?  | |       |\n|       | |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾")
                            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________\n|{p1c1[0]:2}     | |{p1c2[0]:2}     | |{p1c3[0]:2}     |\n|       | |       | |       |\n|   {p1c1[1]}   | |   {p1c2[1]}   | |   {p1c3[1]}   |\n|       | |       | |       |\n|     {p1c1[0]:2}| |     {p1c2[0]:2}| |     {p1c3[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            choice = input("    PICK UP\n(D)eck (P)ile\nINPUT: ").lower()
                            cycle = True
                            while cycle == True:
                                if choice == "d":
                                    pick = random.choice(deck)
                                    deck.pop(deck.index(pick))
                                    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________ _________\n|{p1c1[0]:2}     | |{p1c2[0]:2}     | |{p1c3[0]:2}     | |{pick[0]:2}     |\n|       | |       | |       | |       |\n|   {p1c1[1]}   | |   {p1c2[1]}   | |   {p1c3[1]}   | |   {pick[1]}   |\n|       | |       | |       | |       |\n|     {p1c1[0]:2}| |     {p1c2[0]:2}| |     {p1c3[0]:2}| |     {pick[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    choice = int(input("DISCARD ONE:\n(1)(2)(3)(4)\nINPUT: "))
                                    while True:
                                        if choice == 1:
                                            face = p1c1
                                            p1c1 = p1c2
                                            p1c2 = p1c3
                                            p1c3 = pick
                                            break
                                        if choice == 2:
                                            face = p1c2
                                            p1c2 = p1c3
                                            p1c3 = pick
                                            break
                                        if choice == 3:
                                            face = p1c3
                                            p1c3 = pick
                                            break
                                        if choice == 4:
                                            face = pick
                                            break
                                cycle = False
                                if choice == "p":
                                    pick = face
                                    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t  YOUR CARDS\n_________ _________ _________ _________\n|{p1c1[0]:2}     | |{p1c2[0]:2}     | |{p1c3[0]:2}     | |{face[0]:2}     |\n|       | |       | |       | |       |\n|   {p1c1[1]}   | |   {p1c2[1]}   | |   {p1c3[1]}   | |   {face[1]}   |\n|       | |       | |       | |       |\n|     {p1c1[0]:2}| |     {p1c2[0]:2}| |     {p1c3[0]:2}| |     {face[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    choice = int(input("DISCARD ONE:\n(1)(2)(3)\nINPUT: "))
                                    while True:
                                        if choice == 1:
                                            face = p1c1
                                            p1c1 = p1c2
                                            p1c2 = p1c3
                                            p1c3 = pick
                                            break
                                        if choice == 2:
                                            face = p1c2
                                            p1c2 = p1c3
                                            p1c3 = pick
                                            break
                                        if choice == 3:
                                            face = p1c3
                                            p1c3 = pick
                                            break
                                cycle = False
                        print("FINAL DISPLAY")
                        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\tPLAYER 1 CARDS\n_________ _________ _________\n|{p1c1[0]:2}     | |{p1c2[0]:2}     | |{p1c3[0]:2}     |\n|       | |       | |       |\n|   {p1c1[1]}   | |   {p1c2[1]}   | |   {p1c3[1]}   |\n|       | |       | |       |\n|     {p1c1[0]:2}| |     {p1c2[0]:2}| |     {p1c3[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(f"\tPLAYER 2 CARDS\n_________ _________ _________\n|{p2c1[0]:2}     | |{p2c2[0]:2}     | |{p2c3[0]:2}     |\n|       | |       | |       |\n|   {p2c1[1]}   | |   {p2c2[1]}   | |   {p2c3[1]}   |\n|       | |       | |       |\n|     {p2c1[0]:2}| |     {p2c2[0]:2}| |     {p2c3[0]:2}|\n‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
                        end_game = True
                        game_choose()


    if players == 3:
        deal3(deck)

# Game Selector
def game_choose():
    cash_total = 100
    while True:
        game_select = input("OPTIONS:\n#(1) Random number guessing game\n#(2) Rock Paper Scissors\n\
#(3) Dice roller\n#(4) Blackjack\n#(5) Thirty One\nInput: ").lower().strip()
        if game_select == "1":
            random_number()
        if game_select == "2":
            rps()
        if game_select == "3":
            diceroll()
        if game_select == "4":
            cash_total = blackjack(cash_total)
        if game_select == "5":
            thirty_one()

game_choose()
