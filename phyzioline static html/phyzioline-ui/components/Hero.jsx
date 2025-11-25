import React from 'react'

export default function Hero(){
  return (
    <section className="bg-gray-50 py-16 sm:py-24">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
          <div>
            <h1 className="text-4xl sm:text-5xl font-bold leading-tight mb-4">Your Complete <span className="text-primary block">Medical Platform</span></h1>
            <p className="text-lg text-gray-600 mb-8">Find your doctor, advance your career, and learn new skills. Everything you need for healthcare success in one place.</p>
            <div className="flex flex-col sm:flex-row gap-4">
              <a href="/doctors" className="btn-primary inline-flex items-center justify-center">Find a Doctor <i className="fas fa-arrow-right ml-2"></i></a>
              <a href="/jobs" className="btn-outline-primary inline-flex items-center justify-center">Explore Jobs</a>
            </div>
          </div>

          <div className="hero-image">
            <img src="/images/hero-consultation.jpg" alt="Medical consultation" className="w-full rounded-lg shadow-lg" />
          </div>
        </div>
      </div>
    </section>
  )
}
