# Esteganografia con Python

Este programa utiliza tecnicas de esteganografia para ocultar mensajes en una
imagen. 

## ¿Cómo funciona?
El programa lee un archivo de imagen (por ejemplo JPG), para despues cargar en 
memoria los valores enteros de los canales RGB de una zona de pixeles. Estos
valores enteros son modificados a nivel binario, en donde el bit menos
significativo es cambiado para representar el valor ascii de un caracter.
Es posible representar de manera binaria un caracter en 8 bits, por lo tanto
necesitamos un grupo de al menos tres pixeles para representar un caracter.

## ¿Qué zona de pixeles lee?
Se lee de manera horizontal (eje de las abscisas), comenzando por el primer 
pixel en x=0 hasta x=n, donde n es la logintud horizontal de la imagen. 
Por default se lee y escribe en la fila y=0, es decir, los pixeles que estan 
en la parte superior de la imagen.

## ¿Hasta cuantos caracteres puede guardar el programa?
Se puede guardar hasta n caracteres, donde n es la longitud horizontal de la 
imagen

## ¿Como leo el contenido de una imagen?
El programa recibe tres parametros:
* --imagen Nombre de la imagen a leer.
* --operacion Operacion a ejecutar, puede ser r (read/leer) o w (write/escribir)
* --mensaje Texto a esconder en la imagen


## Uso
Leer contenido de un archivo
```python lsb.py --imagen=imagen.jpg --operacion=r```

Esconder mensaje en un archivo
```python lsb.py --imagen=imagen.jpg --operacion=w --mensaje="MENSAJE OCULTO"```

Leer contenido de un archivo con mensaje oculto
```python lsb.py --imagen=escondido.bmp --operacion=r```

El programa crea una nueva imagen de tipo BMP llamada escondido.bmp, en donde
se ocultara el mensaje configurado previamente.

