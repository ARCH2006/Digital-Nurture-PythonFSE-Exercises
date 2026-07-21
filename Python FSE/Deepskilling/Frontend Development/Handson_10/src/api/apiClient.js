
const mockProductsDatabase = [
  { id: 101, title: "Pro HTML5 & CSS3 Masterclass", price: 49.99, stock: 12, credits: 4 },
  { id: 102, title: "Advanced React & Redux Architecture", price: 89.99, stock: 8, credits: 5 },
  { id: 103, title: "Vue 3 Enterprise Patterns with Pinia", price: 69.99, stock: 15, credits: 3 },
  { id: 104, title: "Full-Stack Node.js & Microservices", price: 99.99, stock: 5, credits: 6 }
];

const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const BASE_URL = (import.meta.env && import.meta.env.VITE_API_BASE_URL)
  || 'https://api.example.com'; // Or your local fallback address

const apiClient = {
  defaults: {
    baseURL: BASE_URL,
    timeout: 10000
  },

  async get(endpoint) {
    console.log(`[API Request Guard]: Outgoing call to simulated endpoint: ${endpoint}`);
    
    await delay(1000);


    if (endpoint.includes('/products') || endpoint.includes('/courses')) {
      return mockProductsDatabase;
    }

    throw new Error(`404: Endpoint ${endpoint} not found.`);
  }
};

export default apiClient;