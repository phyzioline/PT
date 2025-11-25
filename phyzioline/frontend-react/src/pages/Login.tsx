import React, { useState } from 'react'
import api from '../services/api'

export default function Login(){
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string | null>(null)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    try{
      const res = await api.post('/token/', { username, password })
      localStorage.setItem('accessToken', res.data.access)
      localStorage.setItem('refreshToken', res.data.refresh)
      window.location.href = '/'
    }catch(err:any){
      setError(err.response?.data?.detail || 'Login failed')
    }
  }

  return (
    <section>
      <h2>تسجيل الدخول</h2>
      <form onSubmit={submit} style={{maxWidth:400}}>
        <div>
          <label>Username</label>
          <input value={username} onChange={e=>setUsername(e.target.value)} className="p-2 w-full" />
        </div>
        <div className="mt-2">
          <label>Password</label>
          <input type="password" value={password} onChange={e=>setPassword(e.target.value)} className="p-2 w-full" />
        </div>
        {error && <div style={{color:'red'}}>{error}</div>}
        <div className="mt-2">
          <button className="p-2 bg-[#008080] text-white rounded">Login</button>
        </div>
      </form>
    </section>
  )
}
