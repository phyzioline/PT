import React from 'react'

export default function Features(){
  const items = [
    {title:'Expert Doctors', text:'Access to board-certified medical professionals', icon:'fas fa-users'},
    {title:'24/7 Availability', text:'Round-the-clock medical support when you need it', icon:'fas fa-clock'},
    {title:'Secure & Private', text:'HIPAA-compliant platform ensuring your privacy', icon:'fas fa-shield-alt'}
  ]

  return (
    <section className="py-16 sm:py-24 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="text-3xl sm:text-4xl font-bold mb-8">Why Choose Ask Your Doctor?</h2>
            <div className="space-y-6">
              {items.map((it)=> (
                <div key={it.title} className="flex items-start gap-4 p-4 rounded-lg hover:bg-white hover:shadow-sm transition-all">
                  <div className="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center flex-shrink-0 text-primary">
                    <i className={`${it.icon} text-xl`}></i>
                  </div>
                  <div>
                    <h5 className="font-semibold text-lg text-gray-800 mb-1">{it.title}</h5>
                    <p className="text-gray-600">{it.text}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <img src="/images/doctor-patient.jpg" alt="" className="rounded-lg shadow-md" />
            <img src="/images/virtual-consultation.jpg" alt="" className="rounded-lg shadow-md mt-8" />
          </div>
        </div>
      </div>
    </section>
  )
}
