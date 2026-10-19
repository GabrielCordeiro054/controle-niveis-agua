# 💧 Controle de Níveis de Água

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte de uma atividade do curso Técnico em Desenvolvimento de Sistemas da ETEC.

O objetivo é simular um sistema simples de monitoramento de um reservatório de água, utilizando a linguagem Python e a biblioteca Colorama para exibir mensagens coloridas no terminal de acordo com o nível de água.

## 🚀 Funcionalidades

- Monitoramento simulado de cinco níveis de água.
- Exibição de mensagens de acordo com a situação do reservatório.
- Utilização de cores diferentes para cada nível.
- Validação dos níveis informados.
- Restauração automática do estilo padrão do terminal após cada mensagem.

## 🎨 Níveis do reservatório

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | 🔴 Vermelho |
| 2 | Baixo | 🟡 Amarelo |
| 3 | Médio | 🟢 Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | 🔵 Azul |

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Colorama:** biblioteca responsável pelas cores das mensagens.
- **Visual Studio Code:** editor utilizado para desenvolver o projeto.

## 💻 Como executar

**1.** Instale o Python no computador.

**2.** Abra a pasta do projeto no VS Code.

**3.** Instale a biblioteca Colorama pelo terminal:

```bash
pip install colorama
```

**4.** Execute o programa:

```bash
python controle_reservatorio.py
```

O programa exibirá os cinco níveis do reservatório com suas respectivas mensagens e cores.

## 📂 Estrutura do projeto

```text
controle-niveis-agua/
├── controle_reservatorio.py
├── README.md
└── requirements.txt
```

O arquivo `requirements.txt` contém a dependência `colorama`.

## 📚 Conceitos aplicados

Durante o desenvolvimento, foram utilizados os seguintes conceitos de programação:

- Listas para armazenar os níveis e as cores.
- Funções para organizar o código.
- Estruturas condicionais para validar os níveis.
- Estrutura de repetição `for` para simular o monitoramento.
- Importação e utilização de bibliotecas externas.


## 📝 Considerações finais

O projeto demonstra como listas, funções e bibliotecas podem ser utilizadas em conjunto para desenvolver uma aplicação simples de monitoramento.

A utilização de cores facilita a identificação das diferentes situações do reservatório, tornando a visualização das informações mais clara e organizada.
