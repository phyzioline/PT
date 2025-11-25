import React from 'react'
import { Link } from 'react-router-dom'

export default function Sidebar(){
  return (
    <aside style={{width:240,background:'#fff',padding:12,borderRadius:8,border:'1px solid #f1f5f9'}}>
      <div style={{fontWeight:700,marginBottom:8}}>القوائم</div>
      <ul style={{listStyle:'none',padding:0,margin:0}}>
        <li style={{marginBottom:8}}><Link to='/feed'>Feed</Link></li>
        <li style={{marginBottom:8}}><Link to='/ads'>Ads</Link></li>
        <li style={{marginBottom:8}}><Link to='/courses'>Courses</Link></li>
        <li style={{marginBottom:8}}><Link to='/clinics'>Clinics</Link></li>
        <li style={{marginBottom:8}}><Link to='/marketplace'>Marketplace</Link></li>
        <li style={{marginBottom:8}}><Link to='/jobs'>Jobs</Link></li>
        <li style={{marginBottom:8}}><Link to='/ai'>AI Engine</Link></li>
        <li style={{marginBottom:8}}><Link to='/crm'>CRM</Link></li>
        <li style={{marginBottom:8}}><Link to='/global-stats'>Global Stats</Link></li>
      </ul>
    </aside>
  )
}
