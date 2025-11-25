import React from 'react'

export default function Footer() {
  return (
    <footer style={{ backgroundColor: '#008080', color: 'white', marginTop: '3rem', padding: '2rem 0' }}>
      <div style={{ maxWidth: 1100, margin: '0 auto', padding: '0 1rem' }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '2rem', marginBottom: '2rem' }}>
          <div>
            <h5 style={{ fontWeight: 600, marginBottom: '1rem' }}>About Phyzioline</h5>
            <p style={{ fontSize: '0.9rem', opacity: 0.9 }}>
              Your complete medical platform for healthcare professionals, students, and patients.
            </p>
          </div>
          <div>
            <h5 style={{ fontWeight: 600, marginBottom: '1rem' }}>Services</h5>
            <ul style={{ listStyle: 'none', padding: 0 }}>
              <li><a href="/courses" style={{ color: 'white', textDecoration: 'none', opacity: 0.8 }}>Courses</a></li>
              <li><a href="/jobs" style={{ color: 'white', textDecoration: 'none', opacity: 0.8 }}>Jobs</a></li>
              <li><a href="/clinics" style={{ color: 'white', textDecoration: 'none', opacity: 0.8 }}>Clinics</a></li>
              <li><a href="/marketplace" style={{ color: 'white', textDecoration: 'none', opacity: 0.8 }}>Marketplace</a></li>
            </ul>
          </div>
          <div>
            <h5 style={{ fontWeight: 600, marginBottom: '1rem' }}>Support</h5>
            <ul style={{ listStyle: 'none', padding: 0 }}>
              <li><a href="#" style={{ color: 'white', textDecoration: 'none', opacity: 0.8 }}>Contact Us</a></li>
              <li><a href="#" style={{ color: 'white', textDecoration: 'none', opacity: 0.8 }}>FAQ</a></li>
              <li><a href="#" style={{ color: 'white', textDecoration: 'none', opacity: 0.8 }}>Privacy Policy</a></li>
              <li><a href="#" style={{ color: 'white', textDecoration: 'none', opacity: 0.8 }}>Terms</a></li>
            </ul>
          </div>
          <div>
            <h5 style={{ fontWeight: 600, marginBottom: '1rem' }}>Follow Us</h5>
            <div style={{ display: 'flex', gap: '1rem' }}>
              <a href="#" style={{ color: 'white', fontSize: '1.5rem', textDecoration: 'none' }}>f</a>
              <a href="#" style={{ color: 'white', fontSize: '1.5rem', textDecoration: 'none' }}>𝕏</a>
              <a href="#" style={{ color: 'white', fontSize: '1.5rem', textDecoration: 'none' }}>in</a>
            </div>
          </div>
        </div>
        <div style={{ borderTop: '1px solid rgba(255,255,255,0.2)', paddingTop: '1rem', textAlign: 'center', opacity: 0.7 }}>
          <p>&copy; 2025 Phyzioline. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}
