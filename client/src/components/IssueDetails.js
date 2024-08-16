import React from 'react';
import { useNavigate } from 'react-router-dom';
import { deleteIssue } from '../services/issueService';

const IssueDetails = ({ issue }) => {
  const navigate = useNavigate();

  const handleUpdate = () => {
    navigate(`/issues/${issue.id}/update`);
  };

  const handleDelete = async () => {
    await deleteIssue(issue.id);
    navigate('/');
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8">
          <div className="card shadow-sm rounded">
            <div className="card-body d-flex">
              <div className="flex-grow-1 border-end pe-4 me-4">
                <h5>Title</h5>
                <p>{issue.title}</p>
              </div>
              <div className="flex-grow-1">
                <h5>Description</h5>
                <p>{issue.description}</p>
              </div>
            </div>
            <div className="card-footer d-flex justify-content-center">
              <button className="btn btn-primary me-2" onClick={handleUpdate}>
                Edit Issue
              </button>
              <button className="btn btn-danger" onClick={handleDelete}>
                Delete Issue
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default IssueDetails;
