var forumFrontEndServices = angular.module('forumFrontEndServices', ['ngResource']);

// The tool for querying all threads
forumFrontEndServices.factory('Thread', ['$resource',
  function($resource){
  	// define url string in advance of query for potential debug purposes
    var urlString = "api/threads/:threadId/";
    // api get query with empty params
    return $resource(urlString, {}, {
      query: {
      	method:'GET', 
      	//params:{threadId:':threadId'}, 
      }
    });
  }]);
