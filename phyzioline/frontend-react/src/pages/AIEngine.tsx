import React, { useState, useEffect } from 'react'
import api from '../services/api'

export default function AIEngine() {
  const [exercises, setExercises] = useState<any[]>([])
  const [treatmentPlan, setTreatmentPlan] = useState<any>(null)
  const [searchTerm, setSearchTerm] = useState('')
  const [userInput, setUserInput] = useState('')
  const [responses, setResponses] = useState<any[]>([])

  useEffect(() => {
    fetchExercises()
  }, [])

  const fetchExercises = async () => {
    try {
      const res = await api.get('/ai_engine/exercises/').catch(() => ({ data: DEMO_EXERCISES }))
      setExercises(res.data || DEMO_EXERCISES)
    } catch (err) {
      console.log('Error fetching exercises:', err)
    }
  }

  const handleAIQuery = (e: React.FormEvent) => {
    e.preventDefault()
    if (!userInput.trim()) return
    setResponses([...responses, { type: 'user', text: userInput }, { type: 'ai', text: generateAIResponse(userInput) }])
    setUserInput('')
  }

  const generateAIResponse = (query: string) => {
    const responses: { [key: string]: string } = {
      'exercise': 'Try these exercises: 1. Shoulder rotations 2. Quad stretches 3. Core strengthening. Always warm up first!',
      'pain': 'Pain management: Apply ice for acute pain (24-48 hrs), then heat. Take anti-inflammatory medication. Perform gentle stretches.',
      'recovery': 'Recovery protocol: Rest 2-3 days, gradual PT exercises, stay hydrated, proper nutrition with protein.',
      'treatment': 'Treatment plan: Personalized based on your condition. Start with Phase 1: passive range of motion. Progress to Phase 2: active exercises.',
      'help': 'AI Engine helps with: Exercise recommendations, treatment planning, recovery guidance, pain management advice.'
    }
    for (const key in responses) {
      if (query.toLowerCase().includes(key)) return responses[key]
    }
    return 'I can help with exercise recommendations, treatment plans, and recovery guidance. Please ask about a specific condition or treatment.'
  }

  const filtered = exercises.filter(e => e.name?.toLowerCase().includes(searchTerm.toLowerCase()))

  return (
    <div style={{ maxWidth: 1100, margin: '0 auto' }}>
      <div style={{ background: 'linear-gradient(135deg, #008080 0%, #006666 100%)', color: 'white', borderRadius: '12px', padding: '2rem', marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: 0, marginBottom: '0.5rem' }}>🤖 AI Physical Therapy Engine</h1>
        <p style={{ opacity: 0.9, margin: 0 }}>Personalized AI-powered exercise and treatment recommendations</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem', marginBottom: '2rem' }}>
        {/* AI Chat */}
        <div style={{ background: 'white', borderRadius: '10px', padding: '1.5rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)', display: 'flex', flexDirection: 'column' }}>
          <h2 style={{ fontSize: '1.2rem', fontWeight: 600, margin: 0, marginBottom: '1rem' }}>AI Assistant</h2>
          <div style={{ flex: 1, background: '#f9fafb', borderRadius: '8px', padding: '1rem', marginBottom: '1rem', overflowY: 'auto', maxHeight: '400px' }}>
            {responses.length === 0 && (
              <div style={{ textAlign: 'center', color: '#6b7280', padding: '2rem' }}>
                <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>💬</div>
                <p>Ask me about exercises, treatment, or recovery!</p>
              </div>
            )}
            {responses.map((resp, i) => (
              <div key={i} style={{ marginBottom: '1rem', textAlign: resp.type === 'user' ? 'right' : 'left' }}>
                <div style={{
                  display: 'inline-block',
                  background: resp.type === 'user' ? '#008080' : '#e5e7eb',
                  color: resp.type === 'user' ? 'white' : '#333',
                  padding: '0.75rem 1rem',
                  borderRadius: '8px',
                  maxWidth: '80%'
                }}>
                  {resp.text}
                </div>
              </div>
            ))}
          </div>
          <form onSubmit={handleAIQuery} style={{ display: 'flex', gap: '0.5rem' }}>
            <input
              type="text"
              placeholder="Ask about exercises or treatment..."
              value={userInput}
              onChange={(e) => setUserInput(e.target.value)}
              style={{ flex: 1, padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px' }}
            />
            <button type="submit" style={{ background: '#008080', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 600 }}>Send</button>
          </form>
        </div>

        {/* Recommended Exercises */}
        <div style={{ background: 'white', borderRadius: '10px', padding: '1.5rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
          <h2 style={{ fontSize: '1.2rem', fontWeight: 600, margin: 0, marginBottom: '1rem' }}>Recommended Exercises</h2>
          <input
            type="text"
            placeholder="Search exercises..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{ width: '100%', padding: '10px 15px', border: '2px solid #e5e7eb', borderRadius: '6px', marginBottom: '1rem' }}
          />
          <div style={{ maxHeight: '450px', overflowY: 'auto' }}>
            {filtered.map(ex => (
              <div key={ex.id} style={{ padding: '1rem', borderBottom: '1px solid #e5e7eb', cursor: 'pointer' }} onMouseEnter={(e) => (e.currentTarget as HTMLElement).style.background = '#f9fafb'} onMouseLeave={(e) => (e.currentTarget as HTMLElement).style.background = 'white'}>
                <div style={{ fontWeight: 600, marginBottom: '0.25rem' }}>{ex.name}</div>
                <div style={{ color: '#6b7280', fontSize: '0.85rem' }}>📋 {ex.description}</div>
                <div style={{ color: '#6b7280', fontSize: '0.85rem', marginTop: '0.25rem' }}>⏱️ {ex.duration}</div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Treatment Plan */}
      <div style={{ background: 'white', borderRadius: '10px', padding: '1.5rem', boxShadow: '0 2px 8px rgba(0,0,0,0.06)' }}>
        <h2 style={{ fontSize: '1.2rem', fontWeight: 600, margin: 0, marginBottom: '1rem' }}>Your Treatment Plan</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1rem' }}>
          {[
            { phase: 'Phase 1', name: 'Assessment & Warmup', duration: 'Weeks 1-2', status: 'Active' },
            { phase: 'Phase 2', name: 'Active Exercises', duration: 'Weeks 3-6', status: 'Next' },
            { phase: 'Phase 3', name: 'Strength & Endurance', duration: 'Weeks 7-12', status: 'Future' }
          ].map((phase, i) => (
            <div key={i} style={{ background: '#f9fafb', padding: '1.5rem', borderRadius: '8px', borderLeft: `4px solid ${phase.status === 'Active' ? '#008080' : '#e5e7eb'}` }}>
              <div style={{ fontWeight: 700, color: '#008080', marginBottom: '0.5rem' }}>{phase.phase}</div>
              <div style={{ fontWeight: 600, marginBottom: '0.5rem' }}>{phase.name}</div>
              <div style={{ color: '#6b7280', fontSize: '0.9rem', marginBottom: '0.5rem' }}>{phase.duration}</div>
              <span style={{ background: phase.status === 'Active' ? '#008080' : '#e5e7eb', color: phase.status === 'Active' ? 'white' : '#333', padding: '4px 8px', borderRadius: '4px', fontSize: '0.8rem', fontWeight: 600 }}>
                {phase.status}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

const DEMO_EXERCISES = [
  { id: 1, name: 'Shoulder Rotations', description: 'Gentle rotations to improve mobility', duration: '5-10 min', difficulty: 'Easy' },
  { id: 2, name: 'Knee Bends', description: 'Quad strengthening exercise', duration: '10-15 min', difficulty: 'Intermediate' },
  { id: 3, name: 'Core Stabilization', description: 'Engage core muscles', duration: '15-20 min', difficulty: 'Intermediate' },
  { id: 4, name: 'Hip Flexor Stretch', description: 'Flexibility training for hips', duration: '5 min', difficulty: 'Easy' },
  { id: 5, name: 'Resistance Band Work', description: 'Strength building with equipment', duration: '20-25 min', difficulty: 'Hard' },
  { id: 6, name: 'Balance Exercises', description: 'Improve proprioception', duration: '10 min', difficulty: 'Easy' }
]
