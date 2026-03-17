import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';

const API = process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8000';

export default function Register() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  async function submit() {
    try {
      const res = await fetch(`${API}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password, email }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || data.message || 'error');
      setMessage(data.message);
    } catch (err) {
      setMessage(String(err));
    }
  }

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 20, marginBottom: 12 }}>Register</Text>
      <Text>Username</Text>
      <TextInput value={username} onChangeText={setUsername} style={{ borderWidth: 1, padding: 8, marginBottom: 8 }} />
      <Text>Email</Text>
      <TextInput value={email} onChangeText={setEmail} style={{ borderWidth: 1, padding: 8, marginBottom: 8 }} />
      <Text>Password</Text>
      <TextInput value={password} onChangeText={setPassword} secureTextEntry style={{ borderWidth: 1, padding: 8, marginBottom: 12 }} />
      <Button title="Register" onPress={submit} />
      {message ? <Text style={{ marginTop: 12 }}>{message}</Text> : null}
    </View>
  );
}
