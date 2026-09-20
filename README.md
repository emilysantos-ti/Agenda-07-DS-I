# 💧 Sistema de Classificação de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Projeto Acadêmico](https://img.shields.io/badge/Projeto-Acadêmico-blue?style=for-the-badge)

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte da **Agenda 07 da disciplina de Desenvolvimento de Sistemas**.

O objetivo é criar um programa em **Python** capaz de analisar o consumo mensal de água de diferentes tipos de imóveis e apresentar uma classificação acompanhada de uma orientação ao usuário.

O sistema recebe duas informações:

- 🏠 Tipo de imóvel;
- 💧 Consumo mensal de água em metros cúbicos (`m³`).

A partir desses dados, o programa aplica regras de classificação e apresenta o resultado ao usuário.

---

## ⚙️ Funcionalidades

O sistema permite:

- Identificar imóveis do tipo **comercial**, **casa** ou **apartamento**;
- Registrar o consumo mensal de água;
- Aceitar números com ponto ou vírgula;
- Impedir valores negativos de consumo;
- Validar o tipo de imóvel informado;
- Classificar automaticamente o consumo;
- Apresentar uma mensagem educativa de acordo com o resultado.

---

## 📊 Regras de classificação

| Tipo de imóvel | Consumo | Resultado |
|---|---:|---|
| 🏢 Comercial | Qualquer valor válido | Tarifa comercial aplicada |
| 🏠 Apartamento | Menor que 10 m³ | Consumo econômico |
| 🏡 Casa ou apartamento | Até 25 m³ | Consumo moderado |
| ⚠️ Residencial | Acima de 25 m³ | Consumo excessivo |

### Mensagens apresentadas

**Comercial**

> Tarifa COMERCIAL aplicada — consulte o plano corporativo.

**Apartamento com consumo menor que 10 m³**

> Consumo econômico — excelente controle de água!

**Casa ou apartamento com consumo de até 25 m³**

> Consumo moderado — dentro do padrão residencial.

**Consumo residencial acima de 25 m³**

> Consumo excessivo — adote medidas de economia e verifique vazamentos.

---

## 🛠️ Tecnologias utilizadas

- 🐍 **Python 3**
- 🐙 **GitHub**
- 📝 **Markdown**
- 💻 Programação estruturada
- 🔀 Estruturas condicionais
- 🔁 Estruturas de repetição
- ✅ Tratamento e validação de dados

---

## 📁 Estrutura do projeto

```text
Agenda-07-DS-I/
│
├── consumo-agua/
│   └── app.py
│
├── .gitignore
└── README.md
