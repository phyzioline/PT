import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

export default function Feed(){
  const [items, setItems] = useState<any[]>([])

  useEffect(()=>{
    // use demo modules feed endpoint
    api.get('/content/modules/feed/').then(r=> setItems(r.data || [])).catch(()=> setItems([]))
  },[])

  return (
    <section>
      <h2 style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <span>آخر المشاركات</span>
        <span className="pill">Feed</span>
      </h2>

      <div className="feed-container">
        <div className="feed-main">
          {items.length === 0 && <div className="muted">لا توجد منشورات لعرضها.</div>}
          {items.map((f:any) => (
            <article key={f.id} className="feed-card">
              <div className="feed-header">
                <div className="avatar">{(f.author || f.title || 'U').slice(0,1)}</div>
                <div className="feed-meta">
                  <div className="feed-title">{f.title || f.text || 'منشور'}</div>
                  <div className="feed-time muted">{f.author || 'مستخدم'} • {f.year || ''}</div>
                </div>
                <div style={{display:'flex',gap:8}}>
                  <button className="action-btn">•••</button>
                </div>
              </div>

              {f.summary && <div className="feed-body">{f.summary}</div>}

              <div className="feed-media">
                {/* placeholder image or color block */}
                {f.image ? <img src={f.image} alt={f.title} /> : <div style={{color:'#0b7285',fontWeight:700}}>صورة معاينة</div>}
              </div>

              <div className="feed-actions">
                <LikeButton initial={f.likes || 0} />
                <Link to={`/feed/${f.id}`} className="action-btn">عرض التفاصيل</Link>
                <button className="action-btn">مشاركة</button>
              </div>
            </article>
          ))}
        </div>

        <aside className="feed-sidebar">
          <div className="story-card">
            <strong>إنشاء منشور</strong>
            <div style={{marginTop:8}}>
              <input placeholder="ماذا تريد أن تشارك؟" style={{width:'100%',padding:8,borderRadius:6,border:'1px solid #e6e8eb'}} />
            </div>
          </div>
          <div style={{height:12}}/>
          <div className="story-card">
            <strong>جهات الاتصال</strong>
            <div className="muted" style={{marginTop:8}}>قائمة سريعة للمستخدمين</div>
          </div>
        </aside>
      </div>
    </section>
  )
}

function LikeButton({ initial=0 }: { initial?: number }){
  const [count, setCount] = useState(initial)
  const [liked, setLiked] = useState(false)
  return (
    <button
      onClick={() => { setLiked(!liked); setCount(c => liked ? c-1 : c+1) }}
      className={"action-btn" + (liked ? ' liked' : '')}
    >
      {liked ? 'إعجاب' : 'أعجبني'} {count>0 && `· ${count}`}
    </button>
  )
}
