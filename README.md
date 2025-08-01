# Busqueda de Palabras en una Sopa de Letras

---

## 🚀 Objetivo del Proyecto

Desarrollar un servicio web que:

- Inserte palabras en una sopa de letras generada aleatoriamente.
- Permita al usuario enviar palabras y/o una matriz personalizada.
- Detecte las palabras en la matriz en todas las direcciones:
  - Horizontal 
  - Vertical 
  - Diagonal 

---

##  Recursos Utilizados

- **Generador de sopa de letras** que:
  - Inserta palabras en posiciones y direcciones aleatorias.
  - Asegura que no haya conflictos de letras.
  - Rellena automáticamente los espacios vacíos con letras aleatorias.
  
- **Buscador de palabras en matriz** que:
  - Recorre todas las celdas y direcciones.
  - Compara letra por letra respetando límites.
  
- Validación estricta para asegurar que la matriz tenga exactamente **14x14** posiciones.

---

##  Tecnologías Empleadas

| Tipo         | Tecnología                       |
|--------------|----------------------------------|
| Lenguaje     | Python 3.11                      |
| Framework    | FastAPI                          |
| Servidor     | Uvicorn                          |
| Librerías    | typing, random, string           |
| Formato de respuesta | JSON con estructura clara |

---

## 📦 Estructura del Proyecto

SOPA_DE_LETRAS/
├── app/
│ ├── main.py # Endpoint principal de FastAPI
│ ├── word_search.py # Lógica para buscar palabras y generacion de matriz
│ ├── utils.py # Validacion de la matriz
│ └── schemas.py # Tipos de datos que envia/recibe
├── requirements.txt # Lista de dependencias
└── README.md # Documentación 

---

## 📄 Requisitos Previos

- Python 3.10 o superior instalado.
- Git instalado (opcional para clonar el repositorio).

---

## ⚙️ Guía de Despliegue (Ejecutar localmente)

### 1. Clonar el repositorio 

```bash
git clone https://github.com/mateocar/Sopa_de_letras.git
cd Sopa_de_letras 
```
### 2. Crear entorno virtual

```bash
python -m venv env
```
### 3. Activar entorno virtual

En Windows:
    env\Scripts\activate

En macOS/Linux:
    source env/bin/activate
    
### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```
### 6. Abrir en el navegador

Ir a http://127.0.0.1:8000/docs para acceder a la interfaz Swagger y probar el endpoint interactivo.

##  Ejemplo de Uso

POST 
json
    {
    "palabras": ["gato", "perro", "jaguar"],
    "matriz": null
    }
Si no se incluye matriz, se genera una automáticamente y las palabras se insertan en ella.