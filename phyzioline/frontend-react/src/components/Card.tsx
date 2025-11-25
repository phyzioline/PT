import React from 'react'

export default function Card({children, style}:{children:any, style?:React.CSSProperties}){
  return (
    <div style={{background:'white',padding:12,borderRadius:10,boxShadow:'0 1px 4px rgba(0,0,0,0.04)',...style}}>
      {children}
    </div>
  )
}
