package datadidit.jackson2;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;
import java.io.IOException;
import lombok.extern.java.Log;

/** Deserializer for Version */
@Log
public class JacksonVersionDeserializer extends StdDeserializer<Version> {
  public JacksonVersionDeserializer() {
    this(null);
  }

  protected JacksonVersionDeserializer(Class<?> vc) {
    super(vc);
  }

  @Override
  public Version deserialize(JsonParser jsonParser, DeserializationContext deserializationContext)
      throws IOException {
    JsonNode node = jsonParser.getCodec().readTree(jsonParser);
    log.fine("Text " + node.asText());
    return Version.findVersionFromVersionString(node.asText());
  }
}
