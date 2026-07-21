import { Component } from 'react';

class ErrorBoundary extends Component {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Application error caught by ErrorBoundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <main className="error-boundary" role="alert">
          <h1>Something went wrong</h1>
          <p>We could not display the course catalogue. Please try again.</p>
          <button onClick={() => window.location.reload()}>Reload application</button>
        </main>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
