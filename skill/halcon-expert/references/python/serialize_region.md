# serialize_region (Operator)

## Name

`serialize_region` — Serialize a region.

## Signature

`def serialize_region(region: HObject) -> HHandle`

## Description

`serialize_region` serializes a region (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The region is defined by the parameter
*`region`*. The serialized region is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_region`](deserialize_region.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Region.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_region` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_image`,
`read_region`,
`threshold`,
`regiongrowing`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_region`

## See also

`deserialize_region`

## Module

Foundation
