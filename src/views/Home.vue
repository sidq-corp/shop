<template>
	<div class="home">
		<Search />
		<ProductList />
		
	</div>
</template>

<style>

</style>

<script>
// @ is an alias to /src
import Search from "@/components/Search.vue";
import ProductList from "@/components/ProductList.vue";

export default {
	name: "Home",
	components: {
		Search,
		ProductList,
	},
	data () {
        return {

        }
    },
	beforeCreate() {

    },
	methods: {

	}
};
</script>
