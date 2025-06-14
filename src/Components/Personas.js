import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function Personas() {
  const [personas, setPersonas] = useState([]);
  const [busqueda, setBusqueda] = useState('');

  useEffect(() => {
    axios.get('http://localhost:3000/api/personas')
      .then(res => setPersonas(res.data))
      .catch(console.error);
  }, []);

  const filtradas = personas.filter(p => p.nombreCompleto.toLowerCase().includes(busqueda.toLowerCase()));

  return (
    <div style={{ padding: 20 }}>
      <h2>Personas</h2>
      <input 
        type="text" 
        placeholder="Buscar persona..." 
        value={busqueda} 
        onChange={e => setBusqueda(e.target.value)} 
        style={{ marginBottom: 10 }}
      />
      <ul>
        {filtradas.map(p => (
          <li key={p._id}>
            <Link to={`/personas/${p._id}`}>{p.nombreCompleto}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Personas;
