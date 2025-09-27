# OPENAPI Code Gen

## Generate Source Code

* To generate java run this command:

```bash
mvn clean install -PjavaCodeGen
```

This generates way too many 

* To generate python run this command:

```bash
mvn clean install -PpythonCodeGen
```

The python generated is PyDantic and supports not generating support files. Which makes it 
easy to autogen just the model file(s) you need and the test.

* To generate rust run this command:

```bash
mvn clean install -PrustCodeGen
```

## Additional Details

* Maven Plugin Docs https://openapi-generator.tech/docs/generators/java/
* Github for maven plugin https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator-maven-plugin
* Had to look in the pom.xml of the generated code to get past the dependency issues. Found
the suggestion for that on stackoverflow(TODO: link)