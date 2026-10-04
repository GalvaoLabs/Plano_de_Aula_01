# 💬 Entre Emoções e Escolhas

**Plano de aula interativo em Streamlit para uma palestra participativa sobre amor e relacionamentos**

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-52c77e)

---

## 📖 Sobre o projeto

Este projeto é um site que organiza, em um só lugar, o plano de uma palestra participativa para adolescentes (14 a 16 anos) chamada **"Entre Emoções e Escolhas"**.

A palestra é dividida em duas aulas de 55 minutos e usa como fio condutor três visões sobre o amor, de **Kafka**, **Dostoiévski** e **C.S. Lewis**, além dos **Quatro Amores** descritos por Lewis (Storge, Philia, Eros e Ágape). A ideia não é dar respostas prontas, e sim provocar reflexão e conversa com a turma.

O site serve como roteiro de consulta rápida para quem apresenta: o que falar em cada bloco, quem conduz cada parte, quanto tempo dura e como lidar com as perguntas da turma.

## ✨ Funcionalidades

- 🗂️ **Estrutura da aula:** 11 blocos divididos entre a 1ª e a 2ª aula, com tempo estimado e responsável por cada um
- 🎤 **Divisão de falas:** o que cada pessoa (palestrantes e professora) faz em cada momento
- 📜 **Citações:** as três citações da abertura, com sugestões de como usá-las e perguntas para a turma
- ❓ **Perguntas frequentes:** respostas preparadas para dúvidas que costumam surgir, ligadas ao bloco em que se encaixam
- 💡 **Dicas:** orientações práticas para deixar a palestra mais envolvente
- 🚫 **O que evitar:** cuidados para a palestra não perder credibilidade
- 🎨 Tema escuro, layout responsivo e cores que identificam quem conduz cada bloco

## 🗺️ Estrutura da palestra

| Aula | Blocos | Foco |
|------|--------|------|
| 1ª aula (55 min) | 01 a 06 | Abertura, três citações, o que é amor, paixão x amor, Quatro Amores e redes sociais |
| Intervalo | | |
| 2ª aula (55 min) | 07 a 11 | Amor-próprio, relacionamentos saudáveis x tóxicos, dinâmicas em grupo e encerramento |

## 🗂️ Estrutura do repositório

```
.
├── app.py              # Aplicação Streamlit (conteúdo e interface)
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

Todo o conteúdo da palestra fica em listas e dicionários no início do `app.py` (`AULA1`, `AULA2`, `DIVISAO`, `CITACOES`, `FAQ`, `DICAS` e `AVOID`). Para alterar um texto, basta editar a estrutura correspondente, sem mexer no código de interface.

## 🛠️ Tecnologias

| Tecnologia | Utilização |
|------------|------------|
| Python | Linguagem principal |
| Streamlit | Construção do site e das abas interativas |
| HTML e CSS | Estilização dos cartões, cabeçalho e tema escuro |

## 🚀 Como executar

### Pré-requisitos

- Python 3.9 ou superior
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/GalvaoLabs/NOME-DO-REPO.git
cd NOME-DO-REPO
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Se preferir, instale direto:

```bash
pip install streamlit
```

### 4. Execute

```bash
streamlit run app.py
```

O site abrirá no navegador, normalmente em `http://localhost:8501`.

## 🎯 Aprendizados

- Criação de aplicações web com Streamlit (abas, expanders e componentes)
- Personalização visual com CSS e HTML dentro do Streamlit
- Separação entre dados (conteúdo da palestra) e interface (funções de renderização)
- Organização de conteúdo educacional em formato de consulta rápida
- Planejamento de uma atividade participativa com foco em adolescentes

## 🙏 Créditos

**Desenvolvimento:** Miguel Henrique S. Galvão, [@GalvaoLabs](https://github.com/GalvaoLabs).

**Palestrantes:** Miguel e Maria Clara.

As citações de C.S. Lewis, Kafka e Dostoiévski aparecem em tradução livre e pertencem aos seus respectivos autores.

## ⚖️ Uso do material

Este repositório tem finalidade educacional e de portfólio, como registro do projeto e do plano de aula desenvolvidos para a palestra.

Se você é responsável por algum material aqui presente e tem dúvidas ou solicitações, entre em contato pelo GitHub.

---

<p align="center">Python • Streamlit • Educação • Inteligência emocional</p>
