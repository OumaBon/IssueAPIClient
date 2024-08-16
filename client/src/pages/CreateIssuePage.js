import React from 'react';
import { useNavigate } from 'react-router-dom';
import IssueForm from '../components/IssueForm';
import { createIssue } from '../services/issueService';

const CreateIssuePage = () => {
  const navigate = useNavigate();

  const handleSubmit = async (issue) => {
    await createIssue(issue);
    navigate('/');
  };

  return (
    <div>
      <IssueForm onSubmit={handleSubmit} />
    </div>
  );
};

export default CreateIssuePage;
