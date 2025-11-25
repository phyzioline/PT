import React from 'react'
import services from '../data/services.json'

function Card({icon, title, text, link}){
  return (
    <div className="bg-white rounded-lg shadow-sm hover:shadow-lg p-6 text-center card-hover h-full">
      <div className="service-icon mb-4 bg-primary/10">
        <i className={`text-primary text-2xl ${icon}`}></i>
      </div>
      <h4 className="font-semibold text-lg mb-2 text-gray-800">{title}</h4>
      <p className="text-gray-600 mb-6 min-h-12">{text}</p>
      <a href={link || '#'} className="text-primary font-medium hover:text-primary-dark">Learn More <i className="fas fa-arrow-right ml-2"></i></a>
    </div>
  )
}

export default function Services(){
  return (
    <section className="py-16 sm:py-24 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="text-center mb-12">
          <h2 className="text-3xl sm:text-4xl font-bold mb-4">Our Services</h2>
          <p className="text-lg text-gray-600">Comprehensive healthcare solutions designed for patients, professionals, and students</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {services.map(s => (
            <Card key={s.title} icon={s.icon} title={s.title} text={s.text} link={s.link} />
          ))}
        </div>
      </div>
    </section>
  )
}
