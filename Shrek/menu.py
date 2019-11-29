from PPlay.window import*
from PPlay.gameimage import*
from PPlay.mouse import Mouse
from PPlay.keyboard import Keyboard
import globais

class Menu(object):
    def __init__(self, window):
        self.window = window
        self.title = GameImage("./Imagens/Assets/Title.png")
        self.jogar = GameImage("./Imagens/Assets/Jogar.png")
        self.dificuldade = GameImage("./Imagens/Assets/dificuldade.png")
        self.sair = GameImage("./Imagens/Assets/sair.png")
        self.jogar1 = GameImage("./Imagens/Assets/Jogar1.png")
        self.dificuldade1 = GameImage("./Imagens/Assets/dificuldade1.png")
        self.sair1 = GameImage("./Imagens/Assets/sair1.png")
        self.hard = GameImage("./Imagens/Assets/dificil.png")
        self.medio = GameImage("./Imagens/Assets/medio.png")
        self.facil = GameImage("./Imagens/Assets/facil.png")
        self.hard1 = GameImage("./Imagens/Assets/dificil1.png")
        self.medio1 = GameImage("./Imagens/Assets/medio1.png")
        self.facil1 = GameImage("./Imagens/Assets/facil1.png")
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.__set_pos()
        self.__draw()

    def __draw(self):
        self.title.draw()
        self.jogar.draw()
        self.dificuldade.draw()
        self.sair.draw()

    def __draw1(self):
        self.title.draw()
        self.hard.draw()
        self.medio.draw()
        self.facil.draw()

    def __set_pos(self):
        self.title.set_position(globais.BORDER  + 30, globais.BORDER + 30)
        self.jogar.set_position(self.window.width/2 - self.jogar.width / 2, self.jogar.height *1+80*1)
        self.jogar1.set_position(self.window.width/2 - self.jogar1.width / 2, self.jogar1.height *1+80*1)
        self.dificuldade.set_position(self.window.width/2 - self.dificuldade.width/2, self.dificuldade.height* 2+80*2,)
        self.dificuldade1.set_position(self.window.width/2 - self.dificuldade.width/2, self.dificuldade.height* 2+80*2,)
        self.sair.set_position(self.window.width/2 - self.sair.width/2, self.sair.height*3+80*3)
        self.sair1.set_position(self.window.width/2 - self.sair.width/2, self.sair.height*3+80*3)
        #diff
        self.facil.set_position(self.window.width/2 + self.facil.width , self.facil.height*1+80*1)
        self.facil1.set_position(self.window.width/2 + self.facil1.width, self.facil1.height*1+80*1)
        self.medio.set_position(self.window.width/2 + self.medio.width, self.medio.height*2+80*2)
        self.medio1.set_position(self.window.width/2 + self.medio1.width, self.medio1.height*2+80*2)
        self.hard.set_position(self.window.width/2 + self.hard.width, self.hard.height*3+80*3)
        self.hard1.set_position(self.window.width/2 + self.hard1.width, self.hard1.height*3+80*3)

    def run(self):
        self.__draw()

        #play
        if self.mouse.is_over_object(self.jogar):
            self.jogar1.draw()
            if self.mouse.is_button_pressed(1):
                globais.GAME_STATE = 1
        #dificuldade
        if self.mouse.is_over_object(self.dificuldade):
            self.dificuldade1.draw()
            if self.mouse.is_button_pressed(1):
                globais.GAME_STATE = 2
        
        #Quit
        if self.mouse.is_over_object(self.sair):
            self.sair1.draw()
            if self.mouse.is_button_pressed(1):
                globais.GAME_RUNNING = False

    def diff(self):
        self.__draw1()

        if self.keyboard.key_pressed("ESC"):
            globais.GAME_STATE = 0

        if self.mouse.is_over_object(self.medio):
            self.medio1.draw()
            if self.mouse.is_button_pressed(1):
                globais.Dificuldade = 1
                globais.PLAY_INIT = True
                globais.GAME_STATE = 0
        
        if self.mouse.is_over_object(self.facil):
            self.facil1.draw()
            if self.mouse.is_button_pressed(1):
                globais.Dificuldade = 0.75
                globais.PLAY_INIT = True
                globais.GAME_STATE = 0

        if self.mouse.is_over_object(self.hard):
            self.hard1.draw()
            if self.mouse.is_button_pressed(1):
                globais.Dificuldade = 1.5
                globais.PLAY_INIT = True
                GAME_STATE = 0
    
