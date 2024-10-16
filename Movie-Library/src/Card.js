import React from 'react';

const styles = {
  Card: {
    position: 'relative',
    height: '550px', 
    backgroundColor: '#1d2732',
    borderRadius: '78px',
    boxShadow: '0px 0px 30px black',
    opacity: 1,
  },
  
  UCard: {
    position: 'absolute',
    top: '0px',
    height: '15%',
    backgroundColor: '#1d2732',
    opacity: 1,
    width: '100%'
  },

  MoviePoster: {
    position: 'relative',
    display: 'inline-block',
    width: '40vw'
  },

  MoviePosterDetails: {
    position: 'relative',
    display: 'inline-block',
    width: '50vw',
    verticalAlign: 'center',
    padding: '20px',
    color: '#ffffff',
  }
};

// Function to map genre IDs to their names
const mapGenreIdsToNames = (genreIds, genres) => {
    return genreIds.map(genreId => {
      const genre = genres.find(genre => genre.id === genreId);
      return genre ? genre.name : '';
    }).filter(Boolean).join(', ');
  };
  

const Card = ({ Movie, children, genres }) => {
  return (
   
      
      <div style={styles.Card}>
       <div className='Card'>
      <div style={styles.UCard}>
        <h2>CineMax</h2>
      </div>
        {children}
        {Movie && (
          <div className='random-movie'>
            <div style={styles.MoviePoster}>
            <div className='movie-poster'>
              <img src={`https://image.tmdb.org/t/p/w500${Movie.poster_path}`} alt={Movie.title} />
            </div>
            </div>
            <div style={styles.MoviePosterDetails}>
            <div className='movie-poster-details'>
              <h3>{Movie.title}</h3>
              <p>{Movie.release_date}</p>
              <p>{mapGenreIdsToNames(Movie.genre_ids, genres)}</p>
            </div>
              <p>{Movie.overview}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Card;
