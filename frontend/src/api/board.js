import axios from 'axios';

export default{

    getPlayers(){
        return axios.get("/api/players/86/");
    },
    changeChards(){
        return axios.post("");
    },
    getGame(){
        return axios.get("/api/game/86/");
    },
    comprobarGanador(){
        return axios.put("/api/comprobarGanador/86/",{},{xsrfCookieName: "csrftoken",xsrfHeaderName:"X-CSRFTOKEN"})
    },
    

}