import React, { useState } from 'react';
import './App.css';

const API = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [mode, setMode] = useState('login');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  async function submit() {
    const url = `${API}/${mode}`;
    const payload = mode === 'register' ? { username, password, email } : { username, password };
    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || data.message || 'error');
      setMessage(data.message);
    } catch (err) {
      setMessage(String(err));
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h2>Simple login page made by pramod</h2>
        <div style={{ marginBottom: 12 }}>
          <button onClick={() => setMode('login')} disabled={mode === 'login'}>Login</button>
          <button onClick={() => setMode('register')} disabled={mode === 'register'} style={{ marginLeft: 8 }}>Register</button>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', width: 320 }}>
          <input placeholder="username" value={username} onChange={e => setUsername(e.target.value)} />
          {mode === 'register' && (
            <input placeholder="email" value={email} onChange={e => setEmail(e.target.value)} />
          )}
          <input placeholder="password" type="password" value={password} onChange={e => setPassword(e.target.value)} />
          <button onClick={submit} style={{ marginTop: 12 }}>{mode === 'login' ? 'Login' : 'Register'}</button>
        </div>

        {message && <p style={{ marginTop: 16 }}>{message}</p>}
      </header>
    </div>
  );
}

export default App;
