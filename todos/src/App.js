import { Route } from 'react-router-dom'
import { Schedule } from './containers'

const App = () => {
  return (
    <Route exact path='/' component={ Schedule } />
  )
  
}

export default App

