import { useRouter } from 'next/router'
import React, { useEffect, useState } from 'react'
import DashboardLayout from '../../components/DashboardLayout'

export default function DashboardPage(){
  const { query } = useRouter()
  const slug = query.slug || 'overview'
  const [content, setContent] = useState(null)

  useEffect(()=>{
    if (!slug) return
    fetch('/api/dashboard')
      .then(r=> r.json())
      .then(data => {
        const c = (data.content && data.content[slug]) ? data.content[slug] : { title: slug, text: 'No content available.' }
        setContent(c)
      })
      .catch(()=> setContent({ title: slug, text: 'Failed to load content.' }))
  }, [slug])

  return (
    <DashboardLayout>
      {content ? (
        <>
          <h1 className="text-2xl font-bold mb-4">{content.title}</h1>
          <p className="text-gray-600">{content.text}</p>
        </>
      ) : (
        <p className="text-gray-500">Loading...</p>
      )}
    </DashboardLayout>
  )
}
