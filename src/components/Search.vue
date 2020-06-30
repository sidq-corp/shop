<template>	
	<div>	
		<br>
		<div class = 'croco-card'>
			<transition name="donald" appear>
				<div>
					<h3>Покупки. Легко!</h3>
					<input type="text" placeholder="Поиск">
				</div>
			</transition>
		</div>
	</div>	
		
</template>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    .croco-card{
        width: 100%;
        height: 200px;
		display: table;
		padding-bottom: 40px;
		margin-bottom: 30px;

		font-weight: 700;
		font-family: 'Montserrat', sans-serif;
		color: #57E3F4;
        background: linear-gradient(to top, rgba(87, 227, 244,0.5) 0%,#ffffff 50%);
        align-content: center;
        align-items: center;
        text-align: center;
        justify-content: center;
    }
    .croco-card div{
        display: table-cell;
        vertical-align: middle;	
    }
	.croco-card div h3{
		font-weight: 700;
		font-family: 'Montserrat', sans-serif;
	}
	.croco-card div input{
        box-shadow: 0 0px 10px rgba(0,0,0,0.15);
        border: none;
		width: 20%;
		/* height: 30%; */
		font-size: 120%;
		padding: 10px;
		color: #133236;
    }
	.croco-card div input:focus{
		outline: none;
	}
</style>

<script>
export default {
    name: "Search",
    data () {
        return {
            // items: ['a', 'b', 'c']
        }
    },
    methods: {

    }
};
</script>

