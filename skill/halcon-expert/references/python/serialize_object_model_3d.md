# serialize_object_model_3d (Operator)

## Name

`serialize_object_model_3d` — Serialize a 3D object model.

## Signature

`def serialize_object_model_3d(object_model_3d: HHandle) -> HHandle`

## Description

`serialize_object_model_3d` serializes the data of a 3D object
model (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file using the file format 'om3' of [`write_object_model_3d`](write_object_model_3d.md)
is converted to a serialized item. The 3D object model is defined by
the handle *`object_model_3d`*. The serialized 3D object model is
returned by the handle *`serialized_item_handle`* and can be
deserialized by [`deserialize_object_model_3d`](deserialize_object_model_3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d `→` HHandle

Handle of the 3D object model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_object_model_3d` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`read_object_model_3d`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_object_model_3d`

## See also

`read_object_model_3d`

## Module

3D Metrology
