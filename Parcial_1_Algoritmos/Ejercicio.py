from lista import Lista

class Dinosaurio:

    def __init__(self, name, type, number, period, named_by):
        self.name = name
        self.type = type
        self.number = number
        self.period = period
        self.named_by = named_by

    def __str__(self):
        #return f"{self.nombre} , {self.especie} , {self.maestro} , {self.sable_luz}"
        return f"name:, {self.name}, type:,{ self.type}, number:, {self.number}, period, {self.period}, named_by, {self.named_by}"

#(time, zone_code, dino_number, alert_level)
class Alert:

    def __init__(self, time, zone_code, dino_number, alert_level):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
        self.dino_name = None

    def __str__(self):
        return f"{self.time} , {self.zone_code} , {self.dino_number} , {self.alert_level} , {self.dino_name}"



from jurassic_park import dinosaurs
lista_dinosaurios_por_name = Lista()
for dinosaurio in dinosaurs:
    lista_dinosaurios_por_name.insertar(Dinosaurio(dinosaurio['name'],
                                           (dinosaurio['type'])[0:-1],
                                           dinosaurio['number'],
                                           dinosaurio['period'],
                                           dinosaurio['named_by']), 'number')



#file = open('C:/Users/Angel/Documents/Codigos/Codigos en Python/Algoritmos y Estructuras de Datos(Segundo año)/Parcial_1_Algoritmos/alerts.txt')
file = open('alerts.txt')
lineas = file.readlines()

lista = []

lista_alerts_por_fecha = Lista()
lista_alerts_por_nombre = Lista()

#lista_dinosaurios_por_name.barrido()

lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')
    #datos.pop(-1)
    # print(datos[4].split('/'))
    #print('datos[3]: ',datos[3])
    alerta_a_incertar = Alert(datos[0],
                             datos[1],
                             datos[2],
                             datos[3][0:-1])
    nombre_dinosaurio = lista_dinosaurios_por_name.busqueda(int(alerta_a_incertar.dino_number), 'number')
    nombre_dinosaurio = nombre_dinosaurio.info.name
    alerta_a_incertar.dino_name = nombre_dinosaurio
    
    lista_alerts_por_fecha.insertar(alerta_a_incertar, campo='time')
    lista_alerts_por_nombre.insertar(alerta_a_incertar, campo='dino_name')

#lista_alerts_por_fecha.barrido()


'''
Y no olvide determinar cual de nuestro dinosaurios fuel el
ultimo en ser descubierto y quien lo hizo. [actividad para resolver]
'''

def ultimo_dinosaurio_descubierto(lista):
        pos_dinosaurio = 0
        dinosaurio = lista.obtener_elemento(0)
        fecha_ultimo_dinosaurio = 0
        ultimo_dinosaurio = None
        while(dinosaurio is not None):
            #fecha_ultimo_dinosaurio = int(ultimo_dinosaurio.split(',')[1])
            fecha_dinosaurio = int(dinosaurio.named_by.split(',')[1])
            #print(fecha_dinosaurio)
            
            if(fecha_dinosaurio > fecha_ultimo_dinosaurio):
                #print(dinosaurio)
                ultimo_dinosaurio = dinosaurio
                fecha_ultimo_dinosaurio = fecha_dinosaurio
            
            pos_dinosaurio += 1
            dinosaurio = lista.obtener_elemento(pos_dinosaurio)
        return ultimo_dinosaurio
print()      
print('El ultimo dinosaurio descubierto fue: ',ultimo_dinosaurio_descubierto(lista_dinosaurios_por_name))


def eliminar_alertas_de_x_zona(lista, zonas):
        pos_alert = 0
        for i in range(0,len(zonas)):
            alert = lista.obtener_elemento(0)
            #print('i: ', i)
            #print('zona a eliminar:', zonas[i])
            while(alert is not None):
                eliminado = lista.eliminar(zonas[i],'zone_code')
                #if eliminado:
                    #print(eliminado)
                pos_alert += 1
                alert = lista.obtener_elemento(pos_alert)
            pos_alert = 0

eliminar_alertas_de_x_zona(lista_alerts_por_nombre,('WYG075', 'SXH966', 'LYF010'))
eliminar_alertas_de_x_zona(lista_alerts_por_fecha,('WYG075', 'SXH966', 'LYF010'))


'''
Ah casi me olvidaba de decirles modifiquen el registro de la zona
HYD195 el nombre correcto del dinosaurio es Mosasaurus. [actividad para resolver]
'''

alert = lista_alerts_por_fecha.eliminar('HYD195','zone_code')
lista_alerts_por_nombre.eliminar('HYD195','zone_code')
alert.dino_name = 'Mosasaurus'
lista_alerts_por_fecha.insertar(alert, campo='time')
lista_alerts_por_nombre.insertar(alert, campo='dino_name')



'''
Necesito urgente un listado filtrado de los
datos que solo incluya datos de los dinosaurios: Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con
nivel  ́critical’ o ‘high’. [actividad para resolver]
'''
def lista_de_x_dinosuarios_con_x_niveles(lista, names_dinosaurios, alerts_level):
    pos_alert = 0
    alert = lista.obtener_elemento(pos_alert)
    nueva_lista_alerts_por_fecha = Lista()
    while(alert is not None):
        if (alert.dino_name in names_dinosaurios) and (alert.alert_level in alerts_level):
            nueva_lista_alerts_por_fecha.insertar(alert, campo='time')
        pos_alert += 1
        alert = lista.obtener_elemento(pos_alert)
    return nueva_lista_alerts_por_fecha


lista_alerts_por_fecha_filtrada = lista_de_x_dinosuarios_con_x_niveles(lista_alerts_por_fecha,('Tyrannosaurus Rex', 'Spinosaurus', 'Giganotosaurus'),('critical', 'high'))
print()
print('Lista con los dinosaurios (Tyrannosaurus Rex, Spinosaurus o Giganotosaurus) con nivel (critical o high):')
lista_alerts_por_fecha_filtrada.barrido()


'''
Necesito que tomes toda la información de alertas, y las insertes en dos colas, una con los datos de dinosaurios
carnívoros y otra con los herbívoros, descarten las de nivel ‘low’ y ‘medium’. [actividad para resolver]
'''
print()
from cola import Cola
def cola_de_x_tipo(lista_alerts, lista_dinosaurios,types_dinosaurios, alerts_level_a_descartar):
    pos_alert = 0
    alert = lista_alerts.obtener_elemento(pos_alert)
    nueva_cola = Cola()
    while(alert is not None):
        dinosaurio = lista_dinosaurios.busqueda(alert.dino_name, 'name')
        if (dinosaurio.info.type in types_dinosaurios) and not (alert.alert_level in alerts_level_a_descartar):
            nueva_cola.arribo(alert)
        pos_alert += 1
        alert = lista_alerts.obtener_elemento(pos_alert)
    return nueva_cola

cola_1 = cola_de_x_tipo(lista_alerts_por_fecha,lista_dinosaurios_por_name,('carnívoro'),('low','medium'))
cola_2 = cola_de_x_tipo(lista_alerts_por_fecha,lista_dinosaurios_por_name,('herbívoro'),('low','medium'))
def mostrar_cola(cola):
    for i in range(0,cola.tamanio()):
        print(cola.mover_al_final())
print('carnivoros(descartando los que tienen niveles(low y medium):')
mostrar_cola(cola_1)
print()
print('herbivoros(descartando los que tienen niveles(low y medium):')
mostrar_cola(cola_2)


'''
atiendan las alertas en la cola de carnívoros y muestren
en la pantalla (para que se publiquen en el canal de alerta de banda segura) la información pero
descarten las provenientes de la zona EPC944, ya se encuentra una unidad de respaldo ahí. [actividad
para resolver]
'''
def mostrar_cola_con_excepcion_de_x_zonas(cola, zonas_excepciones):
    for i in range(0,cola.tamanio()):
        dato = cola.mover_al_final()
        if not dato.zone_code in zonas_excepciones:
            print(dato)
print()
print('Mostrar cola de carnivoros con excepcion de la zona EPC944')
mostrar_cola_con_excepcion_de_x_zonas(cola_1,('EPC944'))


'''
un listado de toda la información que tienen procesada del archivo, pero
solo de los dinosaurios Raptors y Carnotaurus; y los códigos de las zonas donde puedo encontrar
dinosaurios Compsognathus. Que sea lo antes posible hoy es un día muy agitado. [actividad para
'''
def lista_de_x_dinosuarios_con_x_niveles(lista, names_dinosaurios):
    pos_alert = 0
    alert = lista.obtener_elemento(pos_alert)
    nueva_lista_alerts_por_fecha = Lista()
    while(alert is not None):
        if (alert.dino_name in names_dinosaurios):
            nueva_lista_alerts_por_fecha.insertar(alert, campo='time')
        pos_alert += 1
        alert = lista.obtener_elemento(pos_alert)
    return nueva_lista_alerts_por_fecha
lista_alert_con_x_dinosaurios = lista_de_x_dinosuarios_con_x_niveles(lista_alerts_por_fecha,('Raptors (Dromaeosauridae)','Carnotaurus'))
print()
print('Un listado de toda la información que tienen procesada del archivo, pero solo de los dinosaurios Raptors y Carnotaurus;')
lista_alert_con_x_dinosaurios.barrido()

print()
'''
y los códigos de las zonas donde puedo encontrar
dinosaurios Compsognathus. Que sea lo antes posible hoy es un día muy agitado. [actividad para
'''
def codigos_de_las_zonas_de_x_dinosaurio(lista, name_dinosaurio):
    pos_alert = 0
    alert = lista.obtener_elemento(pos_alert)
    print('El dinosaurio',name_dinosaurio,'se encuentra en las siguientes zona:')
    while(alert is not None):
        if (alert.dino_name in name_dinosaurio):
            print(alert.zone_code)
        pos_alert += 1
        alert = lista.obtener_elemento(pos_alert)
codigos_de_las_zonas_de_x_dinosaurio(lista_alerts_por_fecha,('Compsognathus'))
