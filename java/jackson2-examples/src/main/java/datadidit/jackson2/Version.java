package datadidit.jackson2;

import static java.util.stream.Collectors.toMap;

import java.util.Map;
import java.util.NoSuchElementException;
import java.util.function.Function;
import java.util.stream.Stream;
import lombok.ToString;
import lombok.extern.java.Log;

@Log
@ToString
public enum Version {
  VERSION_1("1.0.0"),

  VERSION_1_0_2("1.0.2");

  static Map<String, Version> VERSION_MAP;

  static {
    VERSION_MAP =
        Stream.of(Version.values()).collect(toMap(Version::getVersion, Function.identity()));
  }

  String version;

  Version(String version) {
    this.version = version;
  }

  public String getVersion() {
    return version;
  }

  public static Version findVersionFromVersionString(String versionString) {
    Version version = VERSION_MAP.get(versionString);
    log.info("Versions: " + VERSION_MAP);

    if (version != null) return version;

    throw new NoSuchElementException(versionString + " is not a proper version.");
  }
}
