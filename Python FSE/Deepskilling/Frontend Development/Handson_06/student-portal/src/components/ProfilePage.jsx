import { useSelector, useDispatch } from 'react-redux'; 
import { unenroll } from '../enrollmentSlice'; 
import initialCourses from '../coursesData';

export default function ProfilePage() {
    const dispatch = useDispatch(); 
    
    const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses);

    const currentEnrolledDetails = initialCourses.filter(course => 
        enrolledCourses.includes(course.id)
    );

    return (
        <div style={{ background: '#ffffff', padding: '2rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
            <h2 style={{ color: '#0f172a', marginBottom: '0.5rem' }}>Student Profile Dashboard</h2>
            <p style={{ color: '#64748b', marginBottom: '2rem' }}>Manage your active academic schedule.</p>

            <h3 style={{ borderBottom: '2px solid #f1f5f9', paddingBottom: '0.5rem', marginBottom: '1rem' }}>
                Your Registered Courses ({enrolledCourses.length})
            </h3>

            {currentEnrolledDetails.length === 0 ? (
                <p style={{ color: '#64748b', fontStyle: 'italic' }}>No active registrations found.</p>
            ) : (
                <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                    {currentEnrolledDetails.map(course => (
                        <li key={course.id} style={{ padding: '1rem', borderBottom: '1px solid #f1f5f9', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                            <div>
                                <strong style={{ color: '#1e293b' }}>{course.name}</strong>
                                <div style={{ fontSize: '0.8rem', color: '#64748b' }}>{course.id} • {course.credits} Credits</div>
                            </div>
                            <button 
                                onClick={() => dispatch(unenroll(course.id))}
                                style={{ background: '#fee2e2', color: '#b91c1c', border: 'none', padding: '0.5rem 1rem', borderRadius: '4px', cursor: 'pointer', fontWeight: '600', fontSize: '0.85rem' }}
                            >
                                Drop Course
                            </button>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}
