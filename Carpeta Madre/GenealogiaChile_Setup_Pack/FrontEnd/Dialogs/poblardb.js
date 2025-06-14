const mongoose = require('mongoose');
const Familia = require('./models/Familia'); // Ajustar import si está en otro archivo
const Persona = require('./models/Persona');

async function poblar() {
  await mongoose.connect('mongodb://localhost:27017/genealogia', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  // Limpiar datos
  await Familia.deleteMany({});
  await Persona.deleteMany({});

  // Crear familias
  const valdes = new Familia({
    nombre: 'Valdes',
    descripcion: 'Familia prominente en el Maule y Ñuble.',
    personajesNotables: ['José Miguel Valdés - Empresario y político'],
  });
  await valdes.save();

  const hernandez = new Familia({
    nombre: 'Hernandez',
    descripcion: 'Familia Hernández, establecida desde el siglo XVIII.',
    personajesNotables: ['Pedro Hernández - Líder local'],
  });
  await hernandez.save();

  // Crear personas ejemplo
  const joseMiguel = new Persona({
    nombreCompleto: 'José Miguel Valdés',
    apellidoPaterno: 'Valdés',
    apellidoMaterno: 'González',
    fechaNacimiento: new Date('1800-01-01'),
    descripcion: 'Empresario y político influyente en el siglo XIX.',
    familia: valdes._id,
  });
  await joseMiguel.save();

  const pedroH = new Persona({
    nombreCompleto: 'Pedro Hernández',
    apellidoPaterno: 'Hernández',
    apellidoMaterno: 'López',
    fechaNacimiento: new Date('1780-01-01'),
    descripcion: 'Líder local del siglo XVIII.',
    familia: hernandez._id,
  });
  await pedroH.save();

  console.log('Datos iniciales insertados');
  mongoose.connection.close();
}

poblar();
