from settings.config import *

class Banker:
    """
    Класс Банкира
    - Банкир должен находится между игроками
    - Говорить при покупке предприятия кем либо
    - Удачная\неудачная сделка с владельцем бизнеса(при продаже кому либо)
    - 
    """
    def __init__(self) -> None:
        sprite.Sprite.__init__(self)