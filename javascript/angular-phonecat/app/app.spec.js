describe("PhoneListController", () => {
    beforeEach(module('phonecatApp'));

    it("should create a phones model with 3 phones", inject(function($controller) {
        var scrope = {};
        var ctrl = $controller('PhoneListController', {$scope: scope});

        expect(scope.phones.length).toBe(3);
    }));
});
