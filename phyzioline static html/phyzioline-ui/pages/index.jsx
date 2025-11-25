import Head from 'next/head'
import Header from '../components/Header'
import Hero from '../components/Hero'
import Services from '../components/Services'
import Features from '../components/Features'
import Testimonials from '../components/Testimonials'
import Footer from '../components/Footer'

export default function Home(){
  return (
    <>
      <Head>
        <title>Ask Your Doctor - Medical Platform | Healthcare Services, Jobs & Education</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="description" content="Complete healthcare platform connecting doctors, jobs, courses, and medical products." />
      </Head>

      <Header />
      <main>
        <Hero />
        <Services />
        <Features />
        <Testimonials />
        <section className="py-16 sm:py-24 bg-gray-50 text-center">
          <div className="max-w-3xl mx-auto px-4 sm:px-6">
            <h2 className="text-3xl sm:text-4xl font-bold mb-4">Ready to Get Started?</h2>
            <p className="text-lg text-gray-600 mb-8">Join thousands of patients who trust Ask Your Doctor for their healthcare needs.</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <a href="/register" className="btn-primary inline-flex items-center justify-center\">Register as Patient</a>
              <a href="/doctors" className="btn-outline-primary inline-flex items-center justify-center\">Find a Doctor</a>
            </div>
          </div>
        </section>
      </main>

      <Footer />
    </>
  )
}
