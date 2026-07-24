import React from 'react';

function Header(props) {
    return (
        <header style={{
            background: '#0f172a',
            color: '#ffffff',
            padding: '1rem 2rem',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
        }}>
            <h1 style={{ margin: 0, fontSize: '1.5rem' }}>{props.siteName}</h1>
            
            <div style={{
                background: '#2563eb',
                padding: '0.5rem 1rem',
                borderRadius: '20px',
                fontSize: '0.9rem',
                fontWeight: 'bold'
            }}>
                Enrolled Courses: {props.enrollmentCount || 0}
            </div>
        </header>
    );
}

export default Header;