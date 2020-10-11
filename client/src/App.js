import React, { useState } from 'react';
import './App.css';
import 'axios';
import Form from './components/Form.js';
import Result from './components/Result.js'

function App() {



  const [results, setResults] = useState(null)

  return (
    <div className="App">
      <main className=''>
        <h1 className='text-center heading'>AI job finder</h1>
          <Form setResults={setResults}></Form>
          {results ? <Result results={results}></Result> : null}
      </main>
    </div>
  );
}

export default App;