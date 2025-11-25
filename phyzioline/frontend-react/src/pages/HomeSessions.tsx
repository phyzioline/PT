import React, { useEffect, useState } from 'react'
import api from '../services/api'

const DEMO_SESSIONS = [
  { id: 1, therapist: 'Dr. Sarah Lee', date: '2024-11-27', time: '10:00 AM', status: 'Scheduled', type: 'PT Session', rating: null },
  { id: 2, therapist: 'Dr. Mike Johnson', date: '2024-11-28', time: '2:00 PM', status: 'Scheduled', type: 'Consultation', rating: null },
  { id: 3, therapist: 'Dr. Emma Wilson', date: '2024-11-25', time: '3:30 PM', status: 'Completed', type: 'PT Session', rating: 4.8 },
  { id: 4, therapist: 'Dr. James Brown', date: '2024-11-24', time: '11:00 AM', status: 'Completed', type: 'Assessment', rating: 4.9 },
  { id: 5, therapist: 'Dr. Lisa Martinez', date: '2024-11-29', time: '9:00 AM', status: 'Scheduled', type: 'Yoga Therapy', rating: null },
  { id: 6, therapist: 'Dr. Robert Chen', date: '2024-11-30', time: '4:00 PM', status: 'Scheduled', type: 'Massage Therapy', rating: null }
]

export default function HomeSessions() {
  const [sessions, setSessions] = useState<any[]>([])
  const [filter, setFilter] = useState('all')
  const [showSchedule, setShowSchedule] = useState(false)
  const [scheduleData, setScheduleData] = useState({ date: '', time: '', type: 'PT Session', notes: '' })

  useEffect(() => {
    fetchSessions()
  }, [])

  const fetchSessions = async () => {
    try {
      const res = await api.get('/sessions/sessions/').catch(() => ({ data: DEMO_SESSIONS }))
      setSessions(res.data || DEMO_SESSIONS)
    } catch (err) {
      setSessions(DEMO_SESSIONS)
    }
  }

  const handleSchedule = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const res = await api.post('/sessions/schedule/', scheduleData)
      setSessions([...sessions, res.data])
      setScheduleData({ date: '', time: '', type: 'PT Session', notes: '' })
      setShowSchedule(false)
    } catch (err) {
      alert('Error scheduling session')
    }
  }

  const filtered = sessions.filter(s => filter === 'all' || s.status === filter)
  const upcoming = sessions.filter(s => s.status === 'Scheduled')
  const completed = sessions.filter(s => s.status === 'Completed')

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0, marginBottom: '0.5rem' }}>🏠 Home Therapy Sessions</h1>
        <p style={{ opacity: 0.9, margin: 0 }}>Your personalized at-home physical therapy sessions</p>
      </div>

      {/* Quick Stats */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
        <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>📅</div>
          <div style={{ fontSize: '1.5rem', fontWeight: 700, color: '#008080', marginBottom: '0.25rem' }}>{upcoming.length}</div>
          <div style={{ color: '#6b7280' }}>Upcoming Sessions</div>
        </div>
        <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>✅</div>
          <div style={{ fontSize: '1.5rem', fontWeight: 700, color: '#008080', marginBottom: '0.25rem' }}>{completed.length}</div>
          <div style={{ color: '#6b7280' }}>Completed</div>
        </div>
        <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)', textAlign: 'center' }}>
          <button
            onClick={() => setShowSchedule(!showSchedule)}
            style={{ width: '100%', background: '#008080', color: 'white', padding: '10px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}
          >
            {showSchedule ? 'Cancel' : 'Schedule New'}
          </button>
        </div>
      </div>

      {/* Schedule Form */}
      {showSchedule && (
        <form onSubmit={handleSchedule} style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          <h3 style={{ margin: 0, marginBottom: '1rem' }}>Schedule New Session</h3>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
            <input
              type="date"
              value={scheduleData.date}
              onChange={(e) => setScheduleData({ ...scheduleData, date: e.target.value })}
              required
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
            <input
              type="time"
              value={scheduleData.time}
              onChange={(e) => setScheduleData({ ...scheduleData, time: e.target.value })}
              required
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
          </div>
          <select
            value={scheduleData.type}
            onChange={(e) => setScheduleData({ ...scheduleData, type: e.target.value })}
            style={{ width: '100%', padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px', marginBottom: '1rem' }}
          >
            <option value="PT Session">PT Session</option>
            <option value="Yoga Therapy">Yoga Therapy</option>
            <option value="Massage Therapy">Massage Therapy</option>
            <option value="Consultation">Consultation</option>
          </select>
          <textarea
            placeholder="Special notes (optional)"
            value={scheduleData.notes}
            onChange={(e) => setScheduleData({ ...scheduleData, notes: e.target.value })}
            style={{ width: '100%', padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px', marginBottom: '1rem', fontFamily: 'inherit' }}
            rows={2}
          />
          <button type="submit" style={{ background: '#008080', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>Schedule</button>
        </form>
      )}

      {/* Filter */}
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '2rem', flexWrap: 'wrap' }}>
        {['all', 'Scheduled', 'Completed'].map(status => (
          <button
            key={status}
            onClick={() => setFilter(status)}
            style={{
              padding: '8px 16px',
              border: filter === status ? '2px solid #008080' : '2px solid #e5e7eb',
              background: filter === status ? '#008080' : 'white',
              color: filter === status ? 'white' : '#333',
              borderRadius: '6px',
              cursor: 'pointer',
              fontWeight: 600
            }}
          >
            {status}
          </button>
        ))}
      </div>

      {/* Sessions List */}
      <div style={{ display: 'grid', gap: '1rem' }}>
        {filtered.map(session => (
          <div key={session.id} style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)', borderLeft: `4px solid ${session.status === 'Scheduled' ? '#008080' : '#38B2AC'}` }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
              <div>
                <h3 style={{ margin: 0, marginBottom: '0.5rem', fontSize: '1.1rem', fontWeight: 600 }}>{session.therapist}</h3>
                <div style={{ color: '#6b7280', fontSize: '0.9rem' }}>📋 {session.type}</div>
              </div>
              <span style={{ background: session.status === 'Scheduled' ? '#008080' : '#38B2AC', color: 'white', padding: '6px 12px', borderRadius: '4px', fontSize: '0.8rem', fontWeight: 600 }}>
                {session.status}
              </span>
            </div>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem', color: '#6b7280' }}>
              <div>📅 {session.date}</div>
              <div>🕐 {session.time}</div>
            </div>
            {session.status === 'Completed' && session.rating && (
              <div style={{ marginTop: '1rem', padding: '1rem', background: '#f9fafb', borderRadius: '6px', color: '#6b7280' }}>
                Rating: ⭐ {session.rating}
              </div>
            )}
            {session.status === 'Scheduled' && (
              <button style={{
                background: '#008080', color: 'white', padding: '8px 16px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>
                Join Session
              </button>
            )}
          </div>
        ))}
    </div>
    </div >
  )
}
