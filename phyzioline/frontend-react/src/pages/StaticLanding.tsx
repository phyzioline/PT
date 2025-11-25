import React, { useEffect, useState } from 'react'
import api from '../services/api'

type LinkItem = { id?: number; title: string; url: string }

export default function StaticLanding(){
  const [links, setLinks] = useState<LinkItem[]>([])
  const [loading, setLoading] = useState(true)
  const [isAdmin, setIsAdmin] = useState(false)
  const [editing, setEditing] = useState<LinkItem | null>(null)

  useEffect(()=>{
    const fetchLinks = async () => {
      try {
        // use the full API prefix
        const res = await api.get('/api/v1/content/modules/?module=mirror-index').catch(()=> ({ data: null }))
        if (res && res.data && Array.isArray(res.data.items)){
          setLinks(res.data.items.map((i: any)=> ({ id: i.id, title: i.title, url: i.url })))
        } else {
          // fallback to local mirrored files
          setLinks([
            { title: 'Student Dashboard — Ask Your Doctor', url: '/static/phyzioline.vercel.app/client-dashboard/student-dashboard.html' },
            { title: 'Ask Your Doctor — Medical Platform', url: '/static/phyzioline.vercel.app/website/index.html' }
          ])
        }
      } catch (err){
        setLinks([
          { title: 'Student Dashboard — Ask Your Doctor', url: '/static/phyzioline.vercel.app/client-dashboard/student-dashboard.html' },
          { title: 'Ask Your Doctor — Medical Platform', url: '/static/phyzioline.vercel.app/website/index.html' }
        ])
      }
      setLoading(false)
    }

    const checkAdmin = async () => {
      try {
        const profile = await api.get('/api/v1/profile/').catch(()=> ({ data: null }))
        if (profile && profile.data && (profile.data.is_staff || profile.data.is_superuser)) setIsAdmin(true)
      } catch (e){}
    }

    fetchLinks(); checkAdmin();
  },[])

  const startEdit = (item: LinkItem) => setEditing(item)
  const saveEdit = async (updated: LinkItem) => {
    // attempt to persist via API if id exists
    if (updated.id){
      try{
        // attempt to persist using full API path
        await api.put(`/api/v1/content/modules/${updated.id}/`, updated)
      }catch(e){
        // ignore - show local update
      }
    }
    setLinks(links.map(l=> l.id === updated.id ? updated : (l.url === editing?.url ? updated : l)))
    setEditing(null)
  }

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg,#008080 0%,#006666 100%)', color: 'white', borderRadius: 12, padding: '2rem', marginBottom: '1.5rem' }}>
        <h1 style={{ margin: 0, fontSize: '1.9rem' }}>Local Index — Mirrored Pages</h1>
        <p style={{ margin: '6px 0 0', opacity: 0.95 }}>A converted React page of the local static index. Click the items below to open the mirrored pages.</p>
      </div>

      {loading ? <div style={{ color: '#6b7280' }}>Loading...</div> : (
        <div style={{ display: 'grid', gap: 12 }}>
          {links.map(link => (
            <div key={link.url} style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
              <a href={link.url} target="_blank" rel="noreferrer" style={{ flex: 1, display: 'block', padding: 16, borderRadius: 8, background: '#fff', boxShadow: '0 6px 18px rgba(2,6,23,0.06)', textDecoration: 'none', color: '#0f172a', fontWeight: 700 }}>
                {link.title}
                <div style={{ fontWeight: 500, color: '#6b7280', fontSize: 13 }}>{link.url}</div>
              </a>
              {isAdmin && (
                <div style={{ display: 'flex', gap: 6 }}>
                  <button onClick={() => startEdit(link)} style={{ padding: '8px 12px', borderRadius: 8, border: '1px solid #e6eef0', background: 'white' }}>Edit</button>
                </div>
              )}
            </div>
          ))}

          <div style={{ background: 'white', padding: 16, borderRadius: 8, boxShadow: '0 6px 18px rgba(2,6,23,0.04)' }}>
            <h3 style={{ margin: 0, marginBottom: 8 }}>Notes</h3>
            <ul style={{ margin: 0, paddingLeft: 18, color: '#374151' }}>
              <li>These links point to the mirrored static HTML from the project folder.</li>
              <li>If the pages don't open, ensure Django is serving static files or open the HTML files directly in the browser.</li>
              <li>You can convert each mirrored HTML page into a React component for tighter integration.</li>
            </ul>
          </div>
        </div>
      )}

      {/* Edit modal (simple inline) */}
      {editing && (
        <div style={{ position: 'fixed', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'rgba(2,6,23,0.4)' }}>
          <div style={{ background: 'white', padding: 16, borderRadius: 8, width: 600 }}>
            <h4 style={{ marginTop: 0 }}>Edit Link</h4>
            <div style={{ display: 'grid', gap: 8 }}>
              <input value={editing.title} onChange={(e)=> setEditing({...editing, title: e.target.value})} style={{ padding: 10, border: '1px solid #e6eef0', borderRadius: 6 }} />
              <input value={editing.url} onChange={(e)=> setEditing({...editing, url: e.target.value})} style={{ padding: 10, border: '1px solid #e6eef0', borderRadius: 6 }} />
              <div style={{ display: 'flex', gap: 8, justifyContent: 'flex-end' }}>
                <button onClick={()=> setEditing(null)} style={{ padding: '8px 12px', borderRadius: 6 }}>Cancel</button>
                <button onClick={()=> editing && saveEdit(editing)} style={{ padding: '8px 12px', borderRadius: 6, background: '#008080', color: 'white' }}>Save</button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
