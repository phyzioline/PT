import React, { useEffect, useState } from 'react'
import api from '../services/api'

const DEMO_CLIENTS = [
  { id: 1, name: 'John Smith', status: 'Active', lastContact: '2024-11-24', nextAppt: '2024-11-27', email: 'john@email.com', phone: '555-0101' },
  { id: 2, name: 'Sarah Johnson', status: 'Active', lastContact: '2024-11-22', nextAppt: '2024-11-28', email: 'sarah@email.com', phone: '555-0102' },
  { id: 3, name: 'Michael Brown', status: 'Follow-up', lastContact: '2024-11-10', nextAppt: 'Pending', email: 'michael@email.com', phone: '555-0103' },
  { id: 4, name: 'Emily Davis', status: 'Active', lastContact: '2024-11-23', nextAppt: '2024-11-29', email: 'emily@email.com', phone: '555-0104' },
  { id: 5, name: 'David Wilson', status: 'Inactive', lastContact: '2024-10-15', nextAppt: 'None', email: 'david@email.com', phone: '555-0105' },
  { id: 6, name: 'Lisa Garcia', status: 'Active', lastContact: '2024-11-25', nextAppt: '2024-11-26', email: 'lisa@email.com', phone: '555-0106' }
]

export default function CRM(){
  const [contacts, setContacts] = useState<any[]>([])
  const [searchTerm, setSearchTerm] = useState('')
  const [filter, setFilter] = useState('all')
  const [showForm, setShowForm] = useState(false)
  const [formData, setFormData] = useState({ name: '', email: '', phone: '', status: 'Active' })

  useEffect(()=>{
    fetchContacts()
  },[])

  const fetchContacts = async () => {
    try {
      const res = await api.get('/crm/contacts/').catch(() => ({ data: DEMO_CLIENTS }))
      setContacts(res.data || DEMO_CLIENTS)
    } catch (err) {
      setContacts(DEMO_CLIENTS)
    }
  }

  const handleAddClient = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const res = await api.post('/crm/contacts/', formData)
      setContacts([...contacts, res.data])
      setFormData({ name: '', email: '', phone: '', status: 'Active' })
      setShowForm(false)
    } catch (err) {
      console.log('Error adding client')
    }
  }

  const filtered = contacts.filter(c =>
    (c.name?.toLowerCase().includes(searchTerm.toLowerCase()) || '') &&
    (filter === 'all' || c.status === filter)
  )

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0, marginBottom: '0.5rem' }}>📊 CRM - Client Management</h1>
        <p style={{ opacity: 0.9, margin: 0 }}>Manage patient relationships and track interactions</p>
      </div>

      <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr auto', gap: '1rem', marginBottom: '1rem' }}>
          <input
            type="text"
            placeholder="Search clients..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px', fontSize: '1rem' }}
          />
          <button
            onClick={() => setShowForm(!showForm)}
            style={{ background: '#008080', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}
          >
            {showForm ? 'Cancel' : 'Add Client'}
          </button>
        </div>

        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          {['all', 'Active', 'Follow-up', 'Inactive'].map(status => (
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
      </div>

      {showForm && (
        <form onSubmit={handleAddClient} style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
            <input
              type="text"
              placeholder="Full Name"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              required
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
            <input
              type="email"
              placeholder="Email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
            <input
              type="tel"
              placeholder="Phone"
              value={formData.phone}
              onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
            <select
              value={formData.status}
              onChange={(e) => setFormData({ ...formData, status: e.target.value })}
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            >
              <option value="Active">Active</option>
              <option value="Follow-up">Follow-up</option>
              <option value="Inactive">Inactive</option>
            </select>
          </div>
          <button type="submit" style={{ background: '#008080', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>
            Save Client
          </button>
        </form>
      )}

      <div style={{ background: 'white', borderRadius: '10px', overflow: 'hidden', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ background: '#f9fafb', borderBottom: '2px solid #e5e7eb' }}>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Name</th>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Email</th>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Phone</th>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Status</th>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Last Contact</th>
              <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600 }}>Next Apt</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((contact, i) => (
              <tr key={contact.id} style={{ borderBottom: '1px solid #e5e7eb', background: i % 2 === 0 ? 'white' : '#f9fafb' }}>
                <td style={{ padding: '1rem' }}>{contact.name}</td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>{contact.email}</td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>{contact.phone}</td>
                <td style={{ padding: '1rem' }}>
                  <span style={{ background: contact.status === 'Active' ? '#008080' : '#e5e7eb', color: contact.status === 'Active' ? 'white' : '#333', padding: '4px 8px', borderRadius: '4px', fontSize: '0.8rem', fontWeight: 600 }}>
                    {contact.status}
                  </span>
                </td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>{contact.lastContact}</td>
                <td style={{ padding: '1rem', color: '#6b7280' }}>{contact.nextAppt}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {filtered.length === 0 && (
        <div style={{ textAlign: 'center', padding: '3rem', color: '#6b7280' }}>
          No clients found. Try adjusting your search or filters.
        </div>
      )}
    </div>
  )
}
