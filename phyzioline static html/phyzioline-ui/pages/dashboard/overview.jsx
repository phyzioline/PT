import React from 'react'
import DashboardLayout from '../../components/DashboardLayout'
import dashboardData from '../../data/dashboard.json'

const StatCard = ({ label, value, icon, color }) => (
  <div className="bg-white rounded-lg shadow-sm p-6 border-l-4" style={{borderLeftColor: color === 'primary' ? '#008080' : color === 'success' ? '#28a745' : color === 'info' ? '#17a2b8' : '#ffc107'}}>
    <div className="flex items-center justify-between">
      <div>
        <p className="text-gray-600 text-sm font-medium">{label}</p>
        <h3 className="text-3xl font-bold text-gray-900 mt-2">{value}</h3>
      </div>
      <div className="text-4xl" style={{color: color === 'primary' ? '#008080' : color === 'success' ? '#28a745' : color === 'info' ? '#17a2b8' : '#ffc107'}}>
        <i className={icon}></i>
      </div>
    </div>
  </div>
)

const AppointmentItem = ({ appointment }) => (
  <div className="bg-white rounded-lg shadow-sm p-5 border-l-4 border-primary hover:shadow-md transition-all">
    <div className="flex items-start justify-between">
      <div className="flex-1">
        <h4 className="font-semibold text-gray-900">{appointment.doctorName}</h4>
        <p className="text-sm text-gray-600">{appointment.specialty}</p>
        <p className="text-sm text-gray-600 mt-2"><i className="fas fa-calendar mr-2 text-primary"></i>{appointment.date}</p>
        <p className="text-sm text-gray-600"><i className="fas fa-clock mr-2 text-primary"></i>{appointment.time}</p>
      </div>
      <span className={`px-3 py-1 rounded-full text-sm font-medium ${appointment.status === 'upcoming' ? 'bg-blue-100 text-blue-800' : 'bg-green-100 text-green-800'}`}>
        {appointment.status === 'upcoming' ? 'Upcoming' : 'Completed'}
      </span>
    </div>
  </div>
)

export default function OverviewPage() {
  const data = dashboardData.overview

  return (
    <DashboardLayout>
      <div className="space-y-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">{data.title}</h1>
          <p className="text-gray-600 mt-2">Here's an overview of your medical platform activity</p>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {data.stats.map(stat => (
            <StatCard key={stat.label} {...stat} />
          ))}
        </div>

        {/* Recent Appointments */}
        <div>
          <h2 className="text-2xl font-bold text-gray-900 mb-6">Recent Appointments</h2>
          <div className="space-y-4">
            {data.recentAppointments.map(apt => (
              <AppointmentItem key={apt.id} appointment={apt} />
            ))}
          </div>
        </div>

        {/* Quick Actions */}
        <div className="bg-gradient-to-r from-primary to-primary-dark text-white rounded-lg p-8">
          <h3 className="text-2xl font-bold mb-4">Quick Actions</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <button className="bg-white/20 hover:bg-white/30 px-4 py-2 rounded-lg font-medium transition-all">
              <i className="fas fa-plus mr-2"></i>Book Appointment
            </button>
            <button className="bg-white/20 hover:bg-white/30 px-4 py-2 rounded-lg font-medium transition-all">
              <i className="fas fa-book mr-2"></i>View Courses
            </button>
            <button className="bg-white/20 hover:bg-white/30 px-4 py-2 rounded-lg font-medium transition-all">
              <i className="fas fa-file-medical mr-2"></i>Medical Records
            </button>
          </div>
        </div>
      </div>
    </DashboardLayout>
  )
}
