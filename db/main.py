from create_db import create_db
from fill_db import fill


def main():
    # Crear la DB
    create_db()
    # Llenar la DB con datos en base a los CSV
    fill()


if __name__ == '__main__':
    main()