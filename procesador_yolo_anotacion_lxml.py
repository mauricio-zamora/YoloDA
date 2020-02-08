from lxml import etree
import xml.etree.cElementTree as xml
from funcionales_generales import *
import annotation


def parseXML(file_name):
    # Parse XML with ElementTree
    tree = xml.ElementTree(file=file_name)
    print(tree.getroot())
    root = tree.getroot()
    print("tag=%s, attrib=%s" % (root.tag, root.attrib))

    # get the information via the children!
    print("-" * 40)
    print("Iterating using getchildren()")
    print("-" * 40)

    for salary in root.iter("object"):
        salary

    users = root.getchildren()
    for user in users:
        user_children = user.getchildren()

        for user_child in user_children:
            print("%s=%s" % (user_child.tag, user_child.text))


def leer_archivo(archivo):
    return etree.parse(archivo)


def leer_archivo2(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()
    return xml


def procesar_anotacion(xml_ref):
    root = etree.XML(xml_ref)
    context = etree.iterwalk(root, events=("start", "end"), tag="element")
    for action, elem in context:
        print(action, elem.tag)


def cargar_anotacion(xml_ref):
    annotation = annotation()


def imprimir_anotation(annotation):
    print('Archivo de Anotación - Inicio')
    print('Folder - {:^15}'.format(texto_es_none(annotation.folder)))
    print('Filename - {:^15}'.format(texto_es_none(annotation.filename)))
    print('Source ')
    for k, v in annotation.source.items():
        print('{:^15}-{:^60}'.format(k, numero_es_none(v)))
    print('Size ')
    for k, v in annotation.size.items():
        print('{:^15}-{:^15}'.format(k, v))
    print('segmented - {:^15}'.format(texto_es_none(annotation.segmented)))
    for o in annotation.objects:
        imprimir_object(o)
    print('Archivo de Anotación - Fin')


def imprimir_object(object):
    print('Sección de Objeto - Inicio')
    print('Name - {:^15}'.format(texto_es_none(object.name)))
    print('Pose - {:^15}'.format(texto_es_none(object.pose)))
    print('Truncated - {:^15}'.format(texto_es_none(object.pose)))
    print('Difficult - {:^15}'.format(texto_es_none(object.pose)))
    print('Bndbox ')
    for k, v in object.bndbox.items():
        print('{:^15}-{:^15}'.format(k, numero_es_none(v)))
    for p in object.parts:
        imprimir_part(p)
    print('Sección de Objeto - Fin')


def imprimir_part(part):
    print('Sección de Parte - Inicio')
    print('Name - {:^15}'.format(texto_es_none(part.name)))
    print('Bndbox ')
    for k, v in part.bndbox.items():
        print('{:^15}-{:^15}'.format(k, numero_es_none(v)))
    print('Sección de Parte - Fin')


def contruir_xml():
    html = etree.Element("html")
    #print(type(html))
    # etree.SubElement(html, "head").text = "Head of HTML"
    # etree.SubElement(html, "title").text = "I am the title!"
    # etree.SubElement(html, "body").text = "Here is the body of my example"
    return html


def imprimir_xml(documento):
    #html = etree.XML('<html><head>Head of HTML</head><title>I am the title!</title><body>Here is the body</body></html>')
    print(etree.tostring(documento, pretty_print=True).decode('utf-8'))