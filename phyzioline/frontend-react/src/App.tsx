import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Accounts from './pages/Accounts'
import Marketplace from './pages/Marketplace'
import Jobs from './pages/Jobs'
import Explore from './pages/Explore'
import Login from './pages/Login'
import Courses from './pages/Courses'
import CourseDetail from './pages/CourseDetail'
import Clinics from './pages/Clinics'
import ClinicDetail from './pages/ClinicDetail'
import Feed from './pages/Feed'
import FeedDetail from './pages/FeedDetail'
import Dashboard from './pages/Dashboard'
import ModuleList from './pages/ModuleList'
import ModuleDetail from './pages/ModuleDetail'

export default function App(){
  return (
    <div>
      <Header />
      <main style={{padding:'1rem',maxWidth:1100,margin:'0 auto'}}>
        <Routes>
          <Route path='/' element={<Dashboard/>} />
          <Route path='/dashboard' element={<Dashboard/>} />
          <Route path='/accounts' element={<Accounts/>} />
          <Route path='/marketplace' element={<Marketplace/>} />
          <Route path='/jobs' element={<Jobs/>} />
          <Route path='/explore' element={<Explore/>} />
          <Route path='/auth/login' element={<Login/>} />
          <Route path='/courses' element={<Courses/>} />
          <Route path='/courses/:id' element={<CourseDetail/>} />
          <Route path='/clinics' element={<Clinics/>} />
          <Route path='/clinics/:id' element={<ClinicDetail/>} />
          <Route path='/feed' element={<Feed/>} />
          <Route path='/feed/:id' element={<FeedDetail/>} />
          <Route path='/ads' element={<ModuleList moduleName={'ads'} title={'Ads'} />} />
          <Route path='/ads/:id' element={<ModuleDetail moduleName={'ads'} />} />
          <Route path='/ai' element={<ModuleList moduleName={'ai_engine'} title={'AI Engine'} />} />
          <Route path='/ai/:id' element={<ModuleDetail moduleName={'ai_engine'} />} />
          <Route path='/crm' element={<ModuleList moduleName={'crm'} title={'CRM'} />} />
          <Route path='/crm/:id' element={<ModuleDetail moduleName={'crm'} />} />
          <Route path='/global-stats' element={<ModuleList moduleName={'global_stats'} title={'Global Stats'} />} />
          <Route path='/global-stats/:id' element={<ModuleDetail moduleName={'global_stats'} />} />
          <Route path='/library' element={<ModuleList moduleName={'library'} title={'Library'} />} />
          <Route path='/library/:id' element={<ModuleDetail moduleName={'library'} />} />
          <Route path='/home-sessions' element={<ModuleList moduleName={'home_sessions'} title={'Home Sessions'} />} />
          <Route path='/home-sessions/:id' element={<ModuleDetail moduleName={'home_sessions'} />} />
        </Routes>
      </main>
    </div>
  )
}
