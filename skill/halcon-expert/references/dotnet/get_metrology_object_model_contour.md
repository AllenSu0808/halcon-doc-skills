# GetMetrologyObjectModelContour (Operator)

## Name

`GetMetrologyObjectModelContour` — Query the model contour of a metrology object in image coordinates.

## Signature

`static void HOperatorSet.GetMetrologyObjectModelContour(out HObject contour, HTuple metrologyHandle, HTuple index, HTuple resolution)`

`HXLDCont HMetrologyModel.GetMetrologyObjectModelContour(HTuple index, double resolution)`

`HXLDCont HMetrologyModel.GetMetrologyObjectModelContour(int index, double resolution)`

## Description

`GetMetrologyObjectModelContour` returns the contours for the
chosen metrology objects in image coordinates.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrologyHandle`*. The
parameter *`index`* specifies for which metrology objects the contours
are queried. For *`index`* set to *"all"*, the contours of all
metrology objects are returned.

The form and pose of each contour is determined by the
parameters set when adding the object using e.g.,
[`AddMetrologyObjectGeneric`](add_metrology_object_generic.md),
[`AddMetrologyObjectCircleMeasure`](add_metrology_object_circle_measure.md), etc. If a different
reference coordinate system was set for the metrology model using
[`SetMetrologyModelParam`](set_metrology_model_param.md) or an alignment of the metrology model was
performed using [`AlignMetrologyModel`](align_metrology_model.md), these values influence the
current pose of the metrology objects and thus the pose of the contours
returned in *`contour`*.

The resolution of the returned *`contour`* is
controlled via *`resolution`* containing the Euclidean
distance (in pixel) between neighboring contour points. If the input value
falls below the minimal possible value (1.192e-7), the resolution is set
internally to the smallest valid value.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Model contour.

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Index of the metrology object.

Default:
0

Suggested values:
"all", 0, 1, 2

**`resolution`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Distance between neighboring contour points.

Default:
1.5

Restriction:
`Resolution >= 1.192e-7`

## Result

If the parameters are valid, the operator
`GetMetrologyObjectModelContour` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`AddMetrologyObjectGeneric`,
`AddMetrologyObjectCircleMeasure`,
`AddMetrologyObjectEllipseMeasure`,
`AddMetrologyObjectRectangle2Measure`,
`AddMetrologyObjectLineMeasure`

## Possible Successors

`ApplyMetrologyModel`

## See also

`SetMetrologyModelParam`,
`GetMetrologyObjectMeasures`,
`AlignMetrologyModel`

## Module

2D Metrology
