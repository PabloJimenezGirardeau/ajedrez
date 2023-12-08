def partida_ajedrez (mi_fichero):
    '''crear un string que represente al tablero inicial de ajedrez, con sus tabulaciones y saltos de linea
    respresentando las filas y columnas respetcivamente '''
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    print (tablero_inicial)
    #Crear una lista vacía para añadir los movimientos
    movimientos = []
 # Para que el jugador pueda elegir el nombre del fichero con los tableros de su partida
    mi_fichero = input("Ingrese el nombre del archivo para guardar el tablero inicial:  ")
# Bucle que recorre las filas del tablero inicial
    for i in tablero_inicial.split('\n'):
        movimientos.append(i.split('\t'))

# Se abre el fichero con 'w' para que se pueda escibir
    f = open(mi_fichero , 'w')      

 # Este bucle recorre todas las filas del tablero ('i' va tomando el valor de cada fila)
    for i in movimientos:
        f.write('\t'.join(i) + '\n')
    f.close ()
#definir el tablero inicial
    movimientos = 1

#preguntar al usuario si quiere mover ficha o salir
    while True:
        preguntar_jugador = input('Desea mover ficha (m) o salir de la partida(s):  ')
        if preguntar_jugador != 's':
            break

        else:
            # Para hacer un movimiento hay que indicar las coordenadas de origen y destino de la ficha que se prentende mover
            fila_origen = int(input('Introduce la fila de la pieza a mover: '))
            columna_origen = int(input('Introduce la columna de la pieza a mover: '))
            fila_destino = int(input('Introduce la fila de destino: '))
            columna_destino = int(input('Introduce la columna de destino: '))


            # Se hace el movimiento indicado por el jugador
            tablero_inicial[fila_destino-1][columna_destino-1] = tablero_inicial[fila_origen-1][columna_origen-1]
            # Cambiamos las posición inicial de la ficha por un espacio en blanco
            tablero_inicial[fila_origen-1][columna_origen-1] = ''
            
            movimientos += 1
            
            # Abrimos el fichero en modo añadir ('a').
            f = open(mi_fichero, 'a')

            # Añadimos el número de movimiento.
            f.write('Movimiento' + str(movimientos) + '\n')


            # Este bucle recorre todas las filas del tablero ('i' va tomando el valor de cada fila)
            for i in tablero_inicial:
                 # Va uniendo las fichas de cada fila, separadas por tabuladores
                f.write('\t'.join(i) + '\n')


            # Cerramos el fichero.
            f.close()


        # Preguntamos al usuario si quiere ver el tablero en algún movimiento específico.
        ver_jugada_tablero = input('¿Quieres ver el tablero en algún movimiento específico? (s/n): ')
        if ver_jugada_tablero == 's':
            # Solicitamos al jugador el número de movimiento que desea ver.
            num_movimiento = int(input('Introduce el número de movimiento que quieres ver: '))

            # Abrimos el fichero en modo lectura.
            with open(mi_fichero, 'r') as f:
                lineas = f.readlines()

                # Buscamos la línea del fichero que contiene el tablero del movimiento solicitado.
                inicio_tablero = lineas.index(f'Movimiento{num_movimiento}\n') + 1
                fin_tablero = inicio_tablero + 8  # Suponemos que el tablero ocupa 8 líneas.

                # Extraemos las líneas correspondientes al tablero.
                tablero_movimiento = [line.strip().split('\t') for line in lineas[inicio_tablero:fin_tablero]]

                # Mostramos el tablero por pantalla.
                mostrar_tablero(tablero_movimiento)

            
    return


def mostrar_tablero(tablero):
    # Bucle iterativo para recorrer las filas del tablero.
    for i in tablero:
        # Mostramos por pantalla cada fila concatenando los caracteres que contiene.
        print('\t'.join(i) + '\n')




partida_ajedrez ('movimientos_partida.txt')
