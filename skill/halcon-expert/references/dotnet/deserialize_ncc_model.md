# DeserializeNccModel (Operator)

## Name

`DeserializeNccModel` — Deserialize an NCC model.

## Signature

`static void HOperatorSet.DeserializeNccModel(HTuple serializedItemHandle, out HTuple modelID)`

`void HNCCModel.DeserializeNccModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeNccModel` deserializes an NCC model,
that was serialized by [`SerializeNccModel`](serialize_ncc_model.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized NCC model
model is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
NCC model with the handle *`modelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`modelID`** (output_control)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator
`DeserializeNccModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeNccModel`

## Possible Successors

`FindNccModel`

## See also

`CreateNccModel`,
`ClearNccModel`

## Module

Matching
