import type { Categoria } from '../types/categoria'
import CategoriaCard from './CategoriaCard'

interface CategoriaListProps {
  categorias: Categoria[]
  onEditar: (categoria: Categoria) => void
  onEliminar: (id: number) => void
}

function CategoriaList({
  categorias,
  onEditar,
  onEliminar,
}: CategoriaListProps) {
  if (categorias.length === 0) {
    return (
      <div className="rounded-xl bg-white p-8 text-center shadow">
        <p className="text-slate-500">
          No hay categorías cargadas.
        </p>
      </div>
    )
  }

  return (
    <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      {categorias.map((categoria) => (
        <CategoriaCard
          key={categoria.id}
          categoria={categoria}
          onEditar={onEditar}
          onEliminar={onEliminar}
        />
      ))}
    </div>
  )
}

export default CategoriaList