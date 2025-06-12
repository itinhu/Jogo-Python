# 🥷 Ninja Dash

**Ninja Dash** é um jogo de plataforma 2D criado com **Python** e **PgZero**, onde você controla um ninja em uma missão cheia de desafios, plataformas traiçoeiras e inimigos traiçoeiros. O projeto foi desenvolvido como parte de um teste para tutoria em Python e Roblox, seguindo restrições específicas de bibliotecas e estrutura.

---

## 🎮 Como Jogar

1. **Logo de entrada**: Ao iniciar o jogo, a logo aparece por 2 segundos.
2. **Menu principal**: Após isso, você verá o menu com três opções:
   - `Start Game`: Inicia o jogo (em construção).
   - `Sound On/Off`: Liga ou desliga a música de fundo.
   - `Exit`: Sai do jogo.

> Em breve: gameplay completa com inimigos, pulos ninjas e mecânicas de plataforma!

---

## 🛠️ Tecnologias e Regras do Projeto

- Linguagem: **Python 3**
- Biblioteca: **PgZero** (baseada em Pygame, mas com restrições)
- **Somente** os seguintes módulos foram usados:
  - `pgzero`
  - `math`
  - `random`
  - `pygame.Rect` (exceção permitida)
- ❌ Nenhuma outra biblioteca externa foi utilizada
- ✅ Todos os sprites e sons foram adicionados localmente

---

## 📂 Estrutura de Pastas

NinjaDash/
├── main.py
├── images/
│ ├── logo.png
│ └── bg_menu.png
├── sounds/
│ └── bg.wav
└── README.md


---

## ▶️ Como Executar

Certifique-se de ter o **PgZero** instalado:

```bash
pip install pgzero

python -m pgzero main.py
