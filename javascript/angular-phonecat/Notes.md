# Angular Notes

* [Angular Module](https://docs.angularjs.org/api/ng/function/angular.module)
* [ngController](https://docs.angularjs.org/api/ng/directive/ngController): directive attaches a controller class to the view.
* [ngRepeat](https://docs.angularjs.org/api/ng/directive/ngRepeat): directive instantiates a template once per item from a collection.
* [Scope](https://docs.angularjs.org/guide/scope): Is an object that refers to the application model.
* [Angular 1 Style Guide](https://github.com/johnpapa/angular-styleguide/blob/master/a1/README.md)
* [ctrl](): TODO: add some details about what this means and why it's important in templates. I believe it
gets a reference to the actual controller.
* [filter](https://docs.angularjs.org/api/ng/filter/filter): Selects a subset of items from array and returns it as a new
array.
* [ngModel](https://docs.angularjs.org/api/ng/directive/ngModel): directive binds an `input`, `select`, `textarea`, or
custom form control to a property on the scope.
* [orderBy](https://docs.angularjs.org/api/ng/filter/orderBy): Returns an array containing the items from the specified collection,
ordered by a comparator function based on the values computed using the expression predicate.
* [Angular built in $http service](https://docs.angularjs.org/api/ng/service/$http)
* [Dependency Injection](https://docs.angularjs.org/guide/di)
* [AngularJS Services](https://docs.angularjs.org/guide/services)
* The `$` prefix is there to namespace AngularJS-provided services. To prvent collisions it's best to avoid naming your services
and models anything that begins with a `$`.
* `$$` properties are private
* [ngSrc](https://docs.angularjs.org/api/ng/directive/ngSrc): Prevents the browser from treating the AngularJS `{{ expression }}`
markup literally, and initiating a request to an invalid URL.
* [ngRoute](https://docs.angularjs.org/api/ngRoute): provides routing and deeplinking services and directives for AngularJS apps.
* [Deep Linking](https://en.wikipedia.org/wiki/Deep_linking)
* [ngClick](https://docs.angularjs.org/api/ng/directive/ngClick): allows you to specify custom behavior when an element is clicked.