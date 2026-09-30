# SerializeNccModel (Operator)

## Name

`SerializeNccModel` — Serialize an NCC model.

## Signature

`static void HOperatorSet.SerializeNccModel(HTuple modelID, out HTuple serializedItemHandle)`

`HSerializedItem HNCCModel.SerializeNccModel()`

## Description

`SerializeNccModel` serializes the data of an NCC model
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteNccModel`](write_ncc_model.md) is converted to a serialized
item. The NCC model is defined by the handle
*`modelID`*. The serialized NCC model is returned
by the handle *`serializedItemHandle`* and can be
deserialized by [`DeserializeNccModel`](deserialize_ncc_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeNccModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateNccModel`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeNccModel`

## Module

Matching
