var portfolioApp = angular.module('portfolioApp', [], function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

portfolioApp.controller('GalleryListCtrl', function ($scope) {
    $scope.galleries = [
        {
            'title': 'Eden Hazard',
            'when': '9,01/10',
            'url': '../static/img/act1.jpg'
        },
        {
            'title': 'Didier Drogba',
            'when': '9,10/10',
            'url': '../static/img/act2.jpg'
        },
        {
            'title': 'Frank Lampard',
            'when': '9,40/10',
            'url': '../static/img/act3.jpg'
        },
        
        {
            'title': 'Petr Cech',
            'when': '9,10/10',
            'url': '../static/img/act5.jpg'
        },
        {
            'title': 'John Terry',
            'when': '9,37/10',
            'url': '../static/img/act4.jpg'
        }
        
    ];


    $scope.sortList = [
        {
            'label': 'Alfabetycznie',
            'value': 'title'
        },
        {
            'label': 'Rosnąco według ocen',
            'value': 'when'
        }
    ];

    $scope.orderProp = 'when';

});
