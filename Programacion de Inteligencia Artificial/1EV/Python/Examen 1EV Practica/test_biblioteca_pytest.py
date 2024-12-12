import pytest
from gestor_biblioteca import Libro, Usuario, Biblioteca
import os
from pathlib import


@pytest.fixture
def biblioteca():
    return Biblioteca()


def test_registrar_libro(biblioteca):
    libro = Libro("Python Básico", "Autor A", "Programación")
    biblioteca.registrar_libro(libro)
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0].titulo == "Python Básico"


def test_registrar_usuario(biblioteca):
    usuario = Usuario("Juan", "Pérez")
    biblioteca.registrar_usuario(usuario)
    assert len(biblioteca.usuarios) == 1
    assert biblioteca.usuarios[0].nombre == "Juan"


def test_buscar_libro(biblioteca):
    libro1 = Libro("Python Básico", "Autor A", "Programación")
    libro2 = Libro("Python Avanzado", "Autor B", "Programación")
    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    resultados = biblioteca.buscar_libro(genero="Programación")
    assert len(resultados) == 2


def test_prestar_libro(biblioteca):
    libro = Libro("Python Básico", "Autor A", "Programación")
    usuario = Usuario("Juan", "Pérez")
    biblioteca.registrar_libro(libro)
    biblioteca.registrar_usuario(usuario)
    biblioteca.prestar_libro("Python Básico", "Juan")
    assert not biblioteca.libros[0].disponibilidad
    assert len(usuario.libros_prestados) == 1


def test_prestar_libro_no_disponibilidad(biblioteca):
    libro = Libro("Python Básico", "Autor A", "Programación", disponibilidad=False)
    usuario = Usuario("Juan", "Pérez")
    biblioteca.registrar_libro(libro)
    biblioteca.registrar_usuario(usuario)
    with pytest.raises(Exception, match="El libro no está disponible para préstamo."):
        biblioteca.prestar_libro("Python Básico", "Juan")


def test_devolver_libro(biblioteca):
    libro = Libro("Python Básico", "Autor A", "Programación")
    usuario = Usuario("Juan", "Pérez")
    biblioteca.registrar_libro(libro)
    biblioteca.registrar_usuario(usuario)
    biblioteca.prestar_libro("Python Básico", "Juan")
    biblioteca.devolver_libro("Python Básico", "Juan")
    assert biblioteca.libros[0].disponibilidad
    assert len(usuario.libros_prestados) == 0


def test_guardar_estado(biblioteca, tmp_path):
    libro = Libro("Python Básico", "Autor A", "Programación")
    usuario = Usuario("Juan", "Pérez")
    biblioteca.registrar_libro(libro)
    biblioteca.registrar_usuario(usuario)
    directorio = tmp_path / "datos_biblioteca"
    biblioteca.guardar_estado(directorio)
    assert (directorio / "libros.txt").exists()
    assert (directorio / "usuarios.txt").exists()


def test_cargar_estado(biblioteca, tmp_path):
    libro = Libro("Python Básico", "Autor A", "Programación")
    usuario = Usuario("Juan", "Pérez")
    biblioteca.registrar_libro(libro)
    biblioteca.registrar_usuario(usuario)
    directorio = tmp_path / "datos_biblioteca"
    biblioteca.guardar_estado(directorio)

    nueva_biblioteca = Biblioteca()
    nueva_biblioteca.cargar_estado(directorio)

    assert len(nueva_biblioteca.libros) == 1
    assert nueva_biblioteca.libros[0].titulo == "Python Básico"
    assert len(nueva_biblioteca.usuarios) == 1
    assert nueva_biblioteca.usuarios[0].nombre == "Juan"


def test_decorador_registrar_actividad(capsys, biblioteca):
    libro = Libro("Python Básico", "Autor A", "Programación")
    usuario = Usuario("Juan", "Pérez")
    biblioteca.registrar_libro(libro)
    biblioteca.registrar_usuario(usuario)

    biblioteca.prestar_libro("Python Básico", "Juan")

    # Capturar la salida del decorador
    captured = capsys.readouterr()

    assert "Libro 'Python Básico' prestado a Juan Pérez." in captured.out


def test_generador_libros_disponibles(biblioteca):
    libro1 = Libro("Python Básico", "Autor A", "Programación", disponibilidad=True)
    libro2 = Libro("Python Avanzado", "Autor B", "Programación", disponibilidad=False)
    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)

    generador = biblioteca.libros_disponibles()
    libros = list(generador)

    assert len(libros) == 1
    assert libros[0].titulo == "Python Básico"