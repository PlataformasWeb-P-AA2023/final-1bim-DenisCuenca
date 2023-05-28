from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ 
from genera_tablas import Institucion, Parroquia, Provincia, Canton
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


# Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553
inst = session.query(Institucion).filter(Institucion.id_parroquia==110553 ).all()
 
print(inst)


print("------------------------------------------------------")
# Todos los establecimientos de la provincia del Oro

inst = session.query(Institucion).join(Parroquia).join(Canton).join(Provincia).\
        filter(Provincia.provincia == "EL ORO").all()

for i in inst:
    print(i)
    
print("------------------------------------------------------")
# Todos los establecimientos del cantón de Portovelo.

ints = session.query(Institucion).join(Parroquia).join(Canton).\
        filter(Canton.canton == "PORTOVELO").all()

for i in ints:
    print(i)
    
print("------------------------------------------------------")
# Todos los establecimientos del cantón de Zamora.
inst = session.query(Institucion).join(Parroquia).join(Canton).filter(Canton.canton == "ZAMORA").all()

for i in inst:
    print(i)