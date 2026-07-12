import { BrowserRouter, Routes, Route } from 'react-router-dom'
import DocumentList from './pages/DocumentList'
import DocumentDetail from './pages/DocumentDetail'
import CreateDocument from './pages/CreateDocument'

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <header className="header">
          <h1><a href="/">AskDoc</a></h1>
        </header>
        <main className="main">
          <Routes>
            <Route path="/" element={<DocumentList />} />
            <Route path="/new" element={<CreateDocument />} />
            <Route path="/document/:id" element={<DocumentDetail />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}

export default App
