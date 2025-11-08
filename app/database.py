import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Usa la variable de entorno si está definida, o el valor por defecto
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:tu_password_secreto@mariadb-ledger:3306/transaction_ledger"
)

# Crea el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Crea la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()