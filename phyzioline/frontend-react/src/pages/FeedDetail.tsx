import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import api from '../services/api'

export default function FeedDetail(){
  const { id } = useParams()
  const [item, setItem] = useState<any>(null)
  useEffect(()=>{
    if (id) api.get(`/feed/posts/${id}/`).then(r=> setItem(r.data)).catch(()=>{})
  },[id])

  if (!item) return <p>جاري التحميل...</p>
  return (
    <section>
      <div className="feed-card">
        <div className="feed-header">
          <div className="avatar">{(item.author||item.title||'U').slice(0,1)}</div>
          <div className="feed-meta">
            <div className="feed-title">{item.title || item.text}</div>
            <div className="feed-time muted">{item.author || 'مستخدم'} • {item.year || ''}</div>
          </div>
        </div>
        {item.summary && <div className="feed-body">{item.summary}</div>}
        <div className="feed-media" style={{height:260}}>
          {item.image ? <img src={item.image} alt={item.title} /> : <div style={{fontWeight:700,color:'#0b7285'}}>صورة معاينة</div>}
        </div>
      </div>
    </section>
  )
}
