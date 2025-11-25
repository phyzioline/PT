module.exports = {
  content: [
    './pages/**/*.{js,jsx,ts,tsx}',
    './components/**/*.{js,jsx,ts,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#00a0a0',
          DEFAULT: '#008080',
          dark: '#006666'
        },
        secondary: '#f8f9fa',
        success: '#28a745',
        info: '#17a2b8',
        warning: '#ffc107',
        danger: '#dc3545',
        gray: {
          50: '#f9fafb',
          100: '#f8f9fa',
          200: '#e9ecef',
          300: '#dee2e6',
          400: '#ced4da',
          500: '#adb5bd',
          600: '#6c757d',
          700: '#495057',
          800: '#343a40',
          900: '#212529'
        }
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'system-ui', 'BlinkMacSystemFont', 'Segoe UI']
      },
      spacing: {
        '128': '32rem'
      },
      borderRadius: {
        DEFAULT: '0.5rem'
      },
      boxShadow: {
        sm: '0 0.125rem 0.25rem rgba(0, 0, 0, 0.075)',
        DEFAULT: '0 0.125rem 0.25rem rgba(0, 0, 0, 0.075)',
        lg: '0 1rem 3rem rgba(0, 0, 0, 0.175)'
      }
    },
  },
  plugins: [],
}
