from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton, Tipos_sostenimiento, Distrito
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.
inst = session.query(Institucion).filter(Institucion.num_doc>100).order_by(Institucion.num_est).all()
for i in inst:
    print(i)
    

print("------------------------------------------------------")
# Los establecimientos ordenados por número de  100 profesores.
inst = session.query(Institucion).filter(Institucion.num_doc>100).order_by(Institucion.num_doc).all()
for i in inst:
    print(i)
