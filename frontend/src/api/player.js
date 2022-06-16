import axios from 'axios';

export default{
    putCambioCartas(playerId,markedCards){
        return axios.put("/api/player/change_cards/"+playerId+"/",{markedCards:markedCards},{xsrfCookieName: "csrftoken",xsrfHeaderName:"X-CSRFTOKEN"});
    }
}