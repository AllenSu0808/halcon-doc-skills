# SerializeMatrix (Operator)

## Name

`SerializeMatrix` — Serialize a matrix.

## Signature

`static void HOperatorSet.SerializeMatrix(HTuple matrixID, out HTuple serializedItemHandle)`

`HSerializedItem HMatrix.SerializeMatrix()`

## Description

`SerializeMatrix` serializes the data of a matrix (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteMatrix`](write_matrix.md) is converted to a serialized item.
The matrix is defined by the handle *`matrixID`*. The
serialized matrix is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeMatrix`](deserialize_matrix.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeMatrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeMatrix`

## Module

Foundation
