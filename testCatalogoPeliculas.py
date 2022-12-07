from dominio.pelicula import Pelicula
from servicio.catalogoPelicula import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar pelicula')
        print('2. Listar peliculas')
        print('3. Eliminar catalogo peliculas')
        print('4. Salir')
        opcion = int(input('Escribi tu opcion (1-4): '))

        if opcion == 1:
            nombrePelicula = input('Ingresa el nombre de la pelicula: ')
            pelicula = Pelicula(nombrePelicula)
            cp.agregarPelicula(pelicula)
        elif opcion == 2:
            cp.listarPeliculas()
        elif opcion == 3:
            cp.eliminarPeliculas()

    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salirmos del programa')






