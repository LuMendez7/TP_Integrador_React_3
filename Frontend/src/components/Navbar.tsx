function Navbar() {
  return (
    <nav className="bg-slate-900 text-white shadow-lg">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <div>
          <h1 className="text-2xl font-bold">Gestión de Categorías</h1>
          <p className="text-sm text-slate-300">
            TP Integrador React 3
          </p>
        </div>

        <span className="rounded-lg bg-slate-700 px-3 py-2 text-sm">
          React + FastAPI
        </span>
      </div>
    </nav>
  )
}

export default Navbar