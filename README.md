# Proyecto Final Coder House - Python
#### Comisión: 55630
#### Alumno: Figliozzi Justo

## Nombre del Proyecto
Gestión de Red Tecnica de Operación 

## Descripción del Proyecto
Esta página web tiene como proposito gestionar las direcciones IP de los distintos tipos de equipos que se pueden encontrar en la Red Tecnica de Operación de una Estación Transformadora de alta tensión. 

A fin de navegar por algunas secciones de la página web, el usuario será requerido iniciar sesión o registrarse en caso de no contar con usuario o contraseña. En ambas opciones, una vez la página valide la autenticación del usuario, este será redirigido al inicio de la página web.

Los usuarios NO registrados podrán realizar las siguientes accciones:
- Crear una cuenta de usuario
- Iniciar sesión en una cuenta ya registrada
- Visualizar las Estaciones Transformadoras que se encuentran registradas en la Base de Datos (no asi los equipos que estan asociados a ella)

Los usuarios registrados podrán realizar las siguientes accciones:
- Visualizar, crear, editar y eliminar Estaciones Transformadoras (Estaciones Transformadoras: Ver EETT)
- Visualizar los equipos que estan asociados a cada Estacion Transformadora (Sección "Estaciones Transformadoras": Ver        EETT>Ver Detalles)
- Visualizar, crear, editar y eliminar equipos de Red (Sección "Equipos": Red>ver)
- Visualizar, crear, editar y eliminar equipos de Telecontrol (Sección "Equipos": Telecontrol>ver)
- Visualizar, crear, editar y eliminar equipos de Protección (Sección "Equipos": Protección>ver)
- Editar información del usuario (Sección "Configuracion de cuenta": Nombre, apellido y contraseña)
- Modificar Avatar del usuario (Sección "Avatar": se podra cargar un archivo seleccionado)
- Utilizar la barra de busqueda donde se filtraran los resultados de Equipos que conicidan con el patron de busqueda
- Cerrar sesión

## Aclaración
La base de datos solo se encuentra con equipos cargados para la Estacion Vivoratá.

## Tecnología Utilizada

##### Front-End
- HTML 5
- CSS 3
- Javascript
- Bootstrap

##### Back-End
- Python 3.10.4
- Django 4.0

