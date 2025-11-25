import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Footer from './components/Footer'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'
import Feed from './pages/Feed'
import FeedDetail from './pages/FeedDetail'
import FeedCreate from './pages/FeedCreate'
import Accounts from './pages/Accounts'
import Marketplace from './pages/Marketplace'
import Jobs from './pages/Jobs'
import Explore from './pages/Explore'
import Login from './pages/Login'
import Courses from './pages/Courses'
import CourseDetail from './pages/CourseDetail'
import Clinics from './pages/Clinics'
import ClinicDetail from './pages/ClinicDetail'
import ModuleList from './pages/ModuleList'
import ModuleDetail from './pages/ModuleDetail'
import AIEngine from './pages/AIEngine'
import CRM from './pages/CRM'
import GlobalStats from './pages/GlobalStats'
import HomeSessions from './pages/HomeSessions'
import Payments from './pages/Payments'
import StaticLanding from './pages/StaticLanding'
import WebsiteLanding from './pages/WebsiteLanding'
import StudentDashboardMirror from './pages/StudentDashboardMirror'

export default function App(){
  return (
    <div style={{display:'flex',flexDirection:'column',minHeight:'100vh'}}>
      <Header />
      <main style={{padding:'1rem',maxWidth:1100,margin:'0 auto',flex:1,width:'100%'}}>
        <Routes>
          <Route path='/' element={<Home/>} />
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
          <Route path='/feed/new' element={<FeedCreate/>} />
          <Route path='/ai' element={<AIEngine/>} />
          <Route path='/crm' element={<CRM/>} />
          <Route path='/global-stats' element={<GlobalStats/>} />
          <Route path='/home-sessions' element={<HomeSessions/>} />
          <Route path='/payments' element={<Payments/>} />
          <Route path='/static-index' element={<StaticLanding/>} />
          <Route path='/mirror/website' element={<WebsiteLanding/>} />
          <Route path='/mirror/student-dashboard' element={<StudentDashboardMirror/>} />
          <Route path='/equivalency' element={<ModuleList moduleName={'equivalency'} title={'Equivalency'} />} />
          <Route path='/equivalency/:id' element={<ModuleDetail moduleName={'equivalency'} />} />
          <Route path='/ads' element={<ModuleList moduleName={'ads'} title={'Ads'} />} />
          <Route path='/ads/:id' element={<ModuleDetail moduleName={'ads'} />} />
        </Routes>
      </main>
      <Footer />
    </div>
  )
}
