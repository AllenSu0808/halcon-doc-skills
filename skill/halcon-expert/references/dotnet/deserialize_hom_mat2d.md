# DeserializeHomMat2d (Operator)

## Name

`DeserializeHomMat2d` — Deserialize a serialized homogeneous 2D transformation matrix.

## Signature

`static void HOperatorSet.DeserializeHomMat2d(HTuple serializedItemHandle, out HTuple homMat2D)`

`void HHomMat2D.DeserializeHomMat2d(HSerializedItem serializedItemHandle)`

## Description

`DeserializeHomMat2d` deserializes a homogeneous 2D transformation
matrix, that was serialized by [`SerializeHomMat2d`](serialize_hom_mat2d.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized transformation matrix
is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
transformation matrix with the handle *`homMat2D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Transformation matrix.

## Result

If the parameters are valid, the operator
`DeserializeHomMat2d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeHomMat2d`

## Module

Foundation
