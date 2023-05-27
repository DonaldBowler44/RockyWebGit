import React, { useState } from 'react'; 
import regstyles from "../styles/register.module.css";
import { useRouter } from 'next/router';
import { registerUser, getExistingEmails } from '@/api';


export default function RegisterPage({ existingEmails }) {
    const router = useRouter();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    //register user
    const handleRegister = async (e) => {
        e.preventDefault();

        try {
            await registerUser(email, password);
            //registration successfull, redirect to index.js
            router.push('/');
        } catch (error) {
            setError(error.message);
        }
    };

    return (
        <div>
      {/* Registration form */}
      <h2>Sign up</h2>
      <form onSubmit={handleRegister}>
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
        <input type="submit" value="Signup" />
      </form>

      {/* Error message */}
      {error && <p>{error}</p>}

      {/* Existing emails */}
      <h3>Existing Emails:</h3>
      <ul>
        {existingEmails.map((email, index) => (
          <li key={index}>{email}</li>
        ))}
      </ul>
    </div>
    )
}

export async function getServerSideProps() {
    try {
        // fetch existing user emails from server using API
        const existingEmails = await getExistingEmails();

        return {
            props: {
                existingEmails,
            },
        };
    } catch (error) {
        return {
            props: {
                existingEmails: [],
            },
        };
    }
}