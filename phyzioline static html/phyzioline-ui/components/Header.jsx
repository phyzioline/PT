import React, { useState } from 'react'

export default function Header(){
  const [isOpen, setIsOpen] = useState(false)

  return (
    <header className="bg-white shadow-sm sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <a href="/" className="flex items-center gap-3">
              <img src="/images/medical-icons.svg" alt="logo" className="logo-w" />
              <span className="font-semibold text-lg text-gray-800">Ask Your Doctor</span>
            </a>
          </div>

          <button 
            className="md:hidden p-2 rounded hover:bg-gray-100"
            onClick={() => setIsOpen(!isOpen)}
          >
            <i className={`fas fa-${isOpen ? 'times' : 'bars'} text-gray-700`}></i>
          </button>

          <nav className={`${isOpen ? 'block' : 'hidden'} md:flex absolute md:relative top-16 md:top-0 left-0 right-0 md:left-auto md:right-auto bg-white md:bg-transparent border-b md:border-0 w-full md:w-auto md:space-x-6 flex-col md:flex-row`}>
            <a href="/" className="nav-link block md:inline-block px-4 md:px-3 py-2 md:py-2">Home</a>
            <a href="/doctors" className="nav-link block md:inline-block px-4 md:px-3 py-2 md:py-2">Ask Your Doctor</a>
            <a href="/jobs" className="nav-link block md:inline-block px-4 md:px-3 py-2 md:py-2">Find Jobs</a>
            <a href="/courses" className="nav-link block md:inline-block px-4 md:px-3 py-2 md:py-2">Courses</a>
            <a href="/products" className="nav-link block md:inline-block px-4 md:px-3 py-2 md:py-2">Store</a>
          </nav>

          <div className="hidden md:flex items-center gap-3">
            <button className="inline-flex items-center gap-2 border-2 border-primary text-primary px-3 py-2 rounded hover:bg-primary hover:text-white transition-all"> 
              <i className="fas fa-shopping-cart"></i>
              <span id="cartCount" className="text-sm font-medium">0</span>
            </button>
            <a href="/login" className="bg-primary text-white px-4 py-2 rounded hover:bg-primary-dark transition-all font-medium">Login</a>
          </div>
        </div>
      </div>
    </header>
  )
}
