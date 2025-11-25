import React, { useEffect, useState } from 'react'
import api from '../services/api'

export default function Dashboard(){
  const [counts, setCounts] = useState({ ads:0, feed:0, courses:0, clinics:0, users:0 })

  useEffect(()=>{
    let mounted = true
    Promise.all([
      api.get('/content/ads/').then(r=> r.data.length).catch(()=>0),
      api.get('/content/modules/feed/').then(r=> r.data.length).catch(()=>0),
      api.get('/content/modules/courses/').then(r=> r.data.length).catch(()=>0),
      api.get('/content/modules/clinics/').then(r=> r.data.length).catch(()=>0),
      api.get('/content/modules/accounts/').then(r=> r.data.length).catch(()=>0),
    ]).then(([ads, feed, courses, clinics, users])=>{
      if (!mounted) return
      setCounts({ ads, feed, courses, clinics, users })
    })
    return ()=>{ mounted=false }
  },[])

  return (
    <div style={{padding:20}}>
      <header style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <div>
          <h1 style={{margin:0}}>لوحة التحكم — Phyzioline</h1>
          <div className="muted">نظرة عامة سريعة على المحتوى والتفاعل</div>
        </div>
        <div>
          <button className="action-btn">مشاركة</button>
        </div>
      </header>

      <section style={{marginTop:18,display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:14}}>
        <Card title="الإعلانات" value={counts.ads} color="#0b8583"/>
        <Card title="المشاركات" value={counts.feed} color="#0b6b85"/>
        <Card title="الدورات" value={counts.courses} color="#0b5b85"/>
        <Card title="العيادات" value={counts.clinics} color="#0b3b85"/>
      </section>

      <section style={{marginTop:24,display:'grid',gridTemplateColumns:'2fr 1fr',gap:18}}>
        <div>
          <div style={{background:'white',padding:12,borderRadius:8}}>
            <h3 style={{marginTop:0}}>آخر المشاركات</h3>
            <ul>
              {/* small preview list */}
              <FeedPreview limit={5} />
            </ul>
          </div>
        </div>
        <aside>
          <div style={{background:'white',padding:12,borderRadius:8}}>
            <h3 style={{marginTop:0}}>النشاط</h3>
            <div className="muted">لا توجد إشعارات</div>
          </div>
        </aside>
      </section>
    </div>
  )
}

function Card({ title, value, color }:{title:string,value:number,color?:string}){
  return (
    <div style={{background:'white',padding:16,borderRadius:10,display:'flex',justifyContent:'space-between',alignItems:'center'}}>
      <div>
        <div style={{fontSize:12,color:'#6b7280'}}>{title}</div>
        <div style={{fontSize:22,fontWeight:700}}>{value}</div>
      </div>
      <div style={{width:56,height:56,borderRadius:12,background:color||'#888'}}/>
    </div>
  )
}

function FeedPreview({ limit=5 }:{ limit?:number }){
  const [items,setItems] = useState<any[]>([])
  useEffect(()=>{
    api.get('/content/modules/feed/').then(r=> setItems(r.data || [])).catch(()=>setItems([]))
  },[])
  return (<>
    {items.slice(0,limit).map(it=> (
      <li key={it.id} style={{padding:'8px 0',borderBottom:'1px solid #f1f5f9'}}>
        <strong>{it.title}</strong>
        <div className="muted">{it.summary}</div>
      </li>
    ))}
  </>)
}
