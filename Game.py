from Card import Card
from Player import Player
import random

first=Card(type=1,name='First Witness')
criminal=Card(type=2,name="Criminal")
detective=Card(type=3,name='Detective')
alibi=Card(type=4,name='Alibi')
complicity=Card(type=5,name='Complicity')
witness=Card(type=6,name='Witness')
passerby=Card(type=7,name='Passer-by')
dog=Card(type=8,name='God Dog')
exchange=Card(type=9,name='Information Exchange')
rumour=Card(type=10,name='Ramour')
trade=Card(type=11,name='Trade')

cards_total=[first,criminal,detective,alibi,complicity,alibi,detective,complicity,alibi,alibi,alibi,detective,detective,witness,witness,witness,dog,passerby,passerby,exchange,exchange,exchange,exchange,rumour,rumour,rumour,rumour,rumour,trade,trade,trade,trade]
player_number_dict=[-1,-1,4,5,6,8,9,0]#规则中提到不同的人数必须卡牌数不同，这是不同人数的起始卡牌位置

class Game:
    players=[]
    cards_totally=[]
    criminal_list=[]
    player_points=[]
    player_number=0
    order=0
    win_type=0

    def __init__(self,players):
        if len(players)<3:
            return False

        self.players=players
        self.player_number=len(players)


    def start(self):
        self.win_type=0
        self.criminal_list = []
        start = player_number_dict[self.player_number - 1]
        x = cards_total[start:]
        random.shuffle(x)
        self.cards_totally = cards_total[0:start] + x[0:self.player_number * 4 - start]
        random.shuffle(self.cards_totally)
        for i in range(self.player_number):
            self.players[i].init_cards(self.cards_totally[i*4:i*4+4])

        self.order=self.cards_totally.index(first,0)//4
        first_order=self.cards_totally.index(first,0)%4
        self.players[self.order].lose_card(which=first_order)
        print(self.players[self.order].name)
        self.order=(self.order+1)%self.player_number

    def choose_player(self):
        x=self.order+1
        while(x==self.order+1 or x>self.player_number):
            print('Please do not choose yourself!')
            for i in range(self.player_number):
                print('No.{}:{}'.format(i+1,self.players[i].name))
            x=input('Please input the number of the player you choose\n')
            x=eval(x)

        return x-1

    def win(self):
        if self.win_type==1:
            for player in self.players:
                if player in self.criminal_list:
                    player.win(number=2)
            return True
        elif self.win_type==2:
            for player in self.players:
                if player not in self.criminal_list:
                    player.win(number=1)
            self.players[self.order].win(number=1)
            return True
        elif self.win_type==3:
            for player in self.players:
                if player not in self.criminal_list:
                    player.win(number=1)
            self.players[self.order].win(number=2)
            return True
        else:
            return False



    def use_card(self):
        print(self.players[self.order].name)
        choise,choise_number=self.players[self.order].choose()
        if choise.type==2:
            if self.players[self.order].cards_number!=1:
                print('Please use criminal card if and ONLY if you ONLY have this card! ')
                return False
            if self.players[self.order] not in self.criminal_list:
                self.criminal_list.append(self.players[self.order])
            self.win_type=2
            self.win()
        elif choise.type==3:
            if self.players[self.order].cards_number >= 3:
                pass
            else:
                x = self.choose_player()
                if (criminal in self.players[x].cards):
                    if (alibi not in self.players[x]):
                        self.win_type = 1
                        if self.players[self.order] not in self.criminal_list:
                            self.criminal_list.append(self.players[x])
                        self.win()
                    else:
                        pass
                else:
                    pass
        elif choise.type==4:
            pass
        elif choise.type==5:
            self.criminal_list.append(self.players[self.order])
        elif choise.type==6:
            x=self.choose_player()
            self.players[x].card_print()
        elif choise.type==7:
            pass
        elif choise.type==8:
            x=self.choose_player()
            _,number=self.players[x].choose()
            _.print()
            if _.type!=2:
                self.players[x].lose_card(which=number)
                self.players[x].get_card(card=dog)
            else:
                self.win_type=3
                if self.players[self.order] not in self.criminal_list:
                    self.criminal_list.append(self.players[x])
                self.win()
        elif choise.type==9:
            _=[]
            for i in range(self.player_number):
                if i != self.order:
                    card,number=self.players[i].choose()
                else:
                    card,number=self.players[i].choose(except_card=choise_number)
                self.players[i].lose_card(which=number)
                _.append(card)
            for i in range(self.player_number):
                self.players[i].get_card(_[(i+1)%self.player_number])

        elif choise.type==10:
            _=[]
            for i in range(self.player_number):
                card=self.players[i].lose_card(Random=True)
                _.append(card)
            for i in range(self.player_number):
                self.players[i].get_card(_[(i+1)%self.player_number])

        elif choise.type==11:
            if self.players[self.order].cards_number==1:
                print(self.players[self.order].cards_number)
                pass
            x = self.choose_player()
            card1,number1=self.players[self.order].choose(except_card=choise_number)
            card2,number2=self.players[x].choose()
            self.players[self.order].lose_card(number1)
            self.players[self.order].get_card(card2)
            self.players[x].lose_card(number2)
            self.players[x].get_card(card1)
        else:
            return False

        self.players[self.order].lose_card(choise_number)
        return True

    def single_play(self):
        self.start()
        while(self.win_type==0):
            while(not self.use_card()):
                pass
            self.order = (self.order + 1) % self.player_number

        self.win_type=0
        self.criminal_list=[]




player1=Player(name='dada')
player2=Player(name='dasdas')
player3=Player(name='dadasdas')

players=[player1,player2,player3]

game=Game(players=players)
game.single_play()
