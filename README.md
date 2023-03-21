# Auxiliar 1: Git

Git es un software que permite hacer control de versiones de nuestros proyectos. Durante esta actividad vamos a simular un flujo de trabajo de desarrollo de software.

## Introducción

Los objetivos de esta actividad son los siguientes:

* Aprender a realizar commits utilizando los comandos de git.
* Resolver un conflicto en git cuando dos personas modifican un mismo archivo.
* Pasarlo bien.

Para esta actividad necesitarán:
1. Tener instalado un cliente de git, el cual pueden descargar y configurar siguiendo este [tutorial](Por cambiar).
2. Contar con una segunda persona.
3. Su editor de texto favorito. Entre ellos están: [Sublime Text] (https://www.sublimetext.com/blog/articles/sublime-text-4), [VS Code](https://code.visualstudio.com/).

## Actividad

### Parte 1: Fork del proyecto

Cada pareja trabajará sobre el mismo código base, pero deberan hacer una copia de este código en su repositorio personal, así, sus cambios no afectarán a otras parejas.

Una persona de la pareja (Persona A) debería hacer un "Fork de este repositorio (el que están viendo ahora). Para ello, en Github deberán hacer click en "Fork" y seguir las instrucciones. 

Luego de hacer el Fork, deberían tener un repositorio con la misma imagen con el nombre *sunombredeusuario/Auxiliar1-Git*. Esto implica que tendrán su propia versión del repositorio, en el cual podrán tener control de todo.

Ahora, la persona A (quien realizó el fork) deberá darle acceso a su pareja (Persona B). Para ello deberán ir a "settings" en la barra superior del repositorio (como indica la imágen).

![]()

Después...manage access...add people.

| Todos los miembros deben ser colaboradores del repositorio. Esto les dará acceso a hacer modificaciones al proyecto.

### Parte 2: Clonar el proyecto

Ahora, ambas personas deberán clonar el repositorio en sus computadoras siguiendo los siguientes pasos:

1. Clonar el enlace del repositorio. Para ello deberán copiar el enlace que aparece al presionar "<> Code", en la pestaña "HTTP" como indica la imágen.

![]()

2. Clonar el repositorio en sus computadoras utilizando la consola de Git: `git clone https://github...`

### Parte 3: Editar el proyecto

En este paso, cada integrante de la pareja hará un cambio en el proyecto, que no afectará el trabajo del otro y luego ambas personas descargarán los cambios.

1. **Persona 🅰️** editará el archivo `clases/tarea.py`, agregando el siguiente método de clase:
```python
def terminar(self):
        self.listo = True
```

2. **Persona 🅰️** actualizará el repositorio remoto. Desde la consola de Git se deberá "empujar" los cambios que se hicieron. Para ello, debe hacer lo siguiente en la consola de git (situandola en la carpeta raíz del repositorio).

    + `git status` para ver qué cambios se hicieron.
    + `git add nombre-archivo` para agregar un archivo al commit. En este caso el archivo será clases/tarea.py 
    + `git commit -m "descripción del cambio que se hizo" ` para hacer commit de los cambios. 
    + `git push` para subir los cambios al repositorio remoto.  

3. **Persona 🅱️**  editará el archivo `clases/usuario.py`, y agregará los siguientes métodos de clase:

```python
def listarTareas(self):
    for tarea in self.tareas:
        if tarea.estaLista():
            print(f"[X] {tarea.obtenerNombre()}" )
        else:
            print(f"[ ] {tarea.obtenerNombre()}" )
```

4. **Persona 🅱️** actualizará el repositorio remoto con sus cambios según el paso 2. Al hacer `git push` aparecerá un mensaje de error.

Esto pasará porque **Persona 🅰️** hizo cambios a un archivos, cambios que **Persona 🅱️** no ha descargado. Para arreglar esto, **Persona 🅱️** deberá hacer `git pull`. Al hacer esto, juntará (merge) la versión del repostorio remoto con la versión local. Por esta razón aparecerá un editor con un mensaje parecido a este:

![]()

> Si no hay instrucciones para salir de ahí, prueba escribiendo ":wq" y luego presiona enter. Si no funciona, pide ayuda.

Persona B deberá hacer `git push` de nuevo para que sus cambios se suban al repositorio remoto.

5. **Persona A** hará `git pull` en la consola de Git y podrá ver los cambios realizados por Persona B sin problemas.

> Para no tener este problema, se recomienda realizar `git pull` antes de las instrucciones del paso 2, pero después de modificar el código, así te aseguras de arreglar cualquier error que pueda producirse entre el código remoto y tus cambios locales antes de crear el commit.

### Parte 4: Editar mismo archivo

¿Qué pasaría si persona B quiere quitarle el método listarTareas a la clase Usuario en `usuario.py` sin avisar y **Persona A decide moidificar la forma en que se muestran la lista de tareas?

1. Persona B quitará la línea de código en `clases/usuario.py`

```python
def listarTareas(self):
    for tarea in self.tareas:
        if tarea.estaLista():
            print(f"[X] {tarea.obtenerNombre()}" )
        else: <<<<<<< Elimina esta
            print(f"[ ] {tarea.obtenerNombre()}" ) <<<<< y esta
```

2. Persona B actualizará el repositorio remoto segúin las instrucciones de la parte 3, páso 2.

3. Persona A (SIN DESCARGAR LOS CAMBIOS DE LA OTRA PERSONA) editará la siguiente línea del mismo archivo:

```python
def listarTareas(self):
    for tarea in self.tareas:
        if tarea.estaLista():
            print(f"[X] {tarea.obtenerNombre()}" )
        else:
            print(f"[ ] {tarea.obtenerNombre()}" )
```
 Lo reemplazará por:
 
 ```python
def listarTareas(self):
    for tarea in self.tareas:
        if tarea.estaLista():
            print(f"La tarea {tarea.obtenerNombre()} está lista")
        else: <<<<<<< Elimina esta
            print(f"La tarea {tarea.obtenerNombre()} no está lista")
```

4. Persona A actualizará el repositorio remoto según las instrucciones de la parte 3, paso 2. Al hacer `git push`, Persona A verá que hay un conflicto como pasó en la parte anterior. Para resolver esto se debe hacer git pull y aparecerá este mensaje:

![]()

Esto pasa cuando dos personas editan en mismo archivo del proyecto. Muchas veces Git puede solucionar estos conflictos automáticamente, pero otras veces la persona que realiza el push deberá decidir cuál será el código definitivo (luego de conversar con todo el equipo de desarrollo).

5. Persona A verá que su archivo `clase









---

Y en el archivo `clases/tarea.py` agregar los siguientes métodos de clase:
```python
def terminar(self):
        self.listo = True
```

Ahora ambas personas deben 




