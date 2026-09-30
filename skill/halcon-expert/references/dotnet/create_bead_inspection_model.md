# CreateBeadInspectionModel (Operator)

## Name

`CreateBeadInspectionModel` — Create a model to inspect beads or adhesive in images.

## Signature

`static void HOperatorSet.CreateBeadInspectionModel(HObject beadContour, HTuple targetThickness, HTuple thicknessTolerance, HTuple positionTolerance, HTuple polarity, HTuple genParamName, HTuple genParamValue, out HTuple beadInspectionModel)`

`public HBeadInspectionModel(HXLD beadContour, HTuple targetThickness, HTuple thicknessTolerance, HTuple positionTolerance, string polarity, HTuple genParamName, HTuple genParamValue)`

`public HBeadInspectionModel(HXLD beadContour, int targetThickness, int thicknessTolerance, int positionTolerance, string polarity, string genParamName, int genParamValue)`

`void HBeadInspectionModel.CreateBeadInspectionModel(HXLD beadContour, HTuple targetThickness, HTuple thicknessTolerance, HTuple positionTolerance, string polarity, HTuple genParamName, HTuple genParamValue)`

`void HBeadInspectionModel.CreateBeadInspectionModel(HXLD beadContour, int targetThickness, int thicknessTolerance, int positionTolerance, string polarity, string genParamName, int genParamValue)`

## Description

`CreateBeadInspectionModel` creates a model to
inspect beads or adhesive in images.

**The basic principle of bead inspection**

The bead inspection operators enable the user to define a reference contour
that indicates the position and shape of a bead or adhesive on a certain
product. Images of such products can then be inspected to verify that a
bead or adhesive exists at the positions defined by the contour and that it
is of acceptable thickness. The images must already be aligned with the
given contour.

The operator `CreateBeadInspectionModel` returns a handle to the
bead inspection model in *`beadInspectionModel`*, which can later be
used to perform other operations related to bead inspection. These
operations include the modification of the bead inspection model parameters
and performing the inspection on input images as defined by the model.

**Providing the model contour**

In order to inspect beads, a contour serving as the model for the bead must
be provided in *`beadContour`*.
Such a contour can be generated, e.g., by using the
operators [`GenContourPolygonXld`](gen_contour_polygon_xld.md) or [`GenContourNurbsXld`](gen_contour_nurbs_xld.md).
The contour must be defined to be aligned to the beads in the input images.
To achieve this, the user can draw the XLD directly on a reference image
in the graphics window (with [`DrawPolygon`](draw_polygon.md) or
[`DrawNurbs`](draw_nurbs.md)).
To inspect beads consisting of multiple parts, multiple models must be
created.

**Mandatory parameters**

|  |
| --- |
| ![figure](../assets/60c971f02efb8dd8.svg) |
| ( 1) |
| ![figure](../assets/e460d538a421e1a2.svg) |
| ( 2) |

The mandatory parameters for a bead inspection model

In order to inspect beads, the following parameters must be set:

**Edge extraction parameters**

Bead inspection relies on edge extraction to identify the edges of beads.
Accordingly, correct initialization of the [`MeasurePos`](measure_pos.md)
parameters helps improve bead inspection results.

The following parameters can be set for *`genParamName`*.

- ***"sigma"*:** —

  Sets the standard deviation of the Gaussian smoothing kernel. The value
  of *"sigma"* depends on the quality of the images to be
  inspected, namely on the amount of noise.

  Default:
   *2.0*
- ***"threshold"*:** —

  Sets the minimum edge amplitude to be extracted. Setting a higher
  value for *"threshold"* helps to avoid the extraction of
  noise edges and select salient edges. *"threshold"* cannot be less
  than *1*.

  Default:
   *30*

The Measure Assistant can be used to find suitable values for these two
parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator modifies the state of the following input parameter:

- beadInspectionModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`beadContour`** (input_object)  xld `→` [HXLD](HXLD.md)

XLD contour specifying the expected bead's shape and
position.

**`targetThickness`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / double)

Optimal bead thickness.

Default:
50

Value range:
`5
≤
targetThickness`

**`thicknessTolerance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / double)

Tolerance of bead's thickness with respect to
*`targetThickness`*.

Default:
15

Value range:
`0
≤
thicknessTolerance`

**`positionTolerance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / double)

Tolerance of the bead's center position.

Default:
15

Value range:
`0
≤
positionTolerance`

**`polarity`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

The bead's polarity.

Default:
"light"

List of values:
"dark", "light"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that can be
adjusted for the bead inspection model.

Default:
[]

List of values:
"sigma", "threshold"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the generic parameters that can be
adjusted for the bead inspection model.

Default:
[]

Suggested values:
0.6, 1.0, 4.0, 5.0, 10.0, 50.0

**`beadInspectionModel`** (output_control, state is modified)  bead_inspection_model `→` [HBeadInspectionModel](HBeadInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle for using and accessing the bead inspection
model.

## Example (HDevelop)

```
* Read the image of the bead to be inspected.
read_image (Image, 'bead/adhesive_bead_01')
* Define the reference path of the adhesive beads.
gen_contour_nurbs_xld (ContourRef, \
                       [610.974,533.443,461.763,393.009,330.106,287.683, \
                        270.129,265.74,265.74,300.849,331.569,376.917, \
                        438.357,489.557,539.294], \
                       [418.581,424.27,439.441,473.574,526.67,574.078, \
                        644.241,708.715,765.604,818.7,866.107,915.411, \
                        966.611,998.848,993.159], \
                       'auto', \
                       [15,15,15,15,15,15,15,15,15,15,15,15,15,15,15], \
                       3, 1, 5)
*
* Create the bead inspection model, identifying the bead's parameters
create_bead_inspection_model (ContourRef, 14, 7, 30, 'dark', [], [], \
                               BeadInspectionModel)
*
* Apply the bead inspection model to the image
apply_bead_inspection_model (Image, LeftContour, RightContour, \
                              ErrorSegment, BeadInspectionModel, \
                              ErrorType)
```

## Result

The operator `CreateBeadInspectionModel` returns the value 2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`GenContourNurbsXld`,
`GenContourPolygonXld`

## Possible Successors

`ApplyBeadInspectionModel`,
`SetBeadInspectionParam`

## See also

`ClearBeadInspectionModel`

## Module

2D Metrology
