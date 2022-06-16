<template>
    <b-container fluid>
        <b-row >
            <b-col v-for="player in players" v-bind:key="player.id">
                <player @cardsChanged="refreshBoard" :player="player"></player>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <b-button @click="comprobarGanador" v-if="game && game.fase == 3">COMPROBAR GANADOR</b-button>
            </b-col>
        </b-row>
        <b-row v-if="game && game.fase == 4">
            <b-col>
               EL GANADOR ES:  {{game.winner.name}}
            </b-col>
        </b-row>
    </b-container>
</template>
<script>
import BoardApi from '../api/board.js';
import Player from './Player.vue';
export default{
    name:"Board",
    components:{
        Player
    },
    async created(){
        this.refreshBoard();
    },
    data: function(){
        return {
            players: [],
            game: null
        }
    },
    methods:{
        async refreshBoard(){
            const response = await BoardApi.getPlayers();
            this.$data.players = response.data;
            const responseGame = await BoardApi.getGame();
            this.$data.game = responseGame.data;
        },
        async comprobarGanador(){
            const response = await BoardApi.comprobarGanador();
            this.$data.game = response.data;
        }
    }
}
</script>
