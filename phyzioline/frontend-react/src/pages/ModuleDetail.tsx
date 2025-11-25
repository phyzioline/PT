import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import api from '../services/api'

type Props = {
  moduleName?: string
}

export default function ModuleDetail({ moduleName: propModuleName }: Props){
  const params = useParams()
  const routeId = params.id
  // allow moduleName via prop or via path (we use prop from App routes)
  const moduleName = propModuleName || (params as any).module

  const [item, setItem] = useState<any>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (!moduleName || !routeId) return
    setLoading(true)
    api.get(`/content/modules/${moduleName}/${routeId}/`).then(r => setItem(r.data)).catch(() => setItem(null)).finally(() => setLoading(false))
  }, [moduleName, routeId])

  if (!moduleName) return <div>Missing module name</div>

  return (
    <div>
      <h2>{moduleName} / {routeId}</h2>
      {loading && <div>Loading…</div>}
      {!loading && !item && <div>Item not found.</div>}
      {item && (
        <pre style={{whiteSpace:'pre-wrap'}}>{JSON.stringify(item, null, 2)}</pre>
      )}
    </div>
  )
}
