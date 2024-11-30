# MOCO GAME


MOCO GAME es un emocionante juego 2D desarrollado en **Pygame Zero**. El objetivo es esquivar obstáculos y sobrevivir el mayor tiempo posible mientras controlas un personaje animado en un mundo interactivo.

---

## Características
- **Pantalla de bienvenida**: Incluye un menú interactivo con botones de "Jugar" y "Tienda".
- **Controles simples**: Usa las flechas o teclas WASD para moverte.
- **Desafíos**: Esquiva obstáculos en movimiento y fijos.
- **Pantalla de Game Over**: Indica cuándo el jugador pierde.
- **Animaciones suaves**: El personaje puede saltar con efectos animados.
- **Estilo minimalista**: Un diseño sencillo y divertido.

---

## Requisitos del Sistema
- Python 3.8 o superior.
- Pygame Zero instalado.

---

## Instalación
1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/facu1401/moco-game.git

    Navega al directorio del proyecto:

cd moco-game

Asegúrate de tener Pygame Zero instalado. Si no lo tienes, instálalo con:

    pip install pg

Tú dijiste:
no me lo separes, todo dentro lde l codigo
ChatGPT Plus
ChatGPT

Aquí tienes el README.md todo unido dentro de un solo bloque de código en Markdown:

# MOCO GAME
MOCO GAME es un emocionante juego 2D desarrollado en **Pygame Zero**. El objetivo es esquivar obstáculos y sobrevivir el mayor tiempo posible mientras controlas un personaje animado en un mundo interactivo.
## Características
- **Pantalla de bienvenida**: Incluye un menú interactivo con botones de "Jugar" y "Tienda".
- **Controles simples**: Usa las flechas o teclas WASD para moverte.
- **Desafíos**: Esquiva obstáculos en movimiento y fijos.
- **Pantalla de Game Over**: Indica cuándo el jugador pierde.
- **Animaciones suaves**: El personaje puede saltar con efectos animados.
- **Estilo minimalista**: Un diseño sencillo y divertido.
## Requisitos del Sistema
- Python 3.8 o superior.
- Pygame Zero instalado.
## Instalación
1. Clona este repositorio en tu máquina local:
   ```
   git clone https://github.com/facu1401/moco-game.git
  ``
2. Navega al directorio del proyecto:
  ```
  cd moco-game
  ```

3. Asegúrate de tener Pygame Zero instalado. Si no lo tienes, instálalo con:
    ```
    pip install pgzero
    ```

Cómo Jugar

    Ejecuta el juego:

    pgzrun moco_game.py

    En la pantalla de bienvenida:
        Haz clic en Play para iniciar el juego.
        Haz clic en Store para acceder al modo tienda (futura implementación).
    Controles:
        Izquierda/Derecha: Usa las flechas ←/→ o las teclas A/D.
        Saltar: Pulsa la barra espaciadora, ↑ o W.
        Reiniciar: Pulsa Enter si pierdes.
    Objetivo: Evita los obstáculos en movimiento (espinas) y fijos para mantenerte con vida.

Estructura del Código

    Pantalla de bienvenida: Se gestiona con el estado welcome.
    Pantalla de juego: Incluye el fondo, el personaje y los obstáculos.
    Pantalla de Game Over: Se muestra cuando colisionas con un obstáculo.
    Colisiones: Se detectan usando colliderect.
    Animaciones: Los saltos y movimientos se realizan con animate y teclas.

Próximos Pasos

    Implementar el modo tienda para personalizar el personaje.
    Añadir más obstáculos y niveles.
    Crear un sistema de puntuación.

Créditos

Desarrollado por facu1401. 
¡Gracias por jugar MOCO GAME!
