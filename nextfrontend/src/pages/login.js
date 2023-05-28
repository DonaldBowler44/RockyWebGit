import React, { useState } from 'react'; 
import regstyles from "../styles/register.module.css";
import { useRouter } from 'next/router';
import { login } from '@/api';


export default function LoginPage() {
    const router = useRouter();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    //register user
    const handleLogin = async (e) => {
        e.preventDefault();

        try {
            const formData = new FormData();
            formData.append('email', email);
            formData.append('password', password);

            const response = await login(formData);
            //login successfull, redirect to index.js
            if (response.error) {
                setError(response.exception.message);
              } else {
                // Login successful, redirect to the desired page
                router.push('/'); // Replace '/' with the desired page URL
              }
        } catch (error) {
            setError(error.message);
        }
    };

    return (
        <div>
      {/* Registration form */}
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <br />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <br />
        <input type="submit" value="Login" />
      </form>

      {/* Error message */}
      {error && <p>{error}</p>}

    </div>
    )
}
