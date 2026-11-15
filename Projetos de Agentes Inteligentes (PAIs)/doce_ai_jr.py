"""
Módulo: doce_ai_jr.py
Descrição: Aumentando a quantidade de entradas e complexidade do codigo
"""
import random as rd
import time as t

__autor__ = "Marcos Vinicios 'JR' "
__versao__ = "0.1.4"
__data_hora__ = "15/11/2026 - 17:10"

# Funcionamento do Desejo interno de doceiro de JR

# Dados de entrada e calculos de decisão
def calculos_oculto(x1, x2, x3, w1, w2, w3, b):

    positivos = x1 * w1 # Calculo dos valores das entradas positivas
    negativos = (x2 * w2) + (x3 * w3) # Calculo dos valores das entradas negativas
    z = positivos - negativos + b     # Calculo final da decisão

    return z >= 0, z

# Resultado da Saída
def calculos_saida(decisao, z, resultados_P_e_N):
    if decisao:
        return f"{resultados_P_e_N}\n\nResultado da decisão: {z}\nVou comer doce!"
    return f"{resultados_P_e_N}\n\nResultado da decisão: {z}\nNâo vou comer doce!"

# Pesos dos valores
peso_desejo = 2   # Influencia do Desejo 
peso_dinheiro = 1 # Influencia do Dinheiro 
peso_glicose = 3 # Influencia da Glicose 

vies = 0          # Nivel do Vies

tentativa = 1
# Joguinho de Sobrevivencia: Mês da Luta contra o desejo de Açucar
while True:

    print(f"\nTentativa {tentativa}\n")

    # Valores positivos e negativos
    desejo = 50    # Nivel de desejo de doce
    dinheiro = 200 # Quantidade de Dinheiro na conta
    glicose = 40   # O nivel de glicose no sangue 


    vivo = True
    morte = ""

    for dia in range(30):
        print(f" Dia {dia}")

        comer, valor_z = calculos_oculto(desejo, dinheiro, glicose, peso_desejo, peso_dinheiro, peso_glicose, vies)

        if comer:
            print("Decidiu Comprar um Doce Hoje!")
            desejo -= rd.randint(5,15)
            glicose += rd.randint(5,15)
            dinheiro -= 15
        else:
            print("Decidiu Não Comprar um Doce Hoje!")
            desejo += 5
            glicose -= 5

        if desejo < 0:
            desejo = 0
        if glicose < 0:
            glicose = 0

        t.sleep(0.5)


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
            ajuste = rd.uniform(0.1,1.0)

            peso_glicose += ajuste
            peso_desejo -= ajuste

            if peso_desejo < 1:
                peso_desejo = 1

        elif morte == "dinheiro":
            peso_dinheiro += rd.uniform(0.1,1.0)

        elif morte == "desejo":
                    peso_desejo += rd.uniform(0.1,1.0)

    print(f"Fim da Partida")
    tentativa += 1
    
    continuar = int(input("Deseja continuar o jogo? (0 - ñ | 1 - s): "))
    
    if continuar == 0:
        print("\nEncerrando o simulador. Até logo, JR!")
        break

