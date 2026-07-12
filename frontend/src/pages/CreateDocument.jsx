import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'

function CreateDocument() {
  const navigate = useNavigate()
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')
  const [saving, setSaving] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!title.trim() || !content.trim()) return

    setSaving(true)
    const res = await fetch('/document/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, content })
    })
    const doc = await res.json()
    navigate(`/document/${doc.id}`)
  }

  return (
    <div>
      <div className="page-header">
        <h2>New Document</h2>
        <Link to="/" className="btn btn-secondary">Back</Link>
      </div>

      <div className="card">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Title</label>
            <input
              type="text"
              value={title}
              onChange={e => setTitle(e.target.value)}
              placeholder="Document title"
              required
            />
          </div>
          <div className="form-group">
            <label>Content</label>
            <textarea
              value={content}
              onChange={e => setContent(e.target.value)}
              placeholder="Write your document content here..."
              required
            />
          </div>
          <button type="submit" className="btn btn-primary" disabled={saving}>
            {saving ? 'Creating...' : 'Create Document'}
          </button>
        </form>
      </div>
    </div>
  )
}

export default CreateDocument
