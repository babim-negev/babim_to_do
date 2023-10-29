import os
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# ЗАГРУЖАЕМ ДАННЫЕ ИЗ .ENV
load_dotenv()

# ИЗВЛЕКАЕМ ДАННЫЕ
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")

POSTGRES_URL = "postgresql://" + db_user + ":" + db_password + "@" + db_host + ":" + db_port + "/" + db_name

engine = create_engine(
    POSTGRES_URL, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ФУНЦИЦИЯ ДЛЯ ПОДКЛЮЧЕНИЯ
def connect_to_database():
    try:
        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        print("Подключение к базе данных успешно выполнено")
        return connection
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None


# Используйте этот код для тестирования подключения к базе данных
if __name__ == "__main__":
    connection = connect_to_database()

    if connection:
        connection.close()