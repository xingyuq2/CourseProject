import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import FetchData from '../FetchData';
import '../styles/List.css'

export default function List() {
  const [videos, setVideos] = useState([]);

  useEffect(
    () => {
      async function fetchVideosData() {
        const res = await FetchData('api/all');
        setVideos(res);
      }
      fetchVideosData();
    }, 
    [setVideos],
  );

  if (!videos) {
    return (
      <div>Loading</div>
    )
  }

  return (
    <div>
      <div className='list-container'>
        {
          videos.map((video, index) => {
            return (
              <div className='item' key={index}>
                <Link className='link-video' to={`/${video.id}`} target='_blank' rel='noopener noreferrer'>
                  <img src={video.image_url} alt=''/>
                  <div className='video-label'>{video.name}</div>
                </Link>
              </div>
            )
          })
        }
      </div>
    </div>
  );
}
