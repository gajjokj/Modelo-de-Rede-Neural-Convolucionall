# Projeto de Reconhecimento Facial

Este projeto tem como objetivo realizar o reconhecimento facial utilizando a biblioteca OpenCV. Ele captura imagens de uma pessoa e as salva em uma pasta para treinamento de um modelo de reconhecimento facial.

## Funcionalidades

1. **Captura de Imagens**: O sistema captura imagens de um rosto e as salva em uma pasta chamada `fotos/`.
2. **Treinamento de Modelo**: Utiliza as imagens capturadas para treinar um modelo de reconhecimento facial.
3. **Reconhecimento Facial em Tempo Real**: A partir do modelo treinado, o sistema consegue reconhecer rostos em tempo real a partir da webcam.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.x
- Bibliotecas:
  - OpenCV
  - imutils
  - NumPy

Você pode instalar as dependências com o comando:

```bash
pip install opencv-python opencv-python-headless imutils numpy
