async function getPhones($http) {
    let response = await $http.get('phones/phones.json');

    return response.data;
}

angular.module('phoneList').component('phoneList', {
    // To reference a static html file instead of string you must update to templateUrl
    templateUrl: 'phone-list/phone-list.template.html',
    controller: ['Phone',
        function PhoneListController(Phone) {
            this.phones = Phone.query();
            this.orderProp = 'age';
            this.name = "world";
    }
    ]
});