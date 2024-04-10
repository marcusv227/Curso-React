import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { Button } from '@mui/material';

function App() {
  return (
    <div className="App">
      <TextField id="outlined-basic" label="E-mail" variant="outlined" /> 
      <TextField id="outlined-basic" label="Senha" variant="outlined" />
      <Button variant="contained">Cadastrar</Button>
    </div>
  );
}

export default App;
