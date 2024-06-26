# Phone Subscribers By Category

Example to show case how to orchestrate a dbt project to create independent schemas with the same models using dbt variables.

## How to use it?

First run this command to spin up all the required services:

``` sh
docker compose up --build
```

1. Navigate <http://localhost:3000/>
2. Go to assets, and check available models
3. Materialize assets selecting providers as partitions

## Datasets

- [Datos abiertos Colombia - Telefonía Móvil abonados por categoría](<https://www.datos.gov.co/Ciencia-Tecnolog-a-e-Innovaci-n/Telefon-a-M-vil-abonados-por-categor-a/nrst-mwx4>)

## License

[MIT](https://choosealicense.com/licenses/mit/)
