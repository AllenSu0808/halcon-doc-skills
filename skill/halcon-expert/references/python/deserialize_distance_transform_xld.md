# deserialize_distance_transform_xld (Operator)

## Name

`deserialize_distance_transform_xld` — Deserialize an XLD distance transform.

## Signature

`def deserialize_distance_transform_xld(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_distance_transform_xld` deserializes an XLD distance
transform. The serialized XLD distance transform is defined
by the handle *`serialized_item_handle`*.
The deserialized XLD distance transform is returned in
*`distance_transform_id`*.

Note that the previous values of
*`distance_transform_id`* are overwritten, if the handle already exists.

[`get_distance_transform_xld_contour`](get_distance_transform_xld_contour.md)
can be used to get the reference contour that was used
to build the XLD distance transform *`distance_transform_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized XLD distance
transform.

**`distance_transform_id`** (output_control)  xld_dist_trans `→` HHandle

Handle of the deserialized XLD distance
transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`apply_distance_transform_xld`,
`get_distance_transform_xld_contour`,
`get_distance_transform_xld_param`

## See also

`serialize_distance_transform_xld`,
`write_distance_transform_xld`,
`read_distance_transform_xld`,
`create_distance_transform_xld`,
`set_distance_transform_xld_param`,
`clear_distance_transform_xld`

## Module

Foundation
