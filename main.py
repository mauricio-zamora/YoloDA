

def main():
    print('Iniciando procesamiento')
    condicion = True
    while condicion:
        print('+{:_^10}+{:_^60}+'.format('_', '_'))
        print('|{:^10}|{:^60}|'.format('Opción', 'Acción a ejecutar'))
        print('+{:_^10}+{:_^60}+'.format('_', '_'))
        print('|{:^10}|{:^60}|'.format(1,'Establecer diretorio de trabajo'))
        print('|{:^10}|{:^60}|'.format(2, 'Rectificar archivo de anotaciones Yolo'))
        print('|{:^10}|{:^60}|'.format('s', 'Salir'))
        print('+{:_^10}+{:_^60}+'.format('_', '_'))
        entrada = input('Digite la opción S para salir\n')
        condicion = entrada.upper() != 's'.upper()
    print('Fin del procesamiento')
main()