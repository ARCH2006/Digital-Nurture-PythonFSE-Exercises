import { useSelector } from 'react-redux';

function Header() {
    const  enrolledCourses  = useSelector((state) => state.enrollment.enrolledCourses);


    return (
        <header style={{ background: '#0f172a', color: '#fff', padding: '1rem 2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h1 style={{ margin: 0, fontSize: '1.5rem' }}>Student Portal Dashboard</h1>
            
            <div style={{ background: 'var(--accent)', padding: '0.5rem 1rem', borderRadius: '20px', fontSize: '0.9rem', fontWeight: 'bold' }}>
                Enrolled Courses: {enrolledCourses.length}
            </div>
        </header>
    );
}

export default Header;
