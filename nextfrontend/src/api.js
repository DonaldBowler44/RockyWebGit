import axios from "axios";

const apiClient = axios.create({
    baseURL: "http://localhost:5000",
    timeout: 1000,
});

//public routes

export const charInfo = async (id) => {
    try {
        const response = await apiClient.get(`/characters/${id}`);
        const { height, weight, total_fights, wins, wins_by_ko, draws, losses, stance } = response.data;
        return {
            height,
            weight,
            total_fights,
            wins,
            wins_by_ko,
            draws,
            losses,
            stance
        };
    } catch (error) {
        return {
            error: true,
            message: error.message,
        };
    }
};

export const charResults = async (id1, id2) => {
    try {
        const response = await apiClient.get(`/characters/${id1}/${id2}`);
        return response.data;
    } catch (error) { 
        return {
            error: true,
            message: error.message,
        }
    }
}

//auth routes

export const registerUser = async (email, password) => {
    try {
        const response = await apiClient.post('/register', {
            email: email,
            password: password,
        });

        return response.data;
    } catch (error) {
        throw new Error('Registration failed. Please try again.');
    }
};

export const getExistingEmails = async () => {
    try {
        const response = await apiClient.get('/register');
        return response.data.emails;
    } catch (error) {
        throw new Error('Failed to fetch existing emails.');
    }
};