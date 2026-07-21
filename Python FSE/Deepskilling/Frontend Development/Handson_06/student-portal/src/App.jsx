import { Routes, Route, Link } from 'react-router-dom'; // 1. Import Router features
import Header from './components/Header';
import Footer from './components/Footer';

// Import our new pages
import HomePage from './components/HomePage';
import CoursesPage from './components/CoursesPage';
import ProfilePage from './components/ProfilePage';
import CourseDetailPage from './components/CourseDetailPage';

function App() {
    return (
        <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', background: '#f8fafc' }}>
            <Header siteName="Student Portal Client Router" />
            
            {/* Minimalist Navigation Menu Bar for Testing Links */}
            <nav style={{ background: '#e2e8f0', padding: '0.75rem 2rem', display: 'flex', gap: '1.5rem' }}>
                <Link to="/" style={{ textDecoration: 'none', color: '#1e293b', fontWeight: '600' }}>Home</Link>
                <Link to="/courses" style={{ textDecoration: 'none', color: '#1e293b', fontWeight: '600' }}>Catalog</Link>
                <Link to="/profile" style={{ textDecoration: 'none', color: '#1e293b', fontWeight: '600' }}>Profile</Link>
            </nav>

            <main style={{ flexGrow: 1, padding: '2rem', maxWidth: '1200px', margin: '0 auto', width: '100%' }}>
                {/* 2. Declare the Switchboard Wrapper */}
                <Routes>
                    {/* 3. Map URL paths to the target view components */}
                    <Route path="/" element={<HomePage />} />
                    <Route path="/courses" element={<CoursesPage />} />
                    <Route path="/profile" element={<ProfilePage />} />
                    
                    {/* 4. Dynamic Wildcard matching segment using colon (:) operator */}
                    <Route path="/courses/:courseId" element={<CourseDetailPage />} />
                </Routes>
            </main>
            
            <Footer />
        </div>
    );
}

export default App;
