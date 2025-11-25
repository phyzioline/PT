import React, { useEffect, useState } from 'react'
import api from '../services/api'

export default function Accounts(){
  const [items, setItems] = useState<any[]>([])
  useEffect(()=>{
    api.get('/accounts/').then(r=> setItems(r.data)).catch(()=>{})
  },[])

  return (
    <section>
      <h2>Accounts (قائمة المستخدمين)</h2>
      <ul>
        {items.length ? items.map((u:any)=> <li key={u.id}>{u.username || JSON.stringify(u)}</li>) : <li>لا توجد بيانات</li>}
      </ul>
    </section>
  )
}
