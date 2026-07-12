import { useState, useEffect } from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'

function DocumentDetail() {
  const { id } = useParams()
  const navigate = useNavigate()
  const [document, setDocument] = useState(null)
  const [messages, setMessages] = useState([])
  const [chatInput, setChatInput] = useState('')
  const [sending, setSending] = useState(false)

  useEffect(() => {
    fetch(`/document/${id}`)
      .then(res => res.json())
      .then(setDocument)

    fetch(`/document/${id}/chat`)
      .then(res => res.json())
      .then(setMessages)
  }, [id])

  const sendMessage = async () => {
    if (!chatInput.trim() || sending) return
    setSending(true)

    const userMsg = { id: Date.now(), role: 'user', content: chatInput, created_at: new Date().toISOString() }
    setMessages(prev => [...prev, userMsg])
    setChatInput('')

    try {
      const res = await fetch(`/document/${id}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ chat: chatInput })
      })
      const data = await res.json()
      setMessages(prev => [...prev, { id: Date.now() + 1, role: 'assistant', content: data.content, created_at: new Date().toISOString() }])
    } catch {
      setMessages(prev => [...prev, { id: Date.now() + 1, role: 'assistant', content: 'Error getting response', created_at: new Date().toISOString() }])
    }

    setSending(false)
  }

  const handleDelete = async () => {
    if (!confirm('Delete this document?')) return
    await fetch(`/document/${id}`, { method: 'DELETE' })
    navigate('/')
  }

  if (!document) return <p>Loading...</p>

  return (
    <div>
      <div className="doc-header">
        <h2 className="doc-title">{document.title}</h2>
        <div className="doc-actions">
          <button onClick={handleDelete} className="btn btn-danger">Delete</button>
          <Link to="/" className="btn btn-secondary">Back</Link>
        </div>
      </div>

      <div className="chat-section">
        <h2>Chat</h2>
        <div className="chat-messages">
          {messages.length === 0 && <p className="empty-state">No messages yet. Start chatting!</p>}
          {messages.map(msg => (
            <div key={msg.id} className={`message ${msg.role}`}>
              <div className="message-role">{msg.role}</div>
              <div>{msg.content}</div>
            </div>
          ))}
        </div>

        <div className="chat-input">
          <input
            type="text"
            value={chatInput}
            onChange={e => setChatInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && sendMessage()}
            placeholder="Ask about this document..."
            disabled={sending}
          />
          <button onClick={sendMessage} className="btn btn-primary" disabled={sending}>
            {sending ? '...' : 'Send'}
          </button>
        </div>
      </div>
    </div>
  )
}

export default DocumentDetail
