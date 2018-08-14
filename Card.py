class Card:
    type = 0
    name=''
    # add a figure for a card

    def __init__(self,type=0,name='',figure = None):
        self.type=type
        self.name=name
    def print(self):
        print('name:{}'.format(self.name),end=';')

