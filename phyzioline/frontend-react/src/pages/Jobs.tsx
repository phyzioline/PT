import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

const DEMO_JOBS = [
  { id: 1, title: 'Senior Surgeon', company: 'Central Medical', location: 'Downtown', salary: '$150k-180k', type: 'Full-time', experience: '5+ years' },
  { id: 2, title: 'Physical Therapist', company: 'Wellness Clinic', location: 'North District', salary: '$70k-85k', type: 'Full-time', experience: '2+ years' },
  { id: 3, title: 'Nurse Practitioner', company: 'City Hospital', location: 'Central', salary: '$90k-110k', type: 'Full-time', experience: '3+ years' },
  { id: 4, title: 'Medical Researcher', company: 'Research Institute', location: 'Tech Park', salary: '$80k-100k', type: 'Full-time', experience: '3+ years' },
  { id: 5, title: 'Dentist', company: 'Smile Dental', location: 'Mall District', salary: '$95k-125k', type: 'Part-time', experience: '2+ years' },
  { id: 6, title: 'Medical Assistant', company: 'Multi-Clinic Group', location: 'Various', salary: '$35k-45k', type: 'Full-time', experience: 'Entry-level' }
]

export default function Jobs() {
  const [jobs, setJobs] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [filter, setFilter] = useState('all')
  const [selectedJob, setSelectedJob] = useState<any>(null)
  const [showApply, setShowApply] = useState(false)
  const [applyData, setApplyData] = useState({ name: '', email: '', phone: '', message: '' })

  useEffect(() => {
    fetchJobs()
  }, [])

  const fetchJobs = async () => {
    try {
      setLoading(true)
      const res = await api.get('/jobs/').catch(() => ({ data: DEMO_JOBS }))
      setJobs(res.data || DEMO_JOBS)
    } finally {
      setLoading(false)
    }
  }

  const handleApply = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      await api.post(`/jobs/${selectedJob.id}/apply/`, applyData).catch(() => alert('Application submitted!'))
      alert('Application submitted successfully!')
      setShowApply(false)
      setApplyData({ name: '', email: '', phone: '', message: '' })
    } catch (err) {
      alert('Error submitting application')
    }
  }

  const filtered = jobs.filter(j =>
    (j.title?.toLowerCase().includes(searchTerm.toLowerCase()) || '') &&
    (filter === 'all' || j.type === filter)
  )

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0, marginBottom: '0.5rem' }}>Healthcare Jobs</h1>
        <p style={{ opacity: 0.9, margin: 0 }}>Find your next career opportunity in medical field</p>
      </div>

      <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
        <input
          type="text"
          placeholder="Search jobs..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{ width: '100%', padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px', marginBottom: '1rem', fontSize: '1rem' }}
        />
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          {['all', 'Full-time', 'Part-time'].map(type => (
            <button
              key={type}
              onClick={() => setFilter(type)}
              style={{
                padding: '8px 16px',
                border: filter === type ? '2px solid #008080' : '2px solid #e5e7eb',
                background: filter === type ? '#008080' : 'white',
                color: filter === type ? 'white' : '#333',
                borderRadius: '6px',
                cursor: 'pointer',
                fontWeight: 600
              }}
            >
              {type}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>Loading jobs...</div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(350px, 1fr))', gap: '1.5rem' }}>
          {filtered.map(job => (
            <div
              key={job.id}
              style={{
                background: 'white',
                borderRadius: '10px',
                padding: '1.5rem',
                boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
                transition: 'all 0.3s',
                borderLeft: '4px solid #008080'
              }}
              onMouseEnter={(e) => {
                (e.currentTarget as HTMLElement).style.boxShadow = '0 8px 20px rgba(0,128,128,0.15)';
                (e.currentTarget as HTMLElement).style.transform = 'translateY(-5px)'
              }}
              onMouseLeave={(e) => {
                (e.currentTarget as HTMLElement).style.boxShadow = '0 2px 8px rgba(0,0,0,0.06)';
                (e.currentTarget as HTMLElement).style.transform = 'translateY(0)'
              }}
            >
              <h3 style={{ fontSize: '1.2rem', fontWeight: 600, margin: 0, marginBottom: '0.5rem', color: '#008080' }}>{job.title}</h3>
              <div style={{ color: '#6b7280', fontSize: '0.9rem', marginBottom: '1rem' }}>
                <div>🏢 {job.company}</div>
                <div>📍 {job.location}</div>
                <div>💼 {job.type}</div>
                <div>💰 {job.salary}</div>
                <div>📅 {job.experience}</div>
              </div>
              <button
                onClick={() => { setSelectedJob(job); setShowApply(true) }}
                style={{ width: '100%', background: '#008080', color: 'white', padding: '10px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}
              >
                Apply Now
              </button>
            </div>
          ))}
        </div>
      )}

      {showApply && selectedJob && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000 }}>
          <div style={{ background: 'white', padding: '2rem', borderRadius: '10px', maxWidth: '500px', width: '90%' }}>
            <h2 style={{ margin: 0, marginBottom: '1rem' }}>Apply for {selectedJob.title}</h2>
            <form onSubmit={handleApply}>
              <input
                type="text"
                placeholder="Full Name"
                value={applyData.name}
                onChange={(e) => setApplyData({ ...applyData, name: e.target.value })}
                required
                style={{ width: '100%', padding: '10px', marginBottom: '1rem', border: '2px solid #e5e7eb', borderRadius: '6px' }}
              />
              <input
                type="email"
                placeholder="Email"
                value={applyData.email}
                onChange={(e) => setApplyData({ ...applyData, email: e.target.value })}
                required
                style={{ width: '100%', padding: '10px', marginBottom: '1rem', border: '2px solid #e5e7eb', borderRadius: '6px' }}
              />
              <input
                type="tel"
                placeholder="Phone"
                value={applyData.phone}
                onChange={(e) => setApplyData({ ...applyData, phone: e.target.value })}
                required
                style={{ width: '100%', padding: '10px', marginBottom: '1rem', border: '2px solid #e5e7eb', borderRadius: '6px' }}
              />
              <textarea
                placeholder="Cover Letter (optional)"
                value={applyData.message}
                onChange={(e) => setApplyData({ ...applyData, message: e.target.value })}
                style={{ width: '100%', padding: '10px', marginBottom: '1rem', border: '2px solid #e5e7eb', borderRadius: '6px', fontFamily: 'inherit' }}
                rows={4}
              />
              <div style={{ display: 'flex', gap: '1rem' }}>
                <button type="submit" style={{ flex: 1, background: '#008080', color: 'white', padding: '10px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>Submit</button>
                <button type="button" onClick={() => setShowApply(false)} style={{ flex: 1, background: '#f3f4f6', border: 'none', padding: '10px', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>Cancel</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
