# Explicação da refatoração de `refatoracao.py`

## Código original

O código original realizava o cálculo de estatísticas simples em uma lista de números:

- `c(l)` recebia uma lista `l` e retornava 4 valores: total, média, maior e menor.
- O total era calculado em um laço `for` manual.
- A média era calculada com `t / len(l)`.
- O maior e o menor valor eram encontrados em outro laço `for` manual.
- O resultado era impresso usando variáveis de saída posicionais `a, b, c2, d`.

## Refatoração aplicada

No arquivo `refatoracao.py`, o código foi reescrito para melhorar legibilidade, nomenclatura e separação de responsabilidades:

1. Funções bem nomeadas:
   - `calculate_statistics` para indicar claramente que retorna estatísticas.
   - `display_statistics` para separar a lógica de apresentação.
   - `main` para orquestrar o fluxo do programa.

2. Tipagem e estrutura de retorno:
   - Foi criado um `NamedTuple` chamado `Statistics` com campos `total`, `average`, `maximum` e `minimum`.
   - Isso torna o retorno da função mais explícito e evita o uso de valores retornados por posição sem contexto.

3. Uso de funções embutidas do Python:
   - `sum()` para somar valores.
   - `max()` e `min()` para obter o maior e o menor valor.

4. Verificação de entrada:
   - O código passa a aceitar qualquer sequência de números (`Sequence[float]`).
   - Há validação para evitar operação em lista vazia, lançando `ValueError` quando necessário.

5. Legibilidade melhorada:
   - Variáveis como `numbers`, `values` e `sample_numbers` são mais descritivas que `l`, `t`, `m`, `mx` e `mn`.
   - Mensagens de saída foram padronizadas para `Total`, `Média`, `Maior` e `Menor`.

## Benefícios da refatoração

- Maior clareza do que cada parte do código faz.
- Melhor manutenção futura, pois a função `calculate_statistics` pode ser usada em outros contextos.
- Menor risco de erro ao trabalhar com os valores retornados.
- Código mais idiomático e legível em Python.
