# serialize_metrology_model (Operator)

## Name

`serialize_metrology_model` — Serialize a metrology model.

## Signature

`def serialize_metrology_model(metrology_handle: HHandle) -> HHandle`

## Description

`serialize_metrology_model` serializes the data of a metrology
model (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization).

The same data that is written in a file by [`write_metrology_model`](write_metrology_model.md) is
converted to a serialized item. The metrology model is defined by the handle
*`metrology_handle`*. The serialized metrology model is returned by the
handle *`serialized_item_handle`* and can be deserialized by
[`deserialize_metrology_model`](deserialize_metrology_model.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrology_handle`** (input_control)  metrology_model `→` HHandle

Handle of the metrology model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_metrology_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_metrology_model`,
`add_metrology_object_circle_measure`,
`add_metrology_object_ellipse_measure`,
`add_metrology_object_line_measure`,
`add_metrology_object_rectangle2_measure`,
`set_metrology_object_param`,
`set_metrology_object_fuzzy_param`,
`read_metrology_model`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_metrology_model`

## Module

2D Metrology
