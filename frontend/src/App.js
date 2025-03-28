import { BrowserRouter, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import CreateNotePage from './pages/CreateNotePage';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import LandingPage from './pages/LandingPage';
import Header from './components/Header';
import Navbar from './components/Navbar';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Navbar />
      <div style={{ padding: '20px' }}>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/create-note" element={<CreateNotePage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
