from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Table

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()




class Tipos_educacion(Base):
    __tablename__ = 'tipos_educacion'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))
    institucion = relationship("Institucion", back_populates="tipos_educacion")
    
    def __repr__(self):
        return self.descripcion       


class Tipos_sostenimiento(Base):
    __tablename__ = 'tipos_sostenimiento'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))
    institucion = relationship("Institucion", back_populates="tipos_sostenimiento")
    
    def __repr__(self):
        return self.descripcion          



class Distrito(Base):
    __tablename__ = 'distrito'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))
    canton = relationship("Canton", back_populates="distrito")

    def __repr__(self):
        return self.descripcion


class Provincia(Base):
    __tablename__ = 'provincia'
    cod = Column(Integer, primary_key=True)
    provincia = Column(String(250))
    canton = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return self.provincia




class Canton(Base):
    __tablename__ = 'canton'
    cod = Column(Integer, primary_key=True)
    canton = Column(String(250))
    id_provincia = Column(Integer, ForeignKey('provincia.cod'))
    id_distrito = Column(Integer, ForeignKey('distrito.id'))


    provincia = relationship("Provincia", back_populates="canton")
    distrito = relationship("Distrito", back_populates="canton")

    parroquia = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return self.canton


class Parroquia(Base):
    __tablename__ = 'parroquia'
    cod = Column(Integer, primary_key=True)
    parroquia = Column(String(250))
    id_canton = Column(Integer, ForeignKey('canton.cod'))

    canton = relationship("Canton", back_populates="parroquia")

    institucion = relationship("Institucion", back_populates="parroquia")

    def __repr__(self):
        return self.parroquia





class Tipo_acceso(Base):
    __tablename__ = 'tipo_acceso'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))


    instituciones = relationship("Institucion", back_populates ="tipo_acceso")

    def __repr__(self):
        return self.descripcion

class Institucion(Base):
    __tablename__ = 'institucion'
    cod = Column(String(20), primary_key=True)
    nombre = Column(String(550))
    num_est = Column(Integer)
    num_doc = Column(Integer)

    modalidad = Column(String(300))
    jornada = Column(String(300))


    id_parroquia = Column(Integer, ForeignKey('parroquia.cod'))
    id_acceso = Column(Integer, ForeignKey('tipo_acceso.id'))
    id_sostenimiento = Column(Integer, ForeignKey('tipos_sostenimiento.id'))
    id_tipo_educacion = Column(Integer, ForeignKey('tipos_educacion.id'))

    tipo_acceso = relationship("Tipo_acceso", back_populates="instituciones")
    tipos_sostenimiento = relationship("Tipos_sostenimiento", back_populates="institucion")
    tipos_educacion = relationship("Tipos_educacion", back_populates="institucion")
    parroquia = relationship("Parroquia", back_populates="institucion")
    

    def __repr__(self):
        return self.nombre


# class Jornadas_institucion(Base):
#     __tablename__ = 'jornadas_institucion'
#     __table_args__ = (UniqueConstraint('cod_inst', 'cod_jor', name='_cod_inst_jor'),)
    
#     cod_inst = Column(String(10), ForeignKey('institucion.cod'), extend_existing=True,unique=True)
#     cod_jor = Column(Integer, ForeignKey('jornadas.id'), unique=True)

#     institucion = relationship("Intitucion", back_populates="jornadas_institucion")
#     jornada = relationship("Jornadas", back_populates="jornadas_institucion")

#     def __repr__(self):
#         return f"inst: {self.cod_inst} - jor: {self.cod_jor}"

# class Modalidad_institucion(Base):
#     __tablename__ = 'jornadas_institucion'
#     cod_inst = Column(String(10), ForeignKey('institucion.cod'))
#     cod_mod = Column(Integer, ForeignKey('modalidades.id'))

#     institucion = relationship("Intitucion", back_populates="jornadas_institucion")
#     modalidad = relationship("modalidades", back_populates="jornadas_institucion")

#     def __repr__(self):
#         return f"inst: {self.cod_inst} - jor: {self.cod_mod}"



Base.metadata.create_all(engine)









