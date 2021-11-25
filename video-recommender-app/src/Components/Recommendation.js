import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import FetchData from '../FetchData';
import '../styles/Recommendation.css'

export default function Recommendation({idToRecommend}) {
  const [videosRecommended, setVideosRecommended] = useState([]);

  useEffect(
    () => {
      async function fetchRecommendData() {
        const res = await FetchData('api/recommendations?id=' + idToRecommend);
        setVideosRecommended(res);
      }
      fetchRecommendData();
    }, 
    [setVideosRecommended, idToRecommend],
  );

  if (!videosRecommended) {
    return (
      <div>Loading</div>
    )
  }

  return (
    <div>
      <div className='recommend-title'>
        Recommendations:
      </div>
      <div className='recommend-container'>
        {
          videosRecommended.map((video, index) => {
            return (
              <div className='recommended-item' key={index}>
                <Link className='link-video' to={`/${video.id}`} target='_blank' rel='noopener noreferrer'>
                  <img src={video.image_url} alt=''/>
                  <div>{video.name}</div>
                </Link>
              </div>
            )
          })
        }
      </div>
    </div>
  );
}

Recommendation.propTypes = {
  idToRecommend: PropTypes.string.isRequired,
}
