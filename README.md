# bioinformatica-backend

*Grupo 5: Cuoco,Carlos - Markon,Mariano -Verdacanna Mariano* 

## Instalacion Clustal
- Descargar paquete para tu sistema operativa [Link](http://www.clustal.org/download/current/)
- En el caso de linux correr el script ´install-sh´	

## Instalacion con Anaconda para utilizar la aplicación
- Entrar a la carpeta generada al clonar el proyecto:  
	`cd bioinformatica-backend`
- Crear ambiente virtual con conda :  
	   `conda create --name <nombre de env>`
- Activar el entorno virtual:  
	   `conda activate <nombre de env>`      
- Instalar python en el entorno virtual:  
	  `conda install python=3.7.6`	
- Actualizar con las librerias el enviroment de conda   
	  `conda env update --file envname.yml`
- Instalar  algunas librerias que no estaban en los channels de Conda:  
		`pip install -r requirements.txt -U`	 	
- Migrar la base de datos  
		`python manage.py migrate`   
- Iniciar el servidor(por default corre en el puerto 8000)  
		`python manage.py runserver`   

##  Como crear Usuario para admin de Python 
- Crear un superusuario para el admin:  
	   `python manage.py createsuperuser`

## Este proyecto necesita el siguiente repositorio para poder funcionar:
[Proyecto de Frontend](https://github.com/mverdecanna/bioinformatica-frontend)	
