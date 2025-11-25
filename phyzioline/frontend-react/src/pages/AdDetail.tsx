import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import api from '../services/api'

export default function AdDetail(){
  const { id } = useParams()
  const [ad, setAd] = useState<any>(null)
  useEffect(()=>{
    if (!id) return
    api.get(`/ads/ads/${id}/`).then(r=> setAd(r.data)).catch(()=> setAd(null))
  },[id])
  if (!ad) return <div className='muted'>Loading...</div>
  return (
    <section style={{maxWidth:800,margin:'0 auto'}}>
      <h2>{ad.title}</h2>
      <div className='muted'>{ad.description}</div>
      {ad.image && <img src={ad.image} alt={ad.title} style={{width:'100%',marginTop:12}} />}
    </section>
  )
}
