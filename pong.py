'''
Projeto para a disciplina de Algoritmos para Jogos II - 2023.2
Integrantes:
    - 0000000000 : Fulano
    - 0000000000 : Beltrano
'''
'''
Importando a biblioteca arcade que é responsavel por gerenciar
a janela de seu jogo, parte gráfica e possivel física.
docs: https://api.arcade.academy/en/latest/arcade.html
'''
import arcade
'''
Importando a biblioteca de pseudo-aleatoriedade pois pode ser
extremamente útil para o desenvolvimento de seu jogo
docs: https://docs.python.org/pt-br/3/library/random.html
'''
import random

# CONSTANTES
TECLA_W = 119
TECLA_S = 115
TECLA_CIMA = 65362
TECLA_BAIXO = 65364

bolinha = { "x" : 200, "y" : 300, "vx" : 2, "vy" : 2 } 
jogador1 = { "x" :  50, "y" : 200, "pontos": 0 }
jogador2 = { "x" : 550, "y" : 200, "pontos": 0 }
comandos = { "p1_cima" : False, "p1_baixo": False ,
             "p2_cima" : False, "p2_baixo": False }

def key_pressed(simbolo, modificador):
    if(simbolo == TECLA_W):
        comandos["p1_cima"] = True

    if(simbolo == TECLA_S):
        comandos["p1_baixo"] = True
    
    if(simbolo == TECLA_CIMA):
        comandos["p2_cima"] = True

    if(simbolo == TECLA_BAIXO):
        comandos["p2_baixo"] = True
    pass

def key_released(simbolo, modificador):
    if(simbolo == TECLA_W):
        comandos["p1_cima"] = False

    if(simbolo == TECLA_S):
        comandos["p1_baixo"] = False
    
    if(simbolo == TECLA_CIMA):
        comandos["p2_cima"] = False

    if(simbolo == TECLA_BAIXO):
        comandos["p2_baixo"] = False
    pass

def colisao_bolinha():
    if(bolinha["x"] > jogador1["x"] - 5 and 
       bolinha["x"] < jogador1["x"] + 5):
        if(bolinha["y"] > jogador1["y"] - 25 and 
           bolinha["y"] < jogador1["y"] + 25):
            bolinha["vx"] = -bolinha["vx"]
    
    if(bolinha["x"] > jogador2["x"] - 5 and 
       bolinha["x"] < jogador2["x"] + 5):
        if(bolinha["y"] > jogador2["y"] - 25 and 
           bolinha["y"] < jogador2["y"] + 25):
            bolinha["vx"] = -bolinha["vx"]
    pass


def atualiza_bolinha():
    minX = 30
    maxX = 570
    minY = 30
    maxY = 370
    
    # Salvando os valores localmente
    x = bolinha["x"]
    y = bolinha["y"]
    vx = bolinha["vx"]
    vy = bolinha["vy"]

    #verifica os limites
    ## Direita e Esquerda
    if( x < minX ):
        jogador2["pontos"] += 1
        x = 300
        y = 200
        vx = - vx
    elif( x > maxX ):
        jogador1["pontos"] += 1
        x = 300
        y = 200
        vx = - vx

    ## Superior e Inferior
    if ( y < minY ):
        vy = 2
    elif( y > maxY):
        vy = -2

    # Atualiza bolinha:
    bolinha["vx"] = vx
    bolinha["vy"] = vy
    bolinha["x"] = x + vx
    bolinha["y"] = y + vy

    colisao_bolinha()
    pass

def desenha_bolinha():
    arcade.draw_rectangle_filled(
            center_x    = bolinha["x"],
            center_y    = bolinha["y"],
            width       = 10,
            height      = 10,
            color       = (255, 255, 255)
            )

    pass

def desenha_quadra():
    #Inferior
    arcade.draw_lrtb_rectangle_filled(
            left=20, 
            right=580,
            bottom=20,
            top=30, 
            color=(255,255,255)
            )
    #Superior
    arcade.draw_lrtb_rectangle_filled(
            left=20, 
            right=580,
            bottom=370,
            top=380, 
            color=(255,255,255)
            )
    #Esquerda
    arcade.draw_lrtb_rectangle_filled(
            left=20, 
            right=30,
            bottom=20,
            top=380, 
            color=(255,255,255)
            )
    #Direita
    arcade.draw_lrtb_rectangle_filled(
            left=570, 
            right=580,
            bottom=20,
            top=380, 
            color=(255,255,255)
            )

    #Centro
    arcade.draw_lrtb_rectangle_filled(
            left=299, 
            right=301,
            bottom=20,
            top=380, 
            color=(255,255,255)
            )
    pass


def atualiza_jogador1():
    if(comandos["p1_cima"] == True):
        if(jogador1["y"] + 25 < 370):
            jogador1["y"] += 2;

    if(comandos["p1_baixo"] == True):
        if(jogador1["y"] - 25 > 30):
            jogador1["y"] -= 2;

    pass

def desenha_jogador1():
    arcade.draw_rectangle_filled(
            center_x=jogador1["x"],
            center_y=jogador1["y"],
            width=10,
            height=50,
            color=(255, 255, 255)
            )
    pass

def atualiza_jogador2():
    if(comandos["p2_cima"] == True):
        if(jogador2["y"] + 25 < 370):
            jogador2["y"] += 2;

    if(comandos["p2_baixo"] == True):
        if(jogador2["y"] - 25 > 30):
            jogador2["y"] -= 2;

    pass

def desenha_jogador2():
    arcade.draw_rectangle_filled(
            center_x=jogador2["x"],
            center_y=jogador2["y"],
            width=10,
            height=50,
            color=(255, 255, 255)
            )

def desenha_placar():
    arcade.draw_text(jogador1["pontos"], 
                     start_x=100,
                     start_y=300,
                     color=(255, 255, 255),
                     font_size=20,
                     bold=True)
    arcade.draw_text(jogador2["pontos"], 
                     start_x=500,
                     start_y=300,
                     color=(255, 255, 255),
                     font_size=20,
                     bold=True)
    pass
                

'''
Função com a logica de atualização do jogo
'''
def update():
    # Insira aqui a lógica de atualização de seu jogo.
    # Lembre-se de pensar em Elementos reutilizaveis e utilizar
    # Para deixar seu código mais legivel.
    atualiza_bolinha()
    atualiza_jogador1()
    atualiza_jogador2()
    pass

'''
Função para desenhar os elementos na tela
'''
def render():
    arcade.set_background_color((100, 100, 255))
    arcade.start_render()
    # Código de renderização aqui dentro!

    desenha_quadra()
    desenha_bolinha()
    desenha_jogador1()
    desenha_jogador2()
    desenha_placar()
    

    arcade.finish_render()
    pass

'''
Game Loop.
'''
def  MainLoop(delta_t):
    update()
    render()
    pass

'''
Inicialização do arcade
'''
def main():
    arcade.open_window(600, 400, "Primeiro Programa")
    arcade.get_window().on_key_press = key_pressed
    arcade.get_window().on_key_release = key_released
    arcade.schedule(MainLoop, 1/60)

    arcade.run()

if __name__ == "__main__":
    main()
