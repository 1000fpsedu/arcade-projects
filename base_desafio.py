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




'''
Função com a logica de atualização do jogo
'''
def update():
    # Insira aqui a lógica de atualização de seu jogo.
    # Lembre-se de pensar em Elementos reutilizaveis e utilizar
    # Para deixar seu código mais legivel.
    pass

'''
Função para desenhar os elementos na tela
'''
def render():
    arcade.set_background_color((100, 100, 255))
    arcade.start_render()
    # Código de renderização aqui dentro!
    

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

    arcade.schedule(MainLoop, 1/60)

    arcade.run()

if __name__ == "__main__":
    main()
