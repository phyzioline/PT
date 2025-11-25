import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import api from '../services/api'

export default function CourseDetail(){
  const { id } = useParams()
  const [item, setItem] = useState<any>(null)
  useEffect(()=>{
    if (id) api.get(`/courses/${id}/`).then(r=> setItem(r.data)).catch(()=>{})
  },[id])

  if (!item) return <p>جاري التحميل...</p>
  return (
    <section>
      <h2>{item.title || item.name}</h2>
      <div>{item.description || JSON.stringify(item)}</div>
    </section>
  )
}
