
class TV:
    channels = ['ORT','RTR','SPAS','RENTV']
    
    def __init__(self, name):
        self.name=name
        self.current_channel=0
        self.volume=0

    def change_channel(self):
        inp = int(input('Меняем направление или выбираем? (1, 2)'))
        if inp==1:
            inp2 = int(input('Вперед или назад? 1,2'))
            if (inp2==1):
                if (inp2==len(TV.channels)):
                    self.current_channel=0
                else:
                    self.curent_channel+=1
            else:
                if (inp2==0):
                    self.current_channel=len(TV.channels+1)
                else:
                    self.current_channel=-1
        else:
            for numb,chan in enumerate(TV.channels):
                print(f'{numb} - {TV.channels[numb]}')
            inp3 = int(input('Сделайте ваш выбор'))
            self.current_channel=inp3

        print('Текущий канал - ', TV.channels[self.current_channel])



my_tv = TV('SAMSUNG')
my_tv.change_channel()    
                      
            #if self.current_channel=0
        
        
