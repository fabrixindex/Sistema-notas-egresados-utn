# 🎓 Segundo Parcial de Programación I

**Materia:** Programación I
**Carrera:** Tecnicatura Universitaria en Programación
**Universidad:** Universidad Tecnológica Nacional — Facultad Regional Avellaneda (UTN FRA)
**Alumno:** Fabricio Papetti
**División:** 314

---

# 📋 Descripción

Proyecto desarrollado para el **Segundo Parcial de Programación I**, dividido en dos partes independientes, cada una en su propia carpeta.

- **Parte 1**: sistema de gestión de notas escolares usando **matrices** y **archivos CSV**.
- **Parte 2**: sistema de gestión de egresados usando **listas de diccionarios** y **archivos JSON**.

Ambas partes aplican programación estructurada, funciones propias, validaciones y algoritmia de cadenas (sin métodos de `str`), evitando el uso de atajos de Python no vistos en clase.

---

# 🥇 Parte 1 — Matrices y archivos CSV

📁 Carpeta: `Parte 1/`

## 📌 Objetivo

Registrar las notas de 7 alumnos de Matemática a lo largo de 3 trimestres, representando la información en una **matriz**, con carga manual o desde un archivo `notas.csv`.

## ⚙️ Funcionalidades

El sistema presenta un menú con las siguientes opciones:

| Opción | Descripción |
|--------|-------------|
| 1 | **Cargar notas** — Permite elegir entre carga secuencial (7 alumnos x 3 trimestres) o carga desde archivo `notas.csv` |
| 2 | **Mostrar alumnos desaprobados** — Alumnos con al menos una nota menor a 7 |
| 3 | **Mostrar alumnos con aplazos** — Alumnos con al menos una nota menor a 4 |
| 4 | **Mostrar porcentajes** — Porcentaje de aprobados y desaprobados sobre el total |
| 5 | **Mejor trimestre** — Calcula el promedio de cada trimestre e indica cuál fue el mejor (contempla empates) |
| 6 | **Salir** — Si la carga fue manual, guarda la matriz en un CSV nuevo con la fecha del día como nombre |

### 📄 Funciones.py — Lógica y algoritmia

| Función | Descripción |
|---------|-------------|
| `quitar_salto_linea(cadena)` | Elimina manualmente los caracteres `\n` y `\r` de una línea leída de archivo |
| `separar_por_coma(cadena)` | Separa una cadena en una lista de subcadenas usando la coma, sin usar `.split()` |
| `es_entero_valido(cadena)` | Verifica carácter por carácter si una cadena representa un entero positivo |
| `texto_a_entero(cadena)` | Convierte una cadena de dígitos en su valor entero, sin usar `int()` sobre texto no validado |
| `entero_a_texto(numero)` | Convierte un entero no negativo en su representación de texto, dígito por dígito |
| `formatear_dos_digitos(numero)` | Da formato de dos cifras a un número (agrega cero a la izquierda si hace falta), usado para día y mes |
| `obtener_cantidad_columnas(matriz)` | Devuelve la cantidad de columnas de la matriz tomando el largo de la primera fila |
| `cargar_desde_csv(nombre_archivo)` | Lee el CSV línea por línea (sin el módulo `csv`), salta el encabezado y arma la matriz de notas |
| `mostrar_desaprobados(matriz)` | Recorre la matriz y muestra los alumnos con alguna nota menor a 7 |
| `mostrar_aplazos(matriz)` | Recorre la matriz y muestra los alumnos con alguna nota menor a 4 |
| `mostrar_porcentajes(matriz)` | Calcula y muestra el porcentaje de aprobados y desaprobados |
| `mostrar_mejor_trimestre(matriz)` | Calcula el promedio de cada trimestre y determina el/los mejores, contemplando empates |
| `obtener_fecha_actual()` | Obtiene la fecha del sistema y la formatea manualmente como `dd-mm-aaaa` |
| `guardar_csv(matriz)` | Guarda la matriz en un CSV nuevo dentro de `archivos_guardados/`, nombrado con la fecha actual |

### 📄 Inputs.py — Ingreso de datos

| Función | Descripción |
|---------|-------------|
| `pedir_nota(mensaje)` | Solicita una nota por teclado y repite el pedido hasta recibir un entero válido entre 1 y 10 |
| `cargar_secuencial()` | Pide por teclado las notas de los 7 alumnos en los 3 trimestres y arma la matriz |
| `pedir_nombre_archivo()` | Solicita el nombre del archivo CSV a leer |
| `pedir_opcion_menu()` | Solicita al usuario la opción elegida en el menú principal |
| `pedir_opcion_carga()` | Solicita al usuario el tipo de carga a realizar (secuencial o desde archivo) |

### 📄 Prints.py — Salida por consola

| Función | Descripción |
|---------|-------------|
| `imprimir_menu()` | Muestra las 6 opciones del menú principal |
| `imprimir_menu_carga()` | Muestra el submenú para elegir el tipo de carga (secuencial o CSV) |
| `imprimir_error_opcion()` | Informa que la opción ingresada no es válida |
| `imprimir_datos_no_cargados()` | Informa que hay que cargar los datos antes de usar esa opción |
| `imprimir_carga_exitosa()` | Confirma que la carga de datos fue exitosa |
| `imprimir_error_archivo()` | Informa que el archivo no existe o no pudo leerse |
| `imprimir_despedida()` | Muestra el mensaje de cierre del programa |

### 📄 Menu.py — Control del programa

| Función | Descripción |
|---------|-------------|
| `limpiar_consola()` | Limpia la pantalla según el sistema operativo (`cls` en Windows, `clear` en Linux/Mac) |
| `esperar_menu()` | Pausa la ejecución hasta que el usuario presione ENTER y luego limpia la consola |
| `mostrar_menu()` | Bucle principal: controla el flujo completo, bloquea las opciones 2-5 sin carga previa, y guarda el CSV solo si la carga fue manual |

### 📚 Conceptos aplicados

- Matrices y recorridos con doble `for`.
- Lectura y escritura de archivos CSV **sin el módulo `csv`** (lectura línea a línea y separación manual por coma).
- Algoritmia de cadenas propia (reemplazo, separación y unión de cadenas sin métodos de `str`).
- Validaciones de rango sin `try/except`.
- Bloqueo de menú hasta realizar la carga de datos.
- Modularización (`Funciones.py`, `Inputs.py`, `Prints.py`, `Menu.py`, `Main.py`).

### 📁 Estructura

```text
📦 Parte 1
 ┣ 📄 Main.py
 ┣ 📄 Menu.py
 ┣ 📄 Funciones.py
 ┣ 📄 Inputs.py
 ┣ 📄 Prints.py
 ┗ 📄 notas.csv
```

### ▶️ Ejecución

```bash
cd "Parte 1"
python Main.py
```

---

# 🥈 Parte 2 — Egresados UTN FRA (JSON y listas de diccionarios)

📁 Carpeta: `Parte 2/`

## 📌 Objetivo

Gestionar información de los egresados de la Tecnicatura Universitaria en Programación, representando cada alumno como un diccionario (`legajo`, `nombre`, `apellido`, `egreso`, `plan`, `nota_promedio`) dentro de una lista, con persistencia en un archivo `alumnos.json`.

## ⚙️ Funcionalidades

El sistema presenta un menú con las siguientes opciones:

| Opción | Descripción |
|--------|-------------|
| 1 | **Cargar alumnos** — Permite elegir entre carga desde archivo `alumnos.json` o carga manual (con legajo aleatorio y confirmación) |
| 2 | **Mostrar egresados por plan** — Filtra y muestra los alumnos de un plan de estudios (1991/2003/2024) |
| 3 | **Egresados anteriores al año 2000** — Muestra los alumnos egresados antes del 2000 y su promedio general |
| 4 | **Buscar alumno** — Búsqueda parcial por nombre o apellido, sin distinguir mayúsculas/minúsculas |
| 5 | **Salón de la fama** — Alumnos con promedio ≥ 9, ordenados de mayor a menor |
| 6 | **Salir** — Guarda la lista actualizada de alumnos en `alumnos.json` antes de cerrar |

### 📄 Funciones.py — Lógica y algoritmia

| Función | Descripción |
|---------|-------------|
| `legajo_existe(alumnos, legajo)` | Recorre la lista de alumnos y verifica si un legajo ya fue asignado |
| `generar_legajo(alumnos)` | Genera un legajo aleatorio de 6 cifras, repitiendo el sorteo hasta que sea único |
| `es_letra(caracter)` | Verifica si un caracter es una letra (mayúscula, minúscula) o un espacio, sin `isalpha()` |
| `validar_nombre(cadena)` | Valida que un nombre o apellido tenga al menos 3 caracteres y solo contenga letras y espacios |
| `a_minuscula(cadena)` | Convierte una cadena a minúsculas manualmente, sin usar `.lower()` |
| `contiene_subcadena(cadena_grande, subcadena)` | Busca una subcadena dentro de otra con ventana deslizante, sin distinguir mayúsculas/minúsculas y sin usar `in` ni `.find()` |
| `calcular_suma(lista_numeros)` | Suma todos los valores de una lista sin usar `sum()` |
| `calcular_promedio(lista_numeros)` | Calcula el promedio de una lista de números, reutilizando `calcular_suma()` |
| `calcular_promedio_alumnos(lista_alumnos)` | Extrae las notas promedio de una lista de alumnos y calcula el promedio general, reutilizando `calcular_promedio()` |
| `intercambiar_valores(lista, izq, der)` | Intercambia dos elementos de una lista usando una variable auxiliar |
| `ordenar_por_promedio_desc(alumnos)` | Ordena una copia de la lista de alumnos de mayor a menor por `nota_promedio`, usando el algoritmo de selección adaptado a diccionarios |
| `filtrar_por_plan(alumnos, plan)` | Devuelve los alumnos que pertenecen a un plan de estudios determinado |
| `filtrar_anteriores_2000(alumnos)` | Devuelve los alumnos egresados antes del año 2000 |
| `buscar_por_nombre_o_apellido(alumnos, texto)` | Busca alumnos cuyo nombre o apellido contenga el texto ingresado, reutilizando `contiene_subcadena()` |
| `filtrar_salon_fama(alumnos)` | Filtra los alumnos con promedio ≥ 9 y los ordena de mayor a menor, reutilizando `ordenar_por_promedio_desc()` |

### 📄 Inputs.py — Ingreso de datos

| Función | Descripción |
|---------|-------------|
| `es_entero_valido(cadena)` | Verifica carácter por carácter si una cadena representa un número entero (admite signo negativo) |
| `es_flotante_valido(cadena)` | Verifica carácter por carácter si una cadena representa un número decimal válido (un único punto) |
| `pedir_entero(mensaje, minimo, maximo)` | Solicita un entero por teclado, validando formato y rango, repitiendo hasta que sea correcto |
| `pedir_flotante(mensaje, minimo, maximo)` | Solicita un decimal por teclado, validando formato y rango, repitiendo hasta que sea correcto |
| `pedir_nombre_apellido(mensaje)` | Solicita un nombre o apellido válido, reutilizando `Funciones.validar_nombre()` |
| `pedir_plan()` | Solicita al usuario un plan de estudios válido (1991, 2003 o 2024) |
| `pedir_confirmacion(mensaje)` | Solicita una confirmación (s/n) y la devuelve como booleano |
| `pedir_texto_busqueda(mensaje)` | Solicita un texto de búsqueda de al menos 3 letras, reutilizando `Funciones.validar_nombre()` |

### 📄 Archivos.py — Persistencia en JSON

| Función | Descripción |
|---------|-------------|
| `cargar_json(nombre_archivo)` | Lee un archivo JSON y devuelve la lista de diccionarios de alumnos, o informa error si el archivo no existe |
| `guardar_json(alumnos, nombre_archivo)` | Serializa la lista de alumnos y la guarda en un archivo JSON, sobreescribiendo el anterior |

### 📄 Prints.py — Salida por consola

| Función | Descripción |
|---------|-------------|
| `mostrar_menu()` | Muestra las 6 opciones del menú principal con formato de encabezado |
| `mostrar_alumno(alumno)` | Muestra los datos de un alumno individual (legajo, nombre, apellido, egreso, plan, promedio) en formato de tarjeta |
| `mostrar_lista_alumnos(lista_alumnos)` | Muestra todos los alumnos de una lista, o avisa si está vacía, reutilizando `mostrar_alumno()` |
| `mostrar_mensaje(mensaje)` | Muestra un mensaje genérico con formato de encabezado |

### 📄 Menu.py — Control del programa

| Función | Descripción |
|---------|-------------|
| `limpiar_consola()` | Limpia la pantalla según el sistema operativo (`cls` en Windows, `clear` en Linux/Mac) |
| `esperar_menu()` | Pausa la ejecución hasta que el usuario presione ENTER y luego limpia la consola |
| `menu_principal()` | Bucle principal: gestiona la carga de alumnos, bloquea las opciones 2-5 sin datos cargados, deriva cada opción a las funciones de `Funciones.py`, y guarda el JSON al salir |

### 📚 Conceptos aplicados

- Listas de diccionarios como estructura principal.
- Serialización y deserialización con `json.dump()` / `json.load()`.
- Algoritmia de cadenas propia (sin métodos de `str`) para validar nombres/apellidos y hacer búsquedas parciales.
- Algoritmo de ordenamiento por selección adaptado a listas de diccionarios (reutilizado en el Salón de la Fama).
- Generación de legajos aleatorios únicos.
- Bloqueo de menú hasta realizar la carga de datos.
- Sin `list comprehension`, sin operadores ternarios, sin `try/except`, sin `max()/min()/sum()`.
- Separación total en módulos especializados.

### 📁 Estructura

```text
📦 Parte 2
 ┣ 📄 Main.py
 ┣ 📄 Menu.py
 ┣ 📄 Funciones.py
 ┣ 📄 Inputs.py
 ┣ 📄 Prints.py
 ┣ 📄 Archivos.py
 ┗ 📄 alumnos.json
```

### 🗂️ Módulos

| Módulo | Responsabilidad |
|---|---|
| `Main.py` | Punto de entrada del programa (casi vacío, solo invoca el menú). |
| `Menu.py` | Menú principal y lógica de control del programa. |
| `Funciones.py` | Lógica de resolución del problema (filtros, búsquedas, ordenamiento, legajo). |
| `Inputs.py` | Validación e ingreso de datos por teclado. |
| `Prints.py` | Salida de datos por consola. |
| `Archivos.py` | Lectura y escritura del archivo `alumnos.json`. |

### ▶️ Ejecución

```bash
cd "Parte 2"
python Main.py
```

---

# 👨‍💻 Tecnologías utilizadas

- Python 3.10+
- JSON
- CSV (algoritmia propia, sin el módulo `csv`)
- Visual Studio Code
- Git / GitHub

---

# 🎥 Video de defensa

En el siguiente video se muestra el funcionamiento completo de ambas partes del sistema, con la explicación de las funciones desarrolladas.

> *(Agregar enlace de YouTube o Google Drive)*

---

# 📖 Conceptos generales trabajados

- Programación estructurada.
- Funciones propias y reutilizables.
- Modularización y separación de responsabilidades.
- Validación de datos sin excepciones.
- Matrices, listas y diccionarios.
- Algoritmia de cadenas (sin métodos de `str`).
- Persistencia de datos (CSV y JSON).
- Documentación mediante docstrings.