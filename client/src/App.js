import React, { useState } from 'react';
import './App.css';
import 'axios';
import axios from 'axios';

function App() {

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('/person', {number: parseInt(number)})
    if(res.data){
      console.log(res.data)
      setSkills(res.data)
    }
  }

  const [number, setNumber] = useState(0);
  const [skills, setSkills] = useState(null)

  return (
    <div className="App">
      <main className=''>
        <h1 className='text-center'>Details: </h1>
        <form className='text-center'>
          <div className="form-group text-center">
            <label htmlFor="exampleInputEmail1">Name</label>
            <input type="text" className="form-control"  onChange={(e) => {setNumber(e.target.value)}} />
            <small id="emailHelp" className="form-text text-muted">Acc it's the number</small>
          </div>
          <button className='btn btn-primary' onClick={handleSubmit}>Submit</button>
        </form>
      </main>
    </div>
  );
}

export default App;
