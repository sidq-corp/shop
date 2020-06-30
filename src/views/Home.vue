<template>
	<div class="home">
		<Search :page = "$route.params.id"/>
		<transition name="list" appear>
			<ProductList />
		</transition>
		
	</div>
</template>

<style>
.fade-enter-active, .fade-leave-active {
	transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
	opacity: 0;
}
.list-enter-active, .list-leave-active {
	transition: all 1s;
}
.list-enter, .list-leave-to /* .list-leave-active до версии 2.1.8 */ {
	opacity: 0;
	transform: translateY(30px);
}

.donald-enter-active, .donald-leave-active {
	transition: all 1s;
}
.donald-enter, .donald-leave-to /* .list-leave-active до версии 2.1.8 */ {
	opacity: 0;
	transform: scale(0.5);
}

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
