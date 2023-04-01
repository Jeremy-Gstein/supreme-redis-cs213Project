import React, { useState, useEffect } from 'react';

function TopScores() {
  const [topScores, setTopScores] = useState({});

  useEffect(() => {
    fetch('/top-scores')
      .then(response => response.json())
      .then(data => setTopScores(data));
  }, []);

  return (
    <div>
      <h1>Top Scores</h1>
      <ul>
        {Object.entries(topScores).map(([element, score]) => (
          <li key={element}>{element}: {score}</li>
        ))}
      </ul>
    </div>
  );
}

export default TopScores;

