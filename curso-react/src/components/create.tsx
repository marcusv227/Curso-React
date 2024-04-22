import React from "react";
import { useState } from "react";

export default function Create() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const postData = () => {
        console.log(email);
        console.log(password);
    }
    return(
        <div className='content'>
            <div className='header'>
                <h1>
                    Cadastro
                </h1>
                </div>
                <div className="container">
                <div className='email'>
                    <label htmlFor="email">E-mail</label>
                    <input type="text" id='email' placeholder='E-mail' onChange={(e) => setEmail(e.target.value)}/>
                </div>
                <div className='password'>
                    <label htmlFor="password">Senha</label>
                    <input type="password" id='password' placeholder='Senha' onChange={(e) => setPassword(e.target.value)}/>
                </div>
                <div className='button'>
                    <button onClick={postData} type='submit'>Salvar</button>
                </div>
            </div>
        </div>
    )
}
