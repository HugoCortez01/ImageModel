# Verificação de número primo

Este arquivo explica a implementação de `num.primo.py`, que lê um número do usuário e verifica se ele é primo.

## Objetivo

A função `is_prime(n: int) -> bool` retorna `True` quando `n` é primo e `False` caso contrário.

## Entrada do usuário

- O programa solicita que o usuário digite um número inteiro.
- Se a entrada não for um inteiro válido, o código solicita novamente.

## Lógica de verificação

1. Números menores ou iguais a 1 não são primos.
2. Fazemos uma busca por divisores de 2 até a raiz quadrada de `n`.
3. Se houver qualquer divisor exato, `n` não é primo.
4. Se nenhum divisor for encontrado, `n` é primo.

## Por que isso é limpo e eficiente

- O código separa claramente a verificação (`is_prime`) da leitura de entrada (`request_integer`) e da lógica principal (`main`).
- Não usa imports desnecessários.
- A verificação evita divisões desnecessárias usando `int(n**0.5) + 1`.

## Resultado esperado

Quando executado, o script pede um número e imprime se ele "é primo" ou "não é primo".
