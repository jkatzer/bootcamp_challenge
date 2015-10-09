// Declare controller module
var forumFrontEndControllers = angular.module('forumFrontEndControllers', []);


//**********
// Thread Listing Controller
//**********
forumFrontEndControllers.controller('ThreadListCtrl', ['$scope', '$http', 'Thread',
  function($scope, $http, Thread) {
    // init template vars
    $scope.errorMsg = '';
    $scope.threads = Thread.query();
    $scope.blankForm = {};

    //nice latest poster function
    $scope.latest_poster = function(thread){
      return (thread.comments.length > 0 ? thread.comments[thread.comments.length-1].username : thread.username);
    };

    // action to create new thread
    $scope.createThread = function(threadForm){
      // success function resets form and refreshs thread listings
      threadSuccess = function(response){
        $scope.threadForm = $scope.blankForm;
        $scope.threads = Thread.query(); 
      };
      // fail function with debuging info
      threadFail = function(response){
        $scope.errorMsg = 'Sorry, something went wrong. \n' + response.statusText;
        console.log('oops!');
        console.log(response);
      };
      // actual API call to create thread
      $http.post('/api/threads/', threadForm).then(threadSuccess, threadFail);
    };
  }]);


//**********
// Thread Detail Controller
//**********
forumFrontEndControllers.controller('ThreadDetailCtrl', ['$scope', '$routeParams', '$http', 'Thread',
  function($scope, $routeParams, $http, Thread) {
    // init vars
    $scope.errorMsg = '';
    $scope.comments = [];
    $scope.commentForm = {};
    $scope.thread = {};
    // refresh mechanism
    $scope.updateThread = function(response){
      $scope.thread = Thread.get({threadId: $routeParams.threadId}, function(thread) {
        console.log('update!');
        // console.log('should be a new comment!');
        // console.log('response: ');
        // console.log(response);
        $scope.comments = angular.copy(thread.comments);
      });
    };
    // init the session with above
    $scope.updateThread();
    // mechanism to refresh only comments
    $scope.updateComments = function(){
      Thread.get({threadId: $routeParams.threadId}, function(data){
        $scope.comments = data.comments;
        $scope.$apply();
      });
    };
    // action to post new new comment
    $scope.createComment = function(commentForm){
      // get url (rest api's pk to interact with thread)
      commentForm.thread = $scope.thread.url;
      // fail function. TODO: refactor
      var commentFail = function(response){
        $scope.errorMsg =  'Sorry, something went wrong. \n' + response.statusText;
        console.log($scope.errorMsg);
        console.log(response);
      };
      // attempt to create comment loaded with values from the comment form
      $http.post('api/comments/', commentForm).then(function(){ $scope.commentForm = {}; $scope.updateComments(); }, commentFail);
    };


    // comment score functions
    // add one to comment's score
    $scope.scorePlus = function(comment){
      // fail function. TODO: refactor
      var updateFail = function(response){
        comment.errorMsg = 'Sorry, something went wrong. \n' + response.statusText;
        console.log('error:');
        console.log(response);
      };
      // make payload to be sent by API
      var payload = angular.copy(comment);
      payload.score += 1;
      // update comment score with API call, then reflect changes in local model without whole refresh
      $http.put(comment.url, payload).then( function(){ comment.score += 1; $scope.updateComments(); }, updateFail);
    }; 
    // subtract one from comment's score
    $scope.scoreMinus = function(comment){
      // fail function. TODO: refactor
      var updateFail = function(response){
        comment.errorMsg = 'Sorry, something went wrong. \n' + response.statusText;
        console.log('error:');
        console.log(response);
      };
      // make payload to be sent by API
      var payload = angular.copy(comment);
      payload.score -= 1;
      // update comment score with API call, then reflect changes in local model without whole refresh
      $http.put(comment.url, payload).then( function(){ comment.score -= 1; $scope.updateComments(); }, updateFail);
    };




  }]);