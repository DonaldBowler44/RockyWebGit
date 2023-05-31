import React from 'react';

const RedirectInput = ({ email, password, handleEmailChange, handlePasswordChange }) => {
   return (
   <div>
    <div className="relative mb-6" data-te-input-wrapper-init>
  <input
    type="text"
    placeholder="Email..."
    className="peer block min-h-[auto] w-full rounded border-0 px-5 py-[0.52rem] outline-none"
    value={email}
    onChange={handleEmailChange}
    required
  />
  </div>
      <br />
      <input
        type="password"
        placeholder="Password..."
        className="peer block min-h-[auto] w-full rounded border-0 px-5 py-[0.52rem] outline-none"
        value={password}
        onChange={handlePasswordChange}
        required
      />
      <br />
    </div>
   );
};

export default RedirectInput;
