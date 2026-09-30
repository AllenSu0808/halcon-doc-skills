# serialize_xld (Operator)

## Name

`serialize_xld` — Serialize an XLD object.

## Signature

`def serialize_xld(xld: HObject) -> HHandle`

## Description

`serialize_xld` serializes an XLD object (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The XLD object is defined by the parameter
*`xld`*. The serialized XLD object is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_xld`](deserialize_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

XLD object.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_xld` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`gen_contour_polygon_xld`,
`gen_parallels_xld`,
`gen_polygons_xld`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_xld`

## See also

`deserialize_xld`

## Module

Foundation
