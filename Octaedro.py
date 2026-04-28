#Trabalho realizado por Eduardo Rais da Silva

from re import match #Importando as bibliotecas necessárias para manipulação de matrizes e visualização gráfica

import numpy as np
import matplotlib.pyplot as plt

def desenhaLinhas(x1, x2, y1, y2):
    plt.plot([x1, x2], [y1, y2], 'bo-')

def desenhaObjeto(objeto):
    #Desenha as linhas do octaedro
    #p0 conecta com p1, p3, p4, p5
                        #x1           #x2           #y1           #y2
    desenhaLinhas(objeto[0][0], objeto[1][0], objeto[0][1], objeto[1][1])
    desenhaLinhas(objeto[0][0], objeto[3][0], objeto[0][1], objeto[3][1])
    desenhaLinhas(objeto[0][0], objeto[4][0], objeto[0][1], objeto[4][1])
    desenhaLinhas(objeto[0][0], objeto[5][0], objeto[0][1], objeto[5][1])

    #p1 conecta com p0, p2, p4 e p5
    desenhaLinhas(objeto[1][0], objeto[0][0], objeto[1][1], objeto[0][1])
    desenhaLinhas(objeto[1][0], objeto[2][0], objeto[1][1], objeto[2][1])
    desenhaLinhas(objeto[1][0], objeto[4][0], objeto[1][1], objeto[4][1])
    desenhaLinhas(objeto[1][0], objeto[5][0], objeto[1][1], objeto[5][1])

    #p2 conecta com p1, p3, p4 e p5
    desenhaLinhas(objeto[2][0], objeto[1][0], objeto[2][1], objeto[1][1])
    desenhaLinhas(objeto[2][0], objeto[3][0], objeto[2][1], objeto[3][1])
    desenhaLinhas(objeto[2][0], objeto[4][0], objeto[2][1], objeto[4][1])
    desenhaLinhas(objeto[2][0], objeto[5][0], objeto[2][1], objeto[5][1])

    #p3 conecta com p0, p2, p4 e p5
    desenhaLinhas(objeto[3][0], objeto[0][0], objeto[3][1], objeto[0][1])
    desenhaLinhas(objeto[3][0], objeto[2][0], objeto[3][1], objeto[2][1])
    desenhaLinhas(objeto[3][0], objeto[4][0], objeto[3][1], objeto[4][1])
    desenhaLinhas(objeto[3][0], objeto[5][0], objeto[3][1], objeto[5][1])


#Função auxiliar para obter entrada numérica segura
def obter_opcao(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

#Menus para escolher qual ação realizar
def menuPrincipal():
    print("Menu Principal")
    print("1. Manipular o objeto")
    print("2. Manipular a câmera")
    print("3. Modificar projeção")
    print("4. Modificar mapeamento")
    print("5. Visualizar o objeto")
    print("6. Sair")

    return obter_opcao("Escolha uma opção: ")

#Menu para escolher qual transformação realizar no objeto
def menuObjeto():
    print("Como deseja manipular o objeto?")
    print("1. Translação")
    print("2. Escala")
    print("3. Rotação em X")
    print("4. Rotação em Y")
    print("5. Rotação em Z")
    print("6. Voltar ao menu principal")
    return obter_opcao("Escolha uma opção: ")

#Menu para escolher qual transformação realizar na câmera
def menuCamera():
    print("Como deseja manipular a câmera?")
    print("1. Translação")
    print("2. Rotação em X")
    print("3. Rotação em Y")
    print("4. Rotação em Z")
    print("5. Voltar ao menu principal")
    return obter_opcao("Escolha uma opção: ")

#Menu para escolher qual tipo de projeção utilizar
def menuProjecao():
    print("Qual tipo de projeção deseja utilizar?")
    print("1. Projeção Perspectiva")
    print("2. Projeção Paralela")
    return obter_opcao("Escolha uma opção: ")

#Menu para escolher qual tipo de mapeamento utilizar
def menuMapeamento():
    print("Qual tipo de mapeamento deseja alterar?")
    print("1. Window")
    print("2. Viewport")
    print("3. Voltar ao menu principal")
    return obter_opcao("Escolha uma opção: ")


#Transformações no objeto
def translacao(tx, ty, tz):
    matriz = np.array([ [1, 0, 0, tx],
                        [0, 1, 0, ty],
                        [0, 0, 1, tz],
                        [0, 0, 0, 1]])
    return matriz

#Escala é feita multiplicando as coordenadas do objeto pelos fatores de escala em cada eixo
def escala(sx, sy, sz):
    matriz = np.array([ [sx, 0,  0,  0],
                        [0,  sy, 0,  0],
                        [0,  0,  sz, 0],
                        [0,  0,  0,  1]])
    return matriz

#Rotação é feita em cada eixo, onde o ângulo de rotação é convertido para radianos
def rotacaoX(angulo):
    angulo = np.radians(angulo)
    matriz = np.array([ [1,  0,              0,               0],
                        [0,  np.cos(angulo), -np.sin(angulo), 0],
                        [0,  np.sin(angulo),  np.cos(angulo), 0],
                        [0,  0,              0,               1]])
    
    return matriz

#Rotação em Y é feita multiplicando as coordenadas do objeto pelos fatores de rotação em cada eixo
def rotacaoY(angulo):
    angulo = np.radians(angulo)
    matriz = np.array([ [np.cos(angulo),    0,  np.sin(angulo), 0],
                        [0,                 1,  0,              0],
                        [-np.sin(angulo),   0,  np.cos(angulo), 0],
                        [0,                 0,  0,              1]])
    return matriz

#Rotação em Z é feita multiplicando as coordenadas do objeto pelos fatores de rotação em cada eixo
def rotacaoZ(angulo):
    angulo = np.radians(angulo)
    matriz = np.array([ [np.cos(angulo), -np.sin(angulo), 0, 0],
                        [np.sin(angulo), np.cos(angulo),  0, 0],
                        [0,              0,               1, 0],
                        [0,              0,               0, 1]])
    return matriz

#Transformações na câmera
def cameraTranslacao(camx, camy, camz):
    translacao = np.array([[1, 0, 0, -camx],
                           [0, 1, 0, -camy],
                           [0, 0, 1, -camz],
                           [0, 0, 0,    1]])
    return translacao

#Rotação da câmera pelo eixo X
def cameraRotacaoX(angulo):
    angulo = (np.radians(angulo)*-1)
    rotacaoX = np.array([[1,       0,               0,        0],
                         [0, np.cos(angulo), -np.sin(angulo), 0],
                         [0, np.sin(angulo),  np.cos(angulo), 0],
                         [0,       0,               0,        1]])
    return rotacaoX

#Rotação da câmera pelo eixo Y
def cameraRotacaoY(angulo):
    angulo = (np.radians(angulo)*-1)
    rotacaoY = np.array([[np.cos(angulo),    0,  np.sin(angulo), 0],
                         [0,                 1,  0,              0],
                         [-np.sin(angulo),   0,  np.cos(angulo), 0],
                         [0,                 0,  0,              1]])
    return rotacaoY

#Rotação da câmera pelo eixo Z
def cameraRotacaoZ(angulo):
    angulo = (np.radians(angulo)*-1)
    rotacaoZ = np.array([[np.cos(angulo), -np.sin(angulo), 0, 0],
                         [np.sin(angulo), np.cos(angulo),  0, 0],
                         [0,              0,               1, 0],
                         [0,              0,               0, 1]])
    return rotacaoZ

#Projeção perspectiva
def projecaoPerspectiva(fovy, aspect, znear, zfar):
    fovy = np.radians(fovy)
    
    a = 1/(np.tan(fovy/2)*aspect)
    b = 1/np.tan(fovy/2)
    c = (zfar+znear)/(znear-zfar)
    d = (2*zfar*znear)/(znear-zfar)

    mp = np.array([[a, 0, 0, 0],
                   [0, b, 0, 0],
                   [0, 0, c, d],
                   [0, 0, -1, 0]])
    return mp

#Projeção paralela
def projecaoParalela(right, left, top, bottom, near, far):
    a = 2 / (right - left)
    b = 2 / (top - bottom)
    c = -2 / (far - near)
    d = -(right + left) / (right - left)
    e = -(top + bottom) / (top - bottom)
    f = -(far + near) / (far - near)

    mp = np.array([[a, 0, 0, d],
                   [0, b, 0, e],
                   [0, 0, c, f],
                   [0, 0, 0, 1]])
    return mp

#Função para aplicar o mapeamento da Window para a Viewport, onde as coordenadas do objeto são convertidas para a escala da Viewport
def aplicarMapeamento(obj_prsp):
    #Divisão por w para obter as coordenadas dentro de 1
    for i in range(len(obj_prsp)):
        if obj_prsp[i][3] != 0:
            obj_prsp[i][0] /= obj_prsp[i][3]
            obj_prsp[i][1] /= obj_prsp[i][3]

    #Para cada ponto do objeto projetado, as coordenadas são convertidas para a escala da Viewport utilizando a fórmula de mapeamento da Window para a Viewport
    objeto = []
    for p in obj_prsp:
        xw = p[0]
        yw = p[1]

        xv = ((xw - xminw) / (xmaxw - xminw)) * (xmaxv - xminv) + xminv
        yv = ((yw - yminw) / (ymaxw - yminw)) * (ymaxv - yminv) + yminv
        objeto.append([xv, yv])

    return np.array(objeto)

#Função para renderizar o objeto, onde as transformações são aplicadas na ordem: modelo, câmera, projeção e mapeamento
def renderizar():
    obj_modelo = (modelo @ objeto.T).T
    obj_cam = (camera @ obj_modelo.T).T
    obj_prsp = (matrizProjecao @ obj_cam.T).T
    obj_2d = aplicarMapeamento(obj_prsp)

    plt.clf() #Limpa a tela para desenhar o objeto atualizado
    plt.axis('equal') #Mantém a proporção do objeto
    desenhaObjeto(obj_2d)
    plt.draw() #Desenha o objeto na tela
    plt.pause(0.001) #Pausa para permitir que o objeto seja renderizado antes de continuar com o programa


#Definindo os limites da Window, onde os objetos serão renderizados (Valores padrão, podem ser alterados no menu de mapeamento)
xminw = -1
xmaxw = 1
yminw = -1
ymaxw = 1

#Definindo os limites da Viewport, onde os objetos serão renderizados (Valores padrão, podem ser alterados no menu de mapeamento)
xminv = 0
xmaxv = 500
yminv = 0
ymaxv = 500


#Modelagem do octaedro (Nosso objeto 3D)
                    #x    y    z   w
objeto = np.array([[0.5,  0,   0,  1], #p0
                  [0,   0.5,  0,  1],  #p1
                  [-0.5, 0,   0,  1],  #p2
                  [0,  -0.5,  0,  1],  #p3
                  [0,    0,  0.5, 1],  #p4
                  [0,    0, -0.5, 1]]) #p5

#Modelo para aplicar as transformações no objeto
modelo = np.identity(4)

#Matriz de projeção, onde a projeção perspectiva é definida como padrão, mas pode ser alterada no menu de projeção
matrizProjecao = projecaoPerspectiva(60, 1, 0.1, 100)

#Camera é representada por uma matriz identidade para guardas as mudanças na camera
camera = np.identity(4)

#Renderiza o objeto inicial
renderizar()

#Exibindo o menu principal para o usuário escolher as ações a serem realizadas
print("Bem-vindo ao programa de manipulação de objetos 3D!")
print("Modelagem do octaedro criada com sucesso")
print(objeto)

#Loop principal do programa, onde o menu é exibido e as ações são realizadas de acordo com a escolha do usuário, até que a opção de sair seja selecionada
while True:
    opcao = menuPrincipal()
    match opcao:
        case 1:
            while True: 
                opcaoObj = menuObjeto() #Exibe o menu de manipulação do objeto e aguarda a escolha do usuário
                match opcaoObj:
                    case 1:
                        tx = float(input("Digite o valor de translação em X: "))
                        ty = float(input("Digite o valor de translação em Y: "))
                        tz = float(input("Digite o valor de translação em Z: "))
                        matrizTranslacao = translacao(tx, ty, tz)
                        modelo = matrizTranslacao @ modelo
                        print("Objeto transladado")
                        renderizar()

                    case 2:
                        sx = float(input("Digite o valor de escala em X: "))
                        sy = float(input("Digite o valor de escala em Y: "))
                        sz = float(input("Digite o valor de escala em Z: "))
                        matrizEscala = escala(sx, sy, sz)
                        modelo = matrizEscala @ modelo
                        print("Objeto escalado")
                        renderizar()

                    case 3:
                        angulo = float(input("Digite o valor de rotação em X: "))
                        matrizRotacaoX = rotacaoX(angulo)
                        modelo = matrizRotacaoX @ modelo
                        print("Objeto rotacionado em X")
                        renderizar()
                    
                    case 4:
                        angulo = float(input("Digite o valor de rotação em Y: "))
                        matrizRotacaoY = rotacaoY(angulo)
                        modelo = matrizRotacaoY @ modelo
                        print("Objeto rotacionado em Y")
                        renderizar()
                    
                    case 5:
                        angulo = float(input("Digite o valor de rotação em Z: "))
                        matrizRotacaoZ = rotacaoZ(angulo)
                        modelo = matrizRotacaoZ @ modelo
                        print("Objeto rotacionado em Z")
                        renderizar()

                    case _:
                        print("Opção inválida")

                if opcaoObj == 6:
                    print("Voltando ao menu principal")
                    break
        case 2:
            opcaoCam = menuCamera() #Exibe o menu de manipulação da câmera e aguarda a escolha do usuário
            match opcaoCam:
                case 1:
                    cx = float(input("Digite o valor de translação em X: "))
                    cy = float(input("Digite o valor de translação em Y: "))
                    cz = float(input("Digite o valor de translação em Z: "))
                    matrizVisualizacao = cameraTranslacao(cx, cy, cz)
                    camera = matrizVisualizacao @ camera
                    print("Câmera transladada")
                    renderizar()
                
                case 2:
                    angulo = float(input("Digite o valor de rotação em X: "))
                    matrizVisualizacao = cameraRotacaoX(angulo)
                    camera = matrizVisualizacao @ camera
                    print("Câmera rotacionada em X")
                    renderizar()

                case 3:
                    angulo = float(input("Digite o valor de rotação em Y: "))
                    matrizVisualizacao = cameraRotacaoY(angulo)
                    camera = matrizVisualizacao @ camera
                    print("Câmera rotacionada em Y")
                    renderizar()

                case 4:
                    angulo = float(input("Digite o valor de rotação em Z: "))
                    matrizVisualizacao = cameraRotacaoZ(angulo)
                    camera = matrizVisualizacao @ camera
                    print("Câmera rotacionada em Z")
                    renderizar()

                case _:
                    print("Opção inválida")
            
            if opcaoCam == 5:
                print("Voltando ao menu principal")
                break

        case 3:
            match menuProjecao(): #Exibe o menu de projeção e aguarda a escolha do usuário
                case 1:
                    print("Projeção Perspectiva selecionada")
                    fovy = float(input("Digite o valor do campo de visão: "))
                    aspect = float(input("Digite o valor da razão de aspecto: "))
                    znear = float(input("Digite o valor do plano de recorte: "))
                    zfar = float(input("Digite o valor do plano de projeção: "))

                    matrizProjecao = projecaoPerspectiva(fovy, aspect, znear, zfar)
                    renderizar()

                    print("Projeção Perspectiva aplicada")

                case 2:
                    print("Projeção Paralela selecionada")
                    right = float(input("Digite o valor do lado direito: "))
                    left = float(input("Digite o valor do lado esquerdo: "))
                    top = float(input("Digite o valor do topo: "))
                    bottom = float(input("Digite o valor da parte inferior: "))
                    near = float(input("Digite o valor do plano de near: "))
                    far = float(input("Digite o valor do plano de far: "))

                    matrizProjecao = projecaoParalela(right, left, top, bottom, near, far)
                    renderizar()

                    print("Projeção Paralela aplicada")
                    
                case _:
                    print("Opção inválida")

        case 4:
            opcaoMap = menuMapeamento() #Exibe o menu de mapeamento e aguarda a escolha do usuário
            match opcaoMap:
                case 1:
                    xminw = float(input("Digite o valor do limite mínimo em X da Window: "))
                    yminw = float(input("Digite o valor do limite mínimo em Y da Window: "))
                    xmaxw = float(input("Digite o valor do limite máximo em X da Window: "))
                    ymaxw = float(input("Digite o valor do limite máximo em Y da Window: "))
                    
                    renderizar()

                    print("Window atualizada")

                case 2:
                    xminv = float(input("Digite o valor do limite mínimo em X da Viewport: "))
                    yminv = float(input("Digite o valor do limite mínimo em Y da Viewport: "))
                    xmaxv = float(input("Digite o valor do limite máximo em X da Viewport: "))
                    ymaxv = float(input("Digite o valor do limite máximo em Y da Viewport: "))
                    
                    renderizar()

                    print("Viewport atualizada")
                            
                case _:
                    print("Opção inválida")

            if opcaoMap == 3:
                print("Voltando ao menu principal")
                break

        #Renderiza o objeto
        case 5:
            print("Renderizando o objeto...")
            # 1. objeto original
            obj_modelo = (modelo @ objeto.T).T
            print("Objeto modelado")
            print(obj_modelo)

            # 2. câmera
            obj_cam = (camera @ obj_modelo.T).T
            print("Objeto na câmera")
            print(obj_cam)

            # 3. projeção
            obj_prsp = (matrizProjecao @ obj_cam.T).T
            print("Objeto projetado")
            print(obj_prsp)

            # 4. mapping (já faz divisão por w)
            obj_2d = aplicarMapeamento(obj_prsp)
            print("Objeto mapeado para 2D")
            print(obj_2d)

            # 5. desenha
            renderizar()
            print("Objeto renderizado")

        #Caso uma opção inválida seja selecionada, uma mensagem de erro é exibida
        case _:
            print("Opção inválida")

    #Encerrando o programa caso a opção 6 seja selecionada
    if opcao == 6:
        print("Saindo do programa")
        break