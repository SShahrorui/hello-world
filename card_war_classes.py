import random
class Deck:
    deck_of_cards=['A','K','Q','J','10','9','8','7','6','5','4','3','2']*4
    def shuffle(self):
        random.shuffle(self.deck_of_cards)
        return random.sample(self.deck_of_cards,26)

class Hand:
    def remove(self,player_cards):
        open_card=player_cards.pop()
        return open_card

    def add(self,player_cards,higher_card):
        player_cards[1:1]=higher_card
        return player_cards

class Play():
    def __init__(self,player,player_hand):
        self.player=player
        self.player_hand=player_hand


    def game(self):
        card=self.player.remove(self.player_hand)
        return card

    def compare(self,my_card,other_card):
        if(my_card > other_card):
            self.player.add(self.player_hand,my_card)
            self.player.add(self.player_hand,other_card)


    def war(self):
        print("war!")
        card_array=[]
        i=0
        while i<4:
            card_array.append(self.player.remove(self.player_hand))
            i=i+1
        return card_array

    def winner(self,my_cards,other_cards):
        if(my_cards[3]>other_cards[3]):
            self.player.add(self.player_hand,my_cards)
            self.player.add(self.player_hand,other_cards)
        print("success")



computer_cards=Deck()
computer_hand=computer_cards.shuffle()
print(computer_hand)
print("---------------")
user_cards=Deck()
user_hand=user_cards.shuffle()
print(user_hand)
print("---------------")
computer=Hand()
user=Hand()

first_player=Play(computer,computer_hand)
second_player=Play(user,user_hand)

while len(computer_hand)>0 and len(user_hand)>0:

    computer_open=first_player.game()
    user_open=second_player.game()
    print(computer_open)
    print(user_open)

    war1_cards=[]
    war2_cards=[]
    if (computer_open==user_open):
        if (len(computer_hand)>4 and len(user_hand)>4):
            war1_cards=first_player.war()
            war2_cards=second_player.war()
            if (war1_cards[3]==war2_cards[3]):
                war1_cards=first_player.war()
                war2_cards=second_player.war()
        else:
            break

            first_player.winner(war1_cards,war2_cards)
            second_player.winner(war2_cards,war1_cards)
    else:
        first_player.compare(computer_open,user_open)
        second_player.compare(user_open,computer_open)

print(computer_hand)
print("---------------")
print(user_hand)
print("---------------")
if (len(computer_hand)<len(user_hand)):
    print("You win!:'(")
else:
    print("I win! :')")
