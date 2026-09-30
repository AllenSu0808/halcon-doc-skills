# apply_bead_inspection_model (Operator)

## Name

`apply_bead_inspection_model` — Inspect beads in an image, as defined by the bead inspection
model.

## Signature

`apply_bead_inspection_model(Image : LeftContour, RightContour, ErrorSegment : BeadInspectionModel : ErrorType)`

## Description

The operator `apply_bead_inspection_model` applies the bead
inspection model *`BeadInspectionModel`* to the
input *`Image`*. The output parameter *`ErrorSegment`*
indicates the positions of detected errors.
The parameter *`ErrorType`* indicates the type of
the detected errors for each segment. For more details on the possible
errors, refer to the parameters' description and figures in
[`create_bead_inspection_model`](create_bead_inspection_model.md).
The value of *`ErrorType`* can be:

- ***'no bead'*:** —

  No bead could be detected at this position.
- ***'incorrect position'*:** —

  The center of the bead found at
  this position is further away from the contour than allowed by
  `PositionTolerance`.
- ***'too thin'*:** —

  The bead is thinner than allowed by
  `TargetThickness` and `ThicknessTolerance`.
- ***'too thick'*:** —

  The bead is thicker than allowed by
  `TargetThickness` and `ThicknessTolerance`.

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

- BeadInspectionModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Image to apply bead inspection on.

**`LeftContour`** (output_object)  xld-array `→` object

The detected left contour of the beads.

**`RightContour`** (output_object)  xld-array `→` object

The detected right contour of the beads.

**`ErrorSegment`** (output_object)  xld-array `→` object

Detected error segments

**`BeadInspectionModel`** (input_control, state is modified)  bead_inspection_model `→`  (handle)

Handle of the bead inspection model to be used.

**`ErrorType`** (output_control)  string-array `→`  (string)

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
