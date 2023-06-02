from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Tipo_acceso, Tipos_educacion, Tipos_sostenimiento, Institucion, Canton, Parroquia, Provincia, Distrito

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


data = open('data/ins_educativas.csv', 'r', encoding="utf-8")
lineas = data.readlines()
    


lista = [l.replace("\n", "").replace("\ufeff", "").split(";") for l in lineas]



# provincias::

provincias = []
for l in lista:
        tupla = (l[2], l[3])
        provincias.append(tupla)

provincias_unicas = []
for sweet in provincias:
  if sweet not in provincias_unicas:
    provincias_unicas.append(sweet)

provincias_unicas = provincias_unicas[1:]


for l in provincias_unicas:
        obj = Provincia(cod = int(l[0]), provincia = l[1])
        session.add(obj)
    



data.close()

session.commit()
