# deserialize_hom_mat2d (Operator)

## Name

`deserialize_hom_mat2d` — Deserialize a serialized homogeneous 2D transformation matrix.

## Signature

`def deserialize_hom_mat2d(serialized_item_handle: HHandle) -> Sequence[float]`

## Description

`deserialize_hom_mat2d` deserializes a homogeneous 2D transformation
matrix, that was serialized by [`serialize_hom_mat2d`](serialize_hom_mat2d.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized transformation matrix
is defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
transformation matrix with the handle *`hom_mat_2d`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`hom_mat_2d`** (output_control)  hom_mat2d `→` Sequence[float]

Transformation matrix.

## Result

If the parameters are valid, the operator
`deserialize_hom_mat2d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_hom_mat2d`

## Module

Foundation
