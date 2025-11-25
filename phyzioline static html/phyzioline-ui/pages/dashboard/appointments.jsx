import React, { useState } from 'react'
import DashboardLayout from '../../components/DashboardLayout'
import dashboardData from '../../data/dashboard.json'

const AppointmentCard = ({ appointment, onCancel }) => (
  <div className="bg-white rounded-lg shadow-sm hover:shadow-lg transition-all p-6">
    <div className="flex items-start justify-between mb-4">
      <div>
        <h3 className="text-lg font-bold text-gray-900">{appointment.doctorName}</h3>
        <p className="text-gray-600">{appointment.specialty}</p>
      </div>
      <span className={`px-3 py-1 rounded-full text-sm font-medium ${appointment.status === 'upcoming' ? 'bg-blue-100 text-blue-800' : 'bg-green-100 text-green-800'}`}>
        {appointment.status === 'upcoming' ? 'Upcoming' : 'Completed'}
      </span>
    </div>

    <div className="space-y-2 mb-4 pb-4 border-b border-gray-200">
      <p className="text-gray-600"><i className="fas fa-calendar-check mr-2 text-primary"></i><strong>Date:</strong> {appointment.date}</p>
      <p className="text-gray-600"><i className="fas fa-clock mr-2 text-primary"></i><strong>Time:</strong> {appointment.time}</p>
      <p className="text-gray-600"><i className="fas fa-stethoscope mr-2 text-primary"></i><strong>Reason:</strong> {appointment.reason}</p>
      <p className="text-gray-600"><i className="fas fa-map-marker-alt mr-2 text-primary"></i><strong>Location:</strong> {appointment.location}</p>
    </div>

    <div className="flex gap-3">
      <button className="flex-1 bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary-dark transition-all font-medium">
        <i className="fas fa-video mr-2"></i>Join Video Call
      </button>
      {appointment.status === 'upcoming' && (
        <button onClick={() => onCancel(appointment.id)} className="flex-1 bg-gray-200 text-gray-800 px-4 py-2 rounded-lg hover:bg-gray-300 transition-all font-medium">
          <i className="fas fa-times mr-2"></i>Cancel
        </button>
      )}
    </div>
  </div>
)

export default function AppointmentsPage() {
  const data = dashboardData.appointments
  const [appointments, setAppointments] = useState(data.appointments)
  const [filter, setFilter] = useState('all')

  const handleCancel = (id) => {
    setAppointments(appointments.filter(a => a.id !== id))
  }

  const filtered = filter === 'all' ? appointments : appointments.filter(a => a.status === filter)

  return (
    <DashboardLayout>
      <div className="space-y-8">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">{data.title}</h1>
            <p className="text-gray-600 mt-2">Manage your medical appointments</p>
          </div>
          <button className="bg-primary text-white px-6 py-3 rounded-lg hover:bg-primary-dark transition-all font-medium">
            <i className="fas fa-plus mr-2"></i>Book New Appointment
          </button>
        </div>

        {/* Filter Tabs */}
        <div className="flex gap-4 border-b border-gray-200">
          {[
            { label: 'All', value: 'all' },
            { label: 'Upcoming', value: 'upcoming' },
            { label: 'Completed', value: 'completed' }
          ].map(tab => (
            <button
              key={tab.value}
              onClick={() => setFilter(tab.value)}
              className={`px-4 py-3 font-medium border-b-2 transition-all ${
                filter === tab.value
                  ? 'border-primary text-primary'
                  : 'border-transparent text-gray-600 hover:text-gray-900'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Appointments Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {filtered.length > 0 ? (
            filtered.map(appointment => (
              <AppointmentCard key={appointment.id} appointment={appointment} onCancel={handleCancel} />
            ))
          ) : (
            <div className="col-span-full text-center py-12">
              <i className="fas fa-calendar-times text-4xl text-gray-300 mb-4"></i>
              <p className="text-gray-600 text-lg">No {filter === 'all' ? '' : filter} appointments found</p>
            </div>
          )}
        </div>
      </div>
    </DashboardLayout>
  )
}
