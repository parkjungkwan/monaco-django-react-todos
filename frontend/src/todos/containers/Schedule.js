import React from 'react'
import { TodoInput, TodoList } from '../components'
import { Provider } from 'react-redux'
import { store } from '../store'

const Schedule = () => {
    return (<>
    <Provider store={store}>
        <TodoInput/>
        <TodoList/>
    </Provider>
    </>)
}
export default Schedule