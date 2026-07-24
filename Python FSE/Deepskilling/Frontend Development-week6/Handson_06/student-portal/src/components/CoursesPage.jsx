import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux'; 
import { enroll } from '../enrollmentSlice'; 
import initialCourses from '../coursesData';

export default function CoursesPage() {
    const navigate = useNavigate();
    const dispatch = useDispatch(); 

    const handleEnrollmentAction = (courseId, courseName) => {
        dispatch(enroll(courseId));
        
        alert(`Successfully enrolled in ${courseName}!`);
        navigate('/profile');
    };

    return (
        <div>
            <h2 style={{ marginBottom: '1.5rem', color: '#0f172a' }}>Available Course Catalog</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '1.5rem' }}>
                {initialCourses.map(course => (
                    <div key={course.id} style={{ background: '#ffffff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                        <div>
                            <span style={{ fontSize: '0.85rem', color: '#2563eb', fontWeight: 'bold' }}>{course.id}</span>
                            <h3 style={{ margin: '0.5rem 0', color: '#0f172a' }}>{course.name}</h3>
                            <p style={{ color: '#64748b', fontSize: '0.9rem' }}>Credits: {course.credits} Units</p>
                        </div>
                        <button 
                            onClick={() => handleEnrollmentAction(course.id, course.name)}
                            style={{ marginTop: '1rem', width: '100%', padding: '0.6rem', background: '#2563eb', color: '#fff', border: 'none', borderRadius: '4px', fontWeight: '600', cursor: 'pointer' }}
                        >
                            Enroll in Course
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}
