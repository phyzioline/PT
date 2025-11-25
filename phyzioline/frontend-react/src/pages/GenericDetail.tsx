import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import api from '../services/api'

// A fallback generic detail page for modules we can't specialize yet.
export default function GenericDetail({ base }:{base?:string}){
  const params:any = useParams()
  const id = params.id || params.pk
  const moduleBase = base || params.module
  const [data, setData] = useState<any>(null)

  useEffect(()=>{
    if (!moduleBase || !id) return
    // try common patterns
    const tryPaths = [
      `/${moduleBase}/${id}/`,
      `/${moduleBase}s/${id}/`,
      `/${moduleBase}/${id}`,
      `/${moduleBase}s/${id}`,
    ]
    let found = false
    ;(async ()=>{
      for(const p of tryPaths){
        try{
          const r = await api.get(p)
          setData(r.data); found=true; break
        }catch(e){ /* ignore */ }
      }
      if (!found) setData({ error: 'Not found' })
    })()
  },[moduleBase,id])

  if (!data) return <div className='muted'>Loading...</div>
  return (
    <section style={{maxWidth:900,margin:'0 auto'}}>
      <pre style={{whiteSpace:'pre-wrap'}}>{JSON.stringify(data,null,2)}</pre>
    </section>
  )
}
