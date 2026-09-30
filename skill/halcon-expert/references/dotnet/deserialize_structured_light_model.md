# DeserializeStructuredLightModel (Operator)

## Name

`DeserializeStructuredLightModel` — Deserialize a structured light model.

## Signature

`static void HOperatorSet.DeserializeStructuredLightModel(HTuple serializedItemHandle, out HTuple structuredLightModel)`

`void HStructuredLightModel.DeserializeStructuredLightModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeStructuredLightModel` deserializes a structured light
model that was serialized by [`SerializeStructuredLightModel`](serialize_structured_light_model.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized structured light model is
defined by the handle *`serializedItemHandle`*. The deserialized values
are stored in an automatically created structured light model with the
handle *`structuredLightModel`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- structuredLightModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`structuredLightModel`** (output_control, state is modified)  structured_light_model `→` [HStructuredLightModel](HStructuredLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the structured light model.

## Example (HDevelop)

```
* Deserialize the model
deserialize_structured_light_model (SerializedItemHandle, \
                                    StructuredLightModel)
* Get a previously decoded result
get_structured_light_object (CorrespondenceImages, StructuredLightModel, \
                             'correspondence_image')
* Decode new camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
* Get the decoded result
get_structured_light_object (CorrespondenceImagesNew, StructuredLightModel, \
                             'correspondence_image')
```

## Result

The operator `DeserializeStructuredLightModel` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeStructuredLightModel`

## See also

`CreateStructuredLightModel`,
`WriteStructuredLightModel`,
`SerializeStructuredLightModel`

## Module

3D Metrology
