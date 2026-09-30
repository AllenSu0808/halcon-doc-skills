# serialize_hom_mat3d (Operator)

## Name

`serialize_hom_mat3d` — Serialize a homogeneous 3D transformation matrix.

## Signature

`def serialize_hom_mat3d(hom_mat_3d: Sequence[float]) -> HHandle`

## Description

`serialize_hom_mat3d` serializes the data of a homogeneous 3D
transformation matrix (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization).
The transformation matrix is defined by the handle *`hom_mat_3d`*.
The serialized transformation matrix is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_hom_mat3d`](deserialize_hom_mat3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

Transformation matrix.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_hom_mat3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_hom_mat3d`

## Module

Foundation
