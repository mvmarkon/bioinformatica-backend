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
    
## Instalacion con Anaconda
    - Crear ambiente virtual con conda:
	   conda create --name <nombre de env>
	- Activar el entorno virtual:
	   conda activate <nombre de env>      
    - Instalar python en el entorno virtual:
	  conda install python=3.7.6
	- Instalar/Actualizar las librerias:
		pip install -r requirements.txt -U
	- Migrar la base de datos
		python manage.py migrate   
    - Crear un superusuario para el admin:
	   python manage.py createsuperuser
	- Iniciar el servidor(por default corre en el puerto 8000)
		python manage.py runserver   


## Instalacion Clustal
- Descargar paquete para tu sistema operativa [Link](http://www.clustal.org/download/current/)
- En el caso de linux correr el script ´install-sh´		