import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

const DEMO_CLINICS = [
  { id: 1, name: 'Central Medical Clinic', location: 'Downtown', specialization: 'General', doctors: 8, rating: 4.8 },
  { id: 2, name: 'Orthopedic Surgery Center', location: 'North District', specialization: 'Orthopedics', doctors: 5, rating: 4.9 },
  { id: 3, name: 'Cardiology Specialists', location: 'Medical Plaza', specialization: 'Cardiology', doctors: 6, rating: 4.7 },
  { id: 4, name: 'Pediatric Care Clinic', location: 'South Branch', specialization: 'Pediatrics', doctors: 4, rating: 4.6 },
  { id: 5, name: 'Neurology Institute', location: 'Research Center', specialization: 'Neurology', doctors: 7, rating: 4.9 },
  { id: 6, name: 'Physical Therapy Center', location: 'Wellness Hub', specialization: 'Rehabilitation', doctors: 10, rating: 4.8 }
]

export default function Clinics() {
  const [clinics, setClinics] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [filter, setFilter] = useState('all')
  const [selectedClinic, setSelectedClinic] = useState<any>(null)
  const [showBooking, setShowBooking] = useState(false)
  const [bookingData, setBookingData] = useState({ date: '', time: '', doctor: '', reason: '' })

  useEffect(() => {
    fetchClinics()
  }, [])

  const fetchClinics = async () => {
    try {
      setLoading(true)
      const res = await api.get('/clinics/').catch(() => ({ data: DEMO_CLINICS }))
      setClinics(res.data || DEMO_CLINICS)
    } finally {
      setLoading(false)
    }
  }

  const handleBookAppointment = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      await api.post(`/clinics/appointments/`, { clinic_id: selectedClinic.id, ...bookingData })
      alert('Appointment booked successfully!')
      setShowBooking(false)
      setBookingData({ date: '', time: '', doctor: '', reason: '' })
    } catch (err) {
      alert('Error booking appointment')
    }
  }

  const filtered = clinics.filter(c =>
    (c.name?.toLowerCase().includes(searchTerm.toLowerCase()) || '') &&
    (filter === 'all' || c.specialization === filter)
  )

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0, marginBottom: '0.5rem' }}>Find a Clinic</h1>
        <p style={{ opacity: 0.9, margin: 0 }}>Book appointments with healthcare professionals</p>
      </div>

      <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
        <input
          type="text"
          placeholder="Search clinics..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{ width: '100%', padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px', marginBottom: '1rem', fontSize: '1rem' }}
        />
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          {['all', 'General', 'Cardiology', 'Orthopedics', 'Pediatrics', 'Neurology', 'Rehabilitation'].map(spec => (
            <button
              key={spec}
              onClick={() => setFilter(spec)}
              style={{
                padding: '8px 16px',
                border: filter === spec ? '2px solid #008080' : '2px solid #e5e7eb',
                background: filter === spec ? '#008080' : 'white',
                color: filter === spec ? 'white' : '#333',
                borderRadius: '6px',
                cursor: 'pointer',
                fontWeight: 600
              }}
            >
              {spec}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>Loading clinics...</div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '1.5rem' }}>
          {filtered.map(clinic => (
            <div
              key={clinic.id}
              style={{
                background: 'white',
                borderRadius: '10px',
                overflow: 'hidden',
                boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
                transition: 'all 0.3s',
                cursor: 'pointer'
              }}
              onClick={() => { setSelectedClinic(clinic); setShowBooking(true) }}
              onMouseEnter={(e) => {
                (e.currentTarget as HTMLElement).style.boxShadow = '0 8px 20px rgba(0,128,128,0.15)';
                (e.currentTarget as HTMLElement).style.transform = 'translateY(-5px)'
              }}
              onMouseLeave={(e) => {
                (e.currentTarget as HTMLElement).style.boxShadow = '0 2px 8px rgba(0,0,0,0.06)';
                (e.currentTarget as HTMLElement).style.transform = 'translateY(0)'
              }}
            >
              <div style={{ background: '#008080', height: '150px', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white', fontSize: '3rem' }}>🏥</div>
              <div style={{ padding: '1.5rem' }}>
                <h3 style={{ fontSize: '1.1rem', fontWeight: 600, margin: 0, marginBottom: '0.5rem' }}>{clinic.name}</h3>
                <div style={{ color: '#6b7280', fontSize: '0.9rem', marginBottom: '1rem' }}>
                  <div>📍 {clinic.location}</div>
                  <div>🏷️ {clinic.specialization}</div>
                  <div>👨‍⚕️ {clinic.doctors} Doctors</div>
                  <div>⭐ {clinic.rating} Rating</div>
                </div>
                <button
                  onClick={(e) => { e.stopPropagation(); setSelectedClinic(clinic); setShowBooking(true) }}
                  style={{ width: '100%', background: '#008080', color: 'white', padding: '10px', borderRadius: '6px', border: 'none', cursor: 'pointer', fontWeight: 600 }}
                >
                  Book Appointment
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {showBooking && selectedClinic && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000 }}>
          <div style={{ background: 'white', padding: '2rem', borderRadius: '10px', maxWidth: '500px', width: '90%' }}>
            <h2 style={{ margin: 0, marginBottom: '1rem' }}>Book Appointment at {selectedClinic.name}</h2>
            <form onSubmit={handleBookAppointment}>
              <input
                type="date"
                value={bookingData.date}
                onChange={(e) => setBookingData({ ...bookingData, date: e.target.value })}
                required
                style={{ width: '100%', padding: '10px', marginBottom: '1rem', border: '2px solid #e5e7eb', borderRadius: '6px' }}
              />
              <input
                type="time"
                value={bookingData.time}
                onChange={(e) => setBookingData({ ...bookingData, time: e.target.value })}
                required
                style={{ width: '100%', padding: '10px', marginBottom: '1rem', border: '2px solid #e5e7eb', borderRadius: '6px' }}
              />
              <input
                type="text"
                placeholder="Doctor Name (optional)"
                value={bookingData.doctor}
                onChange={(e) => setBookingData({ ...bookingData, doctor: e.target.value })}
                style={{ width: '100%', padding: '10px', marginBottom: '1rem', border: '2px solid #e5e7eb', borderRadius: '6px' }}
              />
              <textarea
                placeholder="Reason for visit"
                value={bookingData.reason}
                onChange={(e) => setBookingData({ ...bookingData, reason: e.target.value })}
                style={{ width: '100%', padding: '10px', marginBottom: '1rem', border: '2px solid #e5e7eb', borderRadius: '6px', fontFamily: 'inherit' }}
                rows={3}
              />
              <div style={{ display: 'flex', gap: '1rem' }}>
                <button type="submit" style={{ flex: 1, background: '#008080', color: 'white', padding: '10px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>Confirm</button>
                <button type="button" onClick={() => setShowBooking(false)} style={{ flex: 1, background: '#f3f4f6', border: 'none', padding: '10px', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>Cancel</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
