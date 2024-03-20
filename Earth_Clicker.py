import pygame
class Clicker:
    def __init__(self):
        self.clicks = 0
        self.clicks_plus = 0
        self.cost_plus = 100
        self.peoples = 1
        self.peoples_cost = 10000
        self.rebirth = 1
        self.rebirth_cost = 100000
        self.__Shop_end = False
        self.__font_comic = pygame.font.Font("shrift2.ttf", 50)
        self.__font_comic2 = pygame.font.Font("shrift2.ttf", 20)
    def Add_Clicks(self):
        if self.rebirth > 0:
            self.clicks += ((1 + self.clicks_plus) * self.peoples * self.rebirth)
        else:
            self.clicks += 1 + self.clicks_plus * self.peoples
    
    def Shop(self,screen,fon,Click_Boost,People,Rebirth):
  #      self.__Shop_end = False
        self.__rect_Boost = Click_Boost.get_rect()
        self.__rect_Boost.x,self.__rect_Boost.y = 0,360 
        self.__rect_People = People.get_rect()
        self.__rect_People.x,self.__rect_People.y = 0,500
        self.__rect_Reb = Rebirth.get_rect()
        self.__rect_Reb.x,self.__rect_Reb.y = 0,100
        pygame.mixer.music.load('Shop.mp3')  # <-- Загрузка фоновой музыки       
        pygame.mixer.music.set_volume(0.8)  # <-- Установка громкости -- она ставится от 0 до 1
        pygame.mixer.music.play(loops=-1)
        sound: pygame.mixer.Sound = pygame.mixer.Sound('Buy.mp3')  # <-- Это объект звукового эффекта
        sound.set_volume(1)        
        while not(self.__Shop_end):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    with open("Clicks.txt","w") as file:
                        file.write(str(self.clicks))
                    file.close()
                    with open("Clicks_plus.txt","w") as file:
                        file.write(str(self.clicks_plus))
                    file.close()  
                    with open("Clicks_plus_cost.txt","w") as file:
                        file.write(str(self.cost_plus))
                    file.close()
                    with open("People_cost.txt","w") as file:
                        file.write(str(self.peoples_cost))
                    file.close()
                    with open("Peoples.txt","w") as file:
                        file.write(str(self.peoples))
                    file.close()    
                    with open("Rebirths.txt","w") as file:
                        file.write(f"{str(self.rebirth),{str(self.rebirth_cost)}}")
                    file.close()                   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__x,self.__y = pygame.mouse.get_pos()
                    if self.__rect_Boost.collidepoint(self.__x,self.__y):
                        if self.cost_plus <= self.clicks:
                            sound.play()
                            self.clicks -= int(self.cost_plus)
                            self.clicks_plus += 1
                            self.cost_plus = int(self.cost_plus *1.2)
                    if self.__rect_People.collidepoint(self.__x,self.__y):
                        if self.peoples_cost <= self.clicks:
                            sound.play()
                            self.clicks -= int(self.peoples_cost)
                            self.peoples += 1
                            self.peoples_cost = int(self.peoples_cost * 1.5)
                    if self.__rect_Reb.collidepoint(self.__x,self.__y):
                        if self.clicks >= self.rebirth_cost:
                            self.clicks = 0
                            self.clicks_plus = 0
                            self.cost_plus = 100
                            self.peoples = 1
                            self.peoples_cost = 10000
                            self.rebirth += 1
                            self.rebirth_cost += 200000
            screen.blit(fon,(0,0))
            screen.blit(Click_Boost,(0,360))
            screen.blit(People,self.__rect_People)
            screen.blit(Rebirth,self.__rect_Reb)
            text_img = self.__font_comic.render(f"clicks:{self.clicks}", True, (255,255,255))
            text_cost_peop = self.__font_comic2.render(f"cost:{self.peoples_cost}", True, (255,255,255))
            text_cost_plus = self.__font_comic2.render(f"cost:{self.cost_plus}", True, (255,255,255))
            text__cost_reb = self.__font_comic2.render(f"cost:{self.rebirth_cost}", True, (255,255,255))
            screen.blit(text_img,(0,0))
            screen.blit(text_cost_peop,(130,500))
            screen.blit(text_cost_plus,(230,360))
            screen.blit(text__cost_reb,(130,130))

            pygame.display.flip()
class Game:
    def __init__(self,width,height):
        pygame.init()
        self.__WIDTH = width
        self.__HEIGHT = height
        self.__screen = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        self.__fon = pygame.image.load("images\space.jpg")
        self.__Earth = pygame.image.load("images\Earth.png").convert_alpha()
        self.__Earth1 = pygame.image.load("images\Earth1.png").convert_alpha()
        self.__Earth2 = pygame.image.load("images\Earth2.png").convert_alpha()
        self.__Earth3 = pygame.image.load("images\Earth3.png").convert_alpha()
        self.__Shop = pygame.image.load("images\Shop.png").convert_alpha()
        self.__Click_Boost = pygame.image.load("images\Button.png").convert_alpha()
        self.__People = pygame.image.load("images\Buy_people.png").convert_alpha()
        self.__Rebirth_but = pygame.image.load("images\Rebirth.png").convert_alpha()
        self.__Rebirth_but = pygame.transform.smoothscale(self.__Rebirth_but,(100,100))          
        self.__Click_Boost = pygame.transform.smoothscale(self.__Click_Boost,(200,100))  
        self.__People = pygame.transform.smoothscale(self.__People,(100,100))  
        self.__fon = pygame.transform.smoothscale(self.__fon,(self.__WIDTH,self.__HEIGHT))
        self.__Earth = pygame.transform.smoothscale(self.__Earth,(self.__WIDTH//3,self.__HEIGHT//3))
        self.__Earth1 = pygame.transform.smoothscale(self.__Earth1,(self.__WIDTH//3,self.__HEIGHT//3))
        self.__Earth2 = pygame.transform.smoothscale(self.__Earth2,(self.__WIDTH//3,self.__HEIGHT//3))
        self.__Earth3 = pygame.transform.smoothscale(self.__Earth3,(self.__WIDTH//3,self.__HEIGHT//3))
        self.__Earth_small = pygame.transform.smoothscale(self.__Earth,(self.__WIDTH//3-10,self.__HEIGHT//3-10))
        self.__Shop = pygame.transform.smoothscale(self.__Shop,(70,70))
        self.__font_comic = pygame.font.Font("shrift2.ttf", 50)
        pygame.mixer.init()  # <-- Инициализация проигрывателя
        pygame.mixer.music.load('menu.mp3')  # <-- Загрузка фоновой музыки       
        pygame.mixer.music.set_volume(0.8)  # <-- Установка громкости -- она ставится от 0 до 1
        pygame.mixer.music.play(loops=-1)
        self.__fps = 60
        self.__mouse_click = 0
        self.__clock = pygame.time.Clock()
        self.__rect_Earth = self.__Earth.get_rect()
        self.__rect_Shop = self.__Shop.get_rect()
        self.__rect_Shop.x,self.__rect_Shop.y = self.__WIDTH - 70,self.__HEIGHT//2
        self.__rect_Earth.x = self.__WIDTH//3
        self.__rect_Earth.y = self.__HEIGHT//3
        self.__Cliker = Clicker()
        self.__game_end = False
        self.__Shop_end = True
        try:
            with open("Clicks.txt","r") as file:
                file.seek(0)
                self.__Cliker.clicks = int(file.read())
            file.close()
        except FileNotFoundError:
            self.__Cliker.clicks = 0
        try:
            with open("Clicks_plus.txt","r") as file:
                file.seek(0)
                self.__Cliker.clicks_plus = int(file.read())
            file.close()
        except FileNotFoundError:
            self.__Cliker.clicks_plus = 0
        try:
            with open("Clicks_plus_cost.txt","r") as file:
                file.seek(0)
                self.__Cliker.cost_plus = int(file.read())
            file.close()
        except FileNotFoundError:
            self.__Cliker.cost_plus = 100
        try:
            with open("People_cost.txt", "r") as file:
                file.seek(0)
                self.__Cliker.peoples_cost = int(file.read())
            file.close()
        except FileNotFoundError:
            self.__Cliker.peoples_cost = 10000
        try:
            with open("Peoples.txt", "r") as file:
                file.seek(0)
                self.__Cliker.peoples = int(file.read())
            file.close()
        except FileNotFoundError:
            self.__Cliker.peoples = 1
        try:
            with open("Rebirths.txt", "r") as file:
                file.seek(0)
                text = file.read()
                self.__Cliker.rebirth, self.__Cliker.rebirth_cost = map(int, text.split(","))
            file.close()
        except FileNotFoundError:
            self.__Cliker.rebirth = 1
            self.__Cliker.rebirth_cost = 100000
        except ValueError:
            self.__Cliker.rebirth = 1
            self.__Cliker.rebirth_cost = 100000            
    def __del__(self):
        # Закрываем PyGame
        pygame.quit()

    # Запуск игры
    def run(self):
        while not self.__game_end:
            self.__check_events()
            self.__draw()

            self.__clock.tick(self.__fps)

    # Проверка событий текущего игрового кадра
    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = True
                with open("Clicks.txt","w") as file:
                    file.write(str(self.__Cliker.clicks))
                file.close()   
                with open("Clicks_plus.txt","w") as file:
                    file.write(str(self.__Cliker.clicks_plus))
                file.close() 
                with open("Clicks_plus_cost.txt","w") as file:
                    file.write(str(self.__Cliker.cost_plus))
                file.close() 
                with open("People_cost.txt","w") as file:
                    file.write(str(self.__Cliker.peoples_cost))
                file.close()
                with open("Peoples.txt","w") as file:
                    file.write(str(self.__Cliker.peoples))
                file.close()       
                with open("Rebirths.txt","w") as file:
                    file.write(f"{str(self.__Cliker.rebirth)},{self.__Cliker.rebirth_cost}")
                file.close()       
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__x,self.__y = pygame.mouse.get_pos()
                if self.__rect_Earth.collidepoint((self.__x,self.__y)):
                    self.__Cliker.Add_Clicks()
                    self.__mouse_click += 1
            #        self.__screen.blit(self.__fon,(0,0))
              #      self.__screen.blit(self.__Earth_small,self.__rect_Earth)
              #      self.__screen.blit(self.__Shop,(self.__WIDTH - 70,self.__HEIGHT//2))
               #     pygame.display.flip()
                elif self.__rect_Shop.collidepoint((self.__x,self.__y)):
                    self.__Shop_end = False
                    while not(self.__Shop_end):
                        self.__Shop_end = self.__Cliker.Shop(self.__screen,self.__fon,self.__Click_Boost,self.__People,self.__Rebirth_but)
                    pygame.mixer.music.load('menu.mp3')  # <-- Загрузка фоновой музыки       
                    pygame.mixer.music.set_volume(0.8)  # <-- Установка громкости -- она ставится от 0 до 1
                    pygame.mixer.music.play(loops=-1)

    # Отрисовка игрового кадра
    def __draw(self):
        self.__screen.blit(self.__fon,(0,0))
        if self.__Cliker.peoples >= 2:
            if self.__mouse_click <=2 or self.__mouse_click % 2 == 0:
                self.__screen.blit(self.__Earth2,self.__rect_Earth)
            else:
                self.__screen.blit(self.__Earth3,self.__rect_Earth)
        else:
            if self.__mouse_click <=2 or self.__mouse_click % 2 == 0:
                self.__screen.blit(self.__Earth,self.__rect_Earth)
            else:
                self.__screen.blit(self.__Earth1,self.__rect_Earth)
        
        self.__screen.blit(self.__Shop,(self.__WIDTH - 70,self.__HEIGHT//2))
        text_img = self.__font_comic.render(f"clicks:{self.__Cliker.clicks}", True, (255,255,255))
        text_img2 = self.__font_comic.render(f"Years:{self.__Cliker.rebirth-1}", True, (255,255,255))
        self.__screen.blit(text_img,(0,0))
        self.__screen.blit(text_img2,(0,620))
        pygame.display.flip()

def main():
    game = Game(720, 720)  # Создание объекта игры
    game.run()  # Запуск игры


if __name__ == "__main__":  # Если файл запущен как исполняемый
    main()  # Запустить главную функцию
    