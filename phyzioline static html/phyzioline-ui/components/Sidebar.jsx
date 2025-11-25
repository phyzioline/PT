import React from 'react'
import { useRouter } from 'next/router'

export default function Sidebar({items = []}){
  const router = useRouter()
  
  const defaultItems = [
    {slug: 'overview', label: 'Dashboard Overview', icon: 'fas fa-chart-line'},
    {slug: 'appointments', label: 'Appointments', icon: 'fas fa-calendar-check'},
    {slug: 'courses', label: 'My Courses', icon: 'fas fa-book'},
    {slug: 'profile', label: 'My Profile', icon: 'fas fa-user-circle'}
  ]

  const navItems = items.length > 0 ? items : defaultItems
  const currentSlug = router.query.slug || 'overview'

  return (
    <aside className="w-64 bg-white border-r border-gray-200 h-screen sticky top-16 overflow-y-auto">
      <div className="p-6 border-b border-gray-200">
        <h2 className="text-lg font-bold text-gray-900">Dashboard</h2>
        <p className="text-sm text-gray-600 mt-1">Welcome back!</p>
      </div>
      
      <nav className="p-4 space-y-2">
        {navItems.map(item => (
          <a
            key={item.slug}
            href={`/dashboard/${item.slug}`}
            className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-all ${
              currentSlug === item.slug
                ? 'bg-primary text-white shadow-md'
                : 'text-gray-700 hover:bg-gray-50'
            }`}
          >
            <i className={item.icon}></i>
            <span className="font-medium">{item.label}</span>
          </a>
        ))}
      </nav>

      {/* Sidebar Footer */}
      <div className="absolute bottom-0 left-0 right-0 p-4 border-t border-gray-200 bg-gray-50">
        <button className="w-full bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary-dark transition-all font-medium text-sm">
          <i className="fas fa-sign-out-alt mr-2"></i>Logout
        </button>
      </div>
    </aside>
  )
}
