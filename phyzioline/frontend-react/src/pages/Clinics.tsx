import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

export default function Clinics(){
  const [items, setItems] = useState<any[]>([])
  useEffect(()=>{
    api.get('/clinics/').then(r=> setItems(r.data)).catch(()=>{})
  },[])

  return (
    <section>
      <h2>Clinics</h2>
      <ul>
        {items.length ? items.map((c:any)=> (
          <li key={c.id}><Link to={`/clinics/${c.id}`}>{c.name || JSON.stringify(c)}</Link></li>
        )) : <li>لا توجد عيادات</li>}
      </ul>
    </section>
  )
}
