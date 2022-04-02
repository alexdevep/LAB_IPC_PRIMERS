# Framework Flask
> Pueden utilizar tanto el framework Flask o Django para su desarrollo ambos tienen sus ventajas y desventajas.

### Instalar flask globlamente

> Se puede tambien en entornos virtuales, pero en este caso ser global.

```
pip install flask
flask --version
```

### Para ejecutar nuestro archivo en entorno de produccion

> En este modo siempre tenemos que reiniciar nuestra aplicacion si se hacen cambios.
```
#Esta linea no debe marcar ningun error
export FLASK_APP=app.py

#Este comando genera los binarios y ejecutables de nuestra aplicacion
python3 -m flask run #Linux
python -m flask run #Windows y Mac
```

### Para ejecutar nuestro archivo en entorno de desarrollo

> En este modo nuestra aplicacion se reinicia automaticamente al detectar cambios.
> Nota: No me funciono este metodo :(
```
#Esta linea no debe marcar ningun error
export FLASK_ENV=development

#Este ejecuta nuestra aplicacion 
flask run
```

> Tambien podemos hacer uso del entorno de desarrollo agrendo el siguiente codigo a nuestro archivo principal y ejecutando un comando diferente.

```python
if __name__ == '__main__':
    app.run(debug=True)

# Para ejecutar nuestra app usamos
# python3 app.py
```
