<template>
	<div class="home">
		<Search />
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
	beforeCreate() {
        axios.post('http://localhost:3001/GetArticle', 'lol', {})
        .then(res => { // then print response status
            this.ArticleArray = res.data
        })
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
