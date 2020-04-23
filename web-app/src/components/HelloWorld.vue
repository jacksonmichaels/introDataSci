<template>
	<div class="App">
		<div class="header">
			<h1>Header</h1>
		</div>
		<div class="column side">
			<button v-on:click="">Search</button>
			<button>Filter</button>
			<button>Data</button>
		</div>
		<div class="column middle">
			<h1> Middle Column</h1>
		</div>
	</div>
</template>

<script>
    export default {
        name: 'HelloWorld',
        props: {

        },
        methods: {

        },
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	h3 {
		margin: 40px 0 0;
	}

	ul {
		list-style-type: none;
		padding: 0;
	}

	li {
		display: inline-block;
		margin: 0 10px;
	}

	a {
		color: #42b983;
	}

	.header {
		background-color: #F1F1F1;
		text-align: center;
		padding: 20px;
	}

	.column {
		float: left;
	}

	.column.side {
		width: 25%;
	}

	.column.middle {
		width: 75%;
	}

	@media screen and (max-width: 600px) {
		.column.side, .column.middle {
			width: 100%;
		}
	}
</style>
