# Aplicando decisões e repetições na prática

## Desafio de Código

**Desafio 1: Automatizando Benefícios no Varejo - Decisão de Promoções por Faixa de Compra**

Você foi contratado por uma consultoria especializada em soluções para o varejo.  
Sua missão é automatizar o sistema de promoções de uma grande rede de lojas.  
O sistema deve analisar o valor total da compra de um cliente e, de acordo com regras de negócio, decidir qual benefício será aplicado.

### Regras de Negócio
- Se o valor for menor que 50 → "Obrigado por comprar conosco!"
- Se o valor for de 50 a 99 → "Parabens! Voce ganhou um brinde!"
- Se o valor for de 100 a 199 → "Desconto de 10 reais aplicado!"
- Se o valor for 200 ou mais → "Desconto de 25 reais aplicado!"

### Entrada
Um único número inteiro representando o valor total da compra em reais (≥ 0).

### Saída
Uma única linha contendo a mensagem correspondente ao benefício aplicado.

### Exemplos
| Entrada | Saída                            |
|---------|----------------------------------|
| 30      | Obrigado por comprar conosco!    |
| 75      | Parabens! Voce ganhou um brinde! |
| 150     | Desconto de 10 reais aplicado!   |
| 250     | Desconto de 25 reais aplicado!   |

---

## Tecnologias Utilizadas
- **Python**: implementação da lógica condicional
- **Estruturas de decisão (if/elif/else)**: para aplicar as regras de negócio
- **Entrada e saída padrão**: leitura de valores e exibição de mensagens

---

## Código do Desafio
O código está disponível neste repositório:  
[Link para o desafio]()

---

**Desafio 2: Validação de Transação Bancária**

Você foi contratado por uma consultoria para auxiliar uma empresa do setor financeiro a automatizar a validação de transações bancárias.  
O sistema precisa calcular o valor final da transação (valor menos taxa) e verificar se o valor final é suficiente para cobrir um pagamento mínimo exigido pela empresa.

### Regras de Negócio
- Calcular o valor final: `valor - taxa`
- Se o valor final ≥ pagamento mínimo → imprimir **"Aprovada"**
- Caso contrário → imprimir **"Recusada"**

### Entrada
Três números inteiros separados por espaço:
1. Valor da transação  
2. Taxa de serviço  
3. Pagamento mínimo  

### Saída
Uma única palavra:
- **"Aprovada"** se o valor final for suficiente  
- **"Recusada"** caso contrário  

### Exemplos
| Entrada       | Saída     |
|---------------|-----------|
| 100 10 80     | Aprovada  |
| 50 20 40      | Recusada  |
| 200 50 150    | Aprovada  |
| 75 30 50      | Recusada  |

---

## Tecnologias Utilizadas
- **Python**: implementação da lógica
- **Operadores aritméticos**: subtração para cálculo do valor final
- **Operadores relacionais**: comparação para validar a transação
- **Estruturas condicionais (if/else)**: decisão de aprovação ou recusa

---

## Código do Desafio
O código está disponível neste repositório:  
[Link para o desafio]()