import { useEffect, useState } from 'react'
import Navbar from './components/Navbar'
import CategoriaList from './components/CategoriaList'
import CategoriaModal from './components/CategoriaModal'
import type { Categoria, CategoriaForm } from './types/categoria'

const API_URL = 'http://127.0.0.1:8000/categorias'

function App() {
  const [categorias, setCategorias] = useState<Categoria[]>([])
  const [modalAbierto, setModalAbierto] = useState(false)
  const [categoriaSeleccionada, setCategoriaSeleccionada] =
    useState<Categoria | null>(null)
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState('')

  const cargarCategorias = async () => {
    try {
      setError('')

      const respuesta = await fetch(`${API_URL}/`)

      if (!respuesta.ok) {
        throw new Error('No se pudieron obtener las categorías')
      }

      const datos: Categoria[] = await respuesta.json()
      setCategorias(datos)
    } catch (error) {
      console.error(error)
      setError('No se pudo conectar con el servidor.')
    } finally {
      setCargando(false)
    }
  }

  useEffect(() => {
    cargarCategorias()
  }, [])

  const abrirModalCrear = () => {
    setCategoriaSeleccionada(null)
    setModalAbierto(true)
  }

  const abrirModalEditar = (categoria: Categoria) => {
    setCategoriaSeleccionada(categoria)
    setModalAbierto(true)
  }

  const cerrarModal = () => {
    setModalAbierto(false)
    setCategoriaSeleccionada(null)
  }

  const guardarCategoria = async (datos: CategoriaForm) => {
    if (categoriaSeleccionada) {
      const respuesta = await fetch(
        `${API_URL}/${categoriaSeleccionada.id}`,
        {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(datos),
        },
      )

      if (!respuesta.ok) {
        throw new Error('No se pudo actualizar la categoría')
      }
    } else {
      const respuesta = await fetch(`${API_URL}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(datos),
      })

      if (!respuesta.ok) {
        throw new Error('No se pudo crear la categoría')
      }
    }

    await cargarCategorias()
  }

  const eliminarCategoria = async (id: number) => {
    const confirmar = window.confirm(
      '¿Está seguro de que desea eliminar esta categoría?',
    )

    if (!confirmar) {
      return
    }

    try {
      const respuesta = await fetch(`${API_URL}/${id}`, {
        method: 'DELETE',
      })

      if (!respuesta.ok) {
        throw new Error('No se pudo eliminar la categoría')
      }

      await cargarCategorias()
    } catch (error) {
      console.error(error)
      window.alert('No se pudo eliminar la categoría.')
    }
  }

  return (
    <div className="min-h-screen">
      <Navbar />

      <main className="mx-auto max-w-6xl px-6 py-8">
        <div className="mb-8 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <h2 className="text-3xl font-bold text-slate-800">
              Categorías
            </h2>

            <p className="mt-1 text-slate-500">
              Alta, consulta, modificación y eliminación de categorías.
            </p>
          </div>

          <button
            type="button"
            onClick={abrirModalCrear}
            className="rounded-lg bg-green-600 px-5 py-3 font-medium text-white shadow hover:bg-green-700"
          >
            + Nueva categoría
          </button>
        </div>

        {error && (
          <div className="mb-6 rounded-lg bg-red-100 p-4 text-red-700">
            {error}
          </div>
        )}

        {cargando ? (
          <p className="text-slate-500">Cargando categorías...</p>
        ) : (
          <CategoriaList
            categorias={categorias}
            onEditar={abrirModalEditar}
            onEliminar={eliminarCategoria}
          />
        )}
      </main>

      <CategoriaModal
        abierto={modalAbierto}
        categoria={categoriaSeleccionada}
        onCerrar={cerrarModal}
        onSubmit={guardarCategoria}
      />
    </div>
  )
}

export default App