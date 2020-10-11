import React from 'react'

const Loader = () => {
    return (
        <div className="spinner-border text-success" style={{width: '25px', height: '25px'}} role="status">
            <span className="sr-only">Loading...</span>
        </div>
    )
}

export default Loader