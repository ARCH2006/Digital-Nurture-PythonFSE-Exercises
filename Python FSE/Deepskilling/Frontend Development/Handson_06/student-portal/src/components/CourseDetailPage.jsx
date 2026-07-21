import { useParams, Link } from 'react-router-dom'; 
import initialCourses from '../coursesData'; 

export default function CourseDetailPage() {
    const { courseId } = useParams();

    const course = initialCourses.find(c => c.id === courseId);

    if (!course) {
        return (
            <div style={{ padding: '1.5rem', background: '#fee2e2', borderRadius: '6px', color: '#991b1b' }}>
                <h3>⚠️ Syllabus Record Not Found</h3>
                <p>The course code <strong>"{courseId}"</strong> does not exist in our enrollment register.</p>
                <Link to="/courses" style={{ color: 'var(--accent)', fontWeight: 'bold' }}>Return to Catalog</Link>
            </div>
        );
    }

    return (
        <div style={{ background: '#ffffff', padding: '2rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
            <span style={{ fontSize: '0.9rem', color: 'var(--accent)', fontWeight: 'bold' }}>{course.id}</span>
            <h2 style={{ margin: '0.5rem 0 1.5rem 0', color: '#0f172a' }}>{course.name}</h2>
            
            <div style={{ display: 'flex', gap: '2rem', marginBottom: '1.5rem', paddingBottom: '1rem', borderBottom: '1px solid #f1f5f9' }}>
                <div><strong>Academic Credits:</strong> {course.credits} Units</div>
                <div><strong>Lecture Timing:</strong> {course.schedule}</div>
            </div>

            <h4 style={{ margin: '0 0 0.5rem 0', color: '#334155' }}>Course Description:</h4>
            <p style={{ color: '#475569', lineHeight: '1.6', margin: '0 0 2rem 0' }}>{course.description}</p>

            <Link to="/courses" style={{ textDecoration: 'none', background: '#0f172a', color: '#fff', padding: '0.5rem 1rem', borderRadius: '4px', fontSize: '0.9rem' }}>
                ← Back to Catalog List
            </Link>
        </div>
    );
}
