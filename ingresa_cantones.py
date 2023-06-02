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




# proceso para distritos


distritos = []
for l in lista:

        distritos.append(l[8])

distritos_unicos = []
for sweet in distritos:
  if sweet not in distritos_unicos:
    distritos_unicos.append(sweet)

distritos_unicos = distritos_unicos[1:]


for l in range(0, len(distritos_unicos)):
        obj = Distrito(id = l+1, descripcion = distritos_unicos[l])
        session.add(obj)
    





cantones = []
for l in lista:

        t = (l[4], l[5], l[8], l[2])
        cantones.append(t)


cantones_unicos = []
for sweet in cantones:
  if sweet not in cantones_unicos:
    cantones_unicos.append(sweet)

cantones_unicos = cantones_unicos[1:]



for l in cantones_unicos:
        prov = session.query(Provincia).filter_by(cod = int(l[3])).one()

        dist = session.query(Distrito).filter_by(descripcion=l[2]).one()


        obj = Canton(cod = int(l[0]), canton = l[1], provincia = prov, distrito =dist )
      
        session.add(obj)
   



data.close()

session.commit()

