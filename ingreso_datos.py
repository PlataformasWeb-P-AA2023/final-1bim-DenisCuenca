from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Tipo_acceso, Tipos_educacion, Tipos_sostenimiento, Institucion, Canton, Parroquia, Provincia, Distrito

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


data = open('data/ins_educativas.csv', 'r', encoding="utf-8")
lineas = data.readlines()
    


# proceso para tipo de acceso acceso

lista = [l.replace("\n", "").replace("\ufeff", "").split(";") for l in lineas]

tipos_accesos = []
for l in lista:

        tipos_accesos.append(l[13])


unique_tipos = []
for sweet in tipos_accesos:
  if sweet not in unique_tipos:
    unique_tipos.append(sweet)


for l in range (0, len(unique_tipos[1:])):
        obj = Tipo_acceso(id = int(l+1), descripcion = unique_tipos[1:][l])
        session.add(obj)
        print(obj.id)



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
        print()


# proceso para distritos


distritos = []
for l in lista:
        print(l[8])
#       
        distritos.append(l[8])

distritos_unicos = []
for sweet in distritos:
  if sweet not in distritos_unicos:
    distritos_unicos.append(sweet)

distritos_unicos = distritos_unicos[1:]


for l in range(0, len(distritos_unicos)):
        obj = Distrito(id = l+1, descripcion = distritos_unicos[l])
        session.add(obj)
        print()




data.close()

session.commit()
