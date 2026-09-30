# DeserializeMatrix (Operator)

## Name

`DeserializeMatrix` — Deserialize a serialized matrix.

## Signature

`static void HOperatorSet.DeserializeMatrix(HTuple serializedItemHandle, out HTuple matrixID)`

`void HMatrix.DeserializeMatrix(HSerializedItem serializedItemHandle)`

## Description

`DeserializeMatrix` deserializes a matrix, that was serialized
by [`SerializeMatrix`](serialize_matrix.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized matrix is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
matrix with the handle *`matrixID`*. Access to the
elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`matrixID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle.

## Result

If the parameters are valid, the operator
`DeserializeMatrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeMatrix`

## Possible Successors

`GetFullMatrix`

## Module

Foundation
