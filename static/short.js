$(document).ready(function() {
	
	var animal = $(".short-submit").data("animal");
	var word = $(".short-submit").data("word");
	
	var randomNum = parseInt(Math.random() * 100);
	var specialCharacter;
	
	const specialCharacters = "!?#";
	const specialArray = specialCharacters.split("");
	
	var specialNum = parseInt(Math.random() * specialArray.length);
	specialCharacter = specialArray[specialNum];
	
	const resultArray = [specialCharacter, animal, word, randomNum];
	shuffleArray(resultArray);
	
	
	var result = "";
	for (let i = 0; i < resultArray.length; i++) {
		result += resultArray[i];
	}
	
	$(".result").text(result);
	
	
	
	
	function shuffleArray(array) {
		for (var i = array.length - 1; i >= 0; i--) {
			// generate random number between 0 and i
			var j = Math.floor(Math.random() * (i + 1));	
			
			// swap the array at the current index with the array at the index of the random number generated
			var temp = array[i];
			array[i] = array[j];
			array[j] = temp;
		}
	}
});