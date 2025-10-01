# OPENAPI Code Gen

## Generate Source Code

### Java

* To generate java run this command:

```bash
mvn clean install -PjavaCodeGen
```

Example code can be seen [here](generatedsources/java/src/gen/java/main/org/openapitools/client/model/Person.java)  

Note generated code is not Java code I'd write myself, would be nice if there was some lombok integration
to shrink the number of lines in this file.

#### TODO

* Get the jackson configuration to work.

### Python

```bash
mvn clean install -PpythonCodeGen
```

Example code can be seen [here](generatedsources/python/openapi_client/models/person.py)

The python generated is PyDantic and supports not generating support files. Which makes it 
easy to autogen just the model file(s) you need and the test. Code is resonable enough that I'd
actually use it as my base.

### Rust

* To generate rust run this command:

```bash
mvn clean install -PrustCodeGen
```

Example code can be seen [here](generatedsources/rust/src/models/person.rs)

## TODO:

* Add in code to generate the examples dynamically from the openapi.yaml. Solution is [here](https://stackoverflow.com/a/55997384).

## Additional Details

* Maven Plugin Docs https://openapi-generator.tech/docs/generators/java/
* Github for maven plugin https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator-maven-plugin
* Had to look in the pom.xml of the generated code to get past the dependency issues. Found
the suggestion for that on stackoverflow(TODO: link)