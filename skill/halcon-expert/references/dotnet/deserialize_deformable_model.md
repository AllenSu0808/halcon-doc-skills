# DeserializeDeformableModel (Operator)

## Name

`DeserializeDeformableModel` — Deserialize a deformable model.

## Signature

`static void HOperatorSet.DeserializeDeformableModel(HTuple serializedItemHandle, out HTuple modelID)`

`void HDeformableModel.DeserializeDeformableModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeDeformableModel` deserializes a deformable model,
that was serialized by [`SerializeDeformableModel`](serialize_deformable_model.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized deformable model is
defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
deformable model with the handle *`modelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`modelID`** (output_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator
`DeserializeDeformableModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeDeformableModel`

## Possible Successors

`FindPlanarUncalibDeformableModel`,
`FindPlanarCalibDeformableModel`,
`FindLocalDeformableModel`

## See also

`CreatePlanarUncalibDeformableModel`,
`CreatePlanarCalibDeformableModel`,
`CreateLocalDeformableModel`

## Module

Matching
