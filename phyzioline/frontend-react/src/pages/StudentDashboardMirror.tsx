import React, { useState } from 'react'

export default function StudentDashboardMirror(){
  const [sidebarOpen, setSidebarOpen] = useState(false)

  return (
    <div>
      <button onClick={()=> setSidebarOpen(!sidebarOpen)} style={{ display: 'none' }} id="sidebarToggle">Toggle</button>
      <div style={{ display: 'flex' }}>
        <aside style={{ width: 250, minHeight: '100vh', background: 'linear-gradient(135deg,#008080 0%,#006666 100%)', color: 'white', padding: 20, position: 'sticky', top: 0 }}>
          <div style={{ marginBottom: 12 }}>
            <img src="https://phyzioline.vercel.app/assets/images/medical-icons-white.svg" alt="logo" style={{ height: 36 }} />
            <div style={{ color: 'rgba(255,255,255,0.8)', marginTop: 6 }}>Client Portal</div>
          </div>
          <nav style={{ marginTop: 18 }}>
            {['Dashboard','My Appointments','Medical Records','My Courses','Payments & Billing','Profile','Notifications'].map((n,i)=> (
              <div key={i} style={{ padding: '10px 8px', color: 'rgba(255,255,255,0.9)', marginBottom: 6, borderRadius: 6 }}>{n}</div>
            ))}
            <div style={{ marginTop: 18 }}>
              <a href="/" style={{ color: 'white' }}>Back to Website</a>
            </div>
          </nav>
        </aside>

        <main style={{ flex: 1, padding: 20, background: '#f8fafc', minHeight: '100vh' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
            <div>
              <h2 style={{ margin: 0 }}>Welcome back, Alex Johnson</h2>
              <div style={{ color: '#6b7280' }}>Here's your health and learning overview</div>
            </div>
            <div style={{ display: 'flex', gap: 8 }}>
              <button style={{ padding: '10px 12px', borderRadius: 8, border: '1px solid #e6eef0' }}>Book Appointment</button>
              <button style={{ padding: '10px 12px', borderRadius: 8, background: '#008080', color: 'white' }}>Emergency Consultation</button>
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(220px,1fr))', gap: 12, marginBottom: 18 }}>
            <div style={{ background: 'white', padding: 18, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)' }}>
              <div style={{ color: '#6b7280' }}>Upcoming Appointments</div>
              <h3 style={{ margin: '8px 0' }}>3</h3>
              <small style={{ color: '#10b981' }}>Next: Tomorrow 2:00 PM</small>
            </div>
            <div style={{ background: 'white', padding: 18, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)' }}>
              <div style={{ color: '#6b7280' }}>Active Courses</div>
              <h3 style={{ margin: '8px 0' }}>5</h3>
              <small style={{ color: '#0284c7' }}>75% avg progress</small>
            </div>
            <div style={{ background: 'white', padding: 18, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)' }}>
              <div style={{ color: '#6b7280' }}>Health Status</div>
              <h3 style={{ margin: '8px 0' }}>Good</h3>
              <small style={{ color: '#10b981' }}>All vitals normal</small>
            </div>
            <div style={{ background: 'white', padding: 18, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)' }}>
              <div style={{ color: '#6b7280' }}>Notifications</div>
              <h3 style={{ margin: '8px 0' }}>3</h3>
              <small style={{ color: '#f59e0b' }}>1 urgent</small>
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: 12 }}>
            <div>
              <div style={{ background: 'white', padding: 16, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)', marginBottom: 12 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <h5 style={{ margin: 0 }}>Upcoming Appointments</h5>
                  <a href="#" style={{ color: '#008080' }}>View All</a>
                </div>
                <div style={{ marginTop: 12 }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
                    <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
                      <div style={{ width: 48, height: 48, borderRadius: 24, background: '#008080', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>EW</div>
                      <div>
                        <div style={{ fontWeight: 700 }}>Dr. Emily White</div>
                        <div style={{ color: '#6b7280' }}>Cardiology Consultation • Tomorrow 2:00 PM</div>
                      </div>
                    </div>
                    <div style={{ display: 'flex', gap: 6 }}>
                      <button style={{ padding: 8, borderRadius: 6 }}>📅</button>
                      <button style={{ padding: 8, borderRadius: 6, background: '#008080', color: 'white' }}>📹</button>
                    </div>
                  </div>
                </div>
              </div>

              <div style={{ background: 'white', padding: 16, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)' }}>
                <h5 style={{ marginTop: 0 }}>Course Progress</h5>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(180px,1fr))', gap: 10 }}>
                  {['Human Anatomy','Medical Terminology','Pharmacology Basics','Clinical Skills'].map((c,i)=> (
                    <div key={i} style={{ padding: 12, border: '1px solid #eef2f7', borderRadius: 8 }}>
                      <div style={{ fontWeight: 700 }}>{c}</div>
                      <div style={{ height: 8, background: '#f1f5f9', borderRadius: 6, marginTop: 8 }}>
                        <div style={{ width: `${60 + i*10}%`, height: '100%', background: '#008080', borderRadius: 6 }}></div>
                      </div>
                      <div style={{ color: '#6b7280', fontSize: 13, marginTop: 6 }}>{60 + i*10}% Complete</div>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            <aside>
              <div style={{ background: 'white', padding: 16, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)', marginBottom: 12 }}>
                <h5 style={{ marginTop: 0 }}>Health Summary</h5>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2,1fr)', gap: 8, marginTop: 8 }}>
                  <div style={{ textAlign: 'center' }}>
                    <div style={{ width: 72, height: 72, borderRadius: 36, background: 'conic-gradient(#008080 0deg 270deg,#e9ecef 270deg 360deg)', display: 'inline-flex', alignItems: 'center', justifyContent: 'center' }}>
                      <div style={{ width: 52, height: 52, borderRadius: 26, background: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 700 }}>120/80</div>
                    </div>
                    <div style={{ color: '#6b7280', marginTop: 8 }}>Blood Pressure</div>
                  </div>
                  <div style={{ textAlign: 'center' }}>
                    <div style={{ width: 72, height: 72, borderRadius: 36, background: 'conic-gradient(#008080 0deg 200deg,#e9ecef 200deg 360deg)', display: 'inline-flex', alignItems: 'center', justifyContent: 'center' }}>
                      <div style={{ width: 52, height: 52, borderRadius: 26, background: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 700 }}>72</div>
                    </div>
                    <div style={{ color: '#6b7280', marginTop: 8 }}>Heart Rate</div>
                  </div>
                </div>
                <div style={{ textAlign: 'center', marginTop: 10 }}>
                  <a href="#" style={{ color: '#008080' }}>View Full Report</a>
                </div>
              </div>

              <div style={{ background: 'white', padding: 16, borderRadius: 10, boxShadow: '0 6px 18px rgba(2,6,23,0.04)' }}>
                <h5 style={{ marginTop: 0 }}>Quick Actions</h5>
                <div style={{ display: 'grid', gap: 8, marginTop: 8 }}>
                  <a href="#" style={{ padding: 10, borderRadius: 8, border: '1px solid #eef2f7', textDecoration: 'none', color: '#111827' }}>Book New Appointment</a>
                  <a href="#" style={{ padding: 10, borderRadius: 8, border: '1px solid #eef2f7', textDecoration: 'none', color: '#111827' }}>Continue Learning</a>
                </div>
              </div>
            </aside>
          </div>
        </main>
      </div>
    </div>
  )
}
