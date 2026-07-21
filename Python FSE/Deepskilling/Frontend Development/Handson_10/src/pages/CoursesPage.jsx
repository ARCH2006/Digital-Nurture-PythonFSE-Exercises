import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {
  fetchAllCourses,
  selectCourses,
  selectCoursesError,
  selectCoursesLoading,
} from '../store/courseSlice';

function CoursesPage() {
  const dispatch = useDispatch();
  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  return (
    <main>
      <h1>Course catalogue</h1>
      <p>Courses load through a Redux async thunk and centralized API layer.</p>
      <button onClick={() => dispatch(fetchAllCourses())} disabled={loading}>
        {loading ? 'Loading…' : 'Reload courses'}
      </button>
      {error && <p className="error">{error}</p>}
      {!loading && !error && (
        <ul>
          {courses.map((course) => (
            <li key={course.id}>{course.title || course.name}</li>
          ))}
        </ul>
      )}
    </main>
  );
}

export default CoursesPage;
