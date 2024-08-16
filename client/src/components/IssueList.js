import React from 'react';
import { Link } from 'react-router-dom';

const IssueList = ({ issues }) => {
  return (
    <div className="row">
      {issues.map(issue => (
        <div key={issue.id} className="col-md-6 col-lg-4 mb-4">
          <div className="card shadow-sm rounded bg-light d-flex flex-column" style={{ height: '100%' }}>
            <div className="card-body d-flex flex-column">
              <h5 className="card-title">{issue.title}</h5>
              <p className="card-text flex-grow-1 text-truncate" style={{ overflow: 'hidden', textOverflow: 'ellipsis', display: '-webkit-box', WebkitBoxOrient: 'vertical', WebkitLineClamp: 3 }}>
                {issue.description}
              </p>
              <Link to={`/issues/${issue.id}`} className="btn btn-primary mt-auto">View Details</Link>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default IssueList;
