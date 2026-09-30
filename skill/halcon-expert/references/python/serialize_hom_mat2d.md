# serialize_hom_mat2d (Operator)

## Name

`serialize_hom_mat2d` — Serialize a homogeneous 2D transformation matrix.

## Signature

`def serialize_hom_mat2d(hom_mat_2d: Sequence[float]) -> HHandle`

## Description

`serialize_hom_mat2d` serializes the data of a homogeneous 2D
transformation matrix (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization).
The transformation matrix is defined by the handle *`hom_mat_2d`*.
The serialized transformation matrix is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_hom_mat2d`](deserialize_hom_mat2d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Transformation matrix.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

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
