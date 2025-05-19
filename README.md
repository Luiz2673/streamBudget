# Stream Budget

Automatize a criação de orçamentos em poucos segundos, direto no navegador.  
[**▶ Acesse a demo**](https://streambudget.streamlit.app)

---

## Índice
1. [Visão geral](#visão-geral)  
2. [Funcionalidades](#funcionalidades)  
3. [Capturas de tela](#capturas-de-tela)  
4. [Instalação local](#instalação-local)  
5. [Como usar](#como-usar)  
6. [Estrutura do projeto](#estrutura-do-projeto)  
7. [Roadmap](#roadmap)  
8. [Contribuição](#contribuição)  
9. [Licença](#licença)

---

## Visão geral
**Stream Budget** é um app desenvolvido em **Python + Streamlit** que gera orçamentos profissionais a partir de um formulário simples. Os dados do cliente e dos serviços selecionados são renderizados em um template de imagem (.png) pronto para download.

---

## Funcionalidades
- **Formulário dinâmico** (nome, e‑mail, celular, até 3 serviços).  
- **Preços automáticos** carregados de `services.py` (dicionário).  
- **Numeração de O.S. incremental** salva em arquivo local.  
- **Data e totais calculados em tempo real**.  
- **Geração de imagem** com **Pillow** e fonte customizada (`HankenGrotesk-Light.ttf`).  
- **Download 1‑click** do orçamento final.  
- Deploy contínuo no **Streamlit Cloud**.


---

## Instalação local
```bash
# Clone o repositório
git clone https://github.com/Luiz2673/streamBudget.git
cd streamBudget

# Crie ambiente virtual (opcional)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt

# Rode o app
streamlit run app.py
