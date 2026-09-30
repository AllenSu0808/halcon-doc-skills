# get_distance_transform_xld_contour (Operator)

## Name

`get_distance_transform_xld_contour` — Get the reference contour used to build the XLD distance transform.

## Signature

`get_distance_transform_xld_contour( : Contour : DistanceTransformID : )`

## Description

`get_distance_transform_xld_contour` returns the reference contour
*`Contour`* that was used to build the XLD distance transform
*`DistanceTransformID`*.
This can be used for visualization purposes while comparing a given contour
against the reference contour using [`apply_distance_transform_xld`](apply_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (output_object)  xld_cont(-array) `→` object

Reference contour.

**`DistanceTransformID`** (input_control)  xld_dist_trans `→`  (handle)

Handle of the XLD distance transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`read_distance_transform_xld`,
`deserialize_distance_transform_xld`

## See also

`get_distance_transform_xld_param`,
`set_distance_transform_xld_param`,
`create_distance_transform_xld`,
`apply_distance_transform_xld`,
`clear_distance_transform_xld`,
`write_distance_transform_xld`,
`serialize_distance_transform_xld`

## Module

Foundation
