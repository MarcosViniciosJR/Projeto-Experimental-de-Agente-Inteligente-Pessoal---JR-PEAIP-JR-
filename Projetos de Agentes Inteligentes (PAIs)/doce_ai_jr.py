"""
Módulo: doce_ai_jr.py
Descrição: Aumentando a quantidade de entradas e complexidade do codigo
"""
import random as rd
import time as t

__autor__ = "Marcos Vinicios 'JR' "
__versao__ = "0.1.5"
__data_hora__ = "15/11/2026 - 19:49"

# Funcionamento do Desejo interno de doceiro de JR

# Dados de entrada e calculos de decisão
def calculos_oculto(x1, x2, x3, w1, w2, w3, b):

    positivos = x1 * w1 # Calculo dos valores das entradas positivas
    negativos = (x2 * w2) + (x3 * w3) # Calculo dos valores das entradas negativas
    z = positivos - negativos + b     # Calculo final da decisão

    return z >= 0, z

# Pesos dos valores
peso_desejo = float(f"{rd.uniform(0.1, 10.0):.2f}")   # Influencia do Desejo 
peso_dinheiro = float(f"{rd.uniform(0.1, 1.0):.2f}") # Influencia do Dinheiro 
peso_glicose = float(f"{rd.uniform(0.1, 10.0):.2f}")  # Influencia da Glicose 

vies = float(f"{rd.uniform(0.1, 10.0):.2f}")          # Nivel do Vies


# Joguinho de Sobrevivencia: Mês da Luta contra o desejo de Açucar

tentativa = 1
while True:

    print(f"\nTentativa {tentativa}\n")

    # Valores positivos e negativos
    desejo = float(f"{rd.uniform(0.1, 20.0):.2f}")   # Nivel de desejo de doce
    dinheiro = 260 # Quantidade de Dinheiro na conta
    glicose = float(f"{rd.uniform(0.1, 20.0):.2f}")   # O nivel de glicose no sangue 


    vivo = True
    morte = ""
    # Objetivo é chegar no dia 30 sem morrer
    for dia in range(30):
        print(f"Dia {dia}")
        print(f"Seus Status: Desejo: {desejo:.2f} | Dinheiro: {dinheiro:.2f} | Glicose: {glicose:.2f}\n")

        comer, valor_z = calculos_oculto(desejo, dinheiro, glicose, peso_desejo, peso_dinheiro, peso_glicose, vies)

        if comer:
            print("Decidiu Comprar um Doce Hoje!")
            desejo -= 10
            glicose += 5
            dinheiro -= 20
            print("-"*50)
        else:
            print("Decidiu Não Comprar um Doce Hoje!")
            desejo += 10
            glicose -= 5
            print("-"*50)

        if desejo < 0:
            desejo = 0
        if glicose < 0:
            glicose = 0

        t.sleep(0.25)

        if glicose >= 100:
            print("Você morreu por overdose em açucar")
            vivo = False
            morte = "glicose"
            break
        elif dinheiro <= 0:
            print("Você morreu por não conseguir pagar as contas até o fim do mes")
            vivo = False
            morte = "dinheiro"
            break
        elif desejo >= 100:
            print("Você enlouqueceu e perdeu o controle do seu desejo por açucar e foi preso e levado a um manicomio")
            vivo = False
            morte = "desejo"
            break

    if vivo:
        print("Você SOBREVIVEU até o fim do mes, PARABENS")

    else:
        if morte == "glicose":
            ajuste = float(f"{rd.uniform(0.1,1.0):.2f}")

            peso_glicose += ajuste
            peso_desejo -= ajuste
            peso_dinheiro -= ajuste

            if peso_desejo <= 0:
                peso_desejo = 0.1
            if peso_dinheiro <= 0:
                peso_dinheiro = 0.1

        elif morte == "dinheiro":
            ajuste = float(f"{rd.uniform(0.1,1.0):.2f}")

            peso_dinheiro += ajuste
            peso_desejo -= ajuste
            peso_glicose -= ajuste

            if peso_desejo <= 0:
                peso_desejo = 0.1
            if peso_glicose <= 0:
                peso_glicose = 0.1

        elif morte == "desejo":
                ajuste = float(f"{rd.uniform(0.1,1.0):.2f}")

                peso_desejo += ajuste
                peso_glicose -= ajuste
                peso_dinheiro -= ajuste

                if peso_glicose <= 0:
                    peso_glicose = 0.1
                if peso_dinheiro <= 0:
                    peso_glicose = 0.1

    print(f"Fim da Partida")
    print(f"Pesos: glicose: {peso_glicose:.2f} | desejo: {peso_desejo:.2f} | dinheiro: {peso_dinheiro:.2f}")
    tentativa += 1
    
    continuar = int(input("Deseja continuar o jogo? (0 - ñ | 1 - s): "))
    
    if continuar == 0:
        print("\nEncerrando o simulador!")
        break

