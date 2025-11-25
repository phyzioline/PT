import React, { useEffect, useState } from 'react'
import Sidebar from './Sidebar'
import Header from './Header'

export default function DashboardLayout({children, items: initialItems}){
  const [items, setItems] = useState(initialItems || [])
  const [loading, setLoading] = useState(false)

  useEffect(()=>{
    if (!initialItems) {
      setLoading(true)
      fetch('/api/dashboard')
        .then(r=> r.json())
        .then(data => {
          setItems(data.items || [])
        })
        .catch(()=> {})
        .finally(()=> setLoading(false))
    }
  }, [initialItems])

  return (
    <>
      <Header />
      <div className="flex min-h-screen bg-gray-50 pt-16">
        <Sidebar items={items} />
        <main className="flex-1 p-8 overflow-auto">
          {loading ? (
            <div className="flex items-center justify-center h-screen">
              <div className="text-center">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto mb-4"></div>
                <p className="text-gray-600">Loading dashboard...</p>
              </div>
            </div>
          ) : (
            children
          )}
        </main>
      </div>
    </>
  )
}
