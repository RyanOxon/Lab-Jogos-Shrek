from PPlay.window import *
from menu import *
from play import *
import globais
from PPlay.sound import*

def main():
    window = Window(globais.LARGURA, globais.ALTURA)
    window.set_title("Sequestro do Ogro")
    window.set_background_color((0,0,0))
    teclado = Window.get_keyboard()
    
    musica = Sound("./Imagens/som.ogg")
    
    musica.play()
    
    fps=0
    contador = 0
    tempo_decorrido =0

    menu = Menu(window)
    play = Play(window)

    window.update()
    while globais.GAME_RUNNING:
        window.set_background_color((0, 0, 0))
        if globais.PLAY_INIT == True:
            play.__init__(window)
            globais.PLAY_INIT = False
        
        tempo_decorrido += window.delta_time()
        contador += 1
        if tempo_decorrido >=1:
            fps = contador
            contador = 0
            tempo_decorrido = 0
        
        window.draw_text(
            "FPS: {}".format(fps),
            window.width-globais.BORDER-45,
            globais.BORDER,15,(255,255,255),
            "./Imagens/Assets/fonts/pixelmix.ttf"
        )

    #MENU
        if globais.GAME_STATE == 0:
            menu.run()
        if globais.GAME_STATE == 1:
    	    play.run()
    #DIFICULDADE
        if globais.GAME_STATE == 2:
    	    menu.diff()
    #Win
        if globais.GAME_STATE == 3:
            play.wr()
    #lose
        if globais.GAME_STATE == 4:
            play.ls()
        window.update()
    
main()
