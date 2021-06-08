import React, { useState } from 'react'

const Counter = () => {

    const [ number, setNumber ] = useState(0)

    const onAddClick = () => {
        setNumber( number + 1)
    }
    const onSubClick = () => {
        setNumber( number - 1)
    }
    return (<>
    <h1> { number }</h1>
    <button onClick = {onAddClick}> + </button>
    <button onClick = {onSubClick}> - </button>
    </>)
}

export default Counter

