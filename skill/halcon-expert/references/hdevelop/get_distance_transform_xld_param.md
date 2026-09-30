# get_distance_transform_xld_param (Operator)

## Name

`get_distance_transform_xld_param` — Get the parameters used to build an XLD distance transform.

## Signature

`get_distance_transform_xld_param( : : DistanceTransformID, GenParamName : GenParamValue)`

## Description

`get_distance_transform_xld_param` returns the parameters used
to build the XLD distance transform *`DistanceTransformID`*.
The names of the parameters are passed in *`GenParamName`* and their
values are returned in *`GenParamValue`*. *`GenParamName`* can
contain the names of parameters *'mode'* and *'max_distance'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DistanceTransformID`** (input_control)  xld_dist_trans `→`  (handle)

Handle of the XLD distance transform.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of the generic parameters.

Default:
'mode'

List of values:
'max_distance', 'mode'

**`GenParamValue`** (output_control)  attribute.value(-array) `→`  (string / real)

Values of the generic parameters.

Number of elements:
GenParamValue == 1 || GenParamValue == 2

List of values:
5.0, 'point_to_point', 'point_to_segment'

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`read_distance_transform_xld`,
`deserialize_distance_transform_xld`

## Possible Successors

`set_distance_transform_xld_param`

## See also

`get_distance_transform_xld_contour`,
`create_distance_transform_xld`,
`apply_distance_transform_xld`,
`clear_distance_transform_xld`,
`write_distance_transform_xld`,
`serialize_distance_transform_xld`

## Module

Foundation
