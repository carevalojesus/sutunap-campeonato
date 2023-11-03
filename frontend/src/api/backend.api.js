import axios from 'axios';

export const getAllEditions = () => {
    return axios.get('http://localhost:8000/backend/api/editions/')
}

export const getAllPhases = () => {
    return axios.get('http://localhost:8000/backend/api/phases/')
}

export const getAllGroups = () => {
    return axios.get('http://localhost:8000/backend/api/groups/')
}

export const getAllTeams = () => {
    return axios.get('http://localhost:8000/backend/api/teams/')
}