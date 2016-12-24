angular.module('sortApp', [])

.controller('mainController', function($scope) {
	
	$scope.sortType     = 'goals'; // set the default sort type
	$scope.sortReverse  = true;  // set the default sort order
  
	$scope.players = [
		{ name: 'Valentin', matches: 9, goals: 15 },
		{ name: 'Sylvain', matches: 7, goals: 3 },
		{ name: 'Victor', matches: 12, goals: 9 },
		{ name: 'PF', matches: 9, goals: 9 },
		{ name: 'Gauthier', matches: 11, goals: 2 },
		{ name: 'Thibaut', matches: 1, goals: 0 },
		{ name: 'Nicolas', matches: 0, goals: 0 },
		{ name: 'Pierre', matches: 8, goals: 7 },
		{ name: 'Sevan', matches: 6, goals: 1 },
		{ name: 'Laurent', matches: 10, goals: 3 },
		{ name: 'Emeric', matches: 4, goals: 4 }
	];
	
	$scope.players.forEach(function(player) {
		player.ratio = (player.matches != 0) ? player.goals / player.matches : 0;
	});
});