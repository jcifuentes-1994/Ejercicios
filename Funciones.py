asientos = [[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [19,20,21,22,23,24],
            [25,26,27,28,29,30],
            [31,32,33,34,35,36],
            [37,38,39,40,41,42]]

asientos_ocupados = [[1,2,3,4,5,6],
                    [7,8,9,10,11,12],
                    [13,14,15,16,17,18],
                    [19,20,21,22,23,24],
                    [25,26,27,28,29,30],
                    [31,32,33,34,35,36],
                    [37,38,39,40,41,42]]

def buscar_asiento(eleccion_asiento,asientos): # busca el asiento en el arreglo
    for i in range (len(asientos)): #busca la posición del asiento en las filas
        for j in range (len(asientos[i])): # busca la posición del asiento en las columnas
            if asientos[i][j] == eleccion_asiento:
                f = i
                c = j
    return f,c
