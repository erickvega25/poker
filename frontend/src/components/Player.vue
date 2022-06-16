<template>
    <b-card :title="player.name">
        <b-row>
            <b-col v-for="card in player.hand" v-bind:key="card.id" >
                <Card @cardMarked="cardMarkedEvent" :card="card" :isMarked="isMarked(card.id)" :player="player"></Card>  
            </b-col>  
        </b-row>
            <hr>
        <b-row>
            <b-col>
                <b-button v-if="player.user && !player.haCambiado"  @click="changeCards" href="#" variant="primary">CAMBIAR</b-button>
            </b-col>
        </b-row>
    </b-card>
</template>
<script>
import Card from './Card.vue';
import PlayerApi from '../api/player';
export default{
    name: "Player",
    components:{
        Card
    },
    props:{
        player:{
            type: Object,
            required: true
        }
    },
    data(){
        return{
            // cards: [],
            markedCards: []
        }
    },
    methods:{
        cardMarkedEvent(cardId){
            if(this.$data.markedCards.includes(cardId)){
                let index = this.$data.markedCards.indexOf(cardId);
                this.$data.markedCards.splice(index, 1);
            }
            else{
                this.$data.markedCards.push(cardId);
            }
        },
        isMarked(cardId){
            return this.$data.markedCards.includes(cardId);
        },
        async changeCards(){
            const response = await PlayerApi.putCambioCartas(this.$props.player.id,this.$data.markedCards);
            if(response.data.status == "KO"){
                alert(response.data.message);
            }
            else{
                // this.$data.cards = response.data.hand;
                this.$emit("cardsChanged");
            }
            
            
        }
    }
}
//QUE NO SE VEAN LAS CARTAS DE LOS BOTS SI NO HA CAMBIADO
</script>
