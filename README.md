# Simple api GET docker

Se trata de una simple api que permite arrancar y parar contenedores mediante llamadas GET sobre la api.
He creado esta aplicación para que permita manejar los contenedores de mis servidores locales y raspberry a partir de las startPages me mediante peticiones get con javascript.

Esta es un ejemplo de una pagina para consumir esta api :

tiene dos puntos de acceso:

 - **list** crear una lista de los contenedores existentes con las opciones básicas de las start page:

 - **toggle/<container_name>** cambia de estado, arranca o parar el servicio docker que coincide con el nombre

Para correr este servicio

    docker run -p 5000:5000 manologcode/apidocker

y accediendo al navegador 

    http://localhost:5000/list

Con docker compose

    version: '3.1'

    services:
    apidocker:
        image: manologcode/apidocker
        restart: always
        container_name: apidocker
        ports:
        - "8888:5000"
        volumes:
        - /var/run/docker.sock:/var/run/docker.sock

