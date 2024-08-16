import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import UpdateForm from "../components/UpdateForm"
import { getIssueById, updateIssue } from '../services/issueService';

const UpdateIssuePage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [issue, setIssue] = useState(null);

  useEffect(() => {
    const fetchIssue = async () => {
      const data = await getIssueById(id);
      setIssue(data);
    };
    fetchIssue();
  }, [id]);

  const handleSubmit = async (updatedIssue) => {
    await updateIssue(id, updatedIssue);
    navigate(`/issues/${id}`);
  };

  return (
    <div>
      {issue ? <UpdateForm onSubmit={handleSubmit} initialData={issue} /> : <p>Loading...</p>}
    </div>
  );
};

export default UpdateIssuePage;
