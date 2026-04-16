
entrada = input()

palavras = entrada.strip().split()

palavras_formatadas = [palavra.capitalize() for palavra in palavras]

nome_formatado = ' '.join(palavras_formatadas)

print(nome_formatado)