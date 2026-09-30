# SerializeDescriptorModel (Operator)

## Name

`SerializeDescriptorModel` — Serialize a descriptor model.

## Signature

`static void HOperatorSet.SerializeDescriptorModel(HTuple modelID, out HTuple serializedItemHandle)`

`HSerializedItem HDescriptorModel.SerializeDescriptorModel()`

## Description

`SerializeDescriptorModel` serializes the data of a descriptor
model (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteDescriptorModel`](write_descriptor_model.md) is converted to a serialized
item. The descriptor model is defined by the handle
*`modelID`*. The serialized descriptor model is returned by the
handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeDescriptorModel`](deserialize_descriptor_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a model to be saved.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeDescriptorModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`PointsLepetit`,
`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeDescriptorModel`

## See also

`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`

## Module

Matching
