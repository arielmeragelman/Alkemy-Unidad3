import logging

# Inicializo el objeto logging con la configuracion requerida
logging.basicConfig(
                            level=logging.INFO,
                            filename='logs/results.log',
                            format='%(asctime)s - %(levelname)s - %(message)s'

)

fruits = ['Frutilla', 'Melón', 'PERA', '99.6', 'NaranJA', 'mORa',
          'NisPERo', 99]

# Se realiza un lower de los elementos de la lista, se registran en results.log
# en caso de ejecucion correcta como INFO y en caso de falla como ERROR
for fruta in fruits:

    try:
        print(fruta.lower())
        logging.info(f"conversión exitosa: {fruta}")
    except AttributeError:
        logging.error("Conversión fallida: {}".format(fruta))
