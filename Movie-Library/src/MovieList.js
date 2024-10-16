// MovieList.js

import React from 'react';
import './App.css';

function MovieList({ movies, handleMovieClick }) {
  return (
    <ul className='movie-list'>
      {movies.map(movie => (
        <li key={movie.id} className='movie-card' onClick={() => handleMovieClick(movie)}>
          <img src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`} alt={movie.title} />
          <div className='movie-details'>
            <h3>{movie.title}</h3>
          </div>
        </li>
      ))}
    </ul>
  );
}

export default MovieList;
