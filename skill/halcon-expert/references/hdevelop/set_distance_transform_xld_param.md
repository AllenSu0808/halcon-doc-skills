# set_distance_transform_xld_param (Operator)

## Name

`set_distance_transform_xld_param` — Set new parameters for an XLD distance transform.

## Signature

`set_distance_transform_xld_param( : : DistanceTransformID, GenParamName, GenParamValue : )`

## Description

`set_distance_transform_xld_param` sets new parameters for the
XLD distance transform *`DistanceTransformID`*.
The names and values of the parameters are passed in *`GenParamName`*
and *`GenParamValue`*, respectively. *`GenParamName`* can contain
the names of parameters *'mode'* and *'max_distance'*.
The XLD distance transform of the original reference contour is then
rebuilt with updated values of parameters.

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

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of the generic parameters.

Default:
'mode'

List of values:
'max_distance', 'mode'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / real)

Values of the generic parameters.

Default:
'point_to_point'

Suggested values:
'point_to_point', 'point_to_segment', 5.0

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`get_distance_transform_xld_param`

## Possible Successors

`apply_distance_transform_xld`

## See also

`write_distance_transform_xld`,
`serialize_distance_transform_xld`,
`get_distance_transform_xld_contour`,
`read_distance_transform_xld`,
`deserialize_distance_transform_xld`,
`clear_distance_transform_xld`

## Module

Foundation
