// server/index.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

// Conectar a MongoDB
mongoose.connect('mongodb://localhost:27017/genealogia', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Esquema simple familia
const FamiliaSchema = new mongoose.Schema({
  nombre: String,
  descripcion: String,
});
const Familia = mongoose.model('Familia', FamiliaSchema);

// Rutas
app.get('/api/familias', async (req, res) => {
  const familias = await Familia.find();
  res.json(familias);
});

app.get('/api/familias/:id', async (req, res) => {
  const familia = await Familia.findById(req.params.id);
  res.json(familia);
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en puerto ${PORT}`);
});
