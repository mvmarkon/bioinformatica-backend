# bioinformatica-backend

	- Crear ambiente virtual con virtualenv:
		virtualenv -p <path a python3> <nombre de venv>

	- Activar el ambiente virtual:
		source <nombre de venv>/bin/activate

	- Instalar/Actualizar las librerias:
		pip install -r requirements.txt -U

	- Migrar la base de datos
		python manage.py migrate

	- Iniciar el servidor(por default corre en el puerto 8000)
		python manage.py runserver
