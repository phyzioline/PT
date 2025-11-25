import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

type Props = {
  moduleName: string
  title?: string
}

export default function ModuleList({ moduleName, title }: Props){
  const [items, setItems] = useState<any[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let mounted = true
    setLoading(true)
    // For 'ads' prefer the DB-backed endpoint; otherwise use generic modules demo
    const path = moduleName === 'ads' ? `/content/ads/` : `/content/modules/${moduleName}/`
    api.get(path).then(r => {
      if (mounted) setItems(r.data || [])
    }).catch(() => setItems([])).finally(() => setLoading(false))
    return () => { mounted = false }
  }, [moduleName])

  return (
    <div>
      <h2>{title || moduleName}</h2>
      {loading && <div>Loading…</div>}
      {!loading && items.length === 0 && <div>No items found.</div>}
      <ul>
        {items.map(it => (
          <li key={it.id} style={{marginBottom:8}}>
            <Link to={`/${moduleName.replace('_','-')}/${it.id}`}>{it.title || it.name || it.username || it.metric || it.contact || (`Item ${it.id}`)}</Link>
            <div style={{fontSize:12,color:'#666'}}>{it.summary || it.company || it.city || JSON.stringify(it)}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}
