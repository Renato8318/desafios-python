#Análise de faturamento diário

import json

# Simulação de faturamento no formato JSON
faturamento_json = '''
[0, 100, 200, 0, 300, 400, 0, 0, 150, 250, 500, 0, 0]
'''

# Convertendo JSON para lista
faturamento = json.loads(faturamento_json)

# Calculando valores
faturamento = [f for f in faturamento if f > 0]  # Ignorando dias sem faturamento
menor = min(faturamento)
maior = max(faturamento)
media = sum(faturamento) / len(faturamento)
dias_acima_da_media = len([f for f in faturamento if f > media])

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias_acima_da_media}")
