# set_bead_inspection_param (Operator)

## Name

`set_bead_inspection_param` — Set parameters of the bead inspection model.

## Signature

`def set_bead_inspection_param(bead_inspection_model: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> None`

## Description

The operator `set_bead_inspection_param` is used to set parameters
of a bead inspection model in order to adapt it to a particular inspection
task. All parameters except for the model's contour can be set with this
operator. A new bead
inspection model should be used when a new contour is introduced.
The current values of all parameters can be queried with the operator
[`get_bead_inspection_param`](get_bead_inspection_param.md).

**Parameters that can be set**

The following parameters are essential and inspection model specific. It
is vital for the inspection's success to identify accurate values for
those parameters:

- ***"target_thickness"*:** —

  sets the `target_thickness`.
- ***"thickness_tolerance"*:** —

  sets the
  `thickness_tolerance`.
- ***"position_tolerance"*:** —

  sets the
  `position_tolerance`.
- ***"polarity"*:** —

  sets the bead's `polarity`.
- ***"sigma"*** —
- ***"threshold"*** —

For more details, refer to the parameters' description in
[`create_bead_inspection_model`](create_bead_inspection_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- bead_inspection_model

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`bead_inspection_model`** (input_control, state is modified)  bead_inspection_model `→` HHandle

Handle of the bead inspection model.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the model parameter that shall be adjusted for
the specified bead inspection model.

Default:
"target_thickness"

List of values:
"polarity", "position_tolerance", "sigma", "target_thickness", "thickness_tolerance", "threshold"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Value of the model parameter that shall be adjusted
for the specified bead inspection model.

Default:
40

Suggested values:
40, 10, 15, 0.6, 1.0, 4.0, 5.0, "light", "dark"

## Result

The operator `set_bead_inspection_param` returns the value 2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`create_bead_inspection_model`

## Possible Successors

`apply_bead_inspection_model`,
`get_bead_inspection_param`

## Alternatives

`create_bead_inspection_model`

## See also

`create_bead_inspection_model`,
`clear_bead_inspection_model`

## Module

2D Metrology
