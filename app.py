import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # Altere este caminho conforme necessário

def extrair_texto_da_imagem(imagem):
    img = cv2.imread(imagem)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    texto = pytesseract.image_to_string(img_gray_blur, lang='por')

    return texto


imagem = r"C:\Projeto Extrator de Imagem\img\image-to-wiki-wBush.png"
texto = extrair_texto_da_imagem(imagem)
os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"
print("Texto extraído da imagem:")
print(texto)
