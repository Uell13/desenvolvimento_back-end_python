## Código de apoio
Caso precise, ao longo dos exercícios use o módulo `random` para gerar números aleatórios. Exemplo de código:

```
import random
 
numero = random.randint(1, 10)
print(numero)
```

## Posíveis erros em projetos
| ERRO                  | MENSAGEM            | MOTIVO                                                                                                          | SOLUÇÃO                                                        |
|-----------------------|:-------------------:|:---------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------:|
| Entrada inválida      | ValueError          | Ocorre quando tentamos converter um valor que não pode ser transformado no tipo esperado. Ex: `float("abc")`.   | Tratar erro com bloco `try/except`                             |
| Tipo inválido         | TypeError           | Ocorre quando realizamos operacões incompatíveis entre tipos de dados. Ex: `10 + "5"`.                          | Converter valores antes de operações. Ex: `int("5")`.          |
| Índice fora da lista  | IndexError          | Ocorre ao tentar acessar uma chave que não existe em um dicionário.                                             | Usar `.get("chave", valor_padrao)` para evitar erro.           |
| Chave inexistente     | KeyError            | Ocorre ao tentar acessar um índice que não existe em uma lista. Ex: acessar `lista[5]` em uma lista de 3 itens. | Conferir `len(lista)` antes de acessar um índice.              |
| Erro de importação    | ImportError         | Ocorre quando um módulo é encontrado, mas não pode ser carregado corretamente.                                  | Verificar se o módulo está instalado e disponível.             |
| Módulo não encontrado | ModuleNotFoundError | Ocorre quando tentamos importar um módulo que não está instalado ou não existe.                                 | Garantir que o módulo está instalado com `pip install modulo`. |
| Atributo inexistente  | AttributeError      | Ocorre quando tentamos acessar um atributo ou método que não existe em um objeto. Ex: `"abc".append(5)`.        | Converter valores antes de operações. Ex: `int("5")`.          |
| Sintaxe inválida      | SyntaxError         | Ocorre quando há um erro na escrita do código, como esquecer um `:` ou parênteses.                              | Revisar a sintaxe e corrigir erros antes de rodar o código.    |


