# Saltador de texto para Genshin Impact
¿Estás haciendo una misión que contiene mucho texto y como no te interesa su historia te pones a pulsar continuamente el botón izquierdo del ratón o el botón X del mando de PS4/5? Este programa lo hará por ti, incluyendo también las elecciones que a veces aparecen en pantalla.

Es un programa que se ejecuta en consola, tan solo escoge una de las opciones que aparezcan en la consola y el programa empezará su ejecución, no tienes que hacer nada más.

## Instrucciones de uso
1. Abre **primero** el Genshin Impact
2. Abre este programa (*py AutoSkipChat.py* en la consola, o *python* en vez de *py*, depende cómo lo tengas configurado)
3. Elige la opción que se adapte a tus necesidades
4. Si sale un número distinto a 0 en la consola, el programa ya está en funcionamiento; si sale un 0, no has abierto el juego
   
Recuerda que antes tienes que tener la consola en la ruta donde está este programa y que tienes que tener instaladas las librerías de Python necesarias para que funcione el programa (*pip install -r requirements.txt*)

## Consideraciones a tener en cuenta
1. Detecta texto de interacciones y elecciones. No detecta textos que aparecen en el centro de la pantalla (notas, libros...) ni fundidos a negro con texto en el centro (como, por ejemplo, cuando explican una situación sin mostrar nada en pantalla)
2. Disponible solo para teclado/ratón y mando PS4/5 (Funcional también con programas externos que simulan DInput como DS4Windows)
3. Disponible solo para 1080p. También disponible en 1360×768 (WXGA 85:48) para teclado/ratón
4. Si usas el modo mando PS4/5, es obligatorio tener los textos del Genshin Impact en español
5. El programa aunque esté en ejecución continua está optimizado para bajar su velocidad de análisis drásticamente si no estás en el juego o si no estás interactuando con texto. Cuando detecte un texto aumentará mucho su velocidad para que la velocidad de saltar texto sea la más rápida que permita el juego, por tanto no hay que preocuparse por el uso de CPU, el programa se adaptará al momento
6. La versión de Python utilizada es la 3.9.7, desconozco si funciona en otras versiones del mismo

## ¿Seré baneado del Genshin Impact por usar este programa?
Aunque Genshin Impact especifica que está prohibido el uso de programas externos, no te va a pasar nada porque este programa no inyecta código ni modifica archivos del juego. El programa analiza lo que tienes en pantalla en ese momento para realizar las acciones pertinentes por lo que es indetectable a ojos del juego y de la empresa.

Sobre si es moral o no el uso del programa, me parece que si la empresa hubiera decidido hacer un botón de *saltar todo* no hubiera sido necesario hacer este programa, cada uno es libre de jugar como quiera pero si el juego no nos da las herramientas necesarias para jugar de forma cómoda, no creo que sea inmoral saltarse las reglas para este caso.
