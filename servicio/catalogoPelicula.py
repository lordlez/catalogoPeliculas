import os

class CatalogoPeliculas:
    
    rutaArchivo = 'peliculas.txt'

    @classmethod
    def agregarPelicula(cls, pelicula):
        with open(cls.rutaArchivo, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
        
    
    @classmethod
    def listarPeliculas(cls):
        with open(cls.rutaArchivo, 'r') as archivo:
            print('Catalogo de Peliculas'.center(50,'-'))
            print(archivo.read())
    

    @classmethod
    def eliminarPeliculas(cls):
        os.remove(cls.rutaArchivo)
        print(f'Archivo eliminado: {cls.rutaArchivo}')




