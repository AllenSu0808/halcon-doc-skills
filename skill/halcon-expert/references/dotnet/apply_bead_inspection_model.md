# ApplyBeadInspectionModel (Operator)

## Name

`ApplyBeadInspectionModel` — Inspect beads in an image, as defined by the bead inspection
model.

## Signature

`static void HOperatorSet.ApplyBeadInspectionModel(HObject image, out HObject leftContour, out HObject rightContour, out HObject errorSegment, HTuple beadInspectionModel, out HTuple errorType)`

`HXLD HBeadInspectionModel.ApplyBeadInspectionModel(HImage image, out HXLD rightContour, out HXLD errorSegment, out HTuple errorType)`

## Description

The operator `ApplyBeadInspectionModel` applies the bead
inspection model *`beadInspectionModel`* to the
input *`image`*. The output parameter *`errorSegment`*
indicates the positions of detected errors.
The parameter *`errorType`* indicates the type of
the detected errors for each segment. For more details on the possible
errors, refer to the parameters' description and figures in
[`CreateBeadInspectionModel`](create_bead_inspection_model.md).
The value of *`errorType`* can be:

- ***"no bead"*:** —

  No bead could be detected at this position.
- ***"incorrect position"*:** —

  The center of the bead found at
  this position is further away from the contour than allowed by
  `positionTolerance`.
- ***"too thin"*:** —

  The bead is thinner than allowed by
  `targetThickness` and `thicknessTolerance`.
- ***"too thick"*:** —

  The bead is thicker than allowed by
  `targetThickness` and `thicknessTolerance`.

Values of the generic parameters set through
[`CreateBeadInspectionModel`](create_bead_inspection_model.md) or [`SetBeadInspectionParam`](set_bead_inspection_param.md)
highly affect the inspection results of the same model. For more details on
those parameters, please refer to [`CreateBeadInspectionModel`](create_bead_inspection_model.md).

Note that the operator ignores the image domain and applies the model
to the full image

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- beadInspectionModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Image to apply bead inspection on.

**`leftContour`** (output_object)  xld-array `→` [HXLD](HXLD.md)

The detected left contour of the beads.

**`rightContour`** (output_object)  xld-array `→` [HXLD](HXLD.md)

The detected right contour of the beads.

**`errorSegment`** (output_object)  xld-array `→` [HXLD](HXLD.md)

Detected error segments

**`beadInspectionModel`** (input_control, state is modified)  bead_inspection_model `→` [HBeadInspectionModel](HBeadInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bead inspection model to be used.

**`errorType`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Types of detected errors.

## Result

The operator `ApplyBeadInspectionModel` returns the value 2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateBeadInspectionModel`,
`SetBeadInspectionParam`

## Possible Successors

`SetBeadInspectionParam`,
`ClearBeadInspectionModel`

## See also

`GetBeadInspectionParam`,
`CreateBeadInspectionModel`,
`SetBeadInspectionParam`

## Module

2D Metrology
