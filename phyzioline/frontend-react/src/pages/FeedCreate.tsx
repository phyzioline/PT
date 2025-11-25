import React, { useState } from 'react'
import api from '../services/api'

export default function FeedCreate(){
  const [content, setContent] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function submit(e:any){
    e.preventDefault()
    setLoading(true); setError('')
    try{
      const r = await api.post('/feed/posts/', { content })
      alert('Posted!')
      setContent('')
    }catch(err:any){
      setError(err?.response?.data || 'Error')
    }finally{ setLoading(false) }
  }

  return (
    <section style={{maxWidth:800,margin:'0 auto'}}>
      <h2>Create Post</h2>
      <form onSubmit={submit}>
        <textarea value={content} onChange={e=>setContent(e.target.value)} placeholder='Write something...' style={{width:'100%',minHeight:120,padding:8}} />
        <div style={{marginTop:8}}>
          <button disabled={loading} className='action-btn' type='submit'>{loading ? 'Posting...' : 'Post'}</button>
        </div>
        {error && <div style={{color:'red',marginTop:8}}>{JSON.stringify(error)}</div>}
      </form>
    </section>
  )
}
