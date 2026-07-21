/* eslint-disable react-refresh/only-export-components */
import { createContext, useState } from 'react';

export const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {
    const [enrolledCourses, setEnrolledCourses] = useState([]);

    const enrollInCourse = (courseId) => {
        if (enrolledCourses.includes(courseId)) {
            alert("You are already enrolled in this course!");
            return false;
        }
        setEnrolledCourses([...enrolledCourses, courseId]);
        return true;
    };

    const removeCourse = (courseId) => {
        setEnrolledCourses(enrolledCourses.filter(id => id !== courseId));
    };

    return (
        <EnrollmentContext.Provider value={{ enrolledCourses, enrollInCourse, removeCourse }}>
            {children}
        </EnrollmentContext.Provider>
    );
}
