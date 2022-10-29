from settings.config import *
from items import player


class Action:
    def __init__(self):
        sprite.Sprite.__init__(self)
    
    def get_action(self, _pos: str, _money: int):
        if _pos == 'action_kazna': #сверка текущего положения игрока с картой казны
            val = randint(1, 10) * 20
            choice = randint(1, 2)
            kazna_dict = {'kazna': 
            ['Вы потеряли' + str(val) + '$', 
            'Вы получили ' + str(val) + '$']}
            if choice == 1:
                _money -= val
                pyautogui.alert(text = kazna_dict['kazna'][0],title = 'Казна', button = 'Ок')
                return _money
                
            elif choice == 2:
                _money += val
                pyautogui.alert(text = kazna_dict['kazna'][1],title = 'Казна', button = 'Ок')
                return _money
        elif _pos == 'action_nalog':
            choice = randint(1, 3)
            nalog_dict = {'nalog': ['Вы стали слишком богаты и вами заинтересовалась налоговая служба, потеряйте 10% своего бюджета', 
            'Вы обвиняетесь в неуплате налогов в особо крупном размере, отправляйтесь в тюрьму', 
            'Став филантропом, Вы смогли сохранить 5% от своего бюджета, получите их в виде прибыли']}
            if choise == 1:
                _money -= int(money/100 * 10)
                pyautogui.alert(text = nalog_dict['nalog'][0],title = 'Налоги', button = 'Ок')
                return _money
            elif choice == 2:
                _pos = 'corner_01'# текущая позиция должна поменяться на тюрьму
                pyautogui.alert(text = nalog_dict['nalog'][1],title = 'Налоги', button = 'Ок')
                return _pos
            elif choice == 3:
                _money += int(money/100 * 5)
                pyautogui.alert(text = nalog_dict['nalog'][2],title = 'Налоги', button = 'Ок')
                return _money
        elif _pos == 'action_shans':
            val = randint(1,10) * 40
            choice = randint(1,5)
            shans_dict = {'shans': ['Вы выйграли в лотерею, получите ' + str(val) + '$',
            'Штраф за разговор по мобильному телефону за рулем, заплатите 150 $',
            'Вы продали свой билет на финал чемпионата мира по футболу, получите 100 $',
            'Сегодня не Ваш день, отправляйтесь в тюрьму...',
            'Чтобы поднять свои шансы на успех Вы записались на экономические курсы, к сожалению Вы поздно поняли, что экономист из Вас не очень, тк за эти курсы нужно платить, Ваше состояние уменьшилось на 300 $',
            ]}
            if choice == 1:
                _money += val
                pyautogui.alert(text = shans_dict['shans'][0],title = 'Налоги', button = 'Ок')
                return _money
            elif choice == 2:
                _money -= 150
                pyautogui.alert(text = shans_dict['shans'][1],title = 'Налоги', button = 'Ок')
                return _money
            elif choice == 3:
                _money += 100
                pyautogui.alert(text = shans_dict['shans'][2],title = 'Налоги', button = 'Ок')
                return _money
            elif choice == 4:
                _pos = 'corner_01'#отправка в тюрьму, нужно уточнение Id тюрьмы(нужно вызывать на прямую или через img.map.corner.01)
                pyautogui.alert(text = shans_dict['shans'][3],title = 'Налоги', button = 'Ок')
                return _pos
            elif choice == 5:
                _money -= 300
                pyautogui.alert(text = shans_dict['shans'][4],title = 'Налоги', button = 'Ок')
                return _money
        else:
            pass
            
            


