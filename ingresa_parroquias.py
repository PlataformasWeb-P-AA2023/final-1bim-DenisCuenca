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








parr = []
for l in lista:
        t = (l[6], l[7], l[5])
        parr.append(t)


parr_unicos = []
for sweet in parr:
  if sweet not in parr_unicos:
    parr_unicos.append(sweet)

parr_unicos = parr_unicos[1:]



for l in parr_unicos:
        c = session.query(Canton).filter_by(canton = l[2]).one()


        obj = Parroquia(cod = int(l[0]), parroquia = l[1], canton = c )
        session.add(obj)
   




data.close()

session.commit()
