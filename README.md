# **Calculadora Pythonista**

Calculadora con interfaz gráfica que contiene operaciones básicas y científicas, escrita en [Python](https://www.python.org) usando el paquete [Tkinter](https://docs.python.org/es/3/library/tkinter.html) para la interfaz gráfica. Nos basamos en el código encontrado en el artículo de [Acerov Lima](https://acervolima.com/calculadora-de-gui-cientifica-usando-tkinter-em-python/) para la implementación.

---

# Requerimientos de la calculadora

Para el uso de la calculadora se necesitan las bibliotecas de Python3:

* tkinter
* math

---

# Uso de la calculadora

Para usar la calculadora, debe ejecutar el archivo `main.py`. La calculadora cuenta con interfaces:

* **Interfaz estándar:** La calculadora inicia con esta interfaz, la cual contiene las operaciones básicas de suma, resta, multiplicación, división y raíz cuadrada, además de poder escribir números decimales y negativos.
![Interfaz estandar](/images/b5671dc7-d9fa-4c86-82b0-1dbdb19cbbef.JPG)

* **Interfaz científica:** esta interfaz se acopla a la interfaz estándar y trae las operaciones de resto, cociente y potencia. Además, una plétora de funciones, entre ellas las trigonométricas y las funciones de exponencial y logaritmo.
![Interfaz cientifica](/images/0ad3a7ce-7715-4ce0-bafd-04c2997585c6.JPG)

Para el uso de operaciones entre dos números, se debe ingresar el primer número, presionar en la operación que desee utilizar, luego ingresa el segundo número y presiona el signo de igual. Para el uso de funciones, debe ingresar el número y luego la función que desee utilizar.

Para escribir un número, presione los dígitos del número que desee. Si el número es negativo, presione el signo ±. En caso de que su número sea decimal, presione el signo . para escribir los decimales.

Para aplicar funciones, escriba su número y luego presione la función deseada.

Si desea eliminar el número escrito, presione el signo C. Si presionó alguna operación y desea eliminar el primer número escrito y la operación, presione el signo CE.

---

# Flujo de trabajo en GitHub

El proceso de implementación fue el siguiente:

1. Creamos el repositorio y el *README*. Implementaremos un flujo de trabajo basándonos en el flujo de trabajo propuesto por [GitFlow](http://datasift.github.io/gitflow/IntroducingGitFlow.html).
2. Creamos la rama de *Feature/Interfaz Gráfica*, donde trabajaremos ahora. Añadimos la ventana de la calculadora.
3. Agregamos los botones, la división entre parte estándar y científica y las funciones de copiar, cortar y pegar.
4. Cambiamos los botones de 2π y γ por potencia y cociente, dado que son las funciones que queremos implementar. Con esto queda lista la interfaz gráfica, por lo que realizamos una pull request para aplicar los cambios a la rama de *develop*.
5. Aquí cometimos un error y hicimos el merge desde la rama *develop* hacia la rama *main* sin pasar por la rama *release*. Corregimos este error inmediatamente creando la rama *release* y siguiendo el flujo de trabajo de manera correcta, por lo que realizamos la etiquetación de `v1.0`.
6. Creamando la rama *Feature/Operaciones Básicas*, donde trabajaremos ahora. Empezamos a implementar las operaciones básicas de la calculadora, pero se realiza un conflicto de merge. Esto se debe a que en el archivo `operaciones_basicas.py`, Nicolás define la clase `Calc`, la cual contiene las funciones de las operaciones básicas, mientras que Victoria la importa desde el archivo `Interfaz_grafica.py`. El equipo decide aplicar los cambios que Victoria realizó, dado que...
7. Implementamos las operaciones básicas (suma, resta, división y multiplicación) respetando el flujo de trabajo, es decir, se crea una rama *Feature* para cada operación y luego se realiza el merge con la rama develop.
8. Con el fin de no generar errores en el código, llegamos al acuerdo de que solo se trabajará con el archivo `interfaz_grafica.py`, el cual renombramos a `main.py`.
9. Implementamos las operaciones trigonometricas  números π y e respetando el flujo de trabajo, es decir, se crea una rama *Feature* para cada operación y luego se realiza el merge con la rama develop. con esto implementado, realizamos la etiquetación de `v2.0`.
10. Luego de la creación de la version `v2.0`, nos percatamos de un hotfix, el cual se produjo con la implementacion de la funcionalidad del boton ^, por lo que se soluciona y da paso a la version `v2.1`
11. Se continua con la implementacion de las funcionalidades de los botones exp y log por parte de Nicolas, mientras que Victoria implementa las funciones de asinh y acosh, pero todas estas se guardan en la rama de *feature/acosh_and_asinh*, generando un conflicto,, el cual se soluciona al realizar la pull request de dicha rama hacia *develop* y combinando ambos codigos.

---

# Conflictos de Merge
* Conflicto en el paso 5:
![](/images/Captura%20de%20pantalla%202023-11-08%20a%20la(s)%2021.15.50.png)
![](/images/Captura%20de%20pantalla%202023-11-08%20a%20la(s)%2021.18.48.png)

* Conflicto paso 11:
![](/images/Captura%20de%20pantalla%202023-11-08%20a%20la(s)%2023.17.00.png)


