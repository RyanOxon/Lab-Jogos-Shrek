from PPlay.window import*
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from PPlay.keyboard import *
import globais
class Jogador(object):
    def __init__(self,window):
        self.window = window
        self.teclado = Keyboard()
        self.fiona = Sprite("./Imagens/Fiona/fiona.png", 6)
        self.fiona.set_position(globais.BORDER,30)
        self.fiona.set_total_duration(1000)
        self.vet_tiro= []
        self.reload_cron = 0
        self.drag = Dragao(self.fiona.y, 0)
        self.dragCD = 0

    def update(self):
        self.fiona.move_key_x(1)
        self.fiona.move_key_y(1)
        #IFs para limitar espaço de locomoção da fiona
        if self.fiona.x >= self.window.width-self.fiona.width:
            self.fiona.x = self.window.width-self.fiona.width
        if self.fiona.x <=0 :
            self.fiona.x=0
        
        if self.fiona.y <= 0:
            self.fiona.y=1
        if self.fiona.y>= self.window.height- self.fiona.height:
            self.fiona.y = self.window.height- self.fiona.height

        vely = 0
        velx = 0
    
        if (self.teclado.key_pressed("up")==True
            and self.teclado.key_pressed("down")==False
        ):
            vely = -1
        if (self.teclado.key_pressed("up")==False
            and self.teclado.key_pressed("down")==True
        ):        
            vely = 1
        if (self.teclado.key_pressed("left")==True
            and self.teclado.key_pressed("right")==False
        ):
            velx = -1
        if (self.teclado.key_pressed("left")==False
            and self.teclado.key_pressed("right")==True
        ):
            velx = 1
        if self.teclado.key_pressed("space") and self.reload_cron == 0:
            if(
                vely != 0
                or velx !=0
            ):            
                bala = Tiro(self.fiona.x+(self.fiona.width/2), self.fiona.y+(self.fiona.height/2), velx, vely)
                self.vet_tiro.append(bala)
                self.reload_cron = 100

        if self.reload_cron > 0:
            self.reload_cron -= 1
        
        self.fiona.update()
        self.fiona.draw()
        
        if len(self.vet_tiro)>0:
            for bala in self.vet_tiro:
                if (
                    bala.bullet.x < 0
                    or bala.bullet.x + bala.bullet.width > self.window.width
                    or bala.bullet.y < 0
                    or bala.bullet.y+bala.bullet.height > self.window.height
                ):
                    self.vet_tiro.remove(bala)
                else:    
                    bala.bullet.x += bala.vel_x*self.window.delta_time()
                    bala.bullet.y += bala.vel_y*self.window.delta_time()
                    bala.bullet.update()
                    bala.bullet.draw()

        if self.dragCD != 0:
            self.dragCD -=1
        if self.dragCD == 0 and self.teclado.key_pressed("A"):
            self.drag = Dragao(self.fiona.y, 250)
            self.dragCD = 500
        
        if self.drag.count > 0:
            self.drag.dragoneza.update()
            self.drag.dragoneza.draw()
            self.drag.fireBall.x +=10
            self.drag.fireBall.update()
            self.drag.fireBall.draw()
            self.drag.count -= 1

                    
class Tiro(object):
    def __init__(self, x_inicial, y_inicial, vel_x, vel_y):
        self.speed = 300
        self.bullet = Sprite("./Imagens/Fiona/bullet.png",8)
        self.bullet.set_total_duration(1)
        self.bullet.set_position(x_inicial, y_inicial)
        self.vel_x = vel_x *self.speed
        self.vel_y = vel_y *self.speed

class Dragao(object):
    def __init__(self, pos_y, count):
        self.dragoneza = Sprite("./Imagens/Fiona/Dragao_mov.png", 18)
        self.fireBall = Sprite("./Imagens/Fiona/fireBall.png", 4)
        self.fireBall.set_total_duration(1000)
        self.dragoneza.set_total_duration(1000)
        self.dragoneza.set_position(0, pos_y)
        self.fireBall.set_position(self.dragoneza.width,self.dragoneza.y+(self.dragoneza.height/2))
        self.count = count
