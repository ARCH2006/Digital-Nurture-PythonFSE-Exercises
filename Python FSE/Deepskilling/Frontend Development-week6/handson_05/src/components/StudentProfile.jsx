import React, { useState } from 'react';

function StudentProfile() {
    const [name, setName] = useState('Rohith');
    const [email, setEmail] = useState('rohith@university.edu');
    const [semester, setSemester] = useState('6th Semester');

    const [isEditing, setIsEditing] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault(); // Prevents the browser from reloading the page
        setIsEditing(false); // Close the form view back to display mode
    };

    return (
        <div style={{
            background: '#ffffff',
            padding: '1.5rem',
            borderRadius: '8px',
            border: '1px solid #e2e8f0',
            boxShadow: '0 1px 3px rgba(0,0,0,0.05)',
            marginBottom: '2rem',
            width: '100%'
        }}>
            <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a' }}>Student Profile Panel</h3>

            {!isEditing ? (
                <div>
                    <p style={{ margin: '0.5rem 0' }}><strong>Name:</strong> {name}</p>
                    <p style={{ margin: '0.5rem 0' }}><strong>Email:</strong> {email}</p>
                    <p style={{ margin: '0.5rem 0' }}><strong>Current Standing:</strong> {semester}</p>
                    <button 
                        onClick={() => setIsEditing(true)}
                        style={{
                            marginTop: '1rem',
                            padding: '0.5rem 1rem',
                            background: '#0f172a',
                            color: '#ffffff',
                            border: 'none',
                            borderRadius: '4px',
                            cursor: 'pointer'
                        }}
                    >
                        Edit Profile
                    </button>
                </div>
            ) : (
                <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                    <div>
                        <label style={{ display: 'block', marginBottom: '0.25rem', fontWeight: '600', fontSize: '0.9rem' }}>Name:</label>
                        <input 
                            type="text" 
                            value={name}
                            onChange={(e) => setName(e.target.value)} // Bind input to state on change
                            style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }}
                            required
                        />
                    </div>

                    <div>
                        <label style={{ display: 'block', marginBottom: '0.25rem', fontWeight: '600', fontSize: '0.9rem' }}>Email:</label>
                        <input 
                            type="email" 
                            value={email}
                            onChange={(e) => setEmail(e.target.value)} // Bind input to state on change
                            style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }}
                            required
                        />
                    </div>

                    <div>
                        <label style={{ display: 'block', marginBottom: '0.25rem', fontWeight: '600', fontSize: '0.9rem' }}>Semester:</label>
                        <select 
                            value={semester}
                            onChange={(e) => setSemester(e.target.value)} // Bind dropdown to state on change
                            style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1', background: '#fff' }}
                        >
                            <option value="1st Semester">1st Semester</option>
                            <option value="2nd Semester">2nd Semester</option>
                            <option value="3rd Semester">3rd Semester</option>
                            <option value="4th Semester">4th Semester</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', gap: '0.5rem', marginTop: '0.5rem' }}>
                        <button type="submit" style={{ padding: '0.5rem 1rem', background: '#2563eb', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: '600' }}>
                            Save Changes
                        </button>
                        <button type="button" onClick={() => setIsEditing(false)} style={{ padding: '0.5rem 1rem', background: '#e2e8f0', color: '#334155', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
                            Cancel
                        </button>
                    </div>
                </form>
            )}
        </div>
    );
}

export default StudentProfile;