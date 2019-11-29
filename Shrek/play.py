from PPlay.gameimage import*
from PPlay.keyboard import*
from jogador import*
from inimigos import *
import globais

class Play(object):
    def __init__(self, window):
        self.window = window
        self.jogador = Jogador(window)
        self.vidas = 5
        self.cron = 100
        self.fase = 1
        self.time = 0
        self.fundo = GameImage("./Imagens/Assets/fundo.png")
        self.fundo.set_position(0,30)
        self.fundo1 = GameImage("./Imagens/Assets/fundo1.png")
        self.fundo1.set_position(0,30)
        self.fundo2 = GameImage("./Imagens/Assets/fundo2.png")
        self.fundo2.set_position(0,30)
        self.fundo3 = GameImage("./Imagens/Assets/fundo3.png")
        self.fundo3.set_position(0,30)
        self.fundo4 = GameImage("./Imagens/Assets/fundo4.png")
        self.fundo4.set_position(0,30)
        self.keyboard = Keyboard()
        
        self.inimigo = Inimigo(self.window, self.fase, self.jogador)
    
    def run(self):
        if self.keyboard.key_pressed("ESC"):
            globais.PLAY_INIT = True
            globais.GAME_STATE = 0
        
        if self.keyboard.key_pressed("C")and self.keyboard.key_pressed("L"):
            self.inimigo.inimigos = []
            self.window.delay(200)
        
        if len(self.inimigo.inimigos) <= 0:
            self.fase += 1
            if self.fase == 2:
                self.inimigo.__init__(self.window, self.fase, self.jogador) 
            elif self.fase == 3:
                self.inimigo.__init__(self.window, self.fase, self.jogador)
            elif self.fase == 4:
                self.inimigo.__init__(self.window, self.fase, self.jogador)
            elif self.fase == 5:
                self.inimigo.__init__(self.window, self.fase, self.jogador)
            else:
                globais.PLAY_INIT = True
                globais.GAME_STATE = 0

        if self.fase == 1:
            self.fundo.draw()
        elif self.fase == 2:
            self.fundo1.draw()
        elif self.fase == 3:
            self.fundo2.draw()
        elif self.fase == 4:
            self.fundo3.draw()
        elif self.fase == 5:
            self.fundo4.draw()
        
        self.window.draw_text(
            "VIDAS: {}".format(self.vidas),
            globais.BORDER,
            globais.BORDER,
            30,
            (255,255,255),
            "./assets/fonts/pixelmix.ttf",
        )
        self.window.draw_text(
            "SPECIAL em {} segundos".format(self.time),
            self.window.width/2-100,
            globais.BORDER,
            30,
            (255,255,255),
            "./assets/fonts/pixelmix.ttf",
        )
    
        self.window.draw_text(
            "FASE: {}".format(self.fase),
            self.window.width-globais.BORDER-150,
            globais.BORDER,
            30,
            (255,255,255),
            "./assets/fonts/pixelmix.ttf",
        )       
        if self.cron > 0:
            self.cron -=1

        if self.cron <= 0:
            for mob in self.inimigo.inimigos:
                if mob.sprite_mov.collided(self.jogador.fiona):
                    self.vidas -= 1
                    self.cron = 100

        
        #runs
        self.jogador.update()
        self.inimigo.update()