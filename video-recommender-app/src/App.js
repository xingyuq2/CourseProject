import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import List from './Components/List.js'
import Detail from './Components/Detail';

function App() {
  return (
    <Router>
      <div className='App'>
        <div className='header'>Netflix Movies And Shows</div>
        <div className='routes-container'>
          <Routes>
            <Route path='/' exact element={<List/>}/>
            <Route path='/:id' element={<Detail/>}/>
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
