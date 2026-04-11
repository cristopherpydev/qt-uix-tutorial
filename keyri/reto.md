# Reto

Hemos visto como instanciar ventanas y pasar datos a través de ellas. ¿Podrías implementar las siguientes mejoras al programa?

## Fácil

Actualmente tenemos usuarios que están hardcodeados en nuestro registro csv de usuarios. No tenemos la posibilidad de añadir nuevos usuarios cuando el sistema no reconoce a un usuario. 
Si pasa todas las validaciones pertinentes, el sistema debería o bien preguntar al usuario (investigar cuadros de diálogo) si quiere crear una nueva cuenta, o crearla directamente.

## Intermedio 

Tenemos que crear un nuevo apartado (ventana) que nos permita básicamente introducir nuevas cuentas con sus respectivos campos y contraseña.
El sistema debe validar que:
1. Cada campo debe estar cumplimentado y sin caracteres vacíos.
2. Los campos, evidentemente, pertenecen al usuario que está loggeado en el sistema.

Al finalizar, y si todo va bien, la ventana se debe cerrar y se debe actualizar la tabla que muestra todas las cuentas con los datos privados del usuario loggeado.

## Difícil

El sistema es muy vulnerable a espionaje digital y hackeos. Podemos implementar una mejora en cuanto a la seguridad de nuestros datos mediante la aplicación de diversas técnicas de migración de datos y hasheo de la información.
Tenemos varias opciones:
1. Migrar todos los datos a un sistema de stream binario (pickle es un módulo que nos puede ayudar). No mejora la seguridad lógica, pero si mejora la integridad de datos a nivel de lectura visual por un tercero malintencionado.
2. Hashear los datos y crear métodos que encripten y desencripten los datos. Python ofrece módulos para ello. Deberemos refactorizar la aplicación, pudiendo afectar incluso a la arquitectura de diseño.

---
## Enlaces de interés
---
1. [Seguridad con Python](https://cryptography.io/en/latest/)
2. [Tratamiento de datos: archivos binarios](https://www.datacamp.com/es/tutorial/pickle-python-tutorial)

 
