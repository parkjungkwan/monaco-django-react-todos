import { Counter, Todo } from './components/index'
import {Route} from 'react-router-dom'




const App = () => {
  return (<>
     <Route exact path='/' component={ Counter }/>
     <Route exact path='/todo' component={ Todo }/>
  </>)
}




export default App;
