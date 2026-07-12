import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

function DocumentList() {
  const [documents, setDocuments] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/document/')
      .then(res => res.json())
      .then(data => {
        setDocuments(data)
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  const handleDelete = async (id) => {
    if (!confirm('Delete this document?')) return
    await fetch(`/document/${id}`, { method: 'DELETE' })
    setDocuments(documents.filter(d => d.id !== id))
  }

  if (loading) return <p>Loading...</p>

  return (
    <div>
      <div className="page-header">
        <h2>Documents</h2>
        <Link to="/new" className="btn btn-primary">+ New Document</Link>
      </div>

      {documents.length === 0 ? (
        <div className="empty-state">
          <p>No documents yet. Create one to get started!</p>
        </div>
      ) : (
        documents.map(doc => (
          <div key={doc.id} className="card" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <Link to={`/document/${doc.id}`} className="card-link">
              <div className="card-title">{doc.title}</div>
            </Link>
            <button onClick={() => handleDelete(doc.id)} className="btn btn-danger">Delete</button>
          </div>
        ))
      )}
    </div>
  )
}

export default DocumentList
