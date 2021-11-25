import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import FetchData from '../FetchData';
import Recommendation from './Recommendation';
import '../styles/Detail.css'

export default function Detail() {
  const { id } = useParams();
  const [detail, setDetail] = useState(null);

  useEffect(
    () => {
      async function fetchDetailData() {
        const res = await FetchData('api/video?id=' + id);
        setDetail(res);
      }
      fetchDetailData();
    }, 
    [setDetail, id],
  );

  if (!detail) {
    return (
      <div>Loading</div>
    )
  }

  return (
    <div>
      <div className='detail-container'>
        <div className='detail-info'>
          <img className='detail-info-img' src={detail.image_url} alt='' />
        </div>

        <div className='detail-info'>
          <span className='detail-info-name'>{detail.name}</span>
        </div>

        <div className='detail-info'>
          <span className='detail-info-label'>Synopsis: </span>
          <span className='detail-info-item'>{detail.synopsis}</span>
        </div>

        <div className='detail-info'>
          <span className='detail-info-label'>Genres: </span>
          <span className='detail-info-item'>{detail.genres}</span>
        </div>

        <div className='detail-info'>
          <span className='detail-info-label'>Mood Tag: </span>
          <span className='detail-info-item'>{detail.mood_tag}</span>
        </div>
        
        <div className='detail-info'>
          <span className='detail-info-label'>Casts: </span>
          <span className='detail-info-item'>{detail.casts}</span>
        </div>

        <div className='detail-info'>
          <span className='detail-info-label'>Creators: </span>
          <span className='detail-info-item'>{detail.creators}</span>
        </div>

        <div className='detail-info'>
          <span className='detail-info-label'>Netflix Link: </span>
          <a href={detail.netflix_url} target='_blank' rel='noopener noreferrer'>
            <span className='detail-info-item'>{detail.netflix_url}</span>
          </a>
        </div>
        
      </div>

      <Recommendation idToRecommend={detail.id}/>
    </div>
  );
}
