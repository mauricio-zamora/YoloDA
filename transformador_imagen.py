from matplotlib import pyplot as plt
import numpy as np
import cv2


def leer_imagen(nombre):
    return cv2.imread(nombre)


def recortar_imagen(imagen, porcentaje):
    alto, ancho = imagen.shape[0:2]
    corteInicial = (porcentaje / 100)
    corteFinal = (1-corteInicial)
    filaInicial = int(alto*.15)
    colInicial = int(ancho*.15)
    filaFinal = int(alto*.85)
    colFinal = int(ancho*.85)
    imagenRecortada = imagen[filaInicial:filaFinal, colInicial:colFinal]
    return imagenRecortada


def rotar_imagen(imagen, grados):
    alto, ancho = imagen.shape[0:2]
    matrizRotacion = cv2.getRotationMatrix2D((ancho/2, alto/2), grados, 1)
    imagenRotada = cv2.warpAffine(imagen, matrizRotacion, (ancho, alto))
    return imagenRotada


def ajustar_contraste(imagen, nivel=2.5):
    return cv2.addWeighted(imagen, nivel, np.zeros(imagen.shape, img.dtype), 0, 0)


def convertir_en_gris(imagen, gris=cv2.COLOR_RGB2GRAY):
    return cv2.cvtColor(imagen, gris)


def reducir_ruido(imagen):
    return cv2.fastNlMeansDenoisingColored(imagen,None,20,10,7,21)


def aplicarTransformacionAfin(imagen, pts1 = np.float32([[50,50],[200,50],[50,200]]), pts2 = np.float32([[10,100],[200,50],[100,250]])):
    filas,cols,ch = imagen.shape
    M = cv2.getAffineTransform(pts1,pts2)
    imagenSalida = cv2.warpAffine(imagen,M,(cols,filas))


def aplicarTransformacionPerspectiva(imagen, pts1 = np.float32([[50,50],[450,50],[50,450],[450,450]]), pts2 = np.float32([[0,0],[500,0],[0,500],[500,500]])):
    filas,cols,ch = imagen.shape
    M = cv2.getPerspectiveTransform(pts1,pts2)
    imagenSalida = cv2.warpPerspective(img,M,(500,500))