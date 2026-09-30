# serialize_hom_mat2d (Operator)

## Name

`serialize_hom_mat2d` — Serialize a homogeneous 2D transformation matrix.

## Signature

`serialize_hom_mat2d( : : HomMat2D : SerializedItemHandle)`

## Description

`serialize_hom_mat2d` serializes the data of a homogeneous 2D
transformation matrix (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization).
The transformation matrix is defined by the handle *`HomMat2D`*.
The serialized transformation matrix is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_hom_mat2d`](deserialize_hom_mat2d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HomMat2D`** (input_control)  hom_mat2d `→`  (real)

Transformation matrix.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_hom_mat2d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_hom_mat2d`

## Module

Foundation
