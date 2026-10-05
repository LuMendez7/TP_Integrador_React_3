import type { Categoria } from '../types/categoria'

interface CategoriaCardProps {
  categoria: Categoria
  onEditar: (categoria: Categoria) => void
  onEliminar: (id: number) => void
}

function CategoriaCard({
  categoria,
  onEditar,
  onEliminar,
}: CategoriaCardProps) {
  return (
    <article className="rounded-xl bg-white p-6 shadow-md transition hover:shadow-lg">
      <h2 className="mb-2 text-xl font-bold text-slate-800">
        {categoria.nombre}
      </h2>

      <p className="mb-6 text-slate-600">
        {categoria.descripcion}
      </p>

      <div className="flex gap-3">
        <button
          type="button"
          onClick={() => onEditar(categoria)}
          className="rounded-lg bg-blue-600 px-4 py-2 text-white transition hover:bg-blue-700"
        >
          Editar
        </button>

        <button
          type="button"
          onClick={() => onEliminar(categoria.id)}
          className="rounded-lg bg-red-600 px-4 py-2 text-white transition hover:bg-red-700"
        >
          Eliminar
        </button>
      </div>
    </article>
  )
}

export default CategoriaCard