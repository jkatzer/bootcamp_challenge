var forumFrontEndControllers = angular.module('forumFrontEndControllers', []);

forumFrontEndControllers.controller('ThreadListCtrl', ['$scope', 'Thread',
  function($scope, Thread) {
    $scope.threads = Thread.query();
    // [
    //   {
    //     title: "Hello World!",
    //     username: "thatguy",
    //   },
    //   {
    //     title: "Hello, World!",
    //     username: "that_guy",
    //   }
  // ];
  }]);

forumFrontEndControllers.controller('ThreadDetailCtrl', ['$scope', '$routeParams', 'Thread',
  function($scope, $routeParams, Thread) {
    $scope.thread = Thread.query($routeParams.threadId);

    $scope.setImage = function(imageUrl) {
      $scope.mainImageUrl = imageUrl;
    };
  }]);