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
        self.fase = 5
        self.intro = False
        self.time = 10
        self.timer = 0
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
    
    def wr(self):
        self.window.draw_text(
			"Parabens, Voce conseguiu salvar o Shrek",
		    self.window.width/2-350,
		    self.window.height/2-100,
		    50,
		    (255,255,255),
		    "./assets/fonts/pixelmix.ttf",
	    )
        self.window.draw_text(
			"Aperte ENTER para continuar",
		    self.window.width/2-200,
		    self.window.height/2,
		    35,
		    (255,255,255),
		    "./assets/fonts/pixelmix.ttf",
	    )
        if self.keyboard.key_pressed("ENTER"):
            globais.PLAY_INIT = True
            globais.GAME_STATE = 0
    def ls(self):    
        self.window.draw_text(
			"Ops, nao foi dessa vez",
		    self.window.width/2-200,
		    self.window.height/2-100,
		    50,
		    (255,255,255),
		    "./assets/fonts/pixelmix.ttf",
	    )
        self.window.draw_text(
			"Mas nao desista, o shrek ainda precisa de voce",
		    self.window.width/2-400,
		    self.window.height/2,
		    50,
		    (255,255,255),
		    "./assets/fonts/pixelmix.ttf",
	    )
        self.window.draw_text(
			"Aperte ENTER para continuar",
		    self.window.width/2-200,
		    self.window.height/2+100,
		    35,
		    (255,255,255),
		    "./assets/fonts/pixelmix.ttf",
	    )
        if self.keyboard.key_pressed("ENTER"):
            globais.PLAY_INIT = True
            globais.GAME_STATE = 0
    def run(self):
        if self.intro == True:
            self.timer -= self.window.delta_time()
            if self.fase == 0.5:
                self.window.draw_text(
				    "Fase 1: Entrada do castelo",
				    self.window.width/2-200,
				    self.window.height/2-100,
				    50,
				    (255,255,255),
				    "./assets/fonts/pixelmix.ttf",
        	    )
            elif self.fase == 1.5:
                self.window.draw_text(
				    "Fase 2: Salao Real",
				    self.window.width/2-180,
				    self.window.height/2-100,
				    50,
				    (255,255,255),
				    "./assets/fonts/pixelmix.ttf",
        	    )
            elif self.fase == 2.5:
                self.window.draw_text(
				    "Fase 3: Subterraneo do castelo",
				    self.window.width/2-200,
				    self.window.height/2-100,
				    50,
				    (255,255,255),
				    "./assets/fonts/pixelmix.ttf",
        	    )
            elif self.fase == 3.5:
                self.window.draw_text(
			        "Fase 4: Calabouco",
			        self.window.width/2-170,
			        self.window.height/2-100,
			        50,
			        (255,255,255),
			        "./assets/fonts/pixelmix.ttf",
      	        )

            elif self.fase == 4.5:
                self.window.draw_text(
			        "Fase 5: Sala do Carcereiro",
			        self.window.width/2-180,
			        self.window.height/2-100,
			        50,
			        (255,255,255),
			        "./assets/fonts/pixelmix.ttf",
    	        )
            
            if self.timer <= 0:
                self.intro = False

        else:        
            if self.keyboard.key_pressed("ESC"):
                globais.PLAY_INIT = True
                globais.GAME_STATE = 0
        
            if self.keyboard.key_pressed("C")and self.keyboard.key_pressed("L"):
                self.inimigo.inimigos = []
                self.window.delay(200)
        
            if len(self.inimigo.inimigos) <= 0:
                self.jogador.fiona.set_position(globais.BORDER,30)
                self.fase += 0.5
                self.window.set_background_color((0, 0, 0))
                
                if self.fase == 0.5:
                    self.intro = True
                    self.timer = 5


                elif self.fase == 1:
                    self.inimigo.__init__(self.window, self.fase, self.jogador)
            
                elif self.fase == 1.5:
                    self.intro = True
                    self.timer = 5

                elif self.fase == 2:
                    self.inimigo.__init__(self.window, self.fase, self.jogador)
                
                elif self.fase == 2.5:
                    self.intro = True
                    self.timer = 5

                elif self.fase == 3:
                    self.inimigo.__init__(self.window, self.fase, self.jogador)

                elif self.fase == 3.5:
                    self.intro = True
                    self.timer = 5

                elif self.fase == 4:
                    self.inimigo.__init__(self.window, self.fase, self.jogador)
            
                elif self.fase == 4.5:
                    self.intro = True
                    self.timer = 5

                elif self.fase == 5:
                    self.inimigo.__init__(self.window, self.fase, self.jogador)
                
                else:
                    #self.win = True
                    globais.GAME_STATE = 3

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
                "FASE: {:.0f}".format(self.fase),
                self.window.width-globais.BORDER-150,
                globais.BORDER,
                30,
                (255,255,255),
                "./assets/fonts/pixelmix.ttf",
            )
            if self.cron > 0:
                self.cron -= self.window.delta_time()

            if self.cron <= 0:
                for mob in self.inimigo.inimigos:
                    #if self.cron <=0:
                    if mob.sprite_mov.collided(self.jogador.fiona):
                        self.vidas -= mob.dano
                        self.cron = 3
            
            if self.vidas <= 0:
                globais.GAME_STATE = 4

        
            #runs
            if self.fase == 1 or 2 or 3 or 4 or 5:
                self.jogador.update()
                self.inimigo.update()