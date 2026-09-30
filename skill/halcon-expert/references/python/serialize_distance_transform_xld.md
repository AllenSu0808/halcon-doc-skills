# serialize_distance_transform_xld (Operator)

## Name

`serialize_distance_transform_xld` — Serialize an XLD distance transform.

## Signature

`def serialize_distance_transform_xld(distance_transform_id: HHandle) -> HHandle`

## Description

`serialize_distance_transform_xld` serializes the XLD distance
transform *`distance_transform_id`*. The serialized XLD distance
transform is returned in the handle *`serialized_item_handle`* and
can be deserialized with [`deserialize_distance_transform_xld`](deserialize_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`distance_transform_id`** (input_control)  xld_dist_trans `→` HHandle

Handle of the XLD distance transform.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized XLD distance
transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`create_distance_transform_xld`

## Possible Successors

`clear_distance_transform_xld`

## Alternatives

`write_distance_transform_xld`

## See also

`deserialize_distance_transform_xld`,
`read_distance_transform_xld`,
`apply_distance_transform_xld`,
`get_distance_transform_xld_contour`,
`get_distance_transform_xld_param`,
`set_distance_transform_xld_param`

## Module

Foundation
