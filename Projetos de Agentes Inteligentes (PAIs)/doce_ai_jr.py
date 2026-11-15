"""
Módulo: doce_ai_jr.py
Descrição: Primeira tentativa de criação de Agente Inteligente
"""
__autor__ = "Marcos Vinicios 'JR' "
__versao__ = "0.1.0"
__data_hora__ = "14/11/2026 - 21:39"

# Funcionamento do Desejo interno de doceiro de JR

# Dados de entrada e calculos de decisão
def calculos_oculto(x1, x2, y1, y2, vies):
    z = (x1*y1) + (x2*y2) + vies

    if z >= 0:
        return True, z
    return False, z

# Resultado da Saída
def calculos_saida(decisao, z):
    if decisao:
        return f"Vou comer doce!\nResultado da decisão: {z}"
    return f"Não vou comer doce!\nResultado da decisão: {z}"

# Valores e pesos
desejo = 3 # Devia ser 2000
dinheiro = -4
peso_desejo = 2
peso_dinheiro = -3
vies = -2

resultado_decisao, resultado_z = calculos_oculto(desejo,dinheiro,peso_desejo,peso_dinheiro,vies)
resultado = calculos_saida(resultado_decisao, resultado_z)
print(resultado)





