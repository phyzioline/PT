import React from 'react'

export default function Footer(){
  return (
    <footer className="footer bg-primary text-white py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          <div>
            <div className="flex items-center gap-3 mb-4">
              <img src="/images/medical-icons-white.svg" alt="logo" style={{height:40}} />
            </div>
            <p className="text-gray-100 text-sm">Your complete medical platform for healthcare services, career opportunities, and medical products.</p>
          </div>

          <div>
            <h6 className="font-semibold mb-4">Services</h6>
            <ul className="space-y-2 text-gray-100 text-sm">
              <li><a href="/doctors" className="hover:text-gray-200 transition">Ask Your Doctor</a></li>
              <li><a href="/jobs" className="hover:text-gray-200 transition">Find Jobs</a></li>
              <li><a href="/courses" className="hover:text-gray-200 transition">Courses</a></li>
              <li><a href="/products" className="hover:text-gray-200 transition">Products</a></li>
            </ul>
          </div>

          <div>
            <h6 className="font-semibold mb-4">Support</h6>
            <ul className="space-y-2 text-gray-100 text-sm">
              <li><a href="/contact" className="hover:text-gray-200 transition">Help Center</a></li>
              <li><a href="/faq" className="hover:text-gray-200 transition">FAQ</a></li>
              <li><a href="/contact" className="hover:text-gray-200 transition">Contact Support</a></li>
            </ul>
          </div>

          <div>
            <h6 className="font-semibold mb-4">Connect With Us</h6>
            <div className="flex gap-4 mb-4 text-lg">
              <a href="#" className="hover:text-gray-200 transition"><i className="fab fa-facebook"></i></a>
              <a href="#" className="hover:text-gray-200 transition"><i className="fab fa-twitter"></i></a>
              <a href="#" className="hover:text-gray-200 transition"><i className="fab fa-linkedin"></i></a>
              <a href="#" className="hover:text-gray-200 transition"><i className="fab fa-instagram"></i></a>
            </div>
            <p className="text-gray-100 text-sm"><i className="fas fa-envelope mr-2"></i>support@askyourdoctor.com</p>
          </div>
        </div>

        <div className="border-t border-primary-dark pt-8 text-center text-gray-100 text-sm">&copy; 2024 Ask Your Doctor. All rights reserved.</div>
      </div>
    </footer>
  )
}
