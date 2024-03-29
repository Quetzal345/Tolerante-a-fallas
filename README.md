# Computacion tolerante a fallas
En este readme se podran observar todos los trabajos de la materia y los resultados de todos mis trabajos.

## [Conceptos básicos](https://github.com/Quetzal345/Tolerante-a-fallas/blob/33392e27519e095b9e35c778140da41bb6541a79/Conceptos_basicos_delgado.pdf)
Conocer los conceptos básicos en sistemas tolerantes a fallas

## [Otras herramientas para el manejar errores](https://github.com/Quetzal345/Tolerante-a-fallas/blob/414643cb7c26476ef9d6ad2d6dcf0ec8072fcb13/Modulo%201/Manejarerrores.cpp) 
 Genera un ejemplo en el lenguaje de tu preferencia utilizando las herramientas que encontraste.

 El código que hice para dar un ejemplo del try catch, lo realice en c++, lo hice en un programa que sumara dos números que ingrese el usuario, entonces el try catch funciona para que cuando un usuario ingrese 
 algún texto o letra, le marque error, al momento de realizar la suma, esto para que vea que solo debe de ingresar números y no letras.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/19cc00b77861ba11f2a967001458be6a23cae44e/Campturas/captura%201.png)

## [Otra herramienta para manejar errores pt 2](https://github.com/Quetzal345/Tolerante-a-fallas/blob/5795c33e5bd0bcb423e7b5b4da13311e2ca7b021/Modulo%201/manejode_errores_Delgado.pdf)

Java (try-catch):
En Java, el manejo de errores se realiza principalmente mediante bloques try y catch. El código propenso a errores se coloca dentro del bloque try, y cualquier excepción que ocurra se captura y maneja en elbloque catch. Esto permite una gestión controlada de errores.
Ejemplo en codigo:
```
try {
// Código propenso a errores
} catch (ExcepcionTipo1 e1) {
// Manejar ExcepcionTipo1
} catch (ExcepcionTipo2 e2) {
// Manejar ExcepcionTipo2
} finally {
// Código que se ejecuta siempre, independientemente de si hay una excepción 
o no
}
```
En Python, el manejo de errores se realiza con bloques try y except. Similar al enfoque de Java, el código propenso a errores se coloca dentro del bloque try, y cualquier excepción se maneja en el bloque except.
```
try:
# Código propenso a errores
except ExcepcionTipo1 as e1:
# Manejar ExcepcionTipo1
except ExcepcionTipo2 as e2:
# Manejar ExcepcionTipo2
else:
# Código que se ejecuta si no hay excepciones
finally:
# Código que se ejecuta siempre, independientemente de si hay una excepción o 
no
```

## [Principios de prevención de defectos](https://github.com/Quetzal345/Tolerante-a-fallas/blob/9ca1404b9ec8ece3cac088f079c093933c82a39f/Modulo%201/prevencion_de_defectos.pdf)

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/8a0a4278503aac6cac83077867ff7816a36b4658/Campturas/200px-Buggie.svg.png)

Bugzilla es un sistema de seguimiento de errores basado en web, que permite a los equipos de desarrolladores llevar un registro de los problemas, mejoras y otros cambios solicitados en sus productos de software.  Bugzilla fue originalmente desarrollado y usado por el proyecto Mozilla, pero ahora es utilizado por muchas otras organizaciones y proyectos de código abierto. 
Algunas de las características de Bugzilla son:
Búsqueda avanzada: permite encontrar el error exacto que se busca, usando varios criterios y filtros.
Productos y componentes: permite categorizar y rastrear los errores según los productos y componentes a los que pertenecen.

## [Principios y prevención de defectos (2)](https://github.com/Quetzal345/Tolerante-a-fallas/blob/7922f79c347b63b8a6b551a2f14a3d55c8f35d47/Modulo%201/ODC.pdf)

## [Generar un programa que sea capaz de restaurar el estado de ejecución. ](https://github.com/Quetzal345/Tolerante-a-fallas/blob/e3788b0fd670b4b61a65e674379cddf820722278/Modulo%201/reporte_checkpointing.pdf)
Entonces para probarlo, realice un juego sencillo el cual consiste en adivinar un número, lo que hace el juego es que el usuario puede poner un rango desde 1 al 100 para poder adivinar el número, así como se ve en la imagen, el usuario puede mover la barra para elegir el rango de dificultad en el que quiere jugar.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/b50debad1eb38ad9b5d2c4bf2d590900605953ea/Campturas/captura%202.png)

Después de escoger el rango en el que se quiere jugar, ahora solo queda adivinar el número, pero el juego tiene un contador de intentos, como el que aparece a continuación.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/b50debad1eb38ad9b5d2c4bf2d590900605953ea/Campturas/Captura%203.png)

Además, que al usar pickle, se genera un archivo que es binario en el que guarda el estado del juego.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/b50debad1eb38ad9b5d2c4bf2d590900605953ea/Campturas/Captura%204.png)

## [An Introduction to Scaling Distributed Python Applications](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/907ee4e7020e7fff7c8912b5edc3d00e4703c963/Modulo1/Distributed%20Python%20Applications_Delgado.pdf)
Generar un programa utilizando hilos, procesos, demonios y concurrencia. 

En el programa, se logra la concurrencia mediante el uso de hilos y procesos para ejecutar tareas en segundo plano mientras la interfaz de usuario sigue siendo receptiva y funcional.
Por ejemplo, mientras el demonio monitorea el estado del juego, el jugador puede seguir interactuando con la interfaz gráfica y realizar acciones como adivinar un número o cambiar la dificultad.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/3f000ef85567282b6722eb1bdd60ca11e451898c/Campturas/captura%205.png)

## [Estatus](https://github.com/Quetzal345/Tolerante-a-fallas/blob/8075c409ca254a5ef30977e5c0846db11cdc8fdb/Modulo%201/Estatus_Delgado.pdf)

Esta es la línea de comando para poder hacer tu programa un servicio, al cual el nombre le puse mi servicio para identificarlo más fácil. También es importante recalcar que necesitas ejecutar como administrador la terminal, si no funcionara.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/21ae308aee82306d95aac0fb30a95148c1ac9565/Campturas/cap11.png)

Como muestra, es que ya existe otro servicio por eso me marca un error, ya que al momento de ver si funcionaba no tome captura de pantalla, pero si cambio el nombre del 
servicio funcionaria para otro script que se tenga.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/21ae308aee82306d95aac0fb30a95148c1ac9565/Campturas/cap12.png)

Como se puede observar el servicio se crea de y aparece en mis servicios, aunque lo único que realiza es cerrar el Chrome si ve que esta abierto, lo cual hace mediante hilos 
y de una revisión de cada 30 segundos.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/21ae308aee82306d95aac0fb30a95148c1ac9565/Campturas/cap13.png)

## [Workflow managers](https://github.com/Quetzal345/Tolerante-a-fallas/blob/db4f319914e75c4d84f46528c6e4ce0dc6ce8530/Modulo%201/Reporte_Workflow%20managers_Delgado.pdf)

Para esta práctica lo que quiero realizar es un programa que pueda consultar mi top 50 canciones escuchadas en Spotify, ya que Spotify me da un token para poder acceder a la API, así que con ello poder acceder a las canciones, simplemente voy a acceder a los nombres de las canciones y los artistas que interpretan dichas canciones, también voy aagregar hilos, para que el programa pueda intentar varias veces para lograr obtener los resultados que quiero.

Aqui quite una letra del token para que se pueda apreciar que el programa intenta 3 veces para obtener los resultados, después de los 3 intentos, el programa te da un 
mensaje de error, de que no se pudo obtener las canciones.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/f1b8480324756002df86bb26b3862defff8a8410/Campturas/cap16.png)

Una vez obteniendo las canciones, así es como se muestra en el programa

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/f1b8480324756002df86bb26b3862defff8a8410/Campturas/cap15.png)

## [Segundo ejemplo práctico utilizando el orquestador de Prefect](https://github.com/Quetzal345/Tolerante-a-fallas/blob/f1b8480324756002df86bb26b3862defff8a8410/Modulo%201/perfect.pdf)

Prefect es una plataforma de código abierto para la orquestación de flujos de trabajo en Python, diseñada para facilitar la automatización de procesos complejos y la gestión eficiente de tareas en entornos de ciencia de datos y desarrollo de software. Con Prefect, los usuarios pueden definir, programar y ejecutar flujos de trabajo de manera declarativa, lo que permite una mayor claridad y control sobre el flujo de los datos y las dependencias entre las tareas.

En este ejemplo donde utilizo perfect, pero utilizo la API de youtube, para que me diera datos acerca de mi cuenta de youtube, como se puede ver están en 0, ya que no soy un 
youtuber, pero con este programa se podría ver los subscritores, likes, reproducciones y más.

![](https://github.com/Quetzal345/Tolerante-a-fallas/blob/f1b8480324756002df86bb26b3862defff8a8410/Campturas/cap14.png)
