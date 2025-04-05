# Laboratorio 2 - Setup para proyectos de señales
Este es un tutorial para usar Git y Github.
Veremos como crear un entorno virtual para mantener tu proyecto organizado con todas sus dependencias y posteriormente simular señales fisiológicas.


## Crear un entorno en GitBash

### Configuración inicial
```bash
# Inicializar repositorio Git
git init

# Configurar usuario (solo primera vez)
git config --global user.name "TuNombre"
git config --global user.email "tu@email.com"
```

1.	Abrimos Git Bash y navegamos hasta la carpeta donde deseamos crear el repositorio.

![nuevo repositorio](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imágenes/github1.png)

2. Verificamos que Python esté instalado en el sistema y, a continuación, procedemos a crear el entorno virtual.
3. Podemos activar y desactivar el entorno según sea necesario
![opciones repositorio](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%201%20-%20Git%20y%20Github/Imágenes/github2.png)

4. Instalamos las librerías requeridas para el proyecto dentro del entorno recién creado.
5. Verificamos las librerías y dependencias que se han instalado correctamente durante el proceso.
6. Guardamos la lista de dependencias instaladas en un archivo .txt, el cual se almacenará en la ubicación del entorno virtual. Esto puede ser útil para reusar las mismas dependencias en el futuro.
7. ¡Listo! Ya tenemos el entorno con todas sus dependencias instaladas. Ahora podemos agregar el archivo requirements.txt a nuestro repositorio de GitHub, lo que permitirá que otros colaboradores reproduzcan el entorno fácilmente.
   
## Simular señales fisiológicas artificiales

1. Si aún no tenemos las dependencias necesarias, podemos utilizar el archivo requirements.txt para instalarlas en nuestro entorno local. Simplemente ejecutamos el siguiente comando:
```bash
# Instalar dependencias 
pip install -r requirements.txt
```
2. Loading...
