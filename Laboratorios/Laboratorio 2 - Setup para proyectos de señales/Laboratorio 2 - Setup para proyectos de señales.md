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

![abrir git bash](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen1.png)

2. Verificamos que Python esté instalado en el sistema y, a continuación, procedemos a crear el entorno virtual.
   ![python](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen2.png)
3. Podemos activar y desactivar el entorno según sea necesario
   ![entorno1](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen3.png)
   ![entorno2](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen4.png)
4. Instalamos las librerías requeridas para el proyecto dentro del entorno recién creado.
   ![entorno3](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen5.png)
5. Verificamos las librerías y dependencias que se han instalado correctamente durante el proceso.
   ![entorno4](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen6.png)
6. Guardamos la lista de dependencias instaladas en un archivo .txt, el cual se almacenará en la ubicación del entorno virtual. Esto puede ser útil para reusar las mismas dependencias en el futuro.
   ![entorno5](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen7.png)
   ![entorno6](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen8.png)
7. ¡Listo! Ya tenemos el entorno con todas sus dependencias instaladas. Ahora podemos agregar el archivo requirements.txt a nuestro repositorio de GitHub, lo que permitirá que otros colaboradores reproduzcan el entorno fácilmente.
   
## Simular señales fisiológicas artificiales

1. Si aún no tenemos las dependencias necesarias, podemos utilizar el archivo requirements.txt para instalarlas en nuestro entorno local. Simplemente ejecutamos el siguiente comando:
```bash
# Instalar dependencias 
pip install -r requirements.txt
```
2. Loading...
