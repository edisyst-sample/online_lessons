import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/',  // Assicurati che l'URL corrisponda al backend Django
});

export default axiosInstance;
