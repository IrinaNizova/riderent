var myApp=angular.module('adms', []);

myApp.controller("LayersController", function ($scope, $http, $window) {

    $http({
      method: 'GET',
      url: '/adm_data'
    }).then(function successCallback(response) {
        $scope.adm_list = response.data;
        $scope.adm_list.forEach(function(entry) {
            var geom = entry.geometry.coordinates[0];
            var poly = $window.L.polygon(geom).addTo($window.mymap);
            poly.on('click', function(e) {
             $http({
              method: 'GET',
              url: 'points_in_adm/'+ entry.properties.gid
              }).then(function successCallback(response) {
                popup_text = entry.properties.name + '<br/>'
                response.data.forEach(function(entry) {
                    popup_text += " - " + entry.type + " - " + entry.count_points + ' p '
                     + entry.procent_points + '% <br/>'
                })
                poly.bindPopup(popup_text);
              })
             });
        });

      }, function errorCallback(response) {
            console.log(response);
      });
});