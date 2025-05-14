
# Asteroids Game

Jogo inspirado no clássico *Asteroids*, desenvolvido em Python com Pygame e Orientação a Objetos.

## Tecnologias

- **Python 3.x**
- **Pygame**
- **Orientação a Objetos**

## Como Rodar

### 1. Clonar o repositório

```bash
git clone https://github.com/HigorChagas/asteroids.git
```

### 2. Criar e ativar ambiente virtual

```bash
cd asteroids
python -m venv venv
```

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar dependências

```bash
pip install pygame
```

### 4. Executar o jogo

```bash
python main.py
```

## Estrutura

- `main.py`: Arquivo principal.
- `game.py`: Lógica do jogo.
- `player.py`: Nave do jogador.
- `asteroid.py`: Asteroides.
- `bullet.py`: Balas.

## Controles

- **Setas direcionais**: Movimentar a nave.
- **Espaço**: Disparar.

## Licença

MIT License.