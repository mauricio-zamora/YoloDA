from procesador_yolo_anotacion_lxml import *
from annotation import *

def main():
    print('Iniciando procesamiento')
    # xml = leer_archivo2('/home/mauricio/Alicante/ImageManipulator/wrench_combination-00007.xml')
    # imprimir_xml(xml)
    # procesar_anotacion(xml)
    parseXML('/home/mauricio/Alicante/ImageManipulator/wrench_combination-00007.xml')
    # a = Annotation()
    # imprimir_anotation(a)
    print('Fin del procesamiento')
main()