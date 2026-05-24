import { Brain, Zap, Shield, Cpu, ChevronRight, Check } from 'lucide-react';

function App() {
  return (
    <>
      <nav className="navbar container">
        <div className="logo">
          <Brain color="#6366f1" />
          Qadri AI
        </div>
        <ul className="nav-links">
          <li><a href="#features">Features</a></li>
          <li><a href="#pricing">Pricing</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
        <a href="#pricing" className="btn btn-primary">
          Get Started
        </a>
      </nav>

      <main>
        {/* Hero Section */}
        <section className="hero container">
          <div className="hero-badge">🚀 Version 1.0 is Live!</div>
          <h1>
            Your Advanced <br />
            <span className="text-gradient">Desktop Assistant</span>
          </h1>
          <p>
            Qadri AI brings the power of artificial intelligence directly to your desktop. 
            Automate tasks, get smart insights, and boost your productivity seamlessly.
          </p>
          <div className="hero-actions">
            <a href="#pricing" className="btn btn-primary">
              Download Now <ChevronRight size={18} />
            </a>
            <a href="#features" className="btn btn-secondary">
              Explore Features
            </a>
          </div>
        </section>

        {/* Features Section */}
        <section id="features" className="features container">
          <div className="section-header">
            <h2>Powerful Features</h2>
            <p>Everything you need to automate your digital life.</p>
          </div>
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">
                <Zap size={24} />
              </div>
              <h3>Lightning Fast</h3>
              <p>Experience instant responses and quick execution of your daily tasks without any lag.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">
                <Shield size={24} />
              </div>
              <h3>Secure & Private</h3>
              <p>Your data stays on your machine. Qadri AI respects your privacy and ensures local processing where possible.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">
                <Cpu size={24} />
              </div>
              <h3>System Control</h3>
              <p>Deep integration with your OS allows Qadri AI to manage files, settings, and workflows effortlessly.</p>
            </div>
          </div>
        </section>

        {/* Pricing / Sale Section */}
        <section id="pricing" className="pricing container">
          <div className="section-header">
            <h2>Get Qadri AI Today</h2>
            <p>Unlock the full potential of your desktop with our premium features.</p>
          </div>
          
          <div className="pricing-card">
            <h3>Pro License</h3>
            <div className="price">
              $29<span>/lifetime</span>
            </div>
            <p className="text-muted">One-time payment. Yours forever.</p>
            
            <ul className="pricing-features">
              <li><Check size={18} color="#6366f1" /> Full Desktop Access</li>
              <li><Check size={18} color="#6366f1" /> Lifetime Updates</li>
              <li><Check size={18} color="#6366f1" /> Premium Support</li>
              <li><Check size={18} color="#6366f1" /> Unlimited AI Queries</li>
            </ul>
            
            <button className="btn btn-primary" style={{ width: '100%', marginTop: '1rem' }}>
              Buy Now
            </button>
          </div>
        </section>
      </main>

      <footer className="footer">
        <div className="container">
          <p>© {new Date().getFullYear()} Qadri AI. All rights reserved.</p>
        </div>
      </footer>
    </>
  )
}

export default App
