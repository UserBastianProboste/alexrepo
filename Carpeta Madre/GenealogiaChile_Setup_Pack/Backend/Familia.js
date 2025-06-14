const mongoose = require('mongoose');

const familiaSchema = new mongoose.Schema({
  nombre: String,
  descripcion: String,
});

module.exports = mongoose.model('Familia', familiaSchema);
