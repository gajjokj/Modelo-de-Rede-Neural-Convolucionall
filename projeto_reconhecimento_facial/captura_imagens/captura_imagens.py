import cv2

classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
WebCamera = cv2.VideoCapture(0)

amostra = 1
numeroAmostras = 25
id = input('Digite seu identificador: ')

while True:
    conectado, imagem = WebCamera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

    for (x, y, w, a) in facesDetectadas: 
        cv2.rectangle(imagem, (x, y), (x + w, y + a), (0, 0, 255), 2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + w], (220, 220))
            cv2.imwrite('fotos/pessoa.' + str(id) + '.' + str(amostra) + '.jpg', imagemFace)
            print('[foto ' + str(amostra) + ' capturada com sucesso]')
            amostra += 1

    cv2.imshow('Face', imagem)
    cv2.waitKey(1)
    if amostra >= numeroAmostras + 1:
        break

print('Faces capturadas com sucesso')
WebCamera.release()
cv2.destroyAllWindows()
