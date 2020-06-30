<template>	
	<div class="row" style = 'width: 100%;'>
        <div class="col-sm-3">
			<!-- {{Products}} -->

		</div>
        <div class="col-sm-6">
            <div v-for='(product, index) in Products' :key = 'Date.now() * index' >
				<div class = 'col-sm-3 alligator-card'>
					<div class="alligator-inner">
						<div class="alligator-image">

						</div>
						<div class="alligator-bot">
							<h5>{{product[0]}}</h5>
							<p>{{product[1]}}</p>
						</div>
							
					</div>
				</div>
				<div v-if="(index+1) % 4 === 0" class = 'col-sm-12' >
					<!-- delteiem -->
				</div>
					
            </div>
			<div class="alligator-card col-sm-6 ">
				<router-link :to="{ name: 'Home', params: { id: page+1} }">
					<div class="alligator-inner alligator-blue d-flex justify-content-center">
						<div>
							<h2>Следующая страница</h2>

						</div>
					</div>
				</router-link>
			</div>
        </div>
        <div class="col-sm-3"></div>
    </div>	
</template>

<style>
	.alligator-card{
		float: left;
		/* border: 3px solid chartreuse; */
		padding: 20px;

	}
	
	.alligator-card .alligator-bot{
		padding: 5px;
	}
	.alligator-card .alligator-inner{
		transition: 0.5s;
		height: 300px;
		border-bottom: 3px rgba(87, 227, 244,0) solid;
		box-shadow: 0 0px 10px rgba(51, 51, 51,0.2);

	}
	.alligator-blue{
		background: #57E3F4;
		color: #fff;
	}
	.alligator-blue div{
		display: table;
	}
	.alligator-blue div h2{
		font-weight: 700;
		font-family: 'Montserrat', sans-serif;
		display: table-cell;
        vertical-align: middle;	
	}
	.alligator-card .alligator-inner:hover{
		border-bottom: 3px #57E3F4 solid;
		cursor: pointer;
		box-shadow: 0 0px 10px rgba(51, 51, 51,0.5);

	}
	.alligator-image{
		width: 100%;
		padding-top: 100%;
		background-image: url('../assets/bg.jpg');
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
	}
</style>

<script>
import axios from 'axios';

export default {
    name: "ProductList",
    data () {
        return {
            Products: [0],
        }
	},
	props: {
        page: {
			type: Number,
			required: false,
			default: 1
		}
    },
	created() {
		let $axios = axios.create({
			baseURL: 'http://127.0.0.1:5000/get_main_api/'+this.page,
			timeout: 5000,
			headers: {'Content-Type': 'application/json'}
		})
		$axios.get().then(response => {this.Products = response.data})	
    },
	methods: {
        GetProducts(){
            let $axios = axios.create({
				baseURL: 'http://127.0.0.1:5000/get_main_api/'+this.page,
				timeout: 5000,
				headers: {'Content-Type': 'application/json'}
			})
			$axios.get().then(response => {this.Products = response.data})	
		}
	}
    
};
</script>

