import React, { useEffect, useState } from 'react'
import api from '../services/api'

export default function Jobs(){
  const [items, setItems] = useState<any[]>([])
  useEffect(()=>{
    api.get('/jobs/').then(r=> setItems(r.data)).catch(()=>{})
  },[])

  return (
    <section>
      <h2>Jobs</h2>
      <ul>
        {items.length ? items.map((j:any)=> <li key={j.id}>{j.title || JSON.stringify(j)}</li>) : <li>لا توجد وظائف</li>}
      </ul>
    </section>
  )
}
