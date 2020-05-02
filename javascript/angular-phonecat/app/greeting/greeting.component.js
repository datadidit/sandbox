angular.module('phonecatApp').component("greetUser", {
    template: 'Hello, {{$ctrl.user}}!',
    controller: function GreenUserController() {
        this.user = 'world';
    }
});