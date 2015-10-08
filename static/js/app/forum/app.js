var forumFrontEnd = angular.module('forumFrontEnd', [
  'ngRoute',
  'forumFrontEndControllers',

]);

forumFrontEnd.
  // router
  config(['$routeProvider',
    function($routeProvider) {
      $routeProvider.
          when('/', {
            templateUrl: 'static/partials/threadList.html',
            controller: 'ThreadListCtrl',
          })
      //   when('/phones', {
      //     templateUrl: 'partials/phone-list.html',
      //     controller: 'PhoneListCtrl'
      //   }).
      //   when('/phones/:phoneId', {
      //     templateUrl: 'partials/phone-detail.html',
      //     controller: 'PhoneDetailCtrl'
      //   }).
        .otherwise({
          redirectTo: '/'
        });
    }]);
  // fix bindings for django interpolation. Since django uses {{ binding }}, switch to {$ binding $}
  // .config(function($interpolateProvider) {
  //   $interpolateProvider.startSymbol('{$');
  //   $interpolateProvider.endSymbol('$}');
  // });