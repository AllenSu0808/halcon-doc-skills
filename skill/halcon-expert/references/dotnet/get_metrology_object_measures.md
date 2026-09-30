# GetMetrologyObjectMeasures (Operator)

## Name

`GetMetrologyObjectMeasures` — Get the measure regions and the results of the edge location for the
metrology objects of a metrology model.

## Signature

`static void HOperatorSet.GetMetrologyObjectMeasures(out HObject contours, HTuple metrologyHandle, HTuple index, HTuple transition, out HTuple row, out HTuple column)`

`HXLDCont HMetrologyModel.GetMetrologyObjectMeasures(HTuple index, string transition, out HTuple row, out HTuple column)`

`HXLDCont HMetrologyModel.GetMetrologyObjectMeasures(string index, string transition, out HTuple row, out HTuple column)`

## Description

`GetMetrologyObjectMeasures` allows to access the measure regions
of the metrology objects that were created with
[`AddMetrologyObjectGeneric`](add_metrology_object_generic.md),
[`AddMetrologyObjectCircleMeasure`](add_metrology_object_circle_measure.md), etc. as XLD contours and the
results of the edge location in image coordinates that was performed by
[`ApplyMetrologyModel`](apply_metrology_model.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrologyHandle`*. The
parameter *`index`* determines for which metrology objects the
information is accessed. With *`index`* set to *"all"*, the
measure regions and the results of the edge location for all metrology
objects are accessed.

If positive and negative edges are available in the measure regions
(see the generic parameter value *"measure_transition"* of
the operator [`SetMetrologyObjectParam`](set_metrology_object_param.md)), with the
parameter *`transition`* the desired edges (positive or
negative) can be selected. If *`transition`* is
set to *"positive"*, only positive edges are returned. If
*`transition`* is set to *"negative"*, only negative edges
are returned. All edges are returned if the parameter
*`transition`* is set to *"all"*.

The operator `GetMetrologyObjectMeasures` returns for each measure
region one rectangular XLD contour with the boundary of the measure
region in the parameter *`contours`*. After calling
[`ApplyMetrologyModel`](apply_metrology_model.md), additionally the image coordinates
of the results of the edge location are returned as single points in
the parameters *`row`* and *`column`*. Note that the order
for the values of these points is not defined. Furthermore, there is no
possibility to assign the results of the edge location to specific
measure regions. If `GetMetrologyObjectMeasures` is called before
[`ApplyMetrologyModel`](apply_metrology_model.md), the parameters *`row`* and
*`column`* remain empty.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Rectangular XLD Contours of measure regions.

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`transition`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Select light/dark or dark/light edges.

Default:
"all"

List of values:
"all", "negative", "positive"

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the measured edges.

**`column`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the measured edges.

## Result

If the parameters are valid, the operator
`GetMetrologyObjectMeasures` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ApplyMetrologyModel`

## See also

`AddMetrologyObjectGeneric`,
`AddMetrologyObjectEllipseMeasure`,
`AddMetrologyObjectLineMeasure`,
`AddMetrologyObjectRectangle2Measure`,
`AddMetrologyObjectCircleMeasure`

## Module

2D Metrology
