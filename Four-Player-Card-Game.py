# First, we define the priorities of each card from each suit in a dictionary called 'cards hierarchy'.
cards_hierarchy={'SA':13,'SK':12,'SQ':11,'SJ':10,'S10':9,'S9':8,'S8':7,'S7':6,'S6':5,'S5':4,'S4':3,'S3':2,'S2':1,'CA':13,'CK':12,'CQ':11,'CJ':10,'C10':9,'C9':8,'C8':7,'C7':6,'C6':5,'C5':4,'C4':3,'C3':2,'C2':1,'DA':13,'DK':12,'DQ':11,'DJ':10,'D10':9,'D9':8,'D8':7,'D7':6,'D6':5,'D5':4,'D4':3,'D3':2,'D2':1,'HA':13,'HK':12,'HQ':11,'HJ':10,'H10':9,'H9':8,'H8':7,'H7':6,'H6':5,'H5':4,'H4':3,'H3':2,'H2':1}
# We first define all the function that shall be used in the main program.
# Following function distributes the cards among four players by taking an input 'players', a list with 4 empty sub-lists.
def card_distributor(players):
    import random
    ordered_cards=['HA','CA','DA','SA','HK','CK','DK','SK','HQ','CQ','DQ','SQ','HJ','CJ','DJ','SJ','H10','C10','D10','S10','H9','C9','D9','S9','H8','C8','D8','S8','H7','C7','D7','S7','H6','C6','D6','S6','H5','C5','D5','S5','H4','C4','D4','S4','H3','C3','D3','S3','H2','C2','D2','S2']
    for i in range(13):
        for j in players:
            # Using the random module, we randomly choose a card from the list of all cards and then add the cards to the respective sub-list.
            # After appending the randomly chosen card, we remove the card from the list of all cards.
            card=random.choice(ordered_cards)
            j.append(card)
            ordered_cards.remove(card)
    # We return the list of each players' cards.
    return players
# This function is used for the 'call' that each bot makes at the start of every game.
def bot_call(botx_cards):
    call=0
    for i in botx_cards:
        if i[1]=='A' or i[1]=='K' or i[1]=='Q' or i[1]=='J':
            # For every card that is an Ace, a King, a Queen or a Joker, 'call' is increased by 1.
            call+=1
    # We return the call.
    return call
# This function randomly arranges the seating arrangement which will decide the order in which each round is played.
def seating_arrangement():
    import random
    all_players=['bot1','bot2','bot3','player']
    order=[]
    for i in range(4):
        # A player is chosen at random from the list of all players and is appended to 'order'.
        player_choice=random.choice(all_players)
        order.append(player_choice)
        # The randomly chosen player is removed from the list of all players so that no player is repeated.
        all_players.remove(player_choice)
    # 'order' is returned.
    return order
# This function decides what card the bot will play when it plays as the first player of the current round.
# It only inputs the bot's current cards.
def bot_play_1(botx_cards):
    # The played card is the card with highest priority, because the cards will be sorted based on their priorities later in the program.
    round1_play=botx_cards[0]
    # The played card is removed from the bot's current cards.
    botx_cards.remove(round1_play)
    # Played card is returned
    return round1_play
# This function decides what card the bot will play when it plays as the second player of the current round.
# It inputs the bot's current cards as well as the card played in the first round. 
def bot_play_2(botx_cards,round1_play):
    # First, we define the suit of the current round as the suit of the first played card.
    round_suit=round1_play[0]
    # We now check if the bot has cards from the suit of the current round by filtering the bot's current cards to the suit of the round.
    if list(filter(lambda x:x[0]==round_suit,botx_cards))==[]:
        # If the bot has no cards from the suit, it will play the cad with least priority overall.
        round2_play=botx_cards[-1]
    else:
        # If some cards are present in the same suit, then we check if the priority of the highest card after filtering is higher than the
        # priority of the card played in the first round. We do this by using the dictionary defined earlier.
        if cards_hierarchy[list(filter(lambda x:x[0]==round_suit,botx_cards))[0]]>cards_hierarchy[round1_play]:
            # If a higher priority card is present, then the highest priority card from that suit is played.
            round2_play=list(filter(lambda x:x[0]==round_suit,botx_cards))[0]
        else:
            # Otherwise, the lowest priority card from the suit is played.
            round2_play=list(filter(lambda x:x[0]==round_suit,botx_cards))[-1]
    # Finally, the played card is removed from the bot's current cards.
    botx_cards.remove(round2_play)
    # We return the played card.
    return round2_play
# This function decides what card the bot will play when it plays as the third player of the current round.
# It inputs the bot's cards and the cards played in the first two rounds.
def bot_play_3(botx_cards,round1_play,round2_play):
    # Again, we define the suit of the current round.
    round_suit=round1_play[0]
    # We now have to find out the higher priority card among the cards played in the previous two rounds.
    # To do that, we first check if the second played card is of the same suit as the first played card.
    if round1_play[0]!=round2_play[0]:
        # If the suits are different, higher priority is the first played card, because a different suit card doesn't matter.
        max_card=round1_play
    else:
        # If the suits are same, then we check their priority using the dictionary defined at the start of the program.
        if cards_hierarchy[round1_play]>cards_hierarchy[round2_play]:
            # If first played card is of higher priority, then that is the highest priority card.
            max_card=round1_play
        else:
            # Else, the second played card is of higher priority.
            max_card=round2_play
    # Now, we again check, by filtering, whether the bot has cards from the same suit as the suit of the round. 
    if list(filter(lambda x:x[0]==round_suit,botx_cards))==[]:
        # If there isn't any card, then the lowest priority card from all cards is played.
        round3_play=botx_cards[-1]
    else:
        # We again compare the priorities of the highest card from the filter with the highest priority card defined among the previous played cards.
        if cards_hierarchy[list(filter(lambda x:x[0]==round_suit,botx_cards))[0]]>cards_hierarchy[max_card]:
            # If it is higher, then the highest priority card from the filter is played.
            round3_play=list(filter(lambda x:x[0]==round_suit,botx_cards))[0]
        else:
            # Else, the lowest priority card from the filter is played.
            round3_play=list(filter(lambda x:x[0]==round_suit,botx_cards))[-1]
    # Finally, the played card is removed from the bot's current cards.
    botx_cards.remove(round3_play)
    # The played card is returned.
    return round3_play
# This function decides what card the bot will play when it plays as the fourth player of the current round.
# It inputs the bot's cards and the cards played in the first three rounds.
def bot_play_4(botx_cards,round1_play,round2_play,round3_play):
    # Again, we define the suit of the current round.
    round_suit=round1_play[0]
    # Now, we use a for loop to find out the highest priority card among the cards played in the first three rounds.
    max_card=round1_play
    for i in [round2_play,round3_play]:
        if i[0]==round_suit and cards_hierarchy[i]>cards_hierarchy[max_card]:
            # If the suit is same and the card is of higher priority, then the highest priority card is updated. 
            max_card=i
    # Again, the same process is repeated to find out what card to play based on the same above reasoning.
    if list(filter(lambda x:x[0]==round_suit,botx_cards))==[]:
        round4_play=botx_cards[-1]
    else:
        if cards_hierarchy[list(filter(lambda x:x[0]==round_suit,botx_cards))[0]]>cards_hierarchy[max_card]:
            round4_play=list(filter(lambda x:x[0]==round_suit,botx_cards))[0]
        else:
            round4_play=list(filter(lambda x:x[0]==round_suit,botx_cards))[-1]
    # Again, the played card is removed from the bot's current cards.
    botx_cards.remove(round4_play)
    # The played card is returned.
    return round4_play
# This function calculates the score based on the initial call and the number of rounds actually won.
# It inputs the initial call and the number of rounds actually won.
def score_calculator(call,wins):
    if wins>=call:
        # If the number of wins is more than the call, then a specific formula is used to calculate the score.
        score=call*10+(wins-call)
        # Also, 'score_str' stores the scores in a specific format required for the output.
        score_str='10*'+str(call)+' + ('+str(wins)+'-'+str(call)+')'
    else:
        # If the call is higher, then another formula is used.
        score=call*(-10)
        # Again, 'score_str' stores the scores for output.
        score_str='-10*'+str(call)
    # The score and 'score_str' is returned.
    return score,score_str
# This function decides the winner by taking all cases of result.
# It inputs the scores of the four players.
def winner(a,b,c,d):
    if a==b==c==d:
        winner='Bot1, Bot2, Bot3 and Player'
    elif a==b==c and a>d:
        winner='Bot1, Bot2 and Bot3'
    elif a==b==d and a>c:
        winner='Bot1, Bot2 and Player'
    elif a==c==d and a>b:
        winner='Bot1, Bot3 and Player'
    elif b==c==d and b>a:
        winner='Bot2, Bot3 and Player'
    elif a==b and a>c and a>d:
        winner='Bot1 and Bot2'
    elif a==c and a>b and a>d:
        winner='Bot1 and Bot3'
    elif a==d and a>b and a>c:
        winner='Bot1 and Player'
    elif b==c and b>a and b>d:
        winner='Bot2 and Bot3'
    elif b==d and b>a and b>c:
        winner='Bot2 and Player'
    elif c==d and c>a and c>b:
        winner='Bot3 and Player'
    elif a>b and a>c and a>d:
        winner='Bot1'
    elif b>a and b>c and b>d:
        winner='Bot2'
    elif c>a and c>b and c>d:
        winner='Bot3'
    elif d>a and d>b and d>c:
        winner='Player'
    else:
        winner='None'
    # The winner is returned.
    return winner
# The main program starts now.
# The random module is imported to use in the main program.
import random
cards_hierarchy={'SA':13,'SK':12,'SQ':11,'SJ':10,'S10':9,'S9':8,'S8':7,'S7':6,'S6':5,'S5':4,'S4':3,'S3':2,'S2':1,'CA':13,'CK':12,'CQ':11,'CJ':10,'C10':9,'C9':8,'C8':7,'C7':6,'C6':5,'C5':4,'C4':3,'C3':2,'C2':1,'DA':13,'DK':12,'DQ':11,'DJ':10,'D10':9,'D9':8,'D8':7,'D7':6,'D6':5,'D5':4,'D4':3,'D3':2,'D2':1,'HA':13,'HK':12,'HQ':11,'HJ':10,'H10':9,'H9':8,'H8':7,'H7':6,'H6':5,'H5':4,'H4':3,'H3':2,'H2':1}
# The following variables are initialized to store the total score of each player for the series and also the special format for displaying the output.
bot1_total_score=0
bot1_total_score_str=''
bot2_total_score=0
bot2_total_score_str=''
bot3_total_score=0
bot3_total_score_str=''
player_total_score=0
player_total_score_str=''
# The variable 'play_again' is initially True, to go into the while loop once.
play_again=True
# One full game is played inside this loop
while play_again:
    # An input is taken to ask the user if he wants a random distribution or if he wants to read it from a file.
    read_or_random=input("Random card distribution or read from file (Answer: 'Random'/'Read'): ")
    while True:
        # For a random distribution, we use the 'card_distributor' function to distribute the cards.
        if read_or_random=='Random':
            cards=card_distributor([[],[],[],[]])
            # Since the function returns a list of players' cards, each players' cards are distributed by indexing the returned variable.
            bot1_cards=cards[0]
            bot2_cards=cards[1]
            bot3_cards=cards[2]
            player_cards=cards[3]
            break
        elif read_or_random=='Read':
            # If the user wants to read from a file, then we first ask the user for the name of the file, and also make him/her ensure the file is in the correct format.
            filname=input("Please enter the name of the file along with extension: ")
            print("Please ensure your file has the cards as a list in each line with the correct format for card names")
            # The file is opened.
            filopen=open(filname,'r')
            # And each player gets his cards from the file.
            # 'eval' function is used to convert the string represntation of a list back to a list.
            bot1_cards=eval(filopen.readline())
            bot2_cards=eval(filopen.readline())
            bot3_cards=eval(filopen.readline())
            player_cards=eval(filopen.readline())
            filopen.close()
            break
        else:
            # We are also ensuring that the input given by the user matches the format we require for our if statements.
            # If the format isn't the same, then we ask the user again in a sentinel-controlled loop.
            print("Please enter Random/Read)")
            read_or_random=input("Random card distribution or read from file (Answer: 'Random'/'Read'): ")
    # Now, we sort the cards of all the players on the basis of the dictionary defined at the start. This doesn't sort based on suits as it isn't required.
    bot1_cards=sorted(bot1_cards,key=lambda x:cards_hierarchy[x],reverse=True)
    bot2_cards=sorted(bot2_cards,key=lambda x:cards_hierarchy[x],reverse=True)
    bot3_cards=sorted(bot3_cards,key=lambda x:cards_hierarchy[x],reverse=True)
    player_cards=sorted(player_cards,key=lambda x:cards_hierarchy[x],reverse=True)
    # The 'print()' statement gives one line gap at certain places for the user to see the output more clearly.
    print()
    # The user's cards are displayed to him.
    print("YOUR RANDOMLY DISTRIBUTED CARDS ARE:")
    print(player_cards,'\n')
    print("Where H - Hearts, C - Clubs, D - Diamonds and S - Spades")
    print("Similarly, A - Ace, K - King, Q - Queen, J - Joker\n")
    # The bot's calls are found using the earlier defined function.
    bot1_call=bot_call(bot1_cards)
    bot2_call=bot_call(bot2_cards)
    bot3_call=bot_call(bot3_cards)
    # The user's call is inputed.
    # The while loop is used to ensure that the user enters the call in a correct format.
    player_call=input("Enter your call: ")
    while True:
        # This try-except block is used to catch the ValueError that may be raised when user inputs a string which can't be converted to an integer.
        try:
            player_call=int(player_call)
            # We also make sure that the call is between 0 and 13.
            # The following lines are executed only when the first statement of the try block doesn't raise a ValueError.
            if player_call>=0 and player_call<=13:
                break
            else:
                print("Please call a number from 0 to 13")
                player_call=input("Enter your call: ")
        except ValueError:
            # If a ValueError is raised, we ask the user to input his call again in the correct format.
            print("Please enter your call as an integer number")
            player_call=input("Enter your call: ")
    # All the players' calls are displayed to the user.
    print("The calls of the players are as follows: ")
    print("Bot1->",bot1_call)
    print("Bot2->",bot2_call)
    print("Bot3->",bot3_call)
    print("Player->",player_call,'\n')
    # Now, a random seating arrangement is generated by the function we defined before.
    order=seating_arrangement()
    # The cycle is displayed.
    print("The cyclic order is ",order[0],"->",order[1],"->",order[2],"->",order[3],"->",order[0],"...........")
    # The cyclic order has 7 elements instead of 4, to help in defining the order for the current turn by slicing 'cyclic_order'.
    cyclic_order=[order[0],order[1],order[2],order[3],order[0],order[1],order[2]]
    # The player that starts the first turn is randomly chosen.
    start_player=random.choice(['bot1','bot2','bot3','player'])
    # And the chosen player is displayed to the user.
    print("The first round shall start from ",start_player,'\n')
    # The number of wins of each player for the current game is initialized to 0.
    bot1_wins=0
    bot2_wins=0
    bot3_wins=0
    player_wins=0
    # The for loop runs 13 times for the 13 turns in each game.
    for k in range(1,14):
        # Note: turn and round are used somewhat interchangeably.
        # The current turn is displayed.
        print("Turn ",str(k),":")
        # The cycle for each turn is found by slicing 'cyclic_order' after knowing the player who starts the turn.
        cycle=cyclic_order[cyclic_order.index(start_player):cyclic_order.index(start_player)+4]
        # This variable stores all the cards that are played in the current turn.
        round_cards={}
        # Now, using 4 if-elif-elif-else statements, we find out what card each player plays.
        # The first if-elif-elif-else statement is for the first card of the current turn.
        # The if statement is for deciding what set of cards is to be input into the earlier defined function that decides the bot's play.
        # And for, inputting the card from the user. 
        if cycle[0]=='bot1':
            round1_play=bot_play_1(bot1_cards)
            print("Bot1->",round1_play)
            round_cards[round1_play]='bot1'
        elif cycle[0]=='bot2':
            round1_play=bot_play_1(bot2_cards)
            print("Bot2->",round1_play)
            round_cards[round1_play]='bot2'
        elif cycle[0]=='bot3':
            round1_play=bot_play_1(bot3_cards)
            print("Bot3->",round1_play)
            round_cards[round1_play]='bot3'
        else:
            # The while loop takes care of any wrong input the user may give.
            print()
            print("The cards that you have remaining are:")
            print(player_cards)
            round1_play=input("Enter the card you want to play: ")
            while round1_play not in player_cards:
                print()
                print("Please enter a card from the cards that you have remaining.")
                print("If you have played a correct card, ensure that the format is correct.")
                print(player_cards)
                round1_play=input("Enter the card you want to play: ")
            player_cards.remove(round1_play)
            print("Player->",round1_play)
            round_cards[round1_play]='player'
        # This if-elif-elif-else statement is for the second card of the current turn.
        if cycle[1]=='bot1':
            round2_play=bot_play_2(bot1_cards,round1_play)
            print("Bot1->",round2_play)
            round_cards[round2_play]='bot1'
        elif cycle[1]=='bot2':
            round2_play=bot_play_2(bot2_cards,round1_play)
            print("Bot2->",round2_play)
            round_cards[round2_play]='bot2'
        elif cycle[1]=='bot3':
            round2_play=bot_play_2(bot3_cards,round1_play)
            print("Bot3->",round2_play)
            round_cards[round2_play]='bot3'
        else:
            print()
            print("The cards that you have remaining are:")
            print(player_cards)
            round2_play=input("Enter the card you want to play: ")
            while round2_play not in player_cards:
                print()
                print("Please enter a card from the cards that you have remaining.")
                print("If you have played a correct card, ensure that the format is correct.")
                print(player_cards)
                round2_play=input("Enter the card that you want to play: ")
            player_cards.remove(round2_play)
            print("Player->",round2_play)
            round_cards[round2_play]='player'
        # This if-elif-elif-else statement is for the third card of the current turn.
        if cycle[2]=='bot1':
            round3_play=bot_play_3(bot1_cards,round1_play,round2_play)
            print("Bot1->",round3_play)
            round_cards[round3_play]='bot1'
        elif cycle[2]=='bot2':
            round3_play=bot_play_3(bot2_cards,round1_play,round2_play)
            print("Bot2->",round3_play)
            round_cards[round3_play]='bot2'
        elif cycle[2]=='bot3':
            round3_play=bot_play_3(bot3_cards,round1_play,round2_play)
            print("Bot3->",round3_play)
            round_cards[round3_play]='bot3'
        else:
            print()
            print("The cards that you have remaining are:")
            print(player_cards)
            round3_play=input("Enter the card you want to play: ")
            while round3_play not in player_cards:
                print()
                print("Please enter a card from the cards that you have remaining.")
                print("If you have played a correct card, ensure that the format is correct.")
                print(player_cards)
                round3_play=input("Enter the card you want to play: ")
            player_cards.remove(round3_play)
            print("Player->",round3_play)
            round_cards[round3_play]='player'
        # This if-elif-elif-else statement is for the fourth card of the current turn.
        if cycle[3]=='bot1':
            round4_play=bot_play_4(bot1_cards,round1_play,round2_play,round3_play)
            print("Bot1->",round4_play)
            round_cards[round4_play]='bot1'
        elif cycle[3]=='bot2':
            round4_play=bot_play_4(bot2_cards,round1_play,round2_play,round3_play)
            print("Bot2->",round4_play)
            round_cards[round4_play]='bot2'
        elif cycle[3]=='bot3':
            round4_play=bot_play_4(bot3_cards,round1_play,round2_play,round3_play)
            print("Bot3->",round4_play)
            round_cards[round4_play]='bot3'
        else:
            print()
            print("The cards that you have remaining are:")
            print("If you have played a correct card, ensure that the format is correct.")
            print(player_cards)
            round4_play=input("Enter the card you want to play: ")
            while round4_play not in player_cards:
                print()
                print("Please enter a card from the cards that you have remaining.")
                print(player_cards) 
                round4_play=input("Enter the card you want to play: ")
            player_cards.remove(round4_play)
            print("Player->",round4_play)
            round_cards[round4_play]='player'
        # Now, the suit of the round is stored.
        round_suit=round1_play[0]
        # And the card with the highest priority with the same suit as the round suit is decided using a for loop that updates 'max_card'
        max_card=round1_play
        for j in [round2_play,round3_play,round4_play]:
            if j[0]==round_suit and cards_hierarchy[j]>cards_hierarchy[max_card]:
                max_card=j
        # The winner of the round is found.
        round_winner=round_cards[max_card]
        # And diplayed to the user.
        print(round_winner," has won this round")
        print('\n')
        # 'start_player' is updated for the next turn to start from the winner of the current turn.
        start_player=round_winner
        # Also, the count of number of wins for each player is updated.
        if round_winner=='bot1':
            bot1_wins+=1
        elif round_winner=='bot2':
            bot2_wins+=1
        elif round_winner=='bot3':
            bot3_wins+=1
        else:
            player_wins+=1
    # Now, the score is calculated using the function defined earlier.
    bot1_score,bot1_score_str=score_calculator(bot1_call,bot1_wins)
    bot2_score,bot2_score_str=score_calculator(bot2_call,bot2_wins)
    bot3_score,bot3_score_str=score_calculator(bot3_call,bot3_wins)
    player_score,player_score_str=score_calculator(player_call,player_wins)
    # Also, the total score is also updated with the score of the current game.
    bot1_total_score+=bot1_score
    bot2_total_score+=bot2_score
    bot3_total_score+=bot3_score
    player_total_score+=player_score
    # The updation of the specific format for output is slightly more complicated.
    # Because, there are two cases, one when it is the first game, and two, when it is any other game.
    if bot1_total_score_str=='':
        bot1_total_score_str+='('+bot1_score_str+')'
    else:
        bot1_total_score_str+='+('+bot1_score_str+')'
    if bot2_total_score_str=='':
        bot2_total_score_str+='('+bot2_score_str+')'
    else:
        bot2_total_score_str+='+('+bot2_score_str+')'
    if bot3_total_score_str=='':
        bot3_total_score_str+='('+bot3_score_str+')'
    else:
        bot3_total_score_str+='+('+bot3_score_str+')'
    if player_total_score_str=='':
        player_total_score_str+='('+player_score_str+')'
    else:
        player_total_score_str+='+('+player_score_str+')'
    # The scores of the current game are displayed to the user.
    print("The scores for the game are as follows: ")
    print("Bot1 = ",bot1_score_str," (Round Wins = ",bot1_wins,", Call = ",bot1_call,") = ",bot1_score)
    print("Bot2 = ",bot2_score_str," (Round Wins = ",bot2_wins,", Call = ",bot2_call,") = ",bot2_score)
    print("Bot3 = ",bot3_score_str," (Round Wins = ",bot3_wins,", Call = ",bot3_call,") = ",bot3_score)
    print("Player = ",player_score_str," (Round Wins = ",player_wins,", Call = ",player_call,") = ",player_score)
    # The winner is also decided using the function defined earlier.
    game_winner=winner(bot1_score,bot2_score,bot3_score,player_score)
    # Now, we check if there are multiple winners or not, based on the length of the output string from the function 'winner'.   
    if len(game_winner)>7:
        print(game_winner," are the winners of this game!!!!!")
    else:
        print(game_winner," is the winner of this game!!!!!")
    # Now, we ask the user if he/she wants to play another game to continue the series.
    another_game=input("Do you want to play another game to continue this series??('Yes'/'No') ")
    # while loop is to take care of incorrect input.
    while another_game!='Yes' and another_game!='No':
        print("Please reply with a 'Yes' or a 'No' only!")
        another_game=input("Do you want to play another game to continue this series??('Yes'/'No') ")
    if another_game=='No':
        # If the user doesn't want another game, then the initial while loop will end because 'play_again' is set to False.
        play_again=False
    # FOr neatness.
    print('------------------------------------------------------------------------------------------------')
# If the while loop ends, the scores for the whole series will be displayed.
print("The total scores for the whole series are as follows: ")
print("Bot1 = ",bot1_total_score_str," = ",bot1_total_score)
print("Bot2 = ",bot2_total_score_str," = ",bot2_total_score)
print("Bot3 = ",bot3_total_score_str," = ",bot3_total_score)
print("Player = ",player_total_score_str," = ",player_total_score)
print()
# The winner is decided using the same function used before.
series_winner=winner(bot1_total_score,bot2_total_score,bot3_total_score,player_total_score)
# Again, we check if there are multiple equal scores, but for the series we display that it has been drawn between whoever.
if len(series_winner)>7:
    print("The series is drawn between ",series_winner)
else:
    print(series_winner," wins the series!!!!!!!!!!")
# For neatness.
print('------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------')
# End of the program.
