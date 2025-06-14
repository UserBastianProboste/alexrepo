import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

function DetalleFamilia() {
  const { id } = useParams();
  const [familia, setFamilia] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:3000/api/familias/${id}`)
      .then(res => setFamilia(res.data))
      .catch(console.error);
  }, [id]);

  if (!familia) return <div>Cargando familia...</div>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Familia: {familia.nombre}</h2>
      <p>ID: {familia._id}</p>
      <Link to="/familias">Volver a Familias</Link>
    </div>
  );
}

export default DetalleFamilia;
