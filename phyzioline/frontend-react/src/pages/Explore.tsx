import React, { useEffect, useState } from 'react'
import api from '../services/api'
import { Bar } from 'react-chartjs-2'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Tooltip, Legend } from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend)

export default function Explore(){
  const [data, setData] = useState<any>(null)
  useEffect(()=>{
    api.get('/content/explore/').then(r=> setData(r.data)).catch(()=>{})
  },[])

  if (!data) return <p>جاري التحميل...</p>

  const therapists = data['THERAPISTS'] || []
  const chartData = {
    labels: therapists.map((d:any)=> d.country),
    datasets: [{ label: 'عدد المعالجين', data: therapists.map((d:any)=> d.value), backgroundColor: 'rgba(0,128,128,0.7)' }]
  }

  return (
    <section>
      <h2>Explore</h2>
      <div style={{height:300}}>
        <Bar data={chartData} options={{responsive:true, maintainAspectRatio:false}} />
      </div>
    </section>
  )
}
