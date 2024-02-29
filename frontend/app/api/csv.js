const serverUrl = 'http://localhost:8000';

const getAllDatasets = async () => {
  try {
    const response = await fetch(`${serverUrl}/csv`)
    return await response.json();
  } catch (error) {
    return {error: error.message || 'An error occurred'};
  }
};

export { getAllDatasets }