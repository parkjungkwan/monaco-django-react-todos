import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { deleteTodoAction, toggleTodoAction } from '../store/todo.reducer'


const TodoList = () => {
    const todos = useSelector( state => state.todos )
    const dispatch = useDispatch()
    const toggleTodo = id => dispatch(toggleTodoAction(id))
    const deleteTodo = id => dispatch(deleteTodoAction(id))
    return (<>
    {todos.lenght === 0 && (<p className='alert alert-info'>등록된 할일이 없습니다</p>)}
    {todos.lenght !== 0 
    && todos.map( todo => (<div key = {todo.id} className = "row mb-1">
        <div className="col-sm-2"> 
            <input type="checkbox" checked={todo.complete} onChange={toggleTodo.bind(null, todo.id)} />
            {todo.complete 
            ? <span style={{textDecoration: "line-through"}}>{todo.name}</span> 
            : <span>{todo.name}</span>
            }  
            <button onClick={deleteTodo.bind(null, todo.id)}> X </button>       
        </div>
    </div>))}
    </>)
}
export default TodoList