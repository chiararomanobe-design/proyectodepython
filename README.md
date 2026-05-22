# Blog con Django

Este proyecto es una aplicacion web tipo blog desarrollada en Python y Django como proyecto final.

La aplicacion permite que los usuarios puedan registrarse, iniciar sesion, crear y eliminar publicaciones, visualizar posteos de otros usuarios, editar su perfil y enviar mensajes mediante un formulario de contacto.

El objetivo del proyecto es aplicar conceptos basicos de desarrollo web con Django, incluyendo modelos, vistas, templates, formularios, autenticacion, panel de administracion y base de datos.

## Funcionalidades principales

- Pagina principal con listado de posteos.
- Creacion de posteos para usuarios registrados.
- Visualizacion publica de posteos.
- Eliminacion de posteos propios.
- Registro de usuarios.
- Inicio y cierre de sesion.
- Perfil de usuario editable.
- Formulario de contacto con validacion.
- Pagina "Acerca de".
- Panel de administracion de Django.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- CSS

## Instalacion y ejecucion local

1. Clonar el repositorio:

```bash
git clone https://github.com/chiararomanobe-design/proyectodepython
cd proyectodepython
```

2. Crear y activar un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:

```bash
python manage.py migrate
```

5. Crear superusuario:

```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor:

```bash
python manage.py runserver
```

7. Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Panel de administracion

El panel de administracion se encuentra en:

```text
http://127.0.0.1:8000/admin/
```

Desde ahi se pueden gestionar usuarios y posteos.

## URL publica

El proyecto actualmente se ejecuta de forma local en:

```text
http://127.0.0.1:8000/
```

El despliegue publico queda pendiente para una etapa final. Puede realizarse utilizando servicios como Render, Railway o PythonAnywhere.
Y agregá:

```md
## Despliegue

El despliegue se realizo en PythonAnywhere utilizando:
- Repositorio de GitHub.
- Entorno virtual.
- Archivo requirements.txt.
- Configuracion WSGI.
- Migraciones de Django.


## Repositorio

El codigo fuente se encuentra disponible en GitHub:

```text
https://github.com/chiararomanobe-design/proyectodepython
```

## Autor

Proyecto realizado como entrega final del curso de Python y Django.
