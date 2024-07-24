import { useState } from 'react';
import './App.css'
import ManagerDashboard from './components/ManagerDashboard'
import Navbar from './components/Navbar'
import HRDashboard from './components/HRDashboard';

function App() {
  const [currentDashboard, setCurrentDashboard] = useState<string>("HR");
  return (
    <>
      <Navbar currentDashboard={currentDashboard} changeDashboard={setCurrentDashboard} />
      {currentDashboard === 'HR' ? <ManagerDashboard /> : <HRDashboard />}
    </>
  )
}

export default App
