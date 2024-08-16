import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getIssueById } from '../services/issueService';
import IssueDetail from '../components/IssueDetails';

const IssueDetailPage = () => {
  const { id } = useParams();
  const [issue, setIssue] = useState(null);

  useEffect(() => {
    const fetchIssue = async () => {
      const data = await getIssueById(id);
      setIssue(data);
    };
    fetchIssue();
  }, [id]);

  return (
    <div>
      {issue ? <IssueDetail issue={issue} /> : <p>Loading...</p>}
    </div>
  );
};

export default IssueDetailPage;
