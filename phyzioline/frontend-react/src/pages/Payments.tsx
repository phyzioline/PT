import React, { useEffect, useState } from 'react'
import api from '../services/api'

const DEMO_TRANSACTIONS = [
  { id: 1, date: '2024-11-20', type: 'PT Session - Dr. Sarah Lee', amount: 75, status: 'Completed', method: 'Visa •••• 4242' },
  { id: 2, date: '2024-11-18', type: 'Yoga Therapy Package', amount: 150, status: 'Completed', method: 'MasterCard •••• 5555' },
  { id: 3, date: '2024-11-15', type: 'Course Enrollment - Rehabilitation Basics', amount: 45, status: 'Completed', method: 'Visa •••• 4242' },
  { id: 4, date: '2024-11-10', type: 'Monthly Subscription', amount: 299, status: 'Completed', method: 'Bank Transfer' },
  { id: 5, date: '2024-11-05', type: 'Equipment Purchase - Resistance Bands', amount: 35, status: 'Completed', method: 'Visa •••• 4242' },
  { id: 6, date: '2024-10-30', type: 'PT Session - Dr. Mike Johnson', amount: 75, status: 'Completed', method: 'Apple Pay' },
  { id: 7, date: '2024-10-25', type: 'Assessment & Consultation', amount: 100, status: 'Completed', method: 'Visa •••• 4242' },
  { id: 8, date: '2024-10-20', type: 'Refund - Cancelled Session', amount: -50, status: 'Completed', method: 'Original Payment Method' }
]

const DEMO_INVOICES = [
  { id: 'INV-2024-001', date: '2024-11-20', description: 'PT Session - Dr. Sarah Lee', amount: 75, status: 'Paid', dueDate: '2024-11-27' },
  { id: 'INV-2024-002', date: '2024-11-18', description: 'Yoga Therapy Package', amount: 150, status: 'Paid', dueDate: '2024-11-25' },
  { id: 'INV-2024-003', date: '2024-11-15', description: 'Course Enrollment', amount: 45, status: 'Paid', dueDate: '2024-11-22' },
  { id: 'INV-2024-004', date: '2024-11-10', description: 'Monthly Subscription', amount: 299, status: 'Paid', dueDate: '2024-11-17' }
]

const DEMO_METHODS = [
  { id: 1, type: 'Visa', lastFour: '4242', expiry: '12/26', isDefault: true },
  { id: 2, type: 'MasterCard', lastFour: '5555', expiry: '08/25', isDefault: false },
  { id: 3, type: 'Bank Account', lastFour: '6789', expiry: 'N/A', isDefault: false }
]

export default function Payments(){
  const [tx, setTx] = useState<any[]>(DEMO_TRANSACTIONS)
  const [invoices, setInvoices] = useState<any[]>(DEMO_INVOICES)
  const [methods, setMethods] = useState<any[]>(DEMO_METHODS)
  const [tab, setTab] = useState('transactions')
  const [timePeriod, setTimePeriod] = useState('all')
  const [showAddMethod, setShowAddMethod] = useState(false)
  const [newMethod, setNewMethod] = useState({ cardNumber: '', expiry: '', cvc: '', name: '' })

  useEffect(()=>{
    fetchPayments()
  },[])

  const fetchPayments = async () => {
    try {
      const res = await api.get('/payments/transactions/').catch(() => ({ data: DEMO_TRANSACTIONS }))
      setTx(res.data || DEMO_TRANSACTIONS)
    } catch (err) {
      setTx(DEMO_TRANSACTIONS)
    }
  }

  const handleAddMethod = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const res = await api.post('/payments/add-method/', newMethod)
      setMethods([...methods, res.data])
      setNewMethod({ cardNumber: '', expiry: '', cvc: '', name: '' })
      setShowAddMethod(false)
    } catch (err) {
      alert('Error adding payment method')
    }
  }

  const filteredTx = timePeriod === 'all' ? tx : tx.filter(t => {
    const date = new Date(t.date)
    const now = new Date()
    if (timePeriod === 'week') return (now.getTime() - date.getTime()) <= 7 * 24 * 60 * 60 * 1000
    if (timePeriod === 'month') return (now.getTime() - date.getTime()) <= 30 * 24 * 60 * 60 * 1000
    return true
  })

  const totalSpent = tx.reduce((sum, t) => sum + (t.amount > 0 ? t.amount : 0), 0)
  const balance = 1500 - totalSpent

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0, marginBottom: '0.5rem' }}>💳 Payments & Billing</h1>
        <p style={{ opacity: 0.9, margin: 0 }}>Manage your payments, invoices, and billing information</p>
      </div>

      {/* Balance Card */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
        <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          <div style={{ fontSize: '0.85rem', color: '#6b7280', marginBottom: '0.5rem' }}>Account Balance</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: '#008080' }}>${balance.toFixed(2)}</div>
          <div style={{ fontSize: '0.75rem', color: '#9ca3af', marginTop: '0.5rem' }}>Available</div>
        </div>
        <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          <div style={{ fontSize: '0.85rem', color: '#6b7280', marginBottom: '0.5rem' }}>Total Spent</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: '#008080' }}>${totalSpent.toFixed(2)}</div>
          <div style={{ fontSize: '0.75rem', color: '#9ca3af', marginTop: '0.5rem' }}>This year</div>
        </div>
        <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          <button
            onClick={() => setShowAddMethod(true)}
            style={{ width: '100%', background: '#008080', color: 'white', padding: '15px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}
          >
            Add Payment Method
          </button>
        </div>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '1rem', marginBottom: '1.5rem', borderBottom: '2px solid #e5e7eb', paddingBottom: '1rem' }}>
        {['transactions', 'invoices', 'methods'].map(t => (
          <button
            key={t}
            onClick={() => setTab(t)}
            style={{
              padding: '8px 16px',
              background: 'none',
              border: 'none',
              borderBottom: tab === t ? '3px solid #008080' : 'none',
              color: tab === t ? '#008080' : '#6b7280',
              fontWeight: 600,
              cursor: 'pointer',
              textTransform: 'capitalize'
            }}
          >
            {t}
          </button>
        ))}
      </div>

      {/* Add Payment Method Form */}
      {showAddMethod && (
        <form onSubmit={handleAddMethod} style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          <h3 style={{ margin: 0, marginBottom: '1rem' }}>Add Payment Method</h3>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
            <input
              type="text"
              placeholder="Cardholder Name"
              value={newMethod.name}
              onChange={(e) => setNewMethod({ ...newMethod, name: e.target.value })}
              required
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
            <input
              type="text"
              placeholder="Card Number (16 digits)"
              value={newMethod.cardNumber}
              onChange={(e) => setNewMethod({ ...newMethod, cardNumber: e.target.value })}
              required
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
            <input
              type="text"
              placeholder="MM/YY"
              value={newMethod.expiry}
              onChange={(e) => setNewMethod({ ...newMethod, expiry: e.target.value })}
              required
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
            <input
              type="text"
              placeholder="CVC"
              value={newMethod.cvc}
              onChange={(e) => setNewMethod({ ...newMethod, cvc: e.target.value })}
              required
              style={{ padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
          </div>
          <div style={{ display: 'flex', gap: '1rem' }}>
            <button type="submit" style={{ background: '#008080', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>Add Card</button>
            <button type="button" onClick={() => setShowAddMethod(false)} style={{ background: '#e5e7eb', color: '#333', padding: '10px 20px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>Cancel</button>
          </div>
        </form>
      )}

      {/* Transactions Tab */}
      {tab === 'transactions' && (
        <>
          <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1.5rem', flexWrap: 'wrap' }}>
            {['all', 'week', 'month'].map(period => (
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
                  fontWeight: 600,
                  textTransform: 'capitalize'
                }}
              >
                {period === 'all' ? 'All Time' : period === 'week' ? 'Last 7 Days' : 'Last 30 Days'}
              </button>
            ))}
          </div>
          <div style={{ display: 'grid', gap: '1rem' }}>
            {filteredTx.map(t => (
              <div key={t.id} style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <h3 style={{ margin: 0, marginBottom: '0.5rem', fontWeight: 600 }}>{t.type}</h3>
                  <div style={{ color: '#6b7280', fontSize: '0.9rem' }}>📅 {t.date} • {t.method}</div>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <div style={{ fontSize: '1.25rem', fontWeight: 700, color: t.amount < 0 ? '#10b981' : '#008080', marginBottom: '0.5rem' }}>{t.amount < 0 ? '+' : '-'}${Math.abs(t.amount).toFixed(2)}</div>
                  <span style={{ background: '#10b981', color: 'white', padding: '4px 12px', borderRadius: '4px', fontSize: '0.8rem', fontWeight: 600 }}>{t.status}</span>
                </div>
              </div>
            ))}
          </div>
        </>
      )}

      {/* Invoices Tab */}
      {tab === 'invoices' && (
        <div style={{ overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ borderBottom: '2px solid #e5e7eb', background: '#f9fafb' }}>
                <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600, color: '#6b7280' }}>Invoice ID</th>
                <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600, color: '#6b7280' }}>Date</th>
                <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600, color: '#6b7280' }}>Description</th>
                <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600, color: '#6b7280' }}>Amount</th>
                <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600, color: '#6b7280' }}>Status</th>
                <th style={{ padding: '1rem', textAlign: 'left', fontWeight: 600, color: '#6b7280' }}>Action</th>
              </tr>
            </thead>
            <tbody>
              {invoices.map(inv => (
                <tr key={inv.id} style={{ borderBottom: '1px solid #e5e7eb' }}>
                  <td style={{ padding: '1rem', fontWeight: 600, color: '#008080' }}>{inv.id}</td>
                  <td style={{ padding: '1rem', color: '#6b7280' }}>{inv.date}</td>
                  <td style={{ padding: '1rem', color: '#333' }}>{inv.description}</td>
                  <td style={{ padding: '1rem', fontWeight: 600, color: '#008080' }}>${inv.amount}</td>
                  <td style={{ padding: '1rem' }}>
                    <span style={{ background: '#10b981', color: 'white', padding: '4px 12px', borderRadius: '4px', fontSize: '0.8rem', fontWeight: 600 }}>{inv.status}</span>
                  </td>
                  <td style={{ padding: '1rem' }}>
                    <button style={{ background: '#008080', color: 'white', padding: '6px 12px', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 600 }}>Download</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Payment Methods Tab */}
      {tab === 'methods' && (
        <div style={{ display: 'grid', gap: '1rem' }}>
          {methods.map(method => (
            <div key={method.id} style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.06)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <h3 style={{ margin: 0, marginBottom: '0.5rem', fontWeight: 600 }}>{method.type} •••• {method.lastFour}</h3>
                <div style={{ color: '#6b7280', fontSize: '0.9rem' }}>Expires: {method.expiry}</div>
                {method.isDefault && <span style={{ background: '#008080', color: 'white', padding: '4px 12px', borderRadius: '4px', fontSize: '0.75rem', fontWeight: 600, marginTop: '0.5rem', display: 'inline-block' }}>Default</span>}
              </div>
              <div style={{ display: 'flex', gap: '0.5rem' }}>
                <button style={{ background: '#e5e7eb', color: '#333', padding: '8px 12px', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 600 }}>Edit</button>
                <button style={{ background: '#ef4444', color: 'white', padding: '8px 12px', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 600 }}>Delete</button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
