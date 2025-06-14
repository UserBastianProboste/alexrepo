const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();
const PORT = 3000;

// Middlewares
app.use(cors());
app.use(express.json());

// Conexión a MongoDB (debes tener MongoDB corriendo local o en Atlas)
mongoose.connect('mongodb://localhost:27017/genealogia', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Esquemas y modelos

const FamiliaSchema = new mongoose.Schema({
  nombre: String,
  descripcion: String,
  personajesNotables: [String],
});

const PersonaSchema = new mongoose.Schema({
  nombreCompleto: String,
  apellidoPaterno: String,
  apellidoMaterno: String,
  fechaNacimiento: Date,
  fechaFallecimiento: Date,
  familia: { type: mongoose.Schema.Types.ObjectId, ref: 'Familia' },
  descripcion: String,
  imagenUrl: String,
  padres: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Persona' }],
  hijos: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Persona' }],
  conyuge: { type: mongoose.Schema.Types.ObjectId, ref: 'Persona' },
});

const Familia = mongoose.model('Familia', FamiliaSchema);
const Persona = mongoose.model('Persona', PersonaSchema);

// Rutas

// Obtener todas familias
app.get('/api/familias', async (req, res) => {
  const familias = await Familia.find();
  res.json(familias);
});

// Obtener personas por familia
app.get('/api/personas/familia/:familiaId', async (req, res) => {
  const personas = await Persona.find({ familia: req.params.familiaId });
  res.json(personas);
});

// Obtener persona con relaciones
app.get('/api/persona/:id', async (req, res) => {
  const persona = await Persona.findById(req.params.id)
    .populate('padres hijos conyuge familia');
  if (!persona) return res.status(404).json({ error: 'Persona no encontrada' });
  res.json(persona);
});

// Crear familia
app.post('/api/familia', async (req, res) => {
  const fam = new Familia(req.body);
  await fam.save();
  res.json(fam);
});

// Crear persona
app.post('/api/persona', async (req, res) => {
  const per = new Persona(req.body);
  await per.save();
  res.json(per);
});

app.listen(PORT, () => {
  console.log(`API escuchando en http://localhost:${PORT}`);
});
