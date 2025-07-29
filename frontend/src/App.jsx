import { useState } from 'react'
import LandingPage from './pages/landingPage'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <LandingPage />
      </div>

    </>
  )
}

export default App
