# apply_bead_inspection_model (Operator)

## Name

`apply_bead_inspection_model` — Inspect beads in an image, as defined by the bead inspection
model.

## Signature

`def apply_bead_inspection_model(image: HObject, bead_inspection_model: HHandle) -> Tuple[HObject, HObject, HObject, Sequence[str]]`

## Description

The operator `apply_bead_inspection_model` applies the bead
inspection model *`bead_inspection_model`* to the
input *`image`*. The output parameter *`error_segment`*
indicates the positions of detected errors.
The parameter *`error_type`* indicates the type of
the detected errors for each segment. For more details on the possible
errors, refer to the parameters' description and figures in
[`create_bead_inspection_model`](create_bead_inspection_model.md).
The value of *`error_type`* can be:

- ***"no bead"*:** —

  No bead could be detected at this position.
- ***"incorrect position"*:** —

  The center of the bead found at
  this position is further away from the contour than allowed by
  `position_tolerance`.
- ***"too thin"*:** —

  The bead is thinner than allowed by
  `target_thickness` and `thickness_tolerance`.
- ***"too thick"*:** —

  The bead is thicker than allowed by
  `target_thickness` and `thickness_tolerance`.

Values of the generic parameters set through
[`create_bead_inspection_model`](create_bead_inspection_model.md) or [`set_bead_inspection_param`](set_bead_inspection_param.md)
highly affect the inspection results of the same model. For more details on
those parameters, please refer to [`create_bead_inspection_model`](create_bead_inspection_model.md).

Note that the operator ignores the image domain and applies the model
to the full image

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- bead_inspection_model

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Image to apply bead inspection on.

**`left_contour`** (output_object)  xld-array `→` HObject

The detected left contour of the beads.

**`right_contour`** (output_object)  xld-array `→` HObject

The detected right contour of the beads.

**`error_segment`** (output_object)  xld-array `→` HObject

Detected error segments

**`bead_inspection_model`** (input_control, state is modified)  bead_inspection_model `→` HHandle

Handle of the bead inspection model to be used.

**`error_type`** (output_control)  string-array `→` Sequence[str]

Types of detected errors.

## Result

The operator `apply_bead_inspection_model` returns the value 2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`create_bead_inspection_model`,
`set_bead_inspection_param`

## Possible Successors

`set_bead_inspection_param`,
`clear_bead_inspection_model`

## See also

`get_bead_inspection_param`,
`create_bead_inspection_model`,
`set_bead_inspection_param`

## Module

2D Metrology
