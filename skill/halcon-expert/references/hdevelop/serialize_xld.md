# serialize_xld (Operator)

## Name

`serialize_xld` — Serialize an XLD object.

## Signature

`serialize_xld(XLD : : : SerializedItemHandle)`

## Description

`serialize_xld` serializes an XLD object (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The XLD object is defined by the parameter
*`XLD`*. The serialized XLD object is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_xld`](deserialize_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` object

XLD object.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

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
