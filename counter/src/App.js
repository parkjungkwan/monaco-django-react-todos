import { Counter } from './components/index'
import {Route} from 'react-router-dom'



const App = () => {
  return (<>
     <Route exact path='/' component={ Counter }/>
  </>)
}




export default App;
