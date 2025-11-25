import React from 'react'
import { Link } from 'react-router-dom'

export default function Header(){
  return (
    <header style={{background:'#008080',color:'white'}}>
      <div style={{maxWidth:1100,margin:'0 auto',padding:'1rem',display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <div style={{display:'flex',alignItems:'center',gap:12}}>
          <div style={{width:40,height:40,background:'rgba(255,255,255,0.12)',borderRadius:8,display:'flex',alignItems:'center',justifyContent:'center'}}>P</div>
          <strong>Phyzioline</strong>
        </div>
        <nav style={{display:'flex',gap:12}}>
          <Link to="/">الاستكشاف</Link>
          <Link to="/accounts">الحسابات</Link>
          <Link to="/marketplace">السوق</Link>
          <Link to="/jobs">الوظائف</Link>
        </nav>
      </div>
    </header>
  )
}
