$(document).ready(function() {
	console.log("hi");
	var animal = $(".short-submit").dataset.animal;
	// var word = $(".short-submit").dataset.word;
	$("h1").text(animal);
	// console.log($(".short-submit").dataset.animal);
});