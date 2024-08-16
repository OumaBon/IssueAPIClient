import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CreateIssuePage from './pages/CreateIssuePage';
import IssueListPage from './pages/IssueListPage';
import IssueDetailPage from './pages/IssueDetailPage';
import UpdateIssuePage from './pages/UpdateIssuePage';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

const App = () => {
  return (
    <Router>
      <div className="app-container">
        <Navbar />
        <main className="flex-grow-1">
          <Routes>
            <Route path="/create" element={<CreateIssuePage />} />
            <Route path="/issues/:id/update" element={<UpdateIssuePage />} />
            <Route path="/issues/:id" element={<IssueDetailPage />} />
            <Route path="/issues" element={<IssueListPage />} />
            <Route path="/" element={<IssueListPage />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
