const serverUrl = 'http://localhost:8000';

const getAllDatasets = async () => {
  try {
    const response = await fetch(`${serverUrl}/csv`)
    return response.json();
  } catch (error) {
    return {error: error.message || 'An error occurred'};
  }
};

const postCsv = async (file) => {
  try {
    const formData = new FormData();
    formData.append('csv_file', file);
    const response = await fetch(`${serverUrl}/csv`, {
      method: 'POST',
      body: formData,
    });
    return response.json();
  } catch (error) {
    return {error: error.message || 'An error occurred'}
  }
}

const getDataset = async (id) => {
  try {
    const response = await fetch(`${serverUrl}/csv/${id}`)
    return response.json();
  } catch (error) {
    return {error: error.message || 'An error occurred'};
  }
};

const deleteDataset = async (id) => {
  try {
    const response = await fetch(`${serverUrl}/csv/${id}`, { method: 'DELETE'})
    return response.json();
  } catch (error) {
    return {error: error.message || 'An error occurred'};
  }
};

const getAmountPerCustomerPerMonth = async (id) => {
  try {
    const response = await fetch(`${serverUrl}/csv/${id}/plot`)
    return response.json()
  } catch (error) {
    return {error: error.message || 'An error occurred'};
  }
}

export { getAllDatasets, getDataset, deleteDataset, getAmountPerCustomerPerMonth, postCsv }