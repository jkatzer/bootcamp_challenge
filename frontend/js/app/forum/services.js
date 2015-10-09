var forumFrontEndServices = angular.module('forumFrontEndServices', ['ngResource']);

forumFrontEndServices.factory('Thread', ['$resource',
  function($resource){
  	//var urlString = 'api/threads/' + ( params.threadId !== '' ? ':threadId/' : '');
    var urlString = "api/threads/:threadId/?format=json";
    return $resource(urlString, {}, {
      query: {
      	method:'GET', 
      	//params:{threadId:':threadId'}, 
      }
    });
  }]);
