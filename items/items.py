from pygame import *

class CardMap:
    def __init__(self,name:str,id:int,x:int,y:int,width:int,height:int):
        sprite.Sprite.__init__(self)
        self.Name: str = name
        self.ID: str = id
        self.XYpos: tuple = (x,y)
        self.Size: tuple = (width,height)
        self.card_offset: int = 2 # ширина границы карты

    def draw(self, screen:display,rotate: int = 0, miror: tuple[int] = (0,0)): # Выводим себя на экран
        self.rect = Rect(self.XYpos[0],self.XYpos[1],self.Size[0],self.Size[1])
        try:
            self.image = image.load(f"assets/img/map/{self.Name}").convert()
            self.image = transform.scale(self.image,self.Size)
            self.image = transform.rotate(self.image,rotate)
            self.image = transform.flip(self.image,miror[0],miror[1])
        except:
            self.image = Surface(self.Size)
            transform.scale(self.image,self.Size)
            self.image.fill(Color("#888888"))
        screen.blit(self.image, (self.rect.x,self.rect.y))
    
    @property
    def card_area(self):
        return(range(self.XYpos[0],self.XYpos[0]+self.Size[0]),range(self.XYpos[1],self.XYpos[1]+self.Size[1]))

class Map:
    def __init__(self):
        self.__SessionID: str = ""
        self.__CurrentUsersList: dict = {}
        self.__MapImagePath: str = ""
        self.__MapStructure: list[str] = [
            ".---------.",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            "+         +",
            ".---------.",
        ]
        self.__MapCards: list[CardMap] = []
    def reshuffle_cards(self):
        import random
        if len(self.__MapCards) > 4:
            cards = self.__MapCards[4:]
            random.shuffle(cards)
            self.__MapCards[4:] = cards

    def append_card(self,card: CardMap):
        self.__MapCards.append(card)

    def insert_card(self,ind,card: CardMap):
        self.__MapCards.insert(ind,card)

    def set_MapImagePath(self, value: str):
        self.__MapImagePath = value

    def set_CurrentUsersList(self, value: dict):
        self.__CurrentUsersList = value

    def set_SessionID(self, value: str):
        self.__SessionID = value

    @ property
    def get_MapImagePath(self):
        return (self.__MapImagePath)

    @ property
    def get_CurrentUsersList(self):
        return (self.__CurrentUsersList)

    @ property
    def get_SessionID(self):
        return (self.__SessionID)
        
    @ property
    def get_MapStructure(self):
        return (self.__MapStructure)
    @ property
    def get_MapCards(self):
        return (self.__MapCards)

