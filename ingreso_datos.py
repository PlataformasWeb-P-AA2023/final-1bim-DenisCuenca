from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Tipo_acceso, Tipos_educacion, Tipos_sostenimiento, Institucion, Canton, Parroquia, Provincia, Distrito

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()




# proceso para tipo de acceso acceso
accesos = open('data/accesos.csv', "r", encoding="utf-8")
lineas = accesos.readlines()
lista = [l.replace("\n", "").replace("\ufeff", "").split(";") for l in lineas]


for l in lista:
        obj = Tipo_acceso(id = int(l[1]), descripcion = l[0])
        session.add(obj)

accesos.close()



# proceso para distritos
archivo = open('data/distritos.csv', "r", encoding="utf-8")
lineas = archivo.readlines()
lista = [l.replace("\n", "").replace("\ufeff", "").split(";") for l in lineas]


for l in lista:
        obj = Distrito(id = int(l[1]), descripcion = l[0])
        session.add(obj)


archivo.close()


# proceso para provincias
archivo = open('data/provincias.csv', "r", encoding="utf-8")
lineas = archivo.readlines()
lista = [l.replace("\n", "").replace("\ufeff", "").split(";") for l in lineas]


for l in lista:
        obj = Provincia(cod = int(l[0]), provincia = l[1])
        session.add(obj)

archivo.close()




# proceso para tipos_educacion
archivo = open('data/tipos_educacion.csv', "r", encoding="utf-8")
lineas = archivo.readlines()
lista = [l.replace("\n", "").replace("\ufeff", "").replace("Ã³", "ó").split(";") for l in lineas]


for l in lista:
        obj = Tipos_educacion(id = int(l[1]), descripcion = l[0])
        session.add(obj)

archivo.close()


# proceso para tipos sostenimiento
archivo = open('data/tipos_sostenimiento.csv', "r", encoding="utf-8")
lineas = archivo.readlines()
lista = [l.replace("\n", "").replace("\ufeff", "").replace("Ã³", "ó").split(";") for l in lineas]


for l in lista:
        obj = Tipos_sostenimiento(id = int(l[1]), descripcion = l[0])
        session.add(obj)


archivo.close()


# proceso para tipos cantones
archivo = open('data/cantones.csv', "r", encoding="utf-8")
lineas = archivo.readlines()
lista = [l.replace("\n", "").replace("\ufeff", "").replace("Ã³", "ó").split(";") for l in lineas]


for l in lista:
        prov = session.query(Provincia).filter_by(cod=int(l[2])).one()
        dist = session.query(Distrito).filter_by(id=int(l[3])).one()
        obj = Canton(cod = int(l[0]), canton = l[1], provincia = prov, distrito = dist)
        session.add(obj)


archivo.close()


# proceso para tipos parroquias
archivo = open('data/parroquias.csv', "r", encoding="utf-8")
lineas = archivo.readlines()
lista = [l.replace("\n", "").replace("\ufeff", "").replace("Ã³", "ó").split(";") for l in lineas]


for l in lista:
        cant = session.query(Canton).filter_by(cod=int(l[2])).one()
        
        obj = Parroquia(cod = int(l[0]), parroquia = l[1], canton = cant)
        session.add(obj)


archivo.close()


# proceso para tipos instituciones
archivo = open('data/instituciones.csv', "r", encoding="utf-8")
lineas = archivo.readlines()
lista = [l.replace("\n", "").replace("\ufeff", "").replace("Ã³", "ó").replace("Ã‘", "ñ").split(";") for l in lineas]


for l in lista:
        parr = session.query(Parroquia).filter_by(cod=int(l[7])).one()
        acce = session.query(Tipo_acceso).filter_by(id=int(l[4])).one()
        sost = session.query(Tipos_sostenimiento).filter_by(id=int(l[5])).one()
        teduc = session.query(Tipos_educacion).filter_by(id=int(l[6])).one()
        

        if teduc and   acce and sost and parr:

                
                obj = Institucion(cod = l[0], nombre = l[1], num_est = int(l[2]), num_doc = int(l[3]),modalidad = l[8], jornada=l[9],parroquia= parr, tipo_acceso=acce, tipos_sostenimiento = sost,   tipos_educacion=teduc )

                session.add(obj)


archivo.close()

session.commit()
