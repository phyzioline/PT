import React from 'react'

export default function WebsiteLanding(){
  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg,#008080 0%,#006666 100%)', color: 'white', borderRadius: 12, padding: '2rem', marginBottom: '1.5rem' }}>
        <h1 style={{ margin: 0, fontSize: '1.9rem' }}>Ask Your Doctor — Medical Platform</h1>
        <p style={{ margin: '6px 0 0', opacity: 0.95 }}>Find a doctor, explore jobs, and advance your skills.</p>
      </div>

      <section style={{ background: 'white', padding: 20, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)' }}>
        <div style={{ display: 'flex', gap: 20, alignItems: 'center', flexWrap: 'wrap' }}>
          <div style={{ flex: 1, minWidth: 260 }}>
            <h2 style={{ marginTop: 0 }}>Your Complete <span style={{ color: '#008080' }}>Medical Platform</span></h2>
            <p style={{ color: '#6b7280' }}>Find your doctor, advance your career, and learn new skills. Everything you need for healthcare success in one place.</p>
            <div style={{ display: 'flex', gap: 12, marginTop: 12 }}>
              <a href="/clinics" style={{ background: '#008080', color: 'white', padding: '10px 16px', borderRadius: 8, textDecoration: 'none', fontWeight: 700 }}>Find a Doctor</a>
              <a href="/jobs" style={{ border: '2px solid #008080', color: '#008080', padding: '10px 16px', borderRadius: 8, textDecoration: 'none', fontWeight: 700 }}>Explore Jobs</a>
            </div>
          </div>
          <div style={{ width: 420, textAlign: 'center' }}>
            <img src="/assets/images/hero-consultation.jpg" alt="Hero" style={{ width: '100%', borderRadius: 8, boxShadow: '0 8px 24px rgba(2,6,23,0.08)' }} />
          </div>
        </div>
      </section>

      <section style={{ marginTop: 18, display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(260px,1fr))', gap: 16 }}>
        {[
          { title: 'Ask Your Doctor', desc: 'Connect with qualified medical professionals for consultations and health advice', link: '/clinics' },
          { title: 'Find Jobs', desc: 'Discover career opportunities in healthcare and medical fields', link: '/jobs' },
          { title: 'Medical Courses', desc: 'Enhance your skills with professional medical education and training', link: '/courses' },
        ].map(card => (
          <div key={card.title} style={{ background: 'white', padding: 18, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)' }}>
            <h4 style={{ margin: '0 0 8px' }}>{card.title}</h4>
            <p style={{ margin: 0, color: '#6b7280' }}>{card.desc}</p>
            <a href={card.link} style={{ display: 'inline-block', marginTop: 12, color: '#008080', fontWeight: 700 }}>Learn More →</a>
          </div>
        ))}
      </section>

    </div>
  )
}
