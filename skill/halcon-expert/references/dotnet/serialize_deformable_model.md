# SerializeDeformableModel (Operator)

## Name

`SerializeDeformableModel` — Serialize a deformable model.

## Signature

`static void HOperatorSet.SerializeDeformableModel(HTuple modelID, out HTuple serializedItemHandle)`

`HSerializedItem HDeformableModel.SerializeDeformableModel()`

## Description

`SerializeDeformableModel` serializes the data of a deformable
model (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteDeformableModel`](write_deformable_model.md) is converted to a serialized
item. The deformable model is defined by the handle
*`modelID`*. The serialized deformable model is returned by the
handle *`serializedItemHandle`* and can be deserialized
by [`DeserializeDeformableModel`](deserialize_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a model to be saved.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeDeformableModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreatePlanarUncalibDeformableModel`,
`CreatePlanarCalibDeformableModel`,
`CreateLocalDeformableModel`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeDeformableModel`

## Module

Matching
