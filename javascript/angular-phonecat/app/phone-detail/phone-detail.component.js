angular.module('phoneDetail')
    .component('phoneDetail', {
        // template: 'TBD: Detail view for <span>{{$ctrl.phoneId}}</span>',
        templateUrl: 'phone-detail/phone-detail.template.html',
        controller: ['$routeParams', 'Phone', function PhoneDetailController($routeParams, Phone){
            var self = this;

            self.phoneId = $routeParams.phoneId;

            self.setImage = function setImage(imageUrl) {
                self.mainImageUrl = imageUrl;
            };

            self.phone = Phone.get({phoneId: self.phoneId}, function(phone){
                self.setImage(phone.images[0]);
            });

            // $http.get('phones/' + $routeParams.phoneId + '.json').then((response) => {
            //     self.phone = response.data;
            //     self.setImage(self.phone.images[0]);
            // });
        }]
    })