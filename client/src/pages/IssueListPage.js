import React, { useState, useEffect } from 'react';
import { getIssues } from '../services/issueService';
import IssueList from '../components/IssueList';

const IssueListPage = () => {
  const [issues, setIssues] = useState([]);

  useEffect(() => {
    const fetchIssues = async () => {
      const data = await getIssues();
      setIssues(data);
    };
    fetchIssues();
  }, []);

  return (
    <div className="container mt-4">
          <h3 className="text-center mb-0 pb-5">Issue List</h3>
          <IssueList issues={issues} />
    </div>
  );
};

export default IssueListPage;
