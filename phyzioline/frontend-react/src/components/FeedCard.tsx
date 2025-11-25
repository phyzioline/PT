import React from 'react'

export default function FeedCard({item}:{item:any}){
  return (
    <article style={{background:'white',padding:12,borderRadius:10,marginBottom:12}}>
      <div style={{display:'flex',gap:12,alignItems:'center'}}>
        <div style={{width:44,height:44,borderRadius:22,background:'#38B2AC',color:'white',display:'flex',alignItems:'center',justifyContent:'center'}}>{(item.author||'U').slice(0,1)}</div>
        <div style={{flex:1}}>
          <div style={{fontWeight:700}}>{item.title || item.content?.slice(0,40)}</div>
          <div style={{fontSize:12,color:'#6b7280'}}>{item.author || 'مستخدم'}</div>
        </div>
      </div>
      {item.summary && <div style={{marginTop:8}}>{item.summary}</div>}
    </article>
  )
}
