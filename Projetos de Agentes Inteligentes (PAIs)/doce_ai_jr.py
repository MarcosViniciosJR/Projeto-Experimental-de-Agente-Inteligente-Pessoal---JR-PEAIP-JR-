"""
Módulo: doce_ai_jr.py
Descrição: Aumentando a quantidade de entradas e complexidade do codigo
"""
import random as rd

__autor__ = "Marcos Vinicios 'JR' "
__versao__ = "0.1.3"
__data_hora__ = "15/11/2026 - 17:10"

# Funcionamento do Desejo interno de doceiro de JR

# Dados de entrada e calculos de decisão
def calculos_oculto(x1, x2, x3, x4, w1, w2, w3, w4, b):

    positivos = (x1 * w1) + (x2 * w2) # Calculo dos valores das entradas positivas

    negativos = (x3 * w3) + (x4 * w4) # Calculo dos valores das entradas negativas

    z = positivos - negativos + b     # Calculo final da decisão

    if z >= 0:
        return True, z, f'Resultado Positivos: {positivos}\nResultado Negativos: {negativos}'
    return False, z, f'Resultado Positivos: {positivos}\nResultado Negativos: {negativos}'

# Resultado da Saída
def calculos_saida(decisao, z, resultados_P_e_N):
    if decisao:
        return f"{resultados_P_e_N}\n\nResultado da decisão: {z}\nVou comer doce!"
    return f"{resultados_P_e_N}\n\nResultado da decisão: {z}\nNâo vou comer doce!"

# Valores positivos e negativos
desejo = rd.randint(0,10)        # Nivel de desejo de doce (0 a 10)
fome = rd.randint(0,10)          # A quantidade de fome (0 a 10)
prejuizo = rd.randint(0,10)      # O Prejuizo do Doce (0 a 10)
glicose = rd.randint(0,10)       # O nivel de glicose no sangue (0 a 10)

# Pesos dos valores
peso_desejo = rd.randint(1,5)    # Influencia do Desejo (1 a 5)
peso_fome = rd.randint(1,5)      # Influencia da Fome (1 a 5)
peso_prejuizo = rd.randint(1,5)  # Influencia do Prejuizo (1 a 5)
peso_glicose = rd.randint(1,5)   # Influencia da Glicose (1 a 5)

vies = rd.randint(-5,5)          # Nivel do Vies

resultado_decisao, resultado_z, resultado_calculos = calculos_oculto(desejo, fome, prejuizo, glicose, peso_desejo, peso_fome, peso_prejuizo, peso_glicose, vies)
resultado = calculos_saida(resultado_decisao, resultado_z, resultado_calculos)

# Resultado dos valores e pesos
print(f"Desejo: {desejo} | Peso: {peso_desejo}\n"
      F"Fome: {fome} | Peso: {peso_fome}\n"
      f"Prejuízo: {prejuizo} | Peso: {peso_prejuizo}\n"
      f"Glicose: {glicose} | Peso: {peso_glicose}\n"
      f"Viés: {vies}\n")
print(resultado)