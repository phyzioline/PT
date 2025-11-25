import React from 'react'
import { Link } from 'react-router-dom'

export default function Header(){
  return (
    <header style={{background:'white',padding:'12px 20px',borderBottom:'1px solid #eef2f7'}}>
      <div style={{maxWidth:1100,margin:'0 auto',display:'flex',alignItems:'center',justifyContent:'space-between'}}>
        <Link to='/' style={{display:'flex',alignItems:'center',gap:10,textDecoration:'none'}}>
          <div style={{width:40,height:40,background:'#008080',color:'white',borderRadius:8,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:700}}>P</div>
          <div style={{fontWeight:700,color:'#0f1724'}}>Phyzioline</div>
        </Link>
        <nav>
          <Link to='/feed' style={{marginRight:12}}>Feed</Link>
          <Link to='/courses' style={{marginRight:12}}>Courses</Link>
          <Link to='/marketplace' style={{marginRight:12}}>Marketplace</Link>
          <Link to='/ads' style={{marginRight:12}}>Ads</Link>
          <Link to='/dashboard' style={{marginRight:12}}>Dashboard</Link>
        </nav>
      </div>
    </header>
  )
}
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
