# SerializeStructuredLightModel (Operator)

## Name

`SerializeStructuredLightModel` — Serialize a structured light model.

## Signature

`static void HOperatorSet.SerializeStructuredLightModel(HTuple structuredLightModel, out HTuple serializedItemHandle)`

`HSerializedItem HStructuredLightModel.SerializeStructuredLightModel()`

## Description

`SerializeStructuredLightModel` serializes a structured light
model (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The structured light model is defined by the
handle *`structuredLightModel`*. The serialized structured light model
is returned by the handle *`serializedItemHandle`* and can be
deserialized by [`DeserializeStructuredLightModel`](deserialize_structured_light_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`structuredLightModel`** (input_control)  structured_light_model `→` [HStructuredLightModel](HStructuredLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the structured light model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

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

The operator `SerializeStructuredLightModel` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Successors

`ClearStructuredLightModel`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeStructuredLightModel`

## See also

`CreateStructuredLightModel`,
`ReadStructuredLightModel`,
`DeserializeStructuredLightModel`

## Module

3D Metrology
