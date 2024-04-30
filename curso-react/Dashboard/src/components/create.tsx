import api from "../api";
import { useState } from "react";

export default function Create() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const handleSubmit = async (event: any) => {
        event.preventDefault();
        try {
            const response = await api.post('/cadastros/', {
                email: email,
                nome: name,
                senha: password
            });
            console.log('Resposta da API:', response.data);
        } catch (error) {
            console.error('Erro ao enviar dados:', error);
        }
    };
    return(
        <div className='content'>
            <div className='header'>
                <h1>
                    Cadastro
                </h1>
            </div>
            <form onSubmit={handleSubmit} className="container">
                <div className='email'>
                    <label htmlFor="email">E-mail</label>
                    <input type="email" id='email' placeholder='E-mail' value={email} onChange={(e) => setEmail(e.target.value)}/>
                </div>
                <div className='nome'>
                    <label htmlFor="nome">Nome</label>
                    <input type="text" id='nome' placeholder='Nome' value={name} onChange={(e) => setName(e.target.value)}/>
                </div>
                <div className='password'>
                        <label htmlFor="password">Senha</label>
                        <input type="password" id='password' placeholder='Senha' value={password} onChange={(e) => setPassword(e.target.value)}/>
                </div>
                <div className='button'>
                    <button type='submit'>Salvar</button>
                </div>
            </form>
        </div>
    )
}
