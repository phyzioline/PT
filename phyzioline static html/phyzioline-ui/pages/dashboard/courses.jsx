import React, { useState } from 'react'
import DashboardLayout from '../../components/DashboardLayout'
import dashboardData from '../../data/dashboard.json'

const ProgressBar = ({ value }) => (
  <div className="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
    <div
      className="h-full bg-gradient-to-r from-primary to-primary-light transition-all duration-500"
      style={{ width: `${value}%` }}
    />
  </div>
)

const CourseCard = ({ course }) => (
  <div className="bg-white rounded-lg shadow-sm hover:shadow-lg transition-all overflow-hidden h-full flex flex-col">
    <div className="h-40 bg-gradient-to-r from-primary to-primary-dark flex items-center justify-center text-white text-5xl">
      <i className="fas fa-book"></i>
    </div>

    <div className="p-6 flex-1 flex flex-col">
      <h3 className="text-lg font-bold text-gray-900 mb-2">{course.title}</h3>
      <p className="text-gray-600 text-sm mb-4">by {course.instructor}</p>

      <div className="space-y-4 flex-1">
        <div>
          <div className="flex justify-between items-center mb-2">
            <p className="text-sm font-medium text-gray-700">Progress</p>
            <p className="text-sm font-bold text-primary">{course.progress}%</p>
          </div>
          <ProgressBar value={course.progress} />
        </div>

        <div className="flex justify-between text-sm text-gray-600">
          <span><i className="fas fa-check mr-1 text-green-500"></i>{course.completedModules}/{course.modules} Modules</span>
        </div>
      </div>

      <div className="flex gap-2 mt-4 pt-4 border-t border-gray-200">
        <button className="flex-1 bg-primary text-white px-3 py-2 rounded-lg hover:bg-primary-dark transition-all font-medium text-sm">
          <i className="fas fa-play mr-2"></i>Continue
        </button>
        <button className="flex-1 bg-gray-100 text-gray-800 px-3 py-2 rounded-lg hover:bg-gray-200 transition-all font-medium text-sm">
          <i className="fas fa-bookmark mr-2"></i>Save
        </button>
      </div>
    </div>

    <div className="px-6 py-3 bg-gray-50 border-t border-gray-200">
      <span className={`px-3 py-1 rounded-full text-xs font-medium ${
        course.status === 'completed'
          ? 'bg-green-100 text-green-800'
          : course.status === 'active'
          ? 'bg-blue-100 text-blue-800'
          : 'bg-gray-100 text-gray-800'
      }`}>
        {course.status === 'completed' ? 'Completed' : course.status === 'active' ? 'In Progress' : 'Enrolled'}
      </span>
    </div>
  </div>
)

export default function CoursesPage() {
  const data = dashboardData.courses
  const [courses, setCourses] = useState(data.courses)
  const [filter, setFilter] = useState('all')

  const filtered = filter === 'all'
    ? courses
    : courses.filter(c => c.status === filter)

  const stats = {
    total: courses.length,
    active: courses.filter(c => c.status === 'active').length,
    completed: courses.filter(c => c.status === 'completed').length,
    enrolled: courses.filter(c => c.status === 'enrolled').length
  }

  return (
    <DashboardLayout>
      <div className="space-y-8">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">{data.title}</h1>
            <p className="text-gray-600 mt-2">Continue learning and advance your medical skills</p>
          </div>
          <button className="bg-primary text-white px-6 py-3 rounded-lg hover:bg-primary-dark transition-all font-medium">
            <i className="fas fa-plus mr-2"></i>Browse Courses
          </button>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-white rounded-lg shadow-sm p-4 text-center">
            <p className="text-3xl font-bold text-primary">{stats.total}</p>
            <p className="text-gray-600 text-sm mt-2">Total Courses</p>
          </div>
          <div className="bg-white rounded-lg shadow-sm p-4 text-center">
            <p className="text-3xl font-bold text-blue-600">{stats.active}</p>
            <p className="text-gray-600 text-sm mt-2">In Progress</p>
          </div>
          <div className="bg-white rounded-lg shadow-sm p-4 text-center">
            <p className="text-3xl font-bold text-green-600">{stats.completed}</p>
            <p className="text-gray-600 text-sm mt-2">Completed</p>
          </div>
          <div className="bg-white rounded-lg shadow-sm p-4 text-center">
            <p className="text-3xl font-bold text-yellow-600">{stats.enrolled}</p>
            <p className="text-gray-600 text-sm mt-2">Not Started</p>
          </div>
        </div>

        {/* Filter Tabs */}
        <div className="flex gap-4 border-b border-gray-200 overflow-x-auto">
          {[
            { label: 'All Courses', value: 'all' },
            { label: 'In Progress', value: 'active' },
            { label: 'Completed', value: 'completed' },
            { label: 'Enrolled', value: 'enrolled' }
          ].map(tab => (
            <button
              key={tab.value}
              onClick={() => setFilter(tab.value)}
              className={`px-4 py-3 font-medium border-b-2 transition-all whitespace-nowrap ${
                filter === tab.value
                  ? 'border-primary text-primary'
                  : 'border-transparent text-gray-600 hover:text-gray-900'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Courses Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filtered.length > 0 ? (
            filtered.map(course => (
              <CourseCard key={course.id} course={course} />
            ))
          ) : (
            <div className="col-span-full text-center py-12">
              <i className="fas fa-book text-4xl text-gray-300 mb-4"></i>
              <p className="text-gray-600 text-lg">No {filter === 'all' ? '' : filter} courses found</p>
            </div>
          )}
        </div>
      </div>
    </DashboardLayout>
  )
}
