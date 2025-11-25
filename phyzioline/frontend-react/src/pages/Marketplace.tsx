import React, { useState, useEffect } from 'react'
import api from '../services/api'

const DEMO_PRODUCTS = [
  { id: 1, name: 'Stethoscope Pro', price: 89.99, category: 'Equipment', rating: 4.8, inStock: 15 },
  { id: 2, name: 'Digital Blood Pressure Monitor', price: 49.99, category: 'Equipment', rating: 4.6, inStock: 8 },
  { id: 3, name: 'Medical Gloves (Box of 100)', price: 15.99, category: 'Supplies', rating: 4.9, inStock: 50 },
  { id: 4, name: 'Thermometer Infrared', price: 35.99, category: 'Equipment', rating: 4.7, inStock: 12 },
  { id: 5, name: 'First Aid Kit Premium', price: 59.99, category: 'Kits', rating: 4.8, inStock: 25 },
  { id: 6, name: 'Surgical Mask (50 pack)', price: 12.99, category: 'Supplies', rating: 4.5, inStock: 100 },
  { id: 7, name: 'Oxygen Pulse Oximeter', price: 29.99, category: 'Equipment', rating: 4.7, inStock: 18 },
  { id: 8, name: 'Medical Textbook Bundle', price: 149.99, category: 'Books', rating: 4.6, inStock: 6 }
]

export default function Marketplace() {
  const [products, setProducts] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [filter, setFilter] = useState('all')
  const [cart, setCart] = useState<any[]>([])
  const [showCart, setShowCart] = useState(false)

  useEffect(() => {
    fetchProducts()
  }, [])

  const fetchProducts = async () => {
    try {
      setLoading(true)
      const res = await api.get('/marketplace/').catch(() => ({ data: DEMO_PRODUCTS }))
      setProducts(res.data || DEMO_PRODUCTS)
    } finally {
      setLoading(false)
    }
  }

  const addToCart = (product: any) => {
    const existing = cart.find(item => item.id === product.id)
    if (existing) {
      setCart(cart.map(item => item.id === product.id ? { ...item, qty: item.qty + 1 } : item))
    } else {
      setCart([...cart, { ...product, qty: 1 }])
    }
    alert(`${product.name} added to cart!`)
  }

  const removeFromCart = (productId: number) => {
    setCart(cart.filter(item => item.id !== productId))
  }

  const totalPrice = cart.reduce((sum, item) => sum + (item.price * item.qty), 0)

  const filtered = products.filter(p =>
    (p.name?.toLowerCase().includes(searchTerm.toLowerCase()) || '') &&
    (filter === 'all' || p.category === filter)
  )

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0, marginBottom: '0.5rem' }}>Medical Marketplace</h1>
        <p style={{ opacity: 0.9, margin: 0 }}>High-quality medical equipment, supplies & resources</p>
      </div>

      <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)', display: 'flex', gap: '1rem', justifyContent: 'space-between', alignItems: 'center' }}>
        <input
          type="text"
          placeholder="Search products..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{ flex: 1, padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px', fontSize: '1rem' }}
        />
        <button
          onClick={() => setShowCart(!showCart)}
          style={{ background: '#008080', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600, whiteSpace: 'nowrap' }}
        >
          🛒 Cart ({cart.length})
        </button>
      </div>

      {showCart && (
        <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          <h2 style={{ fontSize: '1.3rem', fontWeight: 600, margin: 0, marginBottom: '1rem' }}>Shopping Cart</h2>
          {cart.length === 0 ? (
            <div style={{ color: '#6b7280', padding: '2rem', textAlign: 'center' }}>Your cart is empty</div>
          ) : (
            <>
              {cart.map(item => (
                <div key={item.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '1rem', borderBottom: '1px solid #e5e7eb' }}>
                  <div>
                    <div style={{ fontWeight: 600 }}>{item.name}</div>
                    <div style={{ color: '#6b7280', fontSize: '0.9rem' }}>Qty: {item.qty} × ${item.price}</div>
                  </div>
                  <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
                    <div style={{ fontWeight: 700, color: '#008080' }}>${(item.price * item.qty).toFixed(2)}</div>
                    <button
                      onClick={() => removeFromCart(item.id)}
                      style={{ background: '#f3f4f6', border: 'none', padding: '6px 12px', borderRadius: '6px', cursor: 'pointer' }}
                    >
                      Remove
                    </button>
                  </div>
                </div>
              ))}
              <div style={{ padding: '1rem', textAlign: 'right', fontSize: '1.2rem', fontWeight: 700, borderTop: '2px solid #e5e7eb' }}>
                Total: ${totalPrice.toFixed(2)}
              </div>
              <button style={{ width: '100%', background: '#008080', color: 'white', padding: '12px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600, marginTop: '1rem' }}>
                Checkout
              </button>
            </>
          )}
        </div>
      )}

      <div style={{ background: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap', marginBottom: '1rem' }}>
          {['all', 'Equipment', 'Supplies', 'Kits', 'Books'].map(cat => (
            <button
              key={cat}
              onClick={() => setFilter(cat)}
              style={{
                padding: '8px 16px',
                border: filter === cat ? '2px solid #008080' : '2px solid #e5e7eb',
                background: filter === cat ? '#008080' : 'white',
                color: filter === cat ? 'white' : '#333',
                borderRadius: '6px',
                cursor: 'pointer',
                fontWeight: 600
              }}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: '2rem', color: '#6b7280' }}>Loading products...</div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '1.5rem' }}>
          {filtered.map(product => (
            <div
              key={product.id}
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
              <div style={{ background: '#f3f4f6', height: '150px', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#6b7280', fontSize: '3rem' }}>📦</div>
              <div style={{ padding: '1.5rem' }}>
                <h3 style={{ fontSize: '1rem', fontWeight: 600, margin: 0, marginBottom: '0.5rem' }}>{product.name}</h3>
                <div style={{ color: '#6b7280', fontSize: '0.9rem', marginBottom: '0.75rem' }}>
                  <div>{product.category}</div>
                  <div>⭐ {product.rating}</div>
                  <div>In Stock: {product.inStock}</div>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontWeight: 700, fontSize: '1.2rem', color: '#008080' }}>${product.price}</span>
                  <button
                    onClick={() => addToCart(product)}
                    disabled={product.inStock === 0}
                    style={{
                      background: product.inStock === 0 ? '#ccc' : '#008080',
                      color: 'white',
                      padding: '8px 12px',
                      border: 'none',
                      borderRadius: '6px',
                      cursor: product.inStock === 0 ? 'not-allowed' : 'pointer',
                      fontWeight: 600
                    }}
                  >
                    {product.inStock === 0 ? 'Out of Stock' : 'Add'}
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
