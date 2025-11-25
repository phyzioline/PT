// Simple mock API for dashboard navigation and content
export default function handler(req, res) {
  const items = [
    { slug: 'overview', label: 'Overview' },
    { slug: 'appointments', label: 'Appointments' },
    { slug: 'courses', label: 'My Courses' },
    { slug: 'profile', label: 'Profile' }
  ]

  const content = {
    overview: { title: 'Overview', text: 'Welcome to your dashboard overview. Metrics and quick links go here.' },
    appointments: { title: 'Appointments', text: 'List of upcoming and past appointments.' },
    courses: { title: 'My Courses', text: 'Your enrolled courses and progress.' },
    profile: { title: 'Profile', text: 'Manage your profile and account settings.' }
  }

  res.status(200).json({ items, content })
}
