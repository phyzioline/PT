import React, { useEffect, useState } from 'react'
import api from '../services/api'

const DEMO_STATS = {
  metrics: [
    { label: 'Total Users', value: '45,230', change: '+12%', icon: '👥' },
    { label: 'Active Sessions', value: '3,421', change: '+28%', icon: '🎯' },
    { label: 'Total Revenue', value: '$185,490', change: '+45%', icon: '💰' },
    { label: 'New Signups', value: '1,240', change: '+8%', icon: '📈' }
  ],
  countries: [
    { id: 1, country: 'United States', therapists: 1200, users: 15000, rating: 4.9 },
    { id: 2, country: 'Canada', therapists: 450, users: 5200, rating: 4.8 },
    { id: 3, country: 'UK', therapists: 680, users: 8100, rating: 4.7 },
    { id: 4, country: 'Australia', therapists: 320, users: 3500, rating: 4.8 },
    { id: 5, country: 'Germany', therapists: 540, users: 6200, rating: 4.6 },
    { id: 6, country: 'India', therapists: 890, users: 12000, rating: 4.5 }
  ],
  trends: [
    { week: 'Week 1', users: 1200, sessions: 450, revenue: 12000 },
    { week: 'Week 2', users: 1450, sessions: 520, revenue: 14500 },
    { week: 'Week 3', users: 1680, sessions: 610, revenue: 16800 },
    { week: 'Week 4', users: 1920, sessions: 720, revenue: 19200 }
  ]
}

export default function GlobalStats(){
  const [countries, setCountries] = useState<any[]>([])
  const [timePeriod, setTimePeriod] = useState('month')

  useEffect(()=>{
    fetchStats()
  },[])

  const fetchStats = async () => {
    try {
      const res = await api.get('/global-stats/snapshots/').catch(() => ({ data: DEMO_STATS.countries }))
      setCountries(res.data || DEMO_STATS.countries)
    } catch (err) {
      setCountries(DEMO_STATS.countries)
    }
  }

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0, marginBottom: '0.5rem' }}>📊 Global Statistics</h1>
        <p style={{ opacity: 0.9, margin: 0 }}>Platform analytics and performance metrics</p>
      </div>

      {/* Time Period Selector */}
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '2rem' }}>
        {['week', 'month', 'year'].map(period => (
          <button
            key={period}
            onClick={() => setTimePeriod(period)}
            style={{
              padding: '8px 16px',
              border: timePeriod === period ? '2px solid #008080' : '2px solid #e5e7eb',
              background: timePeriod === period ? '#008080' : 'white',
              color: timePeriod === period ? 'white' : '#333',
              borderRadius: '6px',
              cursor: 'pointer',
              fontWeight: 600
            }}
          >
            {period.charAt(0).toUpperCase() + period.slice(1)}
          </button>
        ))}
      </div>

      {/* Key Metrics */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1.5rem', marginBottom: '2rem' }}>
        {DEMO_STATS.metrics.map((metric, i) => (
          <div key={i} style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <div style={{ fontSize: '2rem' }}>{metric.icon}</div>
              <span style={{ background: '#e6f7f7', color: '#008080', padding: '4px 8px', borderRadius: '4px', fontSize: '0.85rem', fontWeight: 600 }}>
                {metric.change}
              </span>
            </div>
            <div style={{ fontSize: '0.9rem', color: '#6b7280', marginBottom: '0.5rem' }}>{metric.label}</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 700, color: '#008080' }}>{metric.value}</div>
          </div>
        ))}
      </div>

      {/* Chart Placeholder */}
      <div style={{ background: 'white', padding: '2rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
        <h2 style={{ fontSize: '1.2rem', fontWeight: 600, margin: 0, marginBottom: '1.5rem' }}>Trends ({timePeriod})</h2>
        <div style={{ height: '300px', background: '#f9fafb', borderRadius: '8px', display: 'flex', alignItems: 'flex-end', justifyContent: 'space-around', padding: '1rem', gap: '1rem' }}>
          {DEMO_STATS.trends.map((t, i) => (
            <div key={i} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <div style={{ background: '#008080', width: '60%', height: `${(t.users / 30)}%`, borderRadius: '4px', minHeight: '40px', marginBottom: '0.5rem' }} />
              <div style={{ fontSize: '0.8rem', color: '#6b7280', textAlign: 'center' }}>{t.week}</div>
              <div style={{ fontSize: '0.9rem', fontWeight: 600, color: '#008080' }}>{t.users}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Regional Data Table */}
      <div style={{ background: 'white', borderRadius: '10px', overflow: 'hidden', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
        <h2 style={{ fontSize: '1.2rem', fontWeight: 600, padding: '1.5rem', margin: 0, borderBottom: '2px solid #e5e7eb' }}>Regional Breakdown</h2>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ background: '#f9fafb', borderBottom: '2px solid #e5e7eb' }}>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Country</th>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Therapists</th>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Active Users</th>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Rating</th>
            </tr>
          </thead>
          <tbody>
            {countries.map((country, i) => (
              <tr key={country.id} style={{ borderBottom: '1px solid #e5e7eb', background: i % 2 === 0 ? 'white' : '#f9fafb' }}>
                <td style={{ padding: '1rem' }}>{country.country}</td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>{country.therapists}</td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>{country.users || country.population}</td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>⭐ {country.rating}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
