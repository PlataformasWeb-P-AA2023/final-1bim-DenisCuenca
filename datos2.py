from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ , or_
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()



# Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"
inst = session.query(Institucion).filter(Institucion.jornada=="Matutina y Vespertina" ).all()

for i in inst:
    print(f"Int: {i} - Jornada: {i.jornada}")


print("------------------------------------------------------")
# Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459

cant = session.query(Canton).join(Parroquia).join(Institucion).\
        filter(or_(Institucion.num_est == 448, Institucion.num_est == 450, Institucion.num_est == 451, Institucion.num_est == 454, Institucion.num_est == 458, Institucion.num_est == 459)).all()
     

for i in cant:  
    print(i)
