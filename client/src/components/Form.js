import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import Loader from './Loader.js';
import TagField from './TagField'


const Form = (props) => {


    // {
    //     usingSkills: false,
    //     number: 10
    // }
    // {
    //     usingSkills: true,
    //     skills: [1, 2, 3]
    // }

    const { setResults } = props

    const handleSubmit = async (e) => {
        setPending(true)
        e.preventDefault();
        // const res = await axios.post('/person', { number: parseInt(number) })
        // if (res.data) {
        //     setResults(res.data);
        //     setPending(false)
        // }
        const res = await axios.post('/skills', { skills: tags })
        if (res.data) {
            console.log(res.data);
            setResults(res.data);
            setPending(false)
        }
    }

    const [number, setNumber] = useState(0);
    const [pending, setPending] = useState(false);
    const [suggestions, setSuggestions] = useState([]);
    const [tags, setTags] = useState([])

    useEffect(() => {
        const fetchSuggestons = async () => {
            const res = await axios.get('/suggestions');
            const mapped = res.data.map(elem => elem.name)
            // const mapped = ["hello", "test"]
            setSuggestions(mapped)
        }
        fetchSuggestons()
    }, [])

    return (
        <form className='shadow-lg text-center'>
            <div className="form-group text-center">
                {/* <input type="text" className="form-control" onChange={(e) => { setNumber(e.target.value) }} placeholder="Name"/> */}
                <TagField setTags={setTags} key={suggestions[0]} suggestions={suggestions} />
            </div>
            <button className={'btn btn-primary ' + (pending ? 'btn-secondary' : '')} onClick={handleSubmit}>{pending ? <Loader></Loader> : 'Submit'}</button>
        </form>
    )
}

export default Form