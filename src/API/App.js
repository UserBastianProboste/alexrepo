// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { Container, AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import Familias from '../components/Familias';
import DetalleFamilia from '../components/DetalleFamilia';

function App() {
  return (
    <Router>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Genealogía Chile
          </Typography>
          <Button color="inherit" component={Link} to="/">Inicio</Button>
        </Toolbar>
      </AppBar>
      <Container sx={{ mt: 4 }}>
        <Routes>
          <Route path="/" element={<Familias />} />
          <Route path="/familias/:id" element={<DetalleFamilia />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
