var forumFrontEndControllers = angular.module('forumFrontEndControllers', []);

forumFrontEndControllers.controller('ThreadListCtrl', ['$scope', '$http', 'Thread',
  function($scope, $http, Thread) {
    $scope.errorMsg = '';
    $scope.threads = Thread.query();
    $scope.blankForm = {};
    $scope.createThread = function(threadForm){
      // success and fail functions
      threadSuccess = function(response){
        $scope.threadForm = $scope.blankForm;
        $scope.threads = Thread.query();
      };
      threadFail = function(response){
        $scope.errorMsg = 'Sorry, something went wrong. \n' + response.statusText;
      };
      // actual API call to create thread
      $http.post('/api/threads/', threadForm).then(threadSuccess, threadFail);
    };
  }]);

forumFrontEndControllers.controller('ThreadDetailCtrl', ['$scope', '$routeParams', '$http', 'Thread',
  function($scope, $routeParams, $http, Thread) {
    $scope.errorMsg = '';
    $scope.comments = [];
    $scope.thread = {};
    // $scope.thread = Thread.get({threadId: $routeParams.threadId}, function(thread) {
    //   $scope.comments = $scope.thread.results.comments;
    // });
    $scope.updateThread = function(response){
      $scope.thread = Thread.get({threadId: $routeParams.threadId}, function(thread) {
        console.log('should be a new comment!');
        console.log('response: ');
        console.log(response);
        $scope.comments = thread.comments;
      });
    };

    $scope.updateThread();
    $scope.createComment = function(commentForm){
      commentForm.thread = $scope.thread.url;
      console.log('comment form: ');
      console.log(commentForm);
      var commentFail = function(response){
        $scope.errorMsg =  'Sorry, something went wrong. \n' + response.statusText;
        console.log($scope.errorMsg);
        console.log(response);
      };
      $http.post('api/comments/', commentForm).then($scope.updateThread, commentFail);
    };

  }]);