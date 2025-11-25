import React from 'react'
import { useRouter } from 'next/router'

export default function DashboardIndex() {
  const router = useRouter()

  React.useEffect(() => {
    router.push('/dashboard/overview')
  }, [router])

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto mb-4"></div>
        <p className="text-gray-600">Redirecting to dashboard...</p>
      </div>
    </div>
  )
}
