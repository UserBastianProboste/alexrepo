import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

function DetallePersona() {
  const { id } = useParams();
  const [persona, setPersona] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:3000/api/personas/${id}`)
      .then(res => setPersona(res.data))
      .catch(console.error);
  }, [id]);

  if (!persona) return <div>Cargando persona...</div>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Persona: {persona.nombreCompleto}</h2>
      <p>Familia: {persona.familia?.nombre || 'Desconocida'}</p>
      <p>Fecha Nacimiento: {persona.fechaNacimiento || 'Desconocida'}</p>
      <Link to="/personas">Volver a Personas</Link>
    </div>
  );
}

export default DetallePersona;
