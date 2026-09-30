# deserialize_structured_light_model (Operator)

## Name

`deserialize_structured_light_model` — Deserialize a structured light model.

## Signature

`def deserialize_structured_light_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_structured_light_model` deserializes a structured light
model that was serialized by [`serialize_structured_light_model`](serialize_structured_light_model.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized structured light model is
defined by the handle *`serialized_item_handle`*. The deserialized values
are stored in an automatically created structured light model with the
handle *`structured_light_model`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- structured_light_model

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`structured_light_model`** (output_control, state is modified)  structured_light_model `→` HHandle

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

The operator `deserialize_structured_light_model` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_structured_light_model`

## See also

`create_structured_light_model`,
`write_structured_light_model`,
`serialize_structured_light_model`

## Module

3D Metrology
