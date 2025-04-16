import cv2
import os
from imutils import paths
import shutil

pasta = 'Mae'
id = 4

def listNegImagem():
    imagemPaths = list(paths.list_images(pasta))
    numero = 1

    if not os.path.exists('Fotos'):
        os.makedirs('Fotos')

    for i in imagemPaths:
        rename = f'Fotos/pessoa.{id}.{numero}.jpg'
        shutil.copy(i, rename)

        img = cv2.imread(rename, cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img, (220, 220))
        cv2.imwrite(rename, resized_image)

        print(rename)
        numero += 1

listNegImagem()
