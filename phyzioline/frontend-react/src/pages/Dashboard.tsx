import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

export default function Dashboard() {
  const [user, setUser] = useState<any>(null)
  const [recentPosts, setRecentPosts] = useState<any[]>([])
  const [enrolledCourses, setEnrolledCourses] = useState<any[]>([])
  const [upcomingAppointments, setUpcomingAppointments] = useState<any[]>([])

  useEffect(() => {
    fetchDashboardData()
  }, [])

  const fetchDashboardData = async () => {
    try {
      // Try to get user profile
      const userRes = await api.get('/profile/').catch(() => null)
      if (userRes?.data) setUser(userRes.data)

      // Get recent feed posts
      const feedRes = await api.get('/feed/').catch(() => null)
      if (feedRes?.data) setRecentPosts(feedRes.data.slice(0, 3))

      // Get enrolled courses
      const coursesRes = await api.get('/courses/enrollments/').catch(() => null)
      if (coursesRes?.data) setEnrolledCourses(coursesRes.data.slice(0, 3))

      // Get upcoming appointments
      const apptRes = await api.get('/clinics/appointments/').catch(() => null)
      if (apptRes?.data) setUpcomingAppointments(apptRes.data.slice(0, 3))
    } catch (err) {
      console.log('Dashboard fetch error (expected for demo):', err)
    }
  }

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto', padding: '1rem' }}>
      {/* Welcome Section */}
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, marginBottom: '0.5rem' }}>
          Welcome, {user?.name || 'Healthcare Professional'}!
        </h1>
        <p style={{ opacity: 0.9 }}>Manage your medical practice, courses, and professional growth all in one place.</p>
      </div>

      {/* Quick Stats */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
        {[
          { icon: '👥', label: 'My Patients', value: enrolledCourses.length || '0' },
          { icon: '📚', label: 'Active Courses', value: enrolledCourses.length || '0' },
          { icon: '📅', label: 'Appointments', value: upcomingAppointments.length || '0' },
          { icon: '💬', label: 'Messages', value: '5' }
        ].map((stat, i) => (
          <div key={i} style={{
            background: 'white', padding: '1.5rem', borderRadius: '10px',
            boxShadow: '0 2px 8px rgba(0,0,0,0.06)', textAlign: 'center'
          }}>
            <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>{stat.icon}</div>
            <div style={{ color: '#6b7280', fontSize: '0.9rem', marginBottom: '0.5rem' }}>{stat.label}</div>
            <div style={{ fontSize: '1.5rem', fontWeight: 700, color: '#008080' }}>{stat.value}</div>
          </div>
        ))}
      </div>

      {/* Main Content Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '2rem' }}>
        <div>
          {/* Recent Feed Posts */}
          <section style={{ background: 'white', borderRadius: '10px', padding: '1.5rem', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
              <h2 style={{ fontSize: '1.3rem', fontWeight: 600, margin: 0 }}>Recent Posts</h2>
              <Link to="/feed" style={{ color: '#008080', textDecoration: 'none', fontWeight: 600 }}>View All →</Link>
            </div>

            {recentPosts.length === 0 ? (
              <div style={{ color: '#6b7280', padding: '2rem', textAlign: 'center' }}>
                No posts yet. <Link to="/feed" style={{ color: '#008080' }}>Create one</Link>
              </div>
            ) : (
              recentPosts.map((post: any) => (
                <div key={post.id} style={{
                  background: '#f9fafb', padding: '1rem', borderRadius: '8px',
                  marginBottom: '1rem', borderLeft: '4px solid #008080'
                }}>
                  <div style={{ fontWeight: 600, marginBottom: '0.5rem' }}>{post.title || post.content?.slice(0, 50)}</div>
                  <div style={{ color: '#6b7280', fontSize: '0.9rem' }}>
                    {post.author || 'Posted by'} • {post.created_at?.slice(0, 10) || ''}
                  </div>
                </div>
              ))
            )}
          </section>

          {/* Module Cards */}
          <section>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 600, marginBottom: '1rem' }}>All Services</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(150px, 1fr))', gap: '1rem' }}>
              {[
                { name: 'Courses', link: '/courses', icon: '📚' },
                { name: 'Jobs', link: '/jobs', icon: '💼' },
                { name: 'Clinics', link: '/clinics', icon: '🏥' },
                { name: 'Marketplace', link: '/marketplace', icon: '🛍️' },
                { name: 'AI Engine', link: '/ai', icon: '🤖' },
                { name: 'CRM', link: '/crm', icon: '📊' },
                { name: 'Global Stats', link: '/global-stats', icon: '📈' },
                { name: 'Payments', link: '/payments', icon: '💳' },
                { name: 'Ads', link: '/ads', icon: '📢' },
                { name: 'Sessions', link: '/home-sessions', icon: '🎓' }
              ].map((module, i) => (
                <Link key={i} to={module.link} style={{
                  background: 'white', padding: '1rem', borderRadius: '10px',
                  boxShadow: '0 2px 8px rgba(0,0,0,0.06)', textAlign: 'center' as const,
                  textDecoration: 'none', color: 'inherit', transition: 'all 0.3s',
                  border: '2px solid #e5e7eb', cursor: 'pointer'
                }}
                  onMouseEnter={(e: React.MouseEvent<HTMLAnchorElement>) => {
                    (e.currentTarget.style as any).borderColor = '#008080';
                    (e.currentTarget.style as any).transform = 'translateY(-5px)'
                  }}
                  onMouseLeave={(e: React.MouseEvent<HTMLAnchorElement>) => {
                    (e.currentTarget.style as any).borderColor = '#e5e7eb';
                    (e.currentTarget.style as any).transform = 'translateY(0)'
                  }}>
                  <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>{module.icon}</div>
                  <div style={{ fontWeight: 600, fontSize: '0.9rem' }}>{module.name}</div>
                </Link>
              ))}
            </div>
          </section>
        </div>

        {/* Sidebar */}
        <aside>
          {/* Upcoming Appointments */}
          <section style={{ background: 'white', borderRadius: '10px', padding: '1.5rem', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 600, marginBottom: '1rem' }}>📅 Appointments</h3>
            {upcomingAppointments.length === 0 ? (
              <div style={{ color: '#6b7280', fontSize: '0.9rem' }}>No upcoming appointments</div>
            ) : (
              upcomingAppointments.map((apt: any) => (
                <div key={apt.id} style={{
                  background: '#f9fafb', padding: '0.75rem', borderRadius: '6px', marginBottom: '0.75rem'
                }}>
                  <div style={{ fontWeight: 600, fontSize: '0.9rem' }}>{apt.doctor_name || 'Dr. Name'}</div>
                  <div style={{ color: '#6b7280', fontSize: '0.85rem' }}>{apt.date || 'Date TBD'}</div>
                </div>
              ))
            )}
          </section>

          {/* Quick Actions */}
          <section style={{ background: 'white', borderRadius: '10px', padding: '1.5rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 600, marginBottom: '1rem' }}>Quick Actions</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              <Link to="/feed/new" style={{
                background: '#008080', color: 'white', padding: '0.75rem',
                borderRadius: '6px', textDecoration: 'none', textAlign: 'center', fontWeight: 600
              }}>
                New Post
              </Link>
              <Link to="/courses" style={{
                background: '#38B2AC', color: 'white', padding: '0.75rem',
                borderRadius: '6px', textDecoration: 'none', textAlign: 'center', fontWeight: 600
              }}>
                Enroll Course
              </Link>
              <button style={{
                background: '#f3f4f6', border: 'none', padding: '0.75rem',
                borderRadius: '6px', cursor: 'pointer', fontWeight: 600
              }}>
                View Profile
              </button>
            </div>
          </section>
        </aside>
      </div>
    </div>
  )
}
