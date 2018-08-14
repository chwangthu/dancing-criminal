import Card
import random

class Player:
    name=''
    # we will add a seat later
    cards=[]
    cards_number=0
    score=0
    def __init__(self,name='',cards=[]):
        self.name=name
        self.cards=cards
        self.cards_number=len(cards)
    def choose(self,except_card=-2):# 自主选择牌
        while(True):
            for i in range(self.cards_number):
                print('card{}:{}'.format(i+1,self.cards[i].name))
            choise=input('please input the number of the card you choose\n')
            choise=eval(choise)
            if (choise-1)!=except_card:
                break
            print('Please not choose the card you are using!')
        return self.cards[choise-1],choise-1

    def refresh_number(self):
        self.cards_number=len(self.cards)

    def get_card(self,card):
        self.cards.append(card)
        self.refresh_number()

    def init_cards(self,cards):
        self.cards=cards.copy()
        self.refresh_number()

    def lose_card(self,which=-1,Random=False):#which是丢失卡的序号
        if self.cards_number==0 or which<-1 or self.cards_number<which:
            return False

        if Random:
            x=random.randint(0,self.cards_number)
            x=x-1
        else:
            x=which

        card_lost=self.cards[x]
        self.cards.pop(x)
        self.refresh_number()
        return card_lost
    def card_print(self):
        print('your cards:')
        for i in range(self.cards_number):
            self.cards[i].print()
        print()

    def win(self,number=0):
        self.score+=number

