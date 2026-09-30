# SerializeHomMat3d (Operator)

## Name

`SerializeHomMat3d` — Serialize a homogeneous 3D transformation matrix.

## Signature

`static void HOperatorSet.SerializeHomMat3d(HTuple homMat3D, out HTuple serializedItemHandle)`

`HSerializedItem HHomMat3D.SerializeHomMat3d()`

## Description

`SerializeHomMat3d` serializes the data of a homogeneous 3D
transformation matrix (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization).
The transformation matrix is defined by the handle *`homMat3D`*.
The serialized transformation matrix is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeHomMat3d`](deserialize_hom_mat3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Transformation matrix.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeHomMat3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeHomMat3d`

## Module

Foundation
