# Laboratorio1 - Git y Github

# 🧠 Mini Tutorial de Git

Este mini tutorial explica los comandos más usados de **Git**, el sistema de control de versiones que se usa localmente.

---

## 🛠️ Configuración Inicial

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

---

## 📁 Crear un Repositorio

```bash
git init
```
Inicializa un nuevo repositorio en el directorio actual.

---

## 📄 Seguimiento de Archivos

```bash
git status
```
Muestra el estado actual del repositorio.

```bash
git add nombre-archivo
git add .
```
Agrega archivos al área de staging.

```bash
git commit -m "Mensaje descriptivo"
```
Guarda los cambios en el historial del repositorio.

---

## 🌿 Ramas

```bash
git branch nombre-rama
```
Crea una nueva rama.

```bash
git checkout nombre-rama
```
Cambia de rama.

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
git diff
```
Muestra las diferencias entre archivos modificados.

```bash
git rm nombre-archivo
```
Elimina un archivo del repo y lo marca para commit.

---

## 📚 Consejos

- Usa `git status` frecuentemente para estar al tanto del estado del repo.
- Realiza commits pequeños y con mensajes claros.
- Usa ramas para trabajar de forma organizada.

---

## 📌 Recursos útiles

- [Documentación oficial de Git](https://git-scm.com/doc)
- [Guía rápida (Git Cheat Sheet)](https://education.github.com/git-cheat-sheet-education.pdf)

# 🌐 Mini Tutorial de GitHub (plataforma en la nube)

Este tutorial resume cómo usar **GitHub**, la plataforma en línea para alojar y colaborar en repositorios Git.

---

## 📝 Crear un Repositorio en GitHub

1. Entra a [github.com](https://github.com).
2. Haz clic en "New Repository".
3. Asigna un nombre, descripción y elige si será público o privado.
4. Opcional: agrega README, .gitignore o licencia.

---

## 🔗 Clonar un Repositorio desde GitHub

```bash
git clone https://github.com/usuario/repositorio.git
```

---

## 🚀 Subir tu Proyecto Local a GitHub

1. Crea el repo en GitHub (vacío).
2. Desde tu terminal:

```bash
git remote add origin https://github.com/usuario/repositorio.git
git branch -M main
git push -u origin main
```

---

## 🔄 Colaboración

- **Pull Requests**: Sirven para proponer cambios al código.
- **Issues**: Para reportar errores o sugerir mejoras.
- **Fork**: Clonar un repo para trabajar de forma independiente.

---

## 📂 Archivos importantes en GitHub

- `README.md`: Describe el proyecto (se ve al inicio).
- `.gitignore`: Lista de archivos que Git no debe trackear.
- `LICENSE`: Licencia del proyecto.

---

## 👥 GitHub Flow (flujo típico)

1. Clona el repo.
2. Crea una rama: `git checkout -b nueva-funcionalidad`
3. Haz cambios, commits.
4. Sube la rama: `git push origin nueva-funcionalidad`
5. Abre un Pull Request en GitHub.
6. Revisión y merge.

---

## 📚 Recursos

- [Documentación oficial de GitHub](https://docs.github.com/)
- [GitHub Campus](https://education.github.com/)

