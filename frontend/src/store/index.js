import { createStore } from 'redux'
import todoReducer from './todo.reducer'
export const store = createStore(todoReducer)
