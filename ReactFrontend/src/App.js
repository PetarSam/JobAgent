import React, { useState } from 'react';
import './App.css'; 

function App() {

  const [email, setEmail] = useState()
  const [link, setLink] = useState()
  const [position, setPosiiton] = useState()

  const onSubmit = () => {
    fetch('https://us-central1-wide-retina-263810.cloudfunctions.net/function-1', {
      mode: 'no-cors',
      method:'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
          email:email,
          link:link,
          position:position
      })
  }).then(res => alert('Thank you for subscribing!'))
    .catch(err => console.log(err));
}
  return (
    <div className="Main">
      <div className="Half">
        <h3>Custom</h3>
        <h1>Job Agent</h1>
        <h4>Set custom listener on the company you would like to work in
        and get email when there is a match.</h4>
      </div>
      <div className="Half">
        <h2>Add new listener</h2>
        <input onChange={e => setLink(e.target.value)} type="text"  placeholder="Company URL" />
        <input onChange={e => setPosiiton(e.target.value)} type="text"  placeholder="Position" />
        <input onChange={e => setEmail(e.target.value)} type="email" validate="true" placeholder="Your email" />
        <input type="submit" onClick={onSubmit}/>  
      </div>
    </div>
  );
}

export default App; 
