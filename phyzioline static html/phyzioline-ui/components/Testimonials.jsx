import React from 'react'

const TestCard = ({name, role, text}) => (
  <div className="bg-white rounded-lg shadow-sm hover:shadow-lg p-6 card-hover h-full">
    <div className="text-primary mb-4 text-lg">
      <i className="fas fa-star"></i>
      <i className="fas fa-star"></i>
      <i className="fas fa-star"></i>
      <i className="fas fa-star"></i>
      <i className="fas fa-star"></i>
    </div>
    <p className="italic text-gray-700 mb-4 min-h-16">"{text}"</p>
    <div className="border-t pt-4">
      <h6 className="font-semibold text-gray-800">{name}</h6>
      <small className="text-gray-600">{role}</small>
    </div>
  </div>
)

export default function Testimonials(){
  const items = [
    {name:'Dr. Sarah Johnson', role:'Cardiologist', text:'This platform has revolutionized how I connect with patients and continue my education.'},
    {name:'Michael Chen', role:'Medical Student', text:'The courses here helped me advance my career and land my dream job in healthcare.'},
    {name:'Emily Rodriguez', role:'Patient', text:'Quick, professional consultations that saved me time and provided excellent care.'}
  ]

  return (
    <section className="py-16 sm:py-24 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="text-center mb-12">
          <h2 className="text-3xl sm:text-4xl font-bold mb-4">What Our Users Say</h2>
          <p className="text-lg text-gray-600">Trusted by healthcare professionals and patients worldwide</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {items.map(i=> <TestCard key={i.name} {...i} />)}
        </div>
      </div>
    </section>
  )
}
