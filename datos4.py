from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton, Tipos_sostenimiento, Distrito
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


# Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
inst = session.query(Institucion).join(Parroquia).\
        filter(Institucion.num_doc > 40).order_by(Parroquia.parroquia).all()
     
print(inst)

print("...............................")

# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04.

inst = session.query(Institucion).join(Tipos_sostenimiento).join(Parroquia).join(Canton).join(Distrito).\
        filter(Distrito.descripcion  == "07D05").order_by(Tipos_sostenimiento.descripcion).all()
     
print(inst)