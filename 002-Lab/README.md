# SEGUNDO LABORATORIO
Pruebas para segundo laboratorio

### Setear Credenciales GIT
```bash
git config --global user.name "<Your-Full-Name>"
git config --global user.email "<your-email-address>"
```

### Creando un repositorio

```shell
cd repo1
touch README.md
git init
git add README.md
git commit -m "Cargando archivos"
git push -u origin master
git remote add origin http://github.com/<usser>/repo1.git
#*Se crea el repositorio con el archivo README.md
```

### Clonando un repositorio

```sh
git clone http://github.com/<usser>/repo1.git
```

### Creando una rama

```sh
#Primero actualizamos la rama para que todos los cambios vayan a la nueva rama
git pull
#Creamos la rama nueva
git checkout -b feature/branch_name
#Podemos ver nuestra rama actual con el siguiente comando
git branch
```

### Para movernos entre ramos usamos

```sh
git checkout <mi_rama>
```

### Agregando archivos o carpetas a nuestra rama

```sh
#Despues de agregar nuestras ramas a nuestra carpeta de la repo
#Procedemos a evaluar el estado de los archivos
git status
#Podemos ver nuestra rama actual con el siguiente comando
git branch
#Agregamos los archivos a la repo con un comentario
git add .
git commit -m "Upload files"
#Subimos los cambios a la repo, ya que los cambios estan localmente de momento
#Ejemplos:
#git push origin master
#git push origin develop
git push origin <feature/branch_name>
```

### Fusionar una rama a las ramas principales (main, master, develop)

```sh
#Primero nos posicionamos en nuestra rama princial (main, master, develop)
#Para cambiarnos de rama utilizamos
git checkout develop
#Verificamos en que rama estamos
git branch
#Actualizamos la rama principal
git pull
#Fusionamos nuestra rama
git merge --no-ff mi_rama
#Aplicamos los cambios a la repo principal
git push origin develop


###NOTA: En estos pasos es comun cuando se trabaja en equipo que existan conflictos que debamos solucionar.
```