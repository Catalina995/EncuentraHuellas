# EncuentraHuellas

**Aplicación web para la publicación y búsqueda de mascotas perdidas y encontradas.**

EncuentraHuellas es un proyecto académico desarrollado con Python y Django. Su objetivo es facilitar la difusión de avisos de mascotas perdidas y encontradas, permitiendo que las personas compartan información que contribuya al reencuentro de los animales con sus familias.

La aplicación incorpora autenticación de usuarios, operaciones CRUD, administración mediante Django Admin y conexión a una base de datos PostgreSQL alojada en Supabase.

## Funcionalidades

### Consulta y búsqueda de mascotas

- Visualización de avisos recientes.
- Listado de mascotas perdidas, encontradas y reunidas.
- Búsqueda por nombre, comuna, sector y descripción.
- Filtros por especie y estado.
- Vista detallada de cada publicación.

### Gestión de usuarios

- Registro e inicio de sesión.
- Cierre de sesión.
- Protección de páginas que requieren autenticación.
- Control de acceso a las publicaciones de cada usuario.

### Gestión de avisos (CRUD)

Los usuarios registrados pueden:

- Crear avisos con información y fotografías.
- Consultar sus publicaciones desde la sección **Mis avisos**.
- Editar y eliminar sus propios avisos.
- Marcar mascotas como reunidas con sus familias.

El sistema incorpora validaciones para impedir fechas futuras y comprobar el formato de los datos de contacto.

### Panel administrativo

Se utiliza Django Admin para gestionar los registros del sistema.

El panel incorpora:

- Listado personalizado de avisos.
- Filtros por estado, especie, sexo y comuna.
- Búsqueda de publicaciones y usuarios.
- Ordenamiento por fecha de publicación.
- Campos de solo lectura.

### Interfaz

- Diseño responsivo.
- Formularios de registro e inicio de sesión.
- Navegación mediante menú de usuario.
- Visualización de fotografías y detalles de las mascotas.

## Tecnologías utilizadas

- Python 3.12
- Django
- HTML y CSS
- JavaScript
- PostgreSQL
- Supabase
- Pillow
- Git y GitHub

## Arquitectura

El proyecto utiliza la arquitectura MTV de Django:

- **Modelo:** estructura de los datos y relaciones con PostgreSQL.
- **Vista:** procesamiento de solicitudes y lógica de la aplicación.
- **Plantilla:** presentación de la interfaz mediante HTML.

La información de usuarios y avisos se almacena en PostgreSQL mediante Supabase.

Actualmente, las fotografías se almacenan localmente en la carpeta `media/`.

## Instalación y ejecución

Para ejecutar el proyecto es necesario disponer de Python, Git, conexión a Internet y las credenciales correspondientes a la base de datos.

Clonar el repositorio:

```bash
git clone https://github.com/Catalina995/EncuentraHuellas.git
cd EncuentraHuellas
```

Crear y activar el entorno virtual en Windows:

```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

Configurar el archivo `.env` con las variables de conexión a PostgreSQL.

Comprobar la configuración y las migraciones:

```powershell
python manage.py check
python manage.py showmigrations
```

Iniciar el servidor:

```powershell
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

**Importante:** las credenciales de la base de datos no se incluyen en este repositorio.

Para conocer el procedimiento completo de instalación, configuración y evaluación, consultar el archivo:

`MANUAL_INSTALACION_Y_USO_ENCUENTRAHUELLAS.txt`

## Limitaciones y mejoras futuras

Actualmente, las fotografías se almacenan de forma local, por lo que no se transfieren automáticamente al descargar el repositorio.

Como mejora futura se contempla implementar Supabase Storage para almacenar las imágenes en la nube y desplegar la aplicación en un servicio de hosting.

## Uso de inteligencia artificial

Durante el desarrollo del proyecto se utilizó Codex como herramienta de apoyo para:

- Proponer y mejorar aspectos de la interfaz visual.
- Apoyar la implementación y modificación del código.
- Identificar y corregir errores.
- Proponer mejoras en la estructura y organización del proyecto.
- Apoyar la implementación y revisión de funcionalidades.

Las sugerencias generadas fueron revisadas, adaptadas y validadas antes de incorporarlas al proyecto.

## Autora

**Catalina Manríquez**

Proyecto académico desarrollado con fines educativos.