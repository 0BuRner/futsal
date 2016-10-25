angular.module('sortApp', [])

.controller('mainController', function($scope) {
	
	$scope.sortType     = 'goals'; // set the default sort type
	$scope.sortReverse  = true;  // set the default sort order
  
	$scope.players = [
		{ name: 'Valentin', matches: 5, goals: 9 },
		{ name: 'Sylvain', matches: 5, goals: 2 },
		{ name: 'Victor', matches: 6, goals: 3 },
		{ name: 'PF', matches: 5, goals: 4 },
		{ name: 'Gauthier', matches: 5, goals: 1 },
		{ name: 'Thibaut', matches: 1, goals: 0 },
		{ name: 'Nicolas', matches: 0, goals: 0 },
		{ name: 'Pierre', matches: 6, goals: 3 },
		{ name: 'Sevan', matches: 3, goals: 0 },
		{ name: 'Laurent', matches: 4, goals: 0 },
		{ name: 'Emeric', matches: 3, goals: 4 }
	];
	
	$scope.players.forEach(function(player) {
		player.ratio = (player.matches != 0) ? player.goals / player.matches : 0;
	});
});