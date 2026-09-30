# DeserializeDescriptorModel (Operator)

## Name

`DeserializeDescriptorModel` — Deserialize a descriptor model.

## Signature

`static void HOperatorSet.DeserializeDescriptorModel(HTuple serializedItemHandle, out HTuple modelID)`

`void HDescriptorModel.DeserializeDescriptorModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeDescriptorModel` deserializes a descriptor
model, that was serialized by [`SerializeDescriptorModel`](serialize_descriptor_model.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized descriptor model is
defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
descriptor model with the handle *`modelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`modelID`** (output_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator
`DeserializeDescriptorModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeDescriptorModel`

## Possible Successors

`FindUncalibDescriptorModel`,
`FindCalibDescriptorModel`

## See also

`CreateCalibDescriptorModel`,
`CreateUncalibDescriptorModel`

## Module

Matching
