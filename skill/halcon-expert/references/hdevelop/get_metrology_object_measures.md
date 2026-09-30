# get_metrology_object_measures (Operator)

## Name

`get_metrology_object_measures` — Get the measure regions and the results of the edge location for the
metrology objects of a metrology model.

## Signature

`get_metrology_object_measures( : Contours : MetrologyHandle, Index, Transition : Row, Column)`

## Description

`get_metrology_object_measures` allows to access the measure regions
of the metrology objects that were created with
[`add_metrology_object_generic`](add_metrology_object_generic.md),
[`add_metrology_object_circle_measure`](add_metrology_object_circle_measure.md), etc. as XLD contours and the
results of the edge location in image coordinates that was performed by
[`apply_metrology_model`](apply_metrology_model.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`MetrologyHandle`*. The
parameter *`Index`* determines for which metrology objects the
information is accessed. With *`Index`* set to *'all'*, the
measure regions and the results of the edge location for all metrology
objects are accessed.

If positive and negative edges are available in the measure regions
(see the generic parameter value *'measure_transition'* of
the operator [`set_metrology_object_param`](set_metrology_object_param.md)), with the
parameter *`Transition`* the desired edges (positive or
negative) can be selected. If *`Transition`* is
set to *'positive'*, only positive edges are returned. If
*`Transition`* is set to *'negative'*, only negative edges
are returned. All edges are returned if the parameter
*`Transition`* is set to *'all'*.

The operator `get_metrology_object_measures` returns for each measure
region one rectangular XLD contour with the boundary of the measure
region in the parameter *`Contours`*. After calling
[`apply_metrology_model`](apply_metrology_model.md), additionally the image coordinates
of the results of the edge location are returned as single points in
the parameters *`Row`* and *`Column`*. Note that the order
for the values of these points is not defined. Furthermore, there is no
possibility to assign the results of the edge location to specific
measure regions. If `get_metrology_object_measures` is called before
[`apply_metrology_model`](apply_metrology_model.md), the parameters *`Row`* and
*`Column`* remain empty.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (output_object)  xld_cont-array `→` object

Rectangular XLD Contours of measure regions.

**`MetrologyHandle`** (input_control)  metrology_model `→`  (handle)

Handle of the metrology model.

**`Index`** (input_control)  integer(-array) `→`  (string / integer)

Index of the metrology objects.

Default:
'all'

Suggested values:
'all', 0, 1, 2

**`Transition`** (input_control)  string `→`  (string)

Select light/dark or dark/light edges.

Default:
'all'

List of values:
'all', 'negative', 'positive'

**`Row`** (output_control)  point.y-array `→`  (real)

Row coordinates of the measured edges.

**`Column`** (output_control)  point.x-array `→`  (real)

Column coordinates of the measured edges.

## Result

If the parameters are valid, the operator
`get_metrology_object_measures` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`apply_metrology_model`

## See also

`add_metrology_object_generic`,
`add_metrology_object_ellipse_measure`,
`add_metrology_object_line_measure`,
`add_metrology_object_rectangle2_measure`,
`add_metrology_object_circle_measure`

## Module

2D Metrology
