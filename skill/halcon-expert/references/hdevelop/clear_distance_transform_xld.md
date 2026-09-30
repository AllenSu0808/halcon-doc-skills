# clear_distance_transform_xld (Operator)

## Name

`clear_distance_transform_xld` — Clear a XLD distance transform.

## Signature

`clear_distance_transform_xld( : : DistanceTransformID : )`

## Description

`clear_distance_transform_xld` clears the XLD distance transform
*`DistanceTransformID`* that was previously created by
[`create_distance_transform_xld`](create_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- DistanceTransformID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`DistanceTransformID`** (input_control, state is modified)  xld_dist_trans `→`  (handle)

Handle of the XLD distance transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`create_distance_transform_xld`,
`write_distance_transform_xld`,
`serialize_distance_transform_xld`

## See also

`apply_distance_transform_xld`,
`get_distance_transform_xld_contour`,
`get_distance_transform_xld_param`,
`set_distance_transform_xld_param`,
`read_distance_transform_xld`,
`deserialize_distance_transform_xld`

## Module

Foundation
