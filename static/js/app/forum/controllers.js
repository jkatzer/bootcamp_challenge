var forumFrontEndControllers = angular.module('forumFrontEndControllers', []);

forumFrontEndControllers.controller('ThreadListCtrl', ['$scope',
  function($scope) {
    $scope.threads = 
    [
      {
        title: "Hello World!",
        username: "thatguy",
      },
      {
        title: "Hello, World!",
        username: "that_guy",
      }
    ]
  }]);

phonecatControllers.controller('PhoneDetailCtrl', ['$scope', '$routeParams', 'Phone',
  function($scope, $routeParams, Phone) {
    $scope.phone = Phone.get({phoneId: $routeParams.phoneId}, function(phone) {
      $scope.mainImageUrl = phone.images[0];
    });

    $scope.setImage = function(imageUrl) {
      $scope.mainImageUrl = imageUrl;
    };
  }]);