import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

export default function Courses(){
  const [items, setItems] = useState<any[]>([])
  useEffect(()=>{
    api.get('/courses/').then(r=> setItems(r.data)).catch(()=>{})
  },[])

  return (
    <section>
      <h2>Courses</h2>
      <ul>
        {items.length ? items.map((c:any)=> (
          <li key={c.id}><Link to={`/courses/${c.id}`}>{c.title || c.name || JSON.stringify(c)}</Link></li>
        )) : <li>لا توجد دورات</li>}
      </ul>
    </section>
  )
}
