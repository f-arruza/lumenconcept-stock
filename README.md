### Microservicios incluidos:
##### 1.) Stock Manager (API REST)
##### 2.) Stock Verification (Backgroung Task)
##### 3.) Register Transaction (Backgroung Task)
##### 4.) Stock Compensation (Backgroung Task)

###### TODOS desplegables de manera independiente en contenedores Docker.
###### Para iniciar los procesos en segundo plano, se debe ejecutar el siguiente comando: 
python manage.py process_tasks

###### La implementación de los puntos 2-3-4 la puede encontrar en: 
lumenconcept-stock/stock/tasks.py
