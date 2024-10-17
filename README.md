# Meu Portfólio Pessoal

Este é um projeto de portfólio pessoal desenvolvido utilizando Flask, HTML, CSS e JavaScript.

## Estrutura do Projeto

```
app/
├── api/
│   ├── __init__.py
│   └── app.py
├── controllers/
├── models/
├── static/
│   ├── css/
│   ├── img/
│   └── javascript/
│       ├── email.js
│       └── tema.js
├── templates/
│   ├── __init__.py
│   ├── contact.html
│   ├── index.html
│   └── projects.html
├── views/
│   ├── __init__.py
│   └── data.py
├── .gitignore
├── config.py
├── README.md
├── run.py
└── tailwind.config.js (apenas para IntelliSense)
```

## Funcionalidades

- Utiliza Flask para gerenciamento de rotas e renderização de templates
- Implementa `render_template` para renderizar os arquivos HTML
- Usa um arquivo `data.json` para armazenar dados utilizados nos templates
- Implementa funções Jinja nos templates HTML para recuperar dados do backend
- Exibe imagens, skills, links e outras informações dinâmicas

## Tecnologias Utilizadas

- Python (Flask)
- HTML
- CSS (Com Tailwind CSS)
- JavaScript

## Como Executar

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o arquivo `run.py`: `python run.py`

## Funcionalidades Futuras

Algumas pastas ainda não têm funcionalidades implementadas, mas estão planejadas para atualizações futuras:

- views
- models
- controllers

## Contribuição

Sinta-se à vontade para contribuir com o projeto. Abra uma issue ou envie um pull request com suas sugestões.
