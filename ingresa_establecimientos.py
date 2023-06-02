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
 





# 
tipos_educacion = []
for l in lista:

        tipos_educacion.append(l[10])

tipos_educacion_unicos = []
for sweet in tipos_educacion:
  if sweet not in tipos_educacion_unicos:
    tipos_educacion_unicos.append(sweet)

tipos_educacion_unicos = tipos_educacion_unicos[1:]


for l in range(0, len(tipos_educacion_unicos)):
        obj = Tipos_educacion(id = l+1, descripcion = tipos_educacion_unicos[l])
        session.add(obj)
        





 
tipos_sostenimiento = []
for l in lista:
      
        tipos_sostenimiento.append(l[9])

tipos_sostenimiento_unicos = []
for sweet in tipos_sostenimiento:
  if sweet not in tipos_sostenimiento_unicos:
    tipos_sostenimiento_unicos.append(sweet)

tipos_sostenimiento_unicos = tipos_sostenimiento_unicos[1:]


for l in range(0, len(tipos_sostenimiento_unicos)):
        obj = Tipos_sostenimiento(id = l+1, descripcion = tipos_sostenimiento_unicos[l])
        session.add(obj)
        




 
inst = []
for l in lista:
    
        t = (
        l[0], 
        l[1], 
        l[14], 
        l[15], #b
        l[11], 
        l[12], # b
        l[6], # prov
        l[10], # te 
        l[13], # t
        l[9]) # s
        inst.append(t)


inst_unicos = []
for sweet in inst:
  if sweet not in inst_unicos:
    inst_unicos.append(sweet)

inst_unicos = inst_unicos[1:]

for l in inst_unicos:

        p = session.query(Parroquia).filter_by(cod = int(l[6])).one()
        te = session.query(Tipos_educacion).filter_by(descripcion = l[7]).one()
        ta = session.query(Tipo_acceso).filter_by(descripcion = l[8]).one()
        ts = session.query(Tipos_sostenimiento).filter_by(descripcion = l[9]).one()


        obj = Institucion(
                cod = l[0], 
                nombre = l[1], 
                num_est = int(l[2]),
                num_doc = int(l[3]),
                modalidad = l[4],
                jornada = l[5],
                parroquia =p,
                tipos_educacion = te,
                tipo_acceso = ta,
                tipos_sostenimiento = ts

                
                )
    
        session.add(obj)





data.close()

session.commit()
