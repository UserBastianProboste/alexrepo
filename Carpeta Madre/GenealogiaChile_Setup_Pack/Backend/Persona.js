const mongoose = require('mongoose');

const personaSchema = new mongoose.Schema({
  nombre: String,
  apellidoPaterno: String,
  apellidoMaterno: String,
  fechaNacimiento: Date,
  fechaFallecimiento: Date,
  familia: { type: mongoose.Schema.Types.ObjectId, ref: 'Familia' },
  padres: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Persona' }],
  hijos: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Persona' }],
  biografia: String,
});

module.exports = mongoose.model('Persona', personaSchema);
