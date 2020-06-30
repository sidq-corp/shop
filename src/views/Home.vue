<template>
	<div class="home">
		<Search />
		{{data}}
	</div>
</template>

<style>

</style>

<script>
// @ is an alias to /src
import Search from "@/components/Search.vue";
import axios from 'axios';

export default {
	name: "Home",
	components: {
		Search,
	},
	data () {
        return {
            data: [0],
        }
    },
	beforeCreate() {
		let $axios = axios.create({
			baseURL: 'http://127.0.0.1:5000/get_main_api/1',
			timeout: 5000,
			headers: {'Content-Type': 'application/json'}
		})
		$axios.get().then(response => {this.data = response.data})	
    },
	methods: {
        GetArticlesArray(){
            axios.post('http://localhost:3001/GetArticle', 'lol', {})
            .then(res => { // then print response status
                this.ArticleArray = res.data
            })
		}
	}
};
</script>
