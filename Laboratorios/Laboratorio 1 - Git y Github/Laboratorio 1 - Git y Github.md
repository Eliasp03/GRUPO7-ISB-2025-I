# Laboratorio1 - Git y Github

# 🧠 Mini Tutorial de Git y GitHub

Este mini tutorial resume los comandos más comunes usados en Git y GitHub para trabajar con repositorios.

---

## 🔧 Configuración Inicial

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

Configura tu nombre y correo para los commits.

---

## 📁 Crear o Clonar un Repositorio

```bash
git init
```
Inicializa un nuevo repositorio en el directorio actual.

```bash
git clone https://github.com/usuario/repositorio.git
```
Clona un repositorio remoto a tu máquina local.

---

## 📌 Estados y Cambios

```bash
git status
```
Muestra los archivos modificados y pendientes por añadir.

```bash
git add nombre-archivo
git add .
```
Agrega archivos al área de staging (preparados para commit). `.` agrega todos.

```bash
git commit -m "Mensaje descriptivo"
```
Guarda los cambios con un mensaje.

---

## 🔄 Sincronización con Repositorio Remoto

```bash
git push origin main
```
Sube los commits locales a GitHub (rama principal).

```bash
git pull origin main
```
Descarga y fusiona cambios del repositorio remoto.

---

## 🌿 Trabajo con Ramas

```bash
git branch nombre-rama
```
Crea una nueva rama.

```bash
git checkout nombre-rama
```
Cambia a otra rama.

```bash
git merge nombre-rama
```
Fusiona una rama a la actual.

---

## 🧽 Otros útiles

```bash
git log
```
Muestra el historial de commits.

```bash
git remote -v
```
Muestra los repositorios remotos conectados.

```bash
git rm nombre-archivo
```
Elimina un archivo del repo y lo marca para commit.

---

## 📚 Consejos

- Usa commits frecuentes con mensajes claros.
- Siempre haz `git pull` antes de `git push` para evitar conflictos.
- Crea ramas para cada funcionalidad o tarea nueva.

---

## 📌 Recursos útiles

- [Guía de GitHub (oficial)](https://docs.github.com/en/get-started)
- [Git - La guía sencilla (en español)](https://rogerdudler.github.io/git-guide/index.es.html)
- [Cheat Sheet Git](https://education.github.com/git-cheat-sheet-education.pdf)
