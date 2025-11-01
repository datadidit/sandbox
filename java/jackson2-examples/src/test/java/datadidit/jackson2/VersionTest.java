package datadidit.jackson2;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.exc.InvalidDefinitionException;
import com.fasterxml.jackson.databind.module.SimpleModule;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.java.Log;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.EnumSource;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

@Log
public class VersionTest {
    private ObjectMapper mapper;

    @BeforeEach
    public void setup() {
        mapper = new ObjectMapper();

        SimpleModule module = new SimpleModule();
        module.addDeserializer(Version.class, new JacksonVersionDeserializer());

        mapper.registerModule(module);
    }

    @Test
    public void testBlooperDeserializaerJsonParseException() {
        // Tried several different iterations of this
        JsonParseException exception = assertThrows(JsonParseException.class, () -> mapper.readValue(Version.VERSION_1_0_2.version, Version.class));
        log.info("" + exception);
    }

    @Test
    public void testBlooperNeedCustomSerializerForThisToWork() throws JsonProcessingException {
        Example example = new Example();
        example.setVersions(Arrays.asList(Version.VERSION_1));

        InvalidDefinitionException exception = assertThrows(InvalidDefinitionException.class, () -> mapper.readValue(mapper.writeValueAsString(example), Example.class));
        log.info("" + exception);
    }

    @ParameterizedTest
    @EnumSource(Version.class)
    public void testWorks(Version xVersion) throws JsonProcessingException {
        Version version = mapper.readValue("\"" + xVersion.version + "\"", Version.class);
        log.info("Version: " + xVersion);
        assertEquals(xVersion, version);
    }

    @Data
    @NoArgsConstructor
    static class Example {
        List<Version> versions;
    }
}