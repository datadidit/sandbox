# Gradle Tutorial

## Links

* [Beginner Tutorial](https://docs.gradle.org/current/userguide/part1_gradle_init.html)

## Notes

### Part 1

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

### Part 2

* View available tasks:

```bash
./gradlew tasks
```

* TODO: Would be cool to see the tasks that are dependent on each task. Look
  more into TaskInfo plugin.
* 