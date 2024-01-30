import cv2

# Carrega a imagem
img = cv2.imread('placa2.jpg')

# Define o ângulo de rotação
angulo = -13

# Calcula a matriz de rotação
altura, largura = img.shape[:2]
centro = (largura // 2, altura // 2)
matriz = cv2.getRotationMatrix2D(centro, angulo, 1)

# Aplica a rotação na imagem
img_rotacionada = cv2.warpAffine(img, matriz, (largura, altura))

# Exibe a imagem rotacionada
cv2.imshow('Imagem rotacionada', img_rotacionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
