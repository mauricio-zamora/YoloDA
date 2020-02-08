# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://stackoverflow.com/questions/28813876/how-do-i-get-pythons-elementtree-to-pretty-print-to-an-xml-file
import xml.etree.ElementTree as ET
from annotation import *
from procesador_yolo_anotacion_lxml import *
from xml.dom import minidom
import glob


def convertir_anotaciones_directorio(origen, destino):
    nombres_anotaciones = [f for f in glob.glob(origen + '/*.xml')]
    for nombre_anotacion in nombres_anotaciones:
        nombre_archivo = nombre_anotacion.split('/')[-1]
        ruta_archivo = nombre_anotacion[:nombre_anotacion.find(nombre_archivo)]
        tree = ET.parse(nombre_anotacion)
        root = tree.getroot()
        # for child in root:
        #     print( child.tag, child.attrib, child.text )
        # for object in root.iter('object'):
        #     print( object.tag, object.text )
        #     for subobj in object:
        #         print( subobj.tag, subobj.text )
        a = procesar_anotacion(tree)
        # imprimir_anotation(a)
        b = reprocesar_anotacion(a)
        # print('#######################################################################')
        # imprimir_anotation(b)
        r = regenerarxml(b)
        escribir_xml(r, destino + nombre_archivo)


def escribir_xml(anotacionx, nombre_archivo):
    # tree = ET.ElementTree(element=anotacionx)
    # tree.write(nombre_archivo,method="xml")
    xmlstr = minidom.parseString(ET.tostring(anotacionx)).toprettyxml()
    #indent='   '
    xabc = xmlstr[xmlstr.find('?>')+2:]
    with open(nombre_archivo, 'w') as f:
        f.write(xabc)


def regenerarxml(anotacion):
    # root = xml.Element('annotation')
    x_annotation = xml.Element('annotation')
    x_folder = xml.SubElement(x_annotation, 'folder')
    x_folder.text = anotacion.folder
    x_filename = xml.SubElement(x_annotation,'filename')
    x_filename.text = anotacion.filename
    x_source = xml.SubElement(x_annotation,'source')
    x_database = xml.SubElement(x_source,'database')
    x_database.text = anotacion.source['database']
    x_annotation2 = xml.SubElement(x_source,'annotation')
    x_annotation2.text = anotacion.source['annotation']
    x_image = xml.SubElement(x_source,'image')
    x_image.text = anotacion.source['image']
    x_size = xml.SubElement(x_annotation, 'size')
    x_width = xml.SubElement(x_size, 'width')
    x_width.text = anotacion.size['width']
    x_height = xml.SubElement(x_size, 'height')
    x_height.text = anotacion.size['height']
    x_depth = xml.SubElement(x_size, 'depth')
    x_depth.text = anotacion.size['depth']
    x_segmented = xml.SubElement(x_annotation,'segmented')
    x_segmented.text = anotacion.segmented
    x_object = []
    for i in range(len(anotacion.objects)):
        x_object.append( xml.SubElement(x_annotation, 'object') )
        x_obj_name = xml.SubElement(x_object[i], 'name')
        x_obj_name.text = anotacion.objects[i].name
        x_obj_pose = xml.SubElement(x_object[i], 'pose')
        x_obj_pose.text = anotacion.objects[i].pose
        x_obj_truncated = xml.SubElement(x_object[i], 'truncated')
        x_obj_truncated.text = anotacion.objects[i].truncated
        x_obj_difficult = xml.SubElement(x_object[i], 'difficult')
        x_obj_difficult.text = anotacion.objects[i].difficult
        x_obj_bndbox = xml.SubElement(x_object[i], 'bndbox')
        x_obj_bndbox_xmax = xml.SubElement(x_obj_bndbox, 'xmax')
        x_obj_bndbox_xmax.text = anotacion.objects[i].bndbox['xmax']
        x_obj_bndbox_xmin = xml.SubElement(x_obj_bndbox, 'xmin')
        x_obj_bndbox_xmin.text = anotacion.objects[i].bndbox['xmin']
        x_obj_bndbox_ymax = xml.SubElement(x_obj_bndbox, 'ymax')
        x_obj_bndbox_ymax.text = anotacion.objects[i].bndbox['ymax']
        x_obj_bndbox_ymin = xml.SubElement(x_obj_bndbox, 'ymin')
        x_obj_bndbox_ymin.text = anotacion.objects[i].bndbox['ymin']
    return x_annotation


def reprocesar_anotacion(vieja_anotacion):
    nueva_anotacion = Annotation()
    nueva_anotacion.folder = vieja_anotacion.folder
    nueva_anotacion.filename = vieja_anotacion.filename
    for k, v in nueva_anotacion.source.items():
        nueva_anotacion.source[k] = vieja_anotacion.source[k]
    for k, v in nueva_anotacion.size.items():
        nueva_anotacion.size[k] = vieja_anotacion.size[k]
    nueva_anotacion.segmented = vieja_anotacion.segmented
    for o in vieja_anotacion.objects:
        o_nombre = o.name
        o_pose = o.pose
        o_truncated = o.truncated
        o_difficult = o.difficult
        for p in o.parts:
            obj = Object()
            obj.name = o_nombre
            obj.pose = o_pose
            obj.truncated = o_truncated
            obj.difficult = o_difficult
            for k,v in obj.bndbox.items():
                obj.bndbox[k] = p.bndbox[k]
            nueva_anotacion.objects.append(obj)
    return nueva_anotacion


def procesar_parte_bndbox(parte, raiz):
    for source in raiz:
        if source.tag == 'xmax':
            parte.bndbox['xmax'] = source.text
        elif source.tag == 'xmin':
            parte.bndbox['xmin'] = source.text
        elif source.tag == 'ymax':
            parte.bndbox['ymax'] = source.text
        elif source.tag == 'ymin':
            parte.bndbox['ymin'] = source.text


def procesar_parte(objecto, raiz):
    parte = Part()
    for elemento in raiz:
        if elemento.tag == 'name':
            parte.name = elemento.text
        elif elemento.tag == 'bndbox':
            procesar_parte_bndbox(parte,elemento)
    objecto.parts.append(parte)


def procesar_obj_bndbox(objecto, raiz):
    for source in raiz:
        if source.tag == 'xmax':
            objecto.bndbox['xmax'] = source.text
        elif source.tag == 'xmin':
            objecto.bndbox['xmin'] = source.text
        elif source.tag == 'ymax':
            objecto.bndbox['ymax'] = source.text
        elif source.tag == 'ymin':
            objecto.bndbox['ymin'] = source.text


def procesar_objecto(annotation, raiz):
    objecto = Object()
    for elemento in raiz:
        if elemento.tag == 'name':
            objecto.name = elemento.text
        elif elemento.tag == 'pose':
            objecto.pose = elemento.text
        elif elemento.tag == 'truncated':
            objecto.truncated = elemento.text
        elif elemento.tag == 'difficult':
            objecto.difficult = elemento.text
        elif elemento.tag == 'part':
            procesar_parte(objecto, elemento)
        elif elemento.tag == 'bndbox':
            procesar_obj_bndbox(objecto,elemento)
    annotation.objects.append(objecto)


def procesar_source(annotation, raiz):
    for source in raiz:
        if source.tag == 'database':
            annotation.source['database'] = source.text
        elif source.tag == 'annotation':
            annotation.source['annotation'] = source.text
        elif source.tag == 'image':
            annotation.source['image'] = source.text


def procesar_size(annotation, raiz):
    for size in raiz:
        if size.tag == 'width':
            annotation.size['width'] = size.text
        elif size.tag == 'height':
            annotation.size['height'] = size.text
        elif size.tag == 'depth':
            annotation.size['depth'] = size.text


def cargar_anotacion_desde_archivo(archivo):
    tree = ET.parse(archivo)
    anotacion = procesar_anotacion(tree)
    return  anotacion


def procesar_anotacion(arbol):
    salida = Annotation()
    root = arbol.getroot()
    for child in root:
        if child.tag == 'folder':
            salida.folder = child.text
        elif child.tag == 'filename':
            salida.filename = child.text
        elif child.tag == 'segmented':
            salida.segmented = child.text
        elif child.tag == 'source':
            procesar_source(salida, child)
        elif child.tag == 'size':
            procesar_size(salida, child)
        elif child.tag == 'object':
            procesar_objecto(salida, child)
    return salida


def main():
    # tree = ET.parse('/home/mauricio/Alicante/ImageManipulator/wrench_combination-00007b.xml')
    # root = tree.getroot()
    # # for child in root:
    # #     print( child.tag, child.attrib, child.text )
    # # for object in root.iter('object'):
    # #     print( object.tag, object.text )
    # #     for subobj in object:
    # #         print( subobj.tag, subobj.text )
    # a = procesar_anotacion(tree)
    # #imprimir_anotation(a)
    # b = reprocesar_anotacion(a)
    # #print('#######################################################################')
    # #imprimir_anotation(b)
    # r = regenerarxml(b)
    # escribir_xml(r,'r_limpio.xml')

    convertir_anotaciones_directorio('/home/mauricio/Alicante/ImageManipulator/','/home/mauricio/Alicante/ImageManipulator/salida/')

main()