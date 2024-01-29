import React, { useState } from 'react';
import AddTask from './components/AddTasks';
import './App.css'; // Import the CSS file

function App() {
  const [tasks, setTasks] = useState([]);

  const handleAddTask = (newTask) => {
    setTasks([...tasks, newTask]);
  };

  return (
    <div className="App">
      <h1 className="Header">Task Manager</h1>
      <AddTask onAddTask={handleAddTask} />
      <ul className="TaskList">
        {tasks.map((task, index) => (
          <li key={index}>{task}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
