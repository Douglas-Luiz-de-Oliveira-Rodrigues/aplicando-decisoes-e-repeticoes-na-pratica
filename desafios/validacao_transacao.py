
entrada = input()
valor_transacao, taxa_servico, pagamento_minimo = map(int, entrada.split())

valor_final = valor_transacao - taxa_servico

if valor_final >= pagamento_minimo:
    print("Aprovada")
else:
    print("Recusada")