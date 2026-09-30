# deserialize_region (Operator)

## Name

`deserialize_region` — Deserialize a serialized region.

## Signature

`def deserialize_region(serialized_item_handle: HHandle) -> HObject`

## Description

`deserialize_region` deserializes a region, that was serialized
by [`serialize_region`](serialize_region.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized region is defined by the parameter
*`serialized_item_handle`*.
The deserialized region is stored in the region defined by the
parameter *`region`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (output_object)  region(-array) `→` HObject

Region.

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`deserialize_region` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_image`,
`fread_serialized_item`,
`receive_serialized_item`,
`serialize_region`

## Possible Successors

`reduce_domain`,
`disp_region`

## See also

`serialize_region`

## Module

Foundation
