import React from 'react';

function CourseCard(props) {
    return (
        <div style={{
            background: '#ffffff',
            padding: '1.5rem',
            borderRadius: '8px',
            boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
            border: '1px solid #e2e8f0',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between'
        }}>
            <div>
                <span style={{ fontSize: '0.85rem', color: '#64748b', fontWeight: 'bold' }}>{props.code}</span>
                <h3 style={{ margin: '0.5rem 0', color: '#0f172a' }}>{props.name}</h3>
                <p style={{ margin: '0.25rem 0', color: '#334155' }}>Credits: {props.credits}</p>
                <p style={{ margin: '0.25rem 0', color: '#334155' }}>Grade: {props.grade}</p>
            </div>

            <button 
                onClick={() => props.onEnroll(props.id)} 
                style={{
                    marginTop: '1rem',
                    width: '100%',
                    padding: '0.5rem',
                    background: '#2563eb',
                    color: '#ffffff',
                    border: 'none',
                    borderRadius: '4px',
                    fontWeight: '600',
                    cursor: 'pointer'
                }}
            >
                Enroll
            </button>
        </div>
    );
}

export default CourseCard;
