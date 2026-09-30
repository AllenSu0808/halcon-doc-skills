# serialize_distance_transform_xld (Operator)

## Name

`serialize_distance_transform_xld` — Serialize an XLD distance transform.

## Signature

`serialize_distance_transform_xld( : : DistanceTransformID : SerializedItemHandle)`

## Description

`serialize_distance_transform_xld` serializes the XLD distance
transform *`DistanceTransformID`*. The serialized XLD distance
transform is returned in the handle *`SerializedItemHandle`* and
can be deserialized with [`deserialize_distance_transform_xld`](deserialize_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DistanceTransformID`** (input_control)  xld_dist_trans `→`  (handle)

Handle of the XLD distance transform.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

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
