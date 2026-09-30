# set_distance_transform_xld_param (Operator)

## Name

`set_distance_transform_xld_param` — Set new parameters for an XLD distance transform.

## Signature

`def set_distance_transform_xld_param(distance_transform_id: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[float, str]]) -> None`

## Description

`set_distance_transform_xld_param` sets new parameters for the
XLD distance transform *`distance_transform_id`*.
The names and values of the parameters are passed in *`gen_param_name`*
and *`gen_param_value`*, respectively. *`gen_param_name`* can contain
the names of parameters *"mode"* and *"max_distance"*.
The XLD distance transform of the original reference contour is then
rebuilt with updated values of parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- distance_transform_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`distance_transform_id`** (input_control, state is modified)  xld_dist_trans `→` HHandle

Handle of the XLD distance transform.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of the generic parameters.

Default:
"mode"

List of values:
"max_distance", "mode"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[float, str]]

Values of the generic parameters.

Default:
"point_to_point"

Suggested values:
"point_to_point", "point_to_segment", 5.0

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
