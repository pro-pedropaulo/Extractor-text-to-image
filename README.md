## Projeto Extrator de Imagem 

Este projeto usa Python, Tesseract OCR e OpenCV para extrair texto de imagens. Ele lê a imagem, converte-a em escala de cinza, aplica um desfoque gaussiano e, em seguida, extrai o texto usando o Tesseract OCR.

## Requisitos

- Python 3

- Tesseract OCR

- OpenCV

## Instalação

1. Instale o Python 3 a partir do site oficial: https://www.python.org/downloads/

2. Instale o Tesseract OCR seguindo as instruções na documentação oficial: https://tesseract-ocr.github.io/tessdoc/Installation.html

3. Instale as bibliotecas Python necessárias usando o pip:

4 - execute pip install opencv-python pytesseract

5 - Baixe o arquivo por.traineddata a partir deste link: https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata

6 - Copie o arquivo por.traineddata para o diretório tessdata no diretório de instalação do Tesseract OCR.

## Uso

Para executar o projeto, siga os passos abaixo:

1 - Coloque a imagem que deseja extrair texto na pasta img.

2 - No arquivo app.py, atualize o caminho da imagem conforme necessário:

imagem = r"C:\Projeto Extrator de Imagem\img\image-to-wiki-wBush.png"

3 - Execute o arquivo app.py no terminal ou prompt de comando:  python app.py 


## O texto extraído da imagem será exibido no terminal ou na saída do seu IDE.

