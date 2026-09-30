# SerializeHomMat2d (Operator)

## Name

`SerializeHomMat2d` — Serialize a homogeneous 2D transformation matrix.

## Signature

`static void HOperatorSet.SerializeHomMat2d(HTuple homMat2D, out HTuple serializedItemHandle)`

`HSerializedItem HHomMat2D.SerializeHomMat2d()`

## Description

`SerializeHomMat2d` serializes the data of a homogeneous 2D
transformation matrix (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization).
The transformation matrix is defined by the handle *`homMat2D`*.
The serialized transformation matrix is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeHomMat2d`](deserialize_hom_mat2d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Transformation matrix.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeHomMat2d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeHomMat2d`

## Module

Foundation
