angular.module('sortApp', [])

.controller('mainController', function($scope) {
	
	$scope.sortType     = 'goals'; // set the default sort type
	$scope.sortReverse  = true;  // set the default sort order
  
	$scope.players = [
		{ name: 'Valentin', matches: 2, goals: 6 },
		{ name: 'Sylvain', matches: 2, goals: 1 },
		{ name: 'Victor', matches: 3, goals: 2 },
		{ name: 'PF', matches: 3, goals: 2 },
		{ name: 'Gauthier', matches: 2, goals: 1 },
		{ name: 'Thibaut', matches: 0, goals: 0 },
		{ name: 'Nicolas', matches: 0, goals: 0 },
		{ name: 'Pierre', matches: 2, goals: 1 },
		{ name: 'Sevan', matches: 2, goals: 0 },
		{ name: 'Laurent', matches: 2, goals: 0 },
		{ name: 'Emeric', matches: 0, goals: 0 }
	];
	
	$scope.players.forEach(function(player) {
		player.ratio = (player.matches != 0) ? player.goals / player.matches : 0;
	});
});