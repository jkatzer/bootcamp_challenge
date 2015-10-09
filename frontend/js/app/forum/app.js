var forumFrontEnd = angular.module('forumFrontEnd', [
  'ngRoute',
  'forumFrontEndControllers',
  'forumFrontEndServices',

]);

forumFrontEnd
 
  // Don't strip trailing slashes from calculated URLs for API Calls
  .config(['$resourceProvider', function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
  }])

  // Fix CSRF for Django (http://django-angular.readthedocs.org/en/latest/csrf-protection.html)
  .config(['$httpProvider', function($httpProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }])

  // router urls
  .config(['$routeProvider',
    function($routeProvider) {
      $routeProvider.caseInsensitiveMatch = true;
      $routeProvider
        .when('/home', {
            templateUrl: 'static/partials/threadList.html',
            controller: 'ThreadListCtrl',
          })
        .when('/:threadId', {
          templateUrl: 'static/partials/threadDetail.html',
          controller: 'ThreadDetailCtrl'
        })
        .otherwise({
          redirectTo: '/home'
        });
    }]);
  // fix bindings for django interpolation. Since django uses {{ binding }}, switch to {$ binding $}
  // .config(function($interpolateProvider) {
  //   $interpolateProvider.startSymbol('{$');
  //   $interpolateProvider.endSymbol('$}');
  // });