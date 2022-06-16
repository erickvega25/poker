<template>

    <span :style="cursorStyle">
        <b-img :style="markedStyle" @click="markCard" fluid :src="require('../assets/cards/'+imageName)"/>
    </span>
        
</template>
<script>
export default{
    name: "Card",
    props:{
        card:{
            type:Object,
            required: true
        },
        isMarked:{
            type: Boolean,
            required: true
        },
        player:{
            type: Object,
            required: true
        }
    },
    computed:{
        markedStyle(){
            if(this.$props.isMarked){
                return "border: 4px solid blue;"
            }
            return "";
        },
        cursorStyle(){
            if(this.$props.player.user){
                return "cursor:pointer;";
            }
            return "";
        },
        imageName(){
            
            let imageName = "";
            if (!this.$props.player.user && !this.$props.player.haCambiado){
                imageName += "back_card.png";
                return imageName;
            }
            switch(this.$props.card.number){
                case 1:
                    imageName += "ace_of_";
                    break;
                case 11:
                    imageName += "jack_of_";
                    break;
                case 12:
                    imageName += "queen_of_";
                    break;
                case 13:
                    imageName += "king_of_";
                    break;
                default:
                    imageName += this.$props.card.number + "_of_";
                    break;
            }
            switch(this.$props.card.suit){
                case 'DIAMANTE':
                    imageName += "diamonds";
                    break;
                case 'CORAZON':
                    imageName += "hearts";
                    break;
                case 'TREBOL':
                    imageName += "clubs";
                    break;
                case 'PICA':
                    imageName += "spades"
                    break;
            }
            if(this.$props.card.number > 10){
                imageName += "2.png";
            }
            else{
                imageName += ".png"
            }
            return imageName;         
        }
    },
    methods:{
        markCard(){
            if (this.$props.player.user){
                this.$emit('cardMarked',this.$props.card.id);
            }           
        }
    }
}
</script>
