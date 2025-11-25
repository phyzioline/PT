import React, { useState } from 'react'
import { Link } from 'react-router-dom'

const modules = [
  { key: 'feed', label: 'Feed', to: '/feed', icon: '📰' },
  { key: 'clinics', label: 'Clinics', to: '/clinics', icon: '🏥' },
  { key: 'courses', label: 'Courses', to: '/courses', icon: '📚' },
  { key: 'jobs', label: 'Jobs', to: '/jobs', icon: '💼' },
  { key: 'marketplace', label: 'Marketplace', to: '/marketplace', icon: '🛍️' },
  { key: 'ads', label: 'Ads', to: '/ads', icon: '📣' },
  { key: 'ai', label: 'AI Engine', to: '/ai', icon: '🤖' },
  { key: 'crm', label: 'CRM', to: '/crm', icon: '👥' },
  { key: 'equivalency', label: 'Equivalency', to: '/equivalency', icon: '⚖️' },
  { key: 'global-stats', label: 'Global Stats', to: '/global-stats', icon: '📈' },
  { key: 'home-sessions', label: 'Home Sessions', to: '/home-sessions', icon: '🏠' },
  { key: 'payments', label: 'Payments', to: '/payments', icon: '💳' },
  { key: 'dashboard', label: 'Dashboard', to: '/dashboard', icon: '📊' }
]

export default function Header(){
  const [open, setOpen] = useState(false)

  return (
    <header style={{background:'white',padding:'8px 12px',borderBottom:'1px solid #eef2f7',position:'sticky',top:0,zIndex:40}}>
      <div style={{maxWidth:1100,margin:'0 auto',display:'flex',alignItems:'center',justifyContent:'space-between'}}>
        <Link to='/' style={{display:'flex',alignItems:'center',gap:10,textDecoration:'none'}}>
          <div style={{width:44,height:44,background:'#008080',color:'white',borderRadius:10,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:700}}>P</div>
          <div style={{fontWeight:800,color:'#0f1724'}}>Phyzioline</div>
        </Link>

        <nav style={{display:'flex',alignItems:'center',gap:8}}>
          <div style={{display:'flex',gap:8,alignItems:'center'}}>
            <Link to='/' style={{padding:'8px 12px',textDecoration:'none',color:'#0f1724'}}>Home</Link>
            <Link to='/marketplace' style={{padding:'8px 12px',textDecoration:'none',color:'#0f1724'}}>Store</Link>
          </div>

          <div style={{position:'relative'}} onMouseLeave={() => setOpen(false)}>
            <button onClick={() => setOpen(!open)} style={{padding:'8px 12px',border:'1px solid #e6eef0',background:'white',borderRadius:8,cursor:'pointer'}} aria-expanded={open}>
              Modules ▾
            </button>

            {open && (
              <div style={{position:'absolute',right:0,top:'calc(100% + 8px)',background:'white',border:'1px solid #e6eef0',boxShadow:'0 10px 30px rgba(2,6,23,0.08)',borderRadius:8,padding:12,width:360}}>
                <div style={{display:'grid',gridTemplateColumns:'repeat(2,1fr)',gap:8}}>
                  {modules.map(m => (
                    <Link key={m.key} to={m.to} onClick={() => setOpen(false)} style={{display:'flex',alignItems:'center',gap:8,padding:'8px 10px',borderRadius:6,textDecoration:'none',color:'#0f1724',border:'1px solid transparent'}}>
                      <span style={{fontSize:18}}>{m.icon}</span>
                      <span>{m.label}</span>
                    </Link>
                  ))}
                </div>
              </div>
            )}
          </div>

          <button onClick={() => { const nav = document.getElementById('mobile-menu'); if (nav) nav.style.display = nav.style.display === 'block' ? 'none' : 'block' }} style={{display:'none',padding:'8px',borderRadius:8}}>☰</button>

          <Link to='/auth/login' style={{padding:'8px 12px',textDecoration:'none',color:'#008080',border:'1px solid #e6eef0',borderRadius:8}}>Login</Link>
        </nav>
      </div>

      {/* Mobile menu (hidden by default, simple toggle) */}
      <div id="mobile-menu" style={{display:'none',borderTop:'1px solid #eef2f7',background:'white'}}>
        <div style={{maxWidth:1100,margin:'0 auto',padding:12,display:'flex',flexDirection:'column',gap:8}}>
          {modules.map(m => (
            <Link key={m.key} to={m.to} style={{padding:'10px',borderRadius:6,textDecoration:'none',color:'#0f1724'}}>{m.icon} {m.label}</Link>
          ))}
        </div>
      </div>
    </header>
  )
}
