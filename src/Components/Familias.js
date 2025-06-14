import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function Familias() {
  const [familias, setFamilias] = useState([]);
  const [busqueda, setBusqueda] = useState('');

  useEffect(() => {
    axios.get('http://localhost:3000/api/familias')
      .then(res => setFamilias(res.data))
      .catch(console.error);
  }, []);

  const filtradas = familias.filter(f => f.nombre.toLowerCase().includes(busqueda.toLowerCase()));

  return (
    <div style={{ padding: 20 }}>
      <h2>Familias</h2>
      <input 
        type="text" 
        placeholder="Buscar familia..." 
        value={busqueda} 
        onChange={e => setBusqueda(e.target.value)} 
        style={{ marginBottom: 10 }}
      />
      <ul>
        {filtradas.map(f => (
          <li key={f._id}>
            <Link to={`/familias/${f._id}`}>{f.nombre}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Familias;
