## Run Server
Para rodar o sistema é necessario rodar o comando `docker-compose up -d`

## Atualizar o ambiente é necessario
`docker-compose build` e o `docker-compose up -d`

## Environments
Este arquivo Compose contém as seguintes variáveis de ambiente:

* `POSTGRES_USER` o valor padrão é **postgres**
* `POSTGRES_PASSWORD` o valor padrão é **changeme**
* `PGADMIN_PORT` o valor padrão é **5050**
* `PGADMIN_DEFAULT_EMAIL` o valor padrão é **pgadmin4@pgadmin.org**
* `PGADMIN_DEFAULT_PASSWORD` o valor padrão é **admin**

## Acesso ao Servidor Web: 
* Host `localhost`

## Acesso ao postgres: 
* `localhost:5432`
* **Username:** postgres (como padrão)
* **Password:** changeme (como padrão)

## Acesso ao PgAdmin: 
* **URL:** `http://localhost:5050`
* **Username:** pgadmin4@pgadmin.org (como padrão)
* **Password:** admin (como padrão)

## Adicionar um novo servidor no PgAdmin:
* **Host name/address** `postgres`
* **Port** `5432`
* **Username** as `POSTGRES_USER`, como padrão: `postgres`
* **Password** as `POSTGRES_PASSWORD`, como padrão `changeme`
