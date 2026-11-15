"""
Módulo: doce_ai_jr.py
Descrição: Novo Teste com a Implementação da Biblioteca Random
"""
import random as rd

__autor__ = "Marcos Vinicios 'JR' "
__versao__ = "0.1.1"
__data_hora__ = "15/11/2026 - 16:01"

# Funcionamento do Desejo interno de doceiro de JR

# Dados de entrada e calculos de decisão
def calculos_oculto(x1, x2, y1, y2, vies):
    z = (x1*y1) - (x2*y2) + vies # Ajuste no calculo que sempre dava positivo

    if z >= 0:
        return True, z
    return False, z

# Resultado da Saída
def calculos_saida(decisao, z):
    if decisao:
        return f"Vou comer doce!\nResultado da decisão: {z}"
    return f"Não vou comer doce!\nResultado da decisão: {z}"

# Valores e pesos gerados de forma aleatoria
desejo = rd.randint(0,10)        # Nivel de desejo de doce (0 a 10)
prejuizo = rd.randint(0,10)      # O Prejuizo do Doce (-10 a 0)
peso_desejo = rd.randint(1,5)    # Influencia do Desejo (1 a 5)
peso_prejuizo = rd.randint(1,5)  # Influencia do Prejuizo (1 a 5)
vies = rd.randint(-5,5)          # Nivel do Vies

resultado_decisao, resultado_z = calculos_oculto(desejo,prejuizo,peso_desejo,peso_prejuizo,vies)
resultado = calculos_saida(resultado_decisao, resultado_z)

print(f"Desejo: {desejo} | Peso: {peso_desejo}\n"
      f"Prejuízo: {prejuizo} | Peso: {peso_prejuizo}\n"
      f"Viés: {vies}\n")
print(resultado)