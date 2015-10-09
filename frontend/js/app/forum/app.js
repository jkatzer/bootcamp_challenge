var forumFrontEnd = angular.module('forumFrontEnd', [
  'ngRoute',
  'forumFrontEndControllers',
  'forumFrontEndServices',

]);

// the main module, preparing for configuration
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
      // just in case, case shouldn't make a difference
      $routeProvider.caseInsensitiveMatch = true;
      $routeProvider
        // home page route
        .when('/home', {
            templateUrl: 'static/partials/threadList.html',
            controller: 'ThreadListCtrl',
          })
        // thread view route
        .when('/:threadId', {
          templateUrl: 'static/partials/threadDetail.html',
          controller: 'ThreadDetailCtrl'
        })
        // default route.  TODO: 404 route
        .otherwise({
          redirectTo: '/home'
        });
    }]);