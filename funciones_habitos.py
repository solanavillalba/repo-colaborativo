def registrar_habitos():
    """
    Solicita al usuario que ingrese actividades o hábitos y los guarda en una lista.
    Permite seguir ingresando actividades hasta que el usuario decida terminar.

    Returns
    -------
    lista_habitos : list
    Lista que contiene las actividades ingresadas por el usuario.
    """

    lista_act=[]

    seguir="si"
    actividad=input("Ingrese actividad: ")
    lista_act.append(actividad)

    while seguir == "si":
        seguir = input("¿Queres agregar otra actividad? (si/no): ")
        
        if seguir == "si":
            actividad=input("Ingrese actividad: ")
            lista_act.append(actividad)
        else:
            break
    
    return lista_act


def analizar_habitos(lista_act):
    '''

    Esta función contara que cantidad de veces aparece cada actividad de la lista


    Parameters
    ----------

    lista_act: list
    Es la lista de actividades que las personas realizan

    Returns
    ----------
     dicc : dict
    Es un diccionario que cuenta cuantas veces aparece cada actividad. Las claves son las actividades y los valores
    son la cantidad de veces que aparece cada actividad.


    '''
    dicc = {}
    for actividad in lista_act:
        if actividad not in dicc.keys():
            dicc[actividad] = 1
        else:
            dicc[actividad] +=1
    
    return dicc 