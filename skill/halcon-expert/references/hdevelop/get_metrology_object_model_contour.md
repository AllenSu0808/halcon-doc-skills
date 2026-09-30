# get_metrology_object_model_contour (Operator)

## Name

`get_metrology_object_model_contour` — Query the model contour of a metrology object in image coordinates.

## Signature

`get_metrology_object_model_contour( : Contour : MetrologyHandle, Index, Resolution : )`

## Description

`get_metrology_object_model_contour` returns the contours for the
chosen metrology objects in image coordinates.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`MetrologyHandle`*. The
parameter *`Index`* specifies for which metrology objects the contours
are queried. For *`Index`* set to *'all'*, the contours of all
metrology objects are returned.

The form and pose of each contour is determined by the
parameters set when adding the object using e.g.,
[`add_metrology_object_generic`](add_metrology_object_generic.md),
[`add_metrology_object_circle_measure`](add_metrology_object_circle_measure.md), etc. If a different
reference coordinate system was set for the metrology model using
[`set_metrology_model_param`](set_metrology_model_param.md) or an alignment of the metrology model was
performed using [`align_metrology_model`](align_metrology_model.md), these values influence the
current pose of the metrology objects and thus the pose of the contours
returned in *`Contour`*.

The resolution of the returned *`Contour`* is
controlled via *`Resolution`* containing the Euclidean
distance (in pixel) between neighboring contour points. If the input value
falls below the minimal possible value (1.192e-7), the resolution is set
internally to the smallest valid value.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (output_object)  xld_cont(-array) `→` object

Model contour.

**`MetrologyHandle`** (input_control)  metrology_model `→`  (handle)

Handle of the metrology model.

**`Index`** (input_control)  integer(-array) `→`  (integer / string)

Index of the metrology object.

Default:
0

Suggested values:
'all', 0, 1, 2

**`Resolution`** (input_control)  real `→`  (real)

Distance between neighboring contour points.

Default:
1.5

Restriction:
`Resolution >= 1.192e-7`

## Result

If the parameters are valid, the operator
`get_metrology_object_model_contour` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`add_metrology_object_generic`,
`add_metrology_object_circle_measure`,
`add_metrology_object_ellipse_measure`,
`add_metrology_object_rectangle2_measure`,
`add_metrology_object_line_measure`

## Possible Successors

`apply_metrology_model`

## See also

`set_metrology_model_param`,
`get_metrology_object_measures`,
`align_metrology_model`

## Module

2D Metrology
