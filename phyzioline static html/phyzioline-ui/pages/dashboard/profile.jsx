import React, { useState } from 'react'
import DashboardLayout from '../../components/DashboardLayout'
import dashboardData from '../../data/dashboard.json'

const InfoSection = ({ title, children }) => (
  <div className="bg-white rounded-lg shadow-sm p-6">
    <h3 className="text-lg font-bold text-gray-900 mb-4">{title}</h3>
    {children}
  </div>
)

const InfoRow = ({ label, value, editable = false, onEdit = null }) => (
  <div className="flex justify-between items-center py-3 border-b border-gray-100 last:border-b-0">
    <span className="text-gray-600 font-medium">{label}</span>
    <div className="flex items-center gap-3">
      <span className="text-gray-900">{value}</span>
      {editable && (
        <button onClick={onEdit} className="text-primary hover:text-primary-dark">
          <i className="fas fa-edit"></i>
        </button>
      )}
    </div>
  </div>
)

const PreferenceToggle = ({ label, checked, onChange }) => (
  <div className="flex items-center justify-between py-3 border-b border-gray-100 last:border-b-0">
    <span className="text-gray-600 font-medium">{label}</span>
    <label className="relative inline-flex items-center cursor-pointer">
      <input
        type="checkbox"
        checked={checked}
        onChange={onChange}
        className="sr-only peer"
      />
      <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/30 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
    </label>
  </div>
)

export default function ProfilePage() {
  const data = dashboardData.profile
  const [editMode, setEditMode] = useState(false)
  const [preferences, setPreferences] = useState(data.preferences)

  const handlePreferenceChange = (key) => {
    setPreferences({
      ...preferences,
      [key]: !preferences[key]
    })
  }

  return (
    <DashboardLayout>
      <div className="space-y-8">
        {/* Header */}
        <div className="flex items-start justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">{data.title}</h1>
            <p className="text-gray-600 mt-2">Manage your account information and preferences</p>
          </div>
          <button
            onClick={() => setEditMode(!editMode)}
            className={`px-6 py-3 rounded-lg font-medium transition-all ${
              editMode
                ? 'bg-gray-200 text-gray-800 hover:bg-gray-300'
                : 'bg-primary text-white hover:bg-primary-dark'
            }`}
          >
            <i className={`fas fa-${editMode ? 'times' : 'edit'} mr-2`}></i>
            {editMode ? 'Cancel' : 'Edit Profile'}
          </button>
        </div>

        {/* Personal Information */}
        <InfoSection title="Personal Information">
          <div className="flex flex-col sm:flex-row gap-8 mb-6">
            <img
              src={data.user.avatar}
              alt={data.user.name}
              className="w-24 h-24 rounded-full shadow-md"
            />
            <div className="flex-1">
              <InfoRow label="Full Name" value={data.user.name} editable={editMode} />
              <InfoRow label="Email" value={data.user.email} editable={editMode} />
              <InfoRow label="Phone" value={data.user.phone} editable={editMode} />
              <InfoRow label="Date of Birth" value={data.user.dateOfBirth} editable={editMode} />
              <InfoRow label="Gender" value={data.user.gender} editable={editMode} />
              <InfoRow label="User Type" value={data.user.userType.charAt(0).toUpperCase() + data.user.userType.slice(1)} />
            </div>
          </div>
        </InfoSection>

        {/* Address Information */}
        <InfoSection title="Address Information">
          <InfoRow label="Street Address" value={data.address.street} editable={editMode} />
          <InfoRow label="City" value={data.address.city} editable={editMode} />
          <InfoRow label="State/Province" value={data.address.state} editable={editMode} />
          <InfoRow label="Postal Code" value={data.address.zipCode} editable={editMode} />
          <InfoRow label="Country" value={data.address.country} editable={editMode} />
        </InfoSection>

        {/* Medical Information */}
        <InfoSection title="Medical Information">
          <InfoRow label="Blood Type" value={data.medicalInfo.bloodType} editable={editMode} />
          <InfoRow label="Allergies" value={data.medicalInfo.allergies} editable={editMode} />
          <InfoRow label="Medical Conditions" value={data.medicalInfo.conditions} editable={editMode} />
          <InfoRow label="Current Medications" value={data.medicalInfo.medications} editable={editMode} />
        </InfoSection>

        {/* Notification Preferences */}
        <InfoSection title="Notification Preferences">
          <PreferenceToggle
            label="Email Notifications"
            checked={preferences.emailNotifications}
            onChange={() => handlePreferenceChange('emailNotifications')}
          />
          <PreferenceToggle
            label="SMS Notifications"
            checked={preferences.smsNotifications}
            onChange={() => handlePreferenceChange('smsNotifications')}
          />
          <PreferenceToggle
            label="Appointment Reminders"
            checked={preferences.appointmentReminders}
            onChange={() => handlePreferenceChange('appointmentReminders')}
          />
          <PreferenceToggle
            label="Course Updates"
            checked={preferences.courseUpdates}
            onChange={() => handlePreferenceChange('courseUpdates')}
          />
        </InfoSection>

        {/* Danger Zone */}
        <div className="bg-red-50 rounded-lg shadow-sm p-6 border-l-4 border-red-500">
          <h3 className="text-lg font-bold text-red-900 mb-4">Account Danger Zone</h3>
          <p className="text-red-800 mb-4">These actions cannot be undone.</p>
          <div className="flex gap-4">
            <button className="bg-orange-500 text-white px-6 py-2 rounded-lg hover:bg-orange-600 transition-all font-medium">
              <i className="fas fa-lock mr-2"></i>Change Password
            </button>
            <button className="bg-red-500 text-white px-6 py-2 rounded-lg hover:bg-red-600 transition-all font-medium">
              <i className="fas fa-trash mr-2"></i>Delete Account
            </button>
          </div>
        </div>

        {/* Save Changes */}
        {editMode && (
          <div className="flex gap-4 justify-end">
            <button
              onClick={() => setEditMode(false)}
              className="bg-gray-200 text-gray-800 px-6 py-3 rounded-lg hover:bg-gray-300 transition-all font-medium"
            >
              Cancel
            </button>
            <button className="bg-primary text-white px-6 py-3 rounded-lg hover:bg-primary-dark transition-all font-medium">
              <i className="fas fa-save mr-2"></i>Save Changes
            </button>
          </div>
        )}
      </div>
    </DashboardLayout>
  )
}
