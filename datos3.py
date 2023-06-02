from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()



# Los cantones que tiene establecimientos con 0 número de profesores, 5 profesores, 11, profesores
cant = session.query(Canton).join(Parroquia).join(Institucion).\
        filter(or_(Institucion.num_doc == 0, Institucion.num_doc == 5, Institucion.num_doc == 11)).all()
     
for i in cant:
    print(i)


print("------------------------------------------------------")

# Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21
cant = session.query(Institucion).join(Parroquia).\
        filter(Parroquia.parroquia == "PINDAL").filter(Institucion.num_est >= 21).all()

for i in cant:
    print(i)
