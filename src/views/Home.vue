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

export default {
	name: "Home",
	components: {
		Search,
	}
};
</script>
