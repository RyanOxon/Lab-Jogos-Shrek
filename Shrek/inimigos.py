from PPlay.sprite import *
from PPlay.collision import *
import globais

class Mob(object):
    def __init__(self, sprite, frames, time, speed, vida, dano, sp, boss=False):
        self.sprite_mov = Sprite(sprite, frames)
        self.sprite_mov.set_total_duration(time)
        self.vel = globais.MOB_SPEED*speed #*self.multiplier
        self.vel_x = 0
        self.vel_y = 0
        self.vida = vida
        self.dano = dano
        self.sp = sp
        

class Inimigo(object):
    def __init__(self, window, fase, jogador):
        self.window = window
        self.fase = fase
        self.inimigos = []
        self.__setup()
        self.jogador = jogador
        self.j_pos_x = self.jogador.fiona.x
        self.j_pos_y = self.jogador.fiona.y
        self.posCD = 100
    
    def __setup(self): #y<350 #x<650
        if self.fase == 1:
            self.spawn(1, self.window.width/2, self.window.height/2 -200)
            self.spawn(1, self.window.width/2+300, self.window.height/2 -275)
            self.spawn(1, self.window.width/2+150, self.window.height/2-50)
            self.spawn(1, self.window.width/2-150, self.window.height/2+50)
            self.spawn(1, self.window.width/2-350, self.window.height/2+250)
            self.spawn(1, self.window.width/2, self.window.height/2+300)
            self.spawn(3, self.window.width/2, self.window.height/2)
            self.spawn(2, self.window.width/2+550, self.window.height/2+200)
            self.spawn(2, self.window.width/2+450, self.window.height/2+250)

        if self.fase == 2:
            self.spawn(1, self.window.width/2, self.window.height/2-175)
            self.spawn(1, self.window.width/2+325, self.window.height/2-250)
            self.spawn(1, self.window.width/2-250, self.window.height/2-50)
            self.spawn(1, self.window.width/2-350, self.window.height/2+175)
            self.spawn(3, self.window.width/2, self.window.height/2)
            self.spawn(3, self.window.width/2+150, self.window.height/2-150)
            self.spawn(3, self.window.width/2-150, self.window.height/2+150)
            self.spawn(4, self.window.width/2+400, self.window.height/2+150)
            self.spawn(2, self.window.width/2+550, self.window.height/2+100)
            self.spawn(2, self.window.width/2+250, self.window.height/2+300)

        if self.fase == 3:
            self.spawn(3, self.window.width/2-200, self.window.height/2-100)
            self.spawn(3, self.window.width/2-50, self.window.height/2-300)
            self.spawn(3, self.window.width/2-400, self.window.height/2+50)
            self.spawn(3, self.window.width/2-600, self.window.height/2+250)
            self.spawn(2, self.window.width/2+550, self.window.height/2-300)
            self.spawn(2, self.window.width/2+450, self.window.height/2-300)
            self.spawn(2, self.window.width/2+350, self.window.height/2-300)
            self.spawn(2, self.window.width/2+550, self.window.height/2+300)
            self.spawn(2, self.window.width/2+450, self.window.height/2+300)
            self.spawn(2, self.window.width/2+350, self.window.height/2+300)
            self.spawn(4, self.window.width/2+50, self.window.height/2-50)
            self.spawn(4, self.window.width/2+325, self.window.height/2-115)
            self.spawn(4, self.window.width/2-115, self.window.height/2+175)

        if self.fase == 4:
            self.spawn(3, self.window.width/2+150, self.window.height/2-250)
            self.spawn(3, self.window.width/2+50, self.window.height/2-175)
            self.spawn(3, self.window.width/2-50, self.window.height/2-100)
            self.spawn(3, self.window.width/2-150, self.window.height/2-25)
            self.spawn(3, self.window.width/2-250, self.window.height/2+50)
            self.spawn(2, self.window.width/2+500, self.window.height/2-250)
            self.spawn(2, self.window.width/2+500, self.window.height/2-125)
            self.spawn(2, self.window.width/2+500, self.window.height/2)
            self.spawn(2, self.window.width/2+500, self.window.height/2+125)
            self.spawn(2, self.window.width/2+500, self.window.height/2+250)
            self.spawn(4, self.window.width/2+325, self.window.height/2-100)
            self.spawn(4, self.window.width/2+175, self.window.height/2)
            self.spawn(4, self.window.width/2+125, self.window.height/2+100)
            self.spawn(4, self.window.width/2+75, self.window.height/2+200)
            

        if self.fase == 5:
            self.spawn(5,self.window.width-300, self.window.height/2-75)
            self.spawn(2, self.window.width/2+500, self.window.height/2-250)
            self.spawn(2, self.window.width/2+500, self.window.height/2-125)
            self.spawn(2, self.window.width/2+500, self.window.height/2)
            self.spawn(2, self.window.width/2+500, self.window.height/2+125)
            self.spawn(2, self.window.width/2+500, self.window.height/2+250)

    def spawn(self,tipo, x, y):
        if tipo == 1:#Guarda
            mob = Mob(
                "./Imagens/Inimigos/Guarda/Guards_L.png",
                4,
                800,
                0.75,
                3,
                1,
                1
            )
        elif tipo == 2: #Bruxa
            mob = Mob(
                "./Imagens/Inimigos/bruxa/witch_L.png",
                3,
                500,
                1.5,
                3,
                2,
                1
           )
        elif tipo==3: #Capitao
            mob = Mob(
                "./Imagens/Inimigos/Capitao/Guards_lance_L.png",
                3,
                800,
                1,
                6,
                2,
                1                
            )
        elif tipo==4: #Martelo
            mob = Mob(
                "./Imagens/Inimigos/Martelo/Guards_Hammer_L.png",
                3,
                1500,
                0.75,
                12,
                3,
                2
            )
        
        elif tipo==5: #Boss
            mob = Mob(
                "./Imagens/Inimigos/Boss/Warder_L.png",
                8,
                800,
                0.75,
                50,
                1,
                1,
                True
            )

        mob.sprite_mov.set_position(x,y)
        self.inimigos.append(mob)
    
    def update(self):
        if self.posCD <= 0:
            self.j_pos_x = self.jogador.fiona.x
            self.j_pos_y = self.jogador.fiona.y
            self.posCD = 75
        else:
            self.posCD -= 1
        
        for mob in self.inimigos:
            if self.j_pos_x+self.jogador.fiona.width/2 > mob.sprite_mov.x+mob.sprite_mov.width/2:
                mob.vel_x = 1
            if self.j_pos_x+self.jogador.fiona.width/2 < mob.sprite_mov.x+mob.sprite_mov.width/2:
                mob.vel_x = -1
            if self.j_pos_y+self.jogador.fiona.height/2 > mob.sprite_mov.y+mob.sprite_mov.height/2:
                mob.vel_y = 1
            if self.j_pos_y+self.jogador.fiona.height/2 < mob.sprite_mov.y+mob.sprite_mov.height/2:
                mob.vel_y = -1

            mob.sprite_mov.x += mob.vel * mob.vel_x * self.window.delta_time()
            mob.sprite_mov.y += mob.vel * mob.vel_y * self.window.delta_time()
            
        for mob in self.inimigos:
            for tiro in self.jogador.vet_tiro:
                if tiro.bullet.collided(mob.sprite_mov):
                    self.jogador.vet_tiro.remove(tiro)
                    mob.vida -= 1
                if mob.vida <= 0:
                    self.inimigos.remove(mob)
                    break
        
        for mob in self.inimigos:
            mob.sprite_mov.update()
            mob.sprite_mov.draw()
        
        
        
        
            