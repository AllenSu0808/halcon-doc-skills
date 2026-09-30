# DeserializeHomMat3d (Operator)

## Name

`DeserializeHomMat3d` — Deserialize a serialized homogeneous 3D transformation matrix.

## Signature

`static void HOperatorSet.DeserializeHomMat3d(HTuple serializedItemHandle, out HTuple homMat3D)`

`void HHomMat3D.DeserializeHomMat3d(HSerializedItem serializedItemHandle)`

## Description

`DeserializeHomMat3d` deserializes a homogeneous 3D transformation
matrix, that was serialized by [`SerializeHomMat3d`](serialize_hom_mat3d.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized transformation matrix
is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
transformation matrix with the handle *`homMat3D`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`homMat3D`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Transformation matrix.

## Result

If the parameters are valid, the operator
`DeserializeHomMat3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeHomMat3d`

## Module

Foundation
