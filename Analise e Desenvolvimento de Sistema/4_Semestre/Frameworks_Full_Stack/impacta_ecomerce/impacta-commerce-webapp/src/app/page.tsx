'use client'

import React, { useState } from 'react';

export default function Nova_Rota() {

  const [count, setCount] = useState(0);

  function increment() {
    setCount(count + 1);
  }

  return (

    <div className='mx-4'>
      <p>O valor do contador é: {count}</p>
      <button
        className='bg-blue-500 text-white p-2'
        onClick={increment}>

        Incrementar
      </button>
    </div>
  );
}
