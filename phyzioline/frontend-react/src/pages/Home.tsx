import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

const HERO_STYLE = {
  background: 'linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%)',
  padding: '4rem 1rem',
  marginBottom: '3rem'
}

const SERVICE_CARD_STYLE = {
  background: 'white',
  borderRadius: '10px',
  padding: '2rem',
  boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
  textAlign: 'center' as const,
  transition: 'all 0.3s ease'
}

export default function Home() {
  const [stats, setStats] = useState({ doctors: 150, jobs: 340, courses: 280, students: 12500 })

  useEffect(() => {
    // Fetch some stats from backend if available
    api.get('/global-stats/snapshots/').catch(() => setStats(stats))
  }, [])

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Hero Section */}
      <section style={HERO_STYLE}>
        <div style={{ maxWidth: 1100, margin: '0 auto' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem', alignItems: 'center' }}>
            <div>
              <h1 style={{ fontSize: '3.5rem', fontWeight: 700, lineHeight: 1.2, marginBottom: '1.5rem', color: '#1f2937' }}>
                Your Complete
                <span style={{ color: '#008080', display: 'block' }}> Medical Platform</span>
              </h1>
              <p style={{ fontSize: '1.1rem', color: '#6b7280', marginBottom: '2rem', lineHeight: 1.6 }}>
                Find qualified doctors, advance your healthcare career, and expand your medical knowledge. 
                Everything you need for success in one platform.
              </p>
              <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
                <Link to="/clinics" style={{
                  backgroundColor: '#008080', color: 'white', padding: '12px 24px',
                  borderRadius: '6px', textDecoration: 'none', fontWeight: 600, display: 'inline-block'
                }}>
                  Find a Doctor
                </Link>
                <Link to="/jobs" style={{
                  border: '2px solid #008080', color: '#008080', padding: '12px 24px',
                  borderRadius: '6px', textDecoration: 'none', fontWeight: 600, display: 'inline-block'
                }}>
                  Explore Jobs
                </Link>
              </div>
            </div>
            <div>
              <img src="/assets/images/hero-consultation.jpg" alt="Medical consultation"
                style={{ borderRadius: '10px', boxShadow: '0 10px 30px rgba(0,128,128,0.15)', maxWidth: '100%', height: 'auto' }} />
            </div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section style={{ maxWidth: 1100, margin: '0 auto', padding: '2rem 1rem', width: '100%' }}>
        <h2 style={{ fontSize: '2.5rem', fontWeight: 700, textAlign: 'center', marginBottom: '0.5rem', color: '#1f2937' }}>
          Our Services
        </h2>
        <p style={{ textAlign: 'center', color: '#6b7280', marginBottom: '2rem' }}>
          Comprehensive healthcare solutions for patients, professionals, and students
        </p>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '2rem', marginBottom: '2rem' }}>
          {[
            { icon: '🏥', title: 'Clinics & Doctors', desc: 'Connect with qualified medical professionals', link: '/clinics' },
            { icon: '💼', title: 'Find Jobs', desc: 'Discover career opportunities in healthcare', link: '/jobs' },
            { icon: '📚', title: 'Medical Courses', desc: 'Enhance your skills with professional training', link: '/courses' },
            { icon: '🛍️', title: 'Medical Store', desc: 'High-quality medical equipment & supplies', link: '/marketplace' }
          ].map((svc, i) => (
            <div key={i} style={SERVICE_CARD_STYLE}>
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>{svc.icon}</div>
              <h3 style={{ fontWeight: 600, marginBottom: '0.5rem', color: '#1f2937' }}>{svc.title}</h3>
              <p style={{ color: '#6b7280', marginBottom: '1rem' }}>{svc.desc}</p>
              <Link to={svc.link} style={{ color: '#008080', fontWeight: 600, textDecoration: 'none' }}>
                Learn More →
              </Link>
            </div>
          ))}
        </div>
      </section>

      {/* Stats Section */}
      <section style={{ background: '#008080', color: 'white', padding: '3rem 1rem', marginBottom: '2rem' }}>
        <div style={{ maxWidth: 1100, margin: '0 auto' }}>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '2rem', textAlign: 'center' }}>
            {[
              { num: stats.doctors, label: 'Verified Doctors' },
              { num: stats.jobs, label: 'Job Opportunities' },
              { num: stats.courses, label: 'Medical Courses' },
              { num: stats.students, label: 'Active Users' }
            ].map((stat, i) => (
              <div key={i}>
                <div style={{ fontSize: '2.5rem', fontWeight: 700, marginBottom: '0.5rem' }}>
                  {stat.num.toLocaleString()}+
                </div>
                <div style={{ opacity: 0.9 }}>{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section style={{ maxWidth: 1100, margin: '0 auto', padding: '2rem 1rem', width: '100%', textAlign: 'center' }}>
        <h2 style={{ fontSize: '2rem', fontWeight: 700, marginBottom: '1rem', color: '#1f2937' }}>
          Ready to Transform Healthcare?
        </h2>
        <p style={{ color: '#6b7280', marginBottom: '2rem', fontSize: '1.1rem' }}>
          Join thousands of healthcare professionals and students using Phyzioline.
        </p>
        <Link to="/auth/login" style={{
          backgroundColor: '#008080', color: 'white', padding: '12px 32px',
          borderRadius: '6px', textDecoration: 'none', fontWeight: 600, display: 'inline-block'
        }}>
          Get Started Now
        </Link>
      </section>

      <div style={{ flex: 1 }}></div>
    </div>
  )
}
