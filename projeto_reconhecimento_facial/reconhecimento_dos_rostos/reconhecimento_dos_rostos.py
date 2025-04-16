import cv2


classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read('classificadorLBPH.yml')

camera = cv2.VideoCapture(0)

while True:
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))

    for (x, y, w, a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + w], (220, 220))
        cv2.rectangle(imagem, (x, y), (x + w, y + a), (0, 0, 255), 2)
        id, confianca = reconhecedor.predict(imagemFace)

        if id == 1:
            nome = 'Joao'
        elif id == 2:
            nome = 'Murilo'
        elif id == 3:
            nome = 'Nicolas'
        elif id == 4:
            nome = 'Giuseppe'
        else:
            nome = 'Desconhecido'

        cv2.putText(imagem, nome, (x, y + a + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))

    cv2.imshow('Face', imagem)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
