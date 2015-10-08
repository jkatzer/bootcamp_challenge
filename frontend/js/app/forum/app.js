var forumFrontEnd = angular.module('forumFrontEnd', [
  'ngRoute',
  'forumFrontEndControllers',
  'forumFrontEndServices',

]);

forumFrontEnd
  // router
  .config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
    $resourceProvider.defaults.stripTrailingSlashes = false;
  }])


  .config(['$routeProvider',
    function($routeProvider) {
      $routeProvider
        .when('/threads', {
            templateUrl: 'static/partials/threadList.html',
            controller: 'ThreadListCtrl',
          })
      //   when('/phones', {
      //     templateUrl: 'partials/phone-list.html',
      //     controller: 'PhoneListCtrl'
      //   }).
        .when('/threads/:threadId', {
          templateUrl: 'partials/threadDetail.html',
          controller: 'ThreadDetailCtrl'
        })
        .otherwise({
          redirectTo: '/threads'
        });
    }]);
  // fix bindings for django interpolation. Since django uses {{ binding }}, switch to {$ binding $}
  // .config(function($interpolateProvider) {
  //   $interpolateProvider.startSymbol('{$');
  //   $interpolateProvider.endSymbol('$}');
  // });