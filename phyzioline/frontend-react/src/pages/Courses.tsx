import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

export default function Courses() {
  const [courses, setCourses] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [filter, setFilter] = useState('all')
  const [showForm, setShowForm] = useState(false)
  const [formData, setFormData] = useState({ title: '', description: '', instructor: '', price: '', level: 'beginner' })

  useEffect(() => {
    fetchCourses()
  }, [])

  const fetchCourses = async () => {
    try {
      setLoading(true)
      const res = await api.get('/courses/').catch(() => ({ data: DEMO_COURSES }))
      setCourses(res.data || DEMO_COURSES)
    } finally {
      setLoading(false)
    }
  }

  const handleCreateCourse = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const res = await api.post('/courses/', formData)
      setCourses([...courses, res.data])
      setFormData({ title: '', description: '', instructor: '', price: '', level: 'beginner' })
      setShowForm(false)
    } catch (err) {
      console.error('Error creating course:', err)
    }
  }

  const filtered = courses.filter(c =>
    (c.title?.toLowerCase().includes(searchTerm.toLowerCase()) || '') &&
    (filter === 'all' || c.level === filter)
  )

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      {/* Header */}
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0, marginBottom: '0.5rem' }}>Medical Courses</h1>
        <p style={{ opacity: 0.9, margin: 0 }}>Expand your medical knowledge with expert-led courses</p>
      </div>

      {/* Search and Filters */}
      <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr auto', gap: '1rem', marginBottom: '1rem' }}>
          <input
            type="text"
            placeholder="Search courses..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px', fontSize: '1rem' }}
          />
          <button
            onClick={() => setShowForm(!showForm)}
            style={{ background: '#008080', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}
          >
            {showForm ? 'Cancel' : 'Create Course'}
          </button>
        </div>

        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          {['all', 'beginner', 'intermediate', 'advanced'].map(level => (
            <button
              key={level}
              onClick={() => setFilter(level)}
              style={{
                padding: '8px 16px',
                border: filter === level ? '2px solid #008080' : '2px solid #e5e7eb',
                background: filter === level ? '#008080' : 'white',
                color: filter === level ? 'white' : '#333',
                borderRadius: '6px',
                cursor: 'pointer',
                fontWeight: 600
              }}
            >
              {level.charAt(0).toUpperCase() + level.slice(1)}
            </button>
          ))}
        </div>
      </div>

      {/* Create Form */}
      {showForm && (
        <form onSubmit={handleCreateCourse} style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
            <input
              type="text"
              placeholder="Course Title"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
              required
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
            <input
              type="text"
              placeholder="Instructor"
              value={formData.instructor}
              onChange={(e) => setFormData({ ...formData, instructor: e.target.value })}
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
          </div>
          <textarea
            placeholder="Description"
            value={formData.description}
            onChange={(e) => setFormData({ ...formData, description: e.target.value })}
            style={{ width: '100%', padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px', marginBottom: '1rem', fontFamily: 'inherit' }}
            rows={3}
          />
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem' }}>
            <input
              type="number"
              placeholder="Price"
              value={formData.price}
              onChange={(e) => setFormData({ ...formData, price: e.target.value })}
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
            <select
              value={formData.level}
              onChange={(e) => setFormData({ ...formData, level: e.target.value })}
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            >
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
            <button
              type="submit"
              style={{ background: '#008080', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}
            >
              Save Course
            </button>
          </div>
        </form>
      )}

      {/* Courses Grid */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>Loading courses...</div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '1.5rem' }}>
          {filtered.map(course => (
            <div
              key={course.id}
              style={{
                background: 'white',
                borderRadius: '10px',
                overflow: 'hidden',
                boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
                transition: 'all 0.3s'
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
              <div style={{ background: '#008080', height: '150px', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white', fontSize: '2rem' }}>
                📚
              </div>
              <div style={{ padding: '1.5rem' }}>
                <h3 style={{ fontSize: '1.1rem', fontWeight: 600, marginBottom: '0.5rem', margin: 0 }}>{course.title}</h3>
                <div style={{ color: '#6b7280', fontSize: '0.9rem', marginBottom: '0.75rem' }}>
                  {course.instructor && <div>By {course.instructor}</div>}
                  <div>Level: {course.level?.toUpperCase()}</div>
                </div>
                {course.description && <p style={{ color: '#6b7280', fontSize: '0.9rem', marginBottom: '1rem', margin: 0 }}>{course.description.slice(0, 80)}...</p>}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  {course.price && <span style={{ fontWeight: 700, color: '#008080' }}>${course.price}</span>}
                  <Link
                    to={`/courses/${course.id}`}
                    style={{
                      background: '#008080',
                      color: 'white',
                      padding: '8px 16px',
                      borderRadius: '6px',
                      textDecoration: 'none',
                      fontWeight: 600
                    }}
                  >
                    Enroll
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {filtered.length === 0 && !loading && (
        <div style={{ textAlign: 'center', padding: '3rem', color: '#6b7280' }}>
          No courses found. Try adjusting your search or filters.
        </div>
      )}
    </div>
  )
}

const DEMO_COURSES = [
  { id: 1, title: 'Advanced Orthopedic Surgery', instructor: 'Dr. Smith', level: 'advanced', price: 299, description: 'Master advanced surgical techniques in orthopedics' },
  { id: 2, title: 'Physical Therapy Fundamentals', instructor: 'Dr. Johnson', level: 'beginner', price: 149, description: 'Essential concepts in rehabilitation' },
  { id: 3, title: 'Neurology Intensive', instructor: 'Dr. Lee', level: 'intermediate', price: 199, description: 'Deep dive into neurological disorders and treatment' },
  { id: 4, title: 'Cardiology Essentials', instructor: 'Dr. Brown', level: 'beginner', price: 129, description: 'Heart disease diagnosis and management' },
  { id: 5, title: 'Surgical Techniques', instructor: 'Dr. Garcia', level: 'advanced', price: 349, description: 'Expert surgical procedures and approaches' },
  { id: 6, title: 'Pediatric Medicine', instructor: 'Dr. Wilson', level: 'intermediate', price: 179, description: 'Specialized child healthcare' }
]
