# serialize_structured_light_model (Operator)

## Name

`serialize_structured_light_model` — Serialize a structured light model.

## Signature

`def serialize_structured_light_model(structured_light_model: HHandle) -> HHandle`

## Description

`serialize_structured_light_model` serializes a structured light
model (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The structured light model is defined by the
handle *`structured_light_model`*. The serialized structured light model
is returned by the handle *`serialized_item_handle`* and can be
deserialized by [`deserialize_structured_light_model`](deserialize_structured_light_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`structured_light_model`** (input_control)  structured_light_model `→` HHandle

Handle of the structured light model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Example (HDevelop)

```
* Create the model
create_structured_light_model ('deflectometry', StructuredLightModel)
* Generate the patterns to project
gen_structured_light_pattern (PatternImages, StructuredLightModel)
* Decode the camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
* Serialize the model
serialize_structured_light_model (StructuredLightModel, \
                                  SerializedItemHandle)
```

## Result

The operator `serialize_structured_light_model` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Successors

`clear_structured_light_model`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_structured_light_model`

## See also

`create_structured_light_model`,
`read_structured_light_model`,
`deserialize_structured_light_model`

## Module

3D Metrology
