const API_BASE_URL = 'http://localhost:5000'; 

export const createIssue = async (issue) => {
  const response = await fetch(`${API_BASE_URL}/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(issue),
  });
  return response.json();
};

export const getIssues = async () => {
  const response = await fetch(`${API_BASE_URL}/issues`);
  return response.json();
};

export const getIssueById = async (id) => {
  const response = await fetch(`${API_BASE_URL}/issues/${id}`);
  return response.json();
};

export const updateIssue = async (id, issue) => {
  const response = await fetch(`${API_BASE_URL}/issues/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(issue),
  });
  return response.json();
};

export const deleteIssue = async (id) => {
  const response = await fetch(`${API_BASE_URL}/issues/${id}`, {
    method: 'DELETE',
  });
  return response.json();
};
