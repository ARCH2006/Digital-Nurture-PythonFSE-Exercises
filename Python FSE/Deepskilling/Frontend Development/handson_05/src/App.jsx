import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';
import initialCourses from './coursesData';

function App() {
    const [courses, setCourses] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [enrolledCourses, setEnrolledCourses] = useState([]);
    const [loading , setLoading] = useState(true);
    const [error , setError] = useState(null);

    //  New useEffect to monitor and log courses state mutations
    useEffect(() => {
        if (courses.length > 0) {
            console.log('Courses updated');
        }
    }, [courses]); 
    /*  WHY THE DEPENDENCY ARRAY MATTERS HERE:
    The dependency array `[courses]` acts as a watcher list for React. 
    
    1. If left empty `[]`, this effect would only run once when the page loads, 
        missing any data that arrives later from the internet.
    2. If omitted entirely (no array at all), this block would execute on *every single keystroke* in the search input, causing massive performance lag.
    3. By passing `[courses]`, React is instructed to execute this side-effect 
        ONLY when the `courses` state array memory reference actually changes.
    */

    useEffect(() => {
        setLoading(true);
        fetch('https://jsonplaceholder.typicode.com/posts')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Unable to load live course data');
                }
                return response.json();
            })
            .then(data => {
                const firstFivePosts = data.slice(0, 10);
                
                const transformedCourses = firstFivePosts.map((post, index) => ({
                    id: post.id,
                    name: initialCourses[index].name,
                    code: initialCourses[index].code,
                    credits: initialCourses[index].credits,
                    grade: initialCourses[index].grade
                }));

                // Update state with our live network results
                setCourses(transformedCourses);
                setLoading(false);
            })
            .catch(err => {
                console.error("Error fetching data: ", err);
                setError(err.message || "An unknown error occurred");
                setCourses(initialCourses);
                setLoading(false);
            });
    }, []); 

    const enrolledDetails = courses.filter(course => enrolledCourses.includes(course.id));

    const handleEnroll = (courseId) => {
        if (enrolledCourses.includes(courseId)) {
            alert("You are already enrolled in this course!");
            return;
        }
        setEnrolledCourses([...enrolledCourses, courseId]);
    };

    const handleUnenroll = (courseId) => {
        setEnrolledCourses(enrolledCourses.filter(id => id !== courseId));
    };

    const filteredCourses = courses.filter(course => 
        course.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        course.code.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', background: '#f8fafc' }}>
            <Header siteName="Student Portal" enrollmentCount={enrolledCourses.length} />            
            
            <main style={{ 
                flexGrow: 1, 
                padding: '2rem', 
                maxWidth: '1400px', 
                margin: '0 auto', 
                width: '100%',
                display: 'flex',
                gap: '2rem',
                flexWrap: 'wrap'
            }}>
                
                <div style={{ flex: '3', minWidth: '300px' }}>
                    <h2 style={{ marginBottom: '1.5rem', color: '#0f172a' }}>Available Courses (Live API)</h2>
                    {error && (
                        <p style={{ color: '#b91c1c', marginTop: '-1rem', marginBottom: '1rem' }}>
                            Could not load live data. Showing saved courses instead.
                        </p>
                    )}
                    
                    <div style={{ marginBottom: '2rem' }}>
                        <input 
                            type="text" 
                            placeholder="Search by course name or code..." 
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                            style={{ width: '100%', maxWidth: '400px', padding: '0.75rem 1rem', borderRadius: '6px', border: '1px solid #cbd5e1' }}
                        />
                    </div>
                    
                    {/* Visual Loading State */}
                    {loading ? (
                        <p style={{ color: '#64748b', fontSize: '1.2rem' }}>Loading data from server...</p>
                    ) : filteredCourses.length === 0 ? (
                        <p style={{ color: '#64748b', fontSize: '1.1rem' }}>No courses found.</p>
                    ) : (
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '1.5rem' }}>
                            {filteredCourses.map(course => (
                                <CourseCard 
                                    key={course.id} 
                                    {...course} 
                                    onEnroll={handleEnroll} 
                                />
                            ))}
                        </div>
                    )}
                </div>

                <div style={{ flex: '1', minWidth: '280px', alignSelf: 'flex-start' }}>
                    <StudentProfile />

                    <div style={{ background: '#ffffff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
                        <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a', borderBottom: '2px solid #e2e8f0', paddingBottom: '0.5rem' }}>
                            Registration Box ({enrolledCourses.length})
                        </h3>

                        {enrolledDetails.length === 0 ? (
                            <p style={{ color: '#64748b', fontSize: '0.95rem', fontStyle: 'italic' }}>
                                No courses selected yet.
                            </p>
                        ) : (
                            <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                                {enrolledDetails.map(course => (
                                    <li key={course.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0.75rem 0', borderBottom: '1px solid #f1f5f9' }}>
                                        <div>
                                            <div style={{ fontWeight: '600', fontSize: '0.9rem', color: '#1e293b' }}>{course.name}</div>
                                            <div style={{ fontSize: '0.75rem', color: '#64748b' }}>{course.code}</div>
                                        </div>
                                        <button onClick={() => handleUnenroll(course.id)} style={{ background: '#ef4444', color: '#ffffff', border: 'none', padding: '0.25rem 0.5rem', borderRadius: '4px', fontSize: '0.8rem', cursor: 'pointer' }}>
                                            Drop
                                        </button>
                                    </li>
                                ))}
                            </ul>
                        )}
                    </div>
                </div>
            </main>
            
            <Footer />
        </div>
    );
}

export default App;
