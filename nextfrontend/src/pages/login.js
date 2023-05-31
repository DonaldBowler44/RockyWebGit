import React, { useState } from 'react'; 
import regstyles from "../styles/register.module.css";
import RedirectInput from '@/components/redirectInputs';
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

    const handleEmailChange = (e) => {
      setEmail(e.target.value);
    };

    const handlePasswordChange = (e) => {
      setPassword(e.target.value);
    };

    return (
      <section className="flex justify-center items-center h-screen">
      <div className="shadow-lg p-6 bg-cyan-500 rounded">
      <h1 className="text-center font-bold text-white">Login</h1>
      <form onSubmit={handleLogin} className="text-center">
        <RedirectInput
          email={email}
          password={password}
          handleEmailChange={handleEmailChange}
          handlePasswordChange={handlePasswordChange}
        />
        <input type="submit" value="Login" className="mt-4 bg-cyan-400 hover:bg-blue-900 text-white font-bold py-2 px-4 rounded" />
      </form>
    </div>
    </section>
    
    )
}
