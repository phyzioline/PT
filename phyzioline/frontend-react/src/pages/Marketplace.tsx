import React, { useEffect, useState } from 'react'
import api from '../services/api'

export default function Marketplace(){
  const [items, setItems] = useState<any[]>([])
  useEffect(()=>{
    api.get('/marketplace/').then(r=> setItems(r.data)).catch(()=>{})
  },[])

  return (
    <section>
      <h2>Marketplace</h2>
      <ul>
        {items.length ? items.map((it:any)=> <li key={it.id}>{it.title || JSON.stringify(it)}</li>) : <li>لا توجد عناصر</li>}
      </ul>
    </section>
  )
}
