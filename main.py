from db.create_db import create_db
from db.fill_db import fill_db


def main():
    # Crear la DB
    create_db()
    # Llenar la DB con datos en base a los CSV
    fill_db()


if __name__ == '__main__':
    main()
