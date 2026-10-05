import { useState, type FormEvent } from 'react'
import type { Categoria, CategoriaForm } from '../types/categoria'

interface CategoriaModalProps {
  abierto: boolean
  categoria: Categoria | null
  onCerrar: () => void
  onSubmit: (datos: CategoriaForm) => Promise<void>
}

function CategoriaModal({
  abierto,
  categoria,
  onCerrar,
  onSubmit,
}: CategoriaModalProps) {
  const [nombre, setNombre] = useState(categoria?.nombre ?? '')
  const [descripcion, setDescripcion] = useState(
    categoria?.descripcion ?? '',
  )
  const [guardando, setGuardando] = useState(false)

  if (!abierto) {
    return null
  }

  const manejarSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    if (!nombre.trim() || !descripcion.trim()) {
      return
    }

    try {
      setGuardando(true)

      await onSubmit({
        nombre: nombre.trim(),
        descripcion: descripcion.trim(),
      })

      onCerrar()
    } finally {
      setGuardando(false)
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">
      <div className="w-full max-w-md rounded-xl bg-white p-6 shadow-xl">
        <h2 className="mb-5 text-2xl font-bold text-slate-800">
          {categoria ? 'Editar categoría' : 'Nueva categoría'}
        </h2>

        <form onSubmit={manejarSubmit}>
          <div className="mb-4">
            <label
              htmlFor="nombre"
              className="mb-2 block font-medium text-slate-700"
            >
              Nombre
            </label>

            <input
              id="nombre"
              type="text"
              value={nombre}
              onChange={(event) => setNombre(event.target.value)}
              className="w-full rounded-lg border border-slate-300 px-3 py-2 outline-none focus:border-blue-500"
              placeholder="Nombre de la categoría"
              required
            />
          </div>

          <div className="mb-6">
            <label
              htmlFor="descripcion"
              className="mb-2 block font-medium text-slate-700"
            >
              Descripción
            </label>

            <textarea
              id="descripcion"
              value={descripcion}
              onChange={(event) => setDescripcion(event.target.value)}
              className="min-h-28 w-full resize-none rounded-lg border border-slate-300 px-3 py-2 outline-none focus:border-blue-500"
              placeholder="Descripción de la categoría"
              required
            />
          </div>

          <div className="flex justify-end gap-3">
            <button
              type="button"
              onClick={onCerrar}
              className="rounded-lg bg-slate-200 px-4 py-2 text-slate-800 hover:bg-slate-300"
            >
              Cancelar
            </button>

            <button
              type="submit"
              disabled={guardando}
              className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50"
            >
              {guardando ? 'Guardando...' : 'Guardar'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default CategoriaModal