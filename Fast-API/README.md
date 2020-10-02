# Fast API

Es un framework moderno y de alto rendimiento para armar APIs en Python 3.6+

Documentacion [aqui](https://github.com/tiangolo/fastapi)

## Comandos

````
uvicorn main:app --reload
````

- **uvicorn** Es el servicio

- **Main** Es el nombre del archivo python [Variable]

- **App** Es el nombre de la funcion [Variable]

- **-reload** Refresca automaticamente el servicio con cada cambio

### Outputs

Se puede utilizar el preferido

**Swagger -UI**

````
http://127.0.0.1:8000/docs
````

**ReDoc**

````
http://127.0.0.1:8000/redoc
````