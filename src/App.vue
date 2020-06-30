<template>
	<!-- d-flex justify-content-center navy-center -->
	<div id="app">
		<div class="california-wrap d-flex justify-content-center">
			<div class = 'california '>
				<router-link to="/">
					<button class = 'california-west'>
						<br>
					</button>
				</router-link>

				<router-link to="/">
					<button @click='UpdLogin()'>
						Home
					</button>
				</router-link>

				<router-link to="/">
					<button @click='UpdLogin()'>
						Home
					</button>
				</router-link>

				<router-link to="/">
					<button @click='UpdLogin()'>
						Home
					</button>
				</router-link>

				<router-link to="/">
					<button @click='UpdLogin()'>
						Home
					</button>
				</router-link>

				<router-link to="/">
					<button @click='UpdLogin()'>
						Home
					</button>
				</router-link>

			</div>
		</div>
		
		<!-- <transition name="fade"> -->
			<router-view />
		<!-- </transition>	 -->
	</div>
</template>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
	.california-wrap{
		height: 7%;
		box-shadow: 0 0px 10px rgba(0,0,0,0.1);
	}
	.california{
		height: 100%;
		width: 40%;
		/* outline: 2px solid yellow; */

		background-color: #fff;
		color: #57E3F4;

	}
	.california button{
		height: 100%;
		width: 15%;
		float: left;

		font-family: 'Montserrat', sans-serif;
		color: #133236;
		background-color: #fff;
		border: none;
		border-bottom: 3px rgba(87, 227, 244,0) solid;
		transition: 0.5s;

	}
	.california button:hover{
		transform: translateY(0px);
		border-bottom: 3px #57E3F4 solid;
	}
	.california button:focus{
		outline: none;
	}
	
	.california .california-west{
		width: 17%;
		height: 100%;
		float: left;
		margin-left: 4%;

		/* background-color: red; */
		background-image: url('./assets/logo-h.png');
		background-size: 100%;
		background-position: center;
		background-repeat: no-repeat;
	}
	

	html, body, #app {height:100%;}


</style>

<script>
function getCookie(name) {
	const value = `; ${document.cookie}`;
	const parts = value.split(`; ${name}=`);
	if (parts.length === 2) return parts.pop().split(';').shift();
}
export default {
    name: "App",
    data () {
        return {
            ULogin: 'Account',
        }
	},
	created() {
        if (getCookie('login')){
            this.ULogin = '#'+getCookie('login')
        }
	},
	methods: {
		UpdLogin(){
			if (getCookie('login')){
				this.ULogin = '#'+getCookie('login')
			}else{
				this.ULogin = 'ACCOUNT'
			}
		}
	}

}
</script>
