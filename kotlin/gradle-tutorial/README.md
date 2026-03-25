# Gradle Tutorial

## Links

* [Beginner Tutorial](https://docs.gradle.org/current/userguide/part1_gradle_init.html)

## Notes

* Where does gradle store it's local deps:

```bash
ls -l ~/.gradle/caches/modules-2/files-2.1/
```

### [Beginner Tutorial](https://docs.gradle.org/current/userguide/part1_gradle_init.html)

#### Part 1: Initializing the Project

* Help for init command:

```bash
macbookpro:gradle-tutorial mkwyche$ gradle help --task init
Starting a Gradle Daemon (subsequent builds will be faster)
```

* Commands to generate:

```bash
# Generates the Kotlin Template Project which makes the wrapper etc...
macbookpro:gradle-tutorial mkwyche$ gradle init --type kotlin-application --dsl kotlin
# Post outcome is:
macbookpro:gradle-tutorial mkwyche$ ls -l
total 56
-rw-r--r--  1 mkwyche  staff   287 Mar 24 21:43 _README.md
drwxr-xr-x  4 mkwyche  staff   128 Mar 24 21:48 app
drwxr-xr-x  4 mkwyche  staff   128 Mar 24 21:48 gradle
-rw-r--r--  1 mkwyche  staff   194 Mar 24 21:48 gradle.properties
-rwxr-xr-x  1 mkwyche  staff  8654 Mar 24 21:48 gradlew
-rw-r--r--  1 mkwyche  staff  2896 Mar 24 21:48 gradlew.bat
-rw-r--r--  1 mkwyche  staff   531 Mar 24 21:48 settings.gradle.kts
```

* Gain a better understanding of:
  * [settings.gradle.kts](settings.gradle.kts)
  * [build.gradle.kts](app/build.gradle.kts)
  * [libs.versions.toml](gradle/libs.versions.toml)

#### Part 2: Running Tasks

* View available tasks:

```bash
./gradlew tasks
```

* TODO: Would be cool to see the tasks that are dependent on each task. Look
  more into TaskInfo plugin.

#### Part 3: Understanding Dependencies

* Dependencies live in [build.gradle.kts](app/build.gradle.kts) .
  * Scopes:
    * implementation
    * runtimeOnly
    * testImplementation
* Dependency Versions live in [libs.versions.toml](gradle/libs.versions.toml)
  * By defining them there you can clean up the [build.gradle.kts](app/build.gradle.kts) to not need versions. This is
    basically the same concept as parent poms.
* ./gradlew app:dependencies == mvn dependency:tree

#### Part 4: Applying Plugins

* Adding in plugins. For example add this:

```kotlin
    // Apply the maven publish plugin
    id("maven-publish")
```

To the plugins section. This will add Publishing Tasks to your list of tasks:

```bash
Publishing tasks
----------------
publish - Publishes all publications produced by this project.
publishToMavenLocal - Publishes all Maven publications produced by this project to the local Maven cache.
```

* Publish to maven locally:

```bash
./gradlew :app:publishToMavenLocal
```

* Plugins extend Gradles capabilities by adding tasks, configurations and behavior to your build. They are the
  main way to organize and reuse build logic.
  * Plugin Types:
    * Core plugins: Built into Gradle (e.g. java, application) . See full list of core plugins [here](https://docs.gradle.org/current/userguide/plugin_reference.html)
    * Community Plugins: Published by others to the [Gradle Plugin Portal](https://plugins.gradle.org/)
    * Custom Plugins: Created by you or your team for internal use.

#### Part 5: Exploring Incremental Builds

* Label Outcomes:
  * UP-TO-DATE : Task that has been already executed and hasn't changed.
  * SKIPPED : Task was explicitly prevented from running
  * FROM-CACHE : Task output has been copied to local directory from previous builds in the build cache (caching feature)
  * NO-SOURCE : Task was not executed because it's required inputs we not available.

#### Part 6: Enabling the Gradle Build Cache

* The build cache is here

  ```bash
  ls -l ~/.gradle/caches/build-cache-1/
  ```
* Remote build cache can likely be used to speed up build. 
  * Develocity is a tool for that https://gradle.com/develocity/product/build-cache/



