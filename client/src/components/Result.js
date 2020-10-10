import React from 'react'

const Result = (props) => {

    const {results} =props;

    // console.log(results)

    const sliced = results.slice(1)

    // const chunked = []
    // for(let i = 0; i < sliced.length; i+=3){
    //     chunked.push(sliced.slice(i, i+3))
    // }

    const mappedResults = sliced.map((result, i) => {
        return <li className='text-primary' key={i}>{result.position}</li>
    })
    // const mappedResults = chunked.map((arr, i) => {
    //     return(
    //         <ul key={i}>
    //             <li className='text-primary'>{arr[0].position}</li>
    //             <li className='text-primary'>{arr[1].position}</li>
    //             <li className='text-primary'>{arr[2].position}</li>
    //         </ul>
    //     )
    // })

    return(
        <div className="result shadow-lg text-center">
            <h4 className='suitable'>Recommended job:</h4>
            <h3 className='text-success'>{results[0].position}</h3>
            <h4 className='other'>Other suitable jobs:</h4>
            <ul className='text-center other-ul'>
                {mappedResults}
            </ul>
        </div>
    )
}

export default Result
