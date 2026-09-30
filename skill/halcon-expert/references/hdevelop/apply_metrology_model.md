# apply_metrology_model (Operator)

## Name

`apply_metrology_model` — Measure and fit the geometric shapes of all metrology objects of
a metrology model.

## Signature

`apply_metrology_model(Image : : MetrologyHandle : )`

## Description

`apply_metrology_model` locates the edges inside the
measure regions of the metrology objects of the metrology model
*`MetrologyHandle`* within *`Image`* and fits the
corresponding geometric shapes to the resulting edge positions.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The measurements are performed as follows:

**Determining the edge positions**

Within the measure regions of the metrology objects,
the positions of the edges are determined. The edge location is
calculated internally with the operator [`measure_pos`](measure_pos.md) or
[`fuzzy_measure_pos`](fuzzy_measure_pos.md). The latter is used if at least one
fuzzy function was set for the metrology objects with
[`set_metrology_object_fuzzy_param`](set_metrology_object_fuzzy_param.md).

**Fitting geometric shapes to the edge positions**

The geometric shapes of the metrology objects are
adapted to fit optimally to the resulting edge positions. In
particular, a RANSAC algorithm is used to select a set of initial
edge positions that is necessary to create an instance of the specific
geometric shape, e.g., three edge positions are selected for a
metrology object of type circle. Then, those edge positions that are
near the corresponding instance of the geometric shape are determined
and, if
the number of suitable edge positions is sufficient (see the generic
parameter *'min_score'* of [`set_metrology_object_param`](set_metrology_object_param.md)),
are selected for the final fitting of the geometric shape. If the
number of suitable edge positions is not sufficient, another set of
initial edge positions is tested until a suitable selection of edge
positions is found. Into the edge positions that are selected for the
final fitting, the geometric shape is fitted and its parameters are
stored in the metrology model. Note that more than one instance for
each metrology object is returned if the generic parameter
*'num_instances'* is set to value larger than 1. This
and other parameters can be set when adding the metrology objects to the
metrology model or separately with the operator
[`set_metrology_object_param`](set_metrology_object_param.md). Note that for each instance of
the metrology object different initial edge positions are used, i.e., a
second instance is based on edge positions that were not already used
for the fitting of the first instance.
The algorithm stops either when *'num_instances'*
instances were found or if the remaining number of suitable initial edge
positions is too low for a further fitting of the geometric shape.

**Accessing the results**

The results of the measurements can be accessed from the metrology
model using [`get_metrology_object_result`](get_metrology_object_result.md). Note that if more than one
instance of an object is returned, the order of the returned instances
is arbitrary and therefore no measure for the quality of the
fitting. Note further that if the parameters *'camera_param'*
and *'plane_pose'* were set for the metrology model using
[`set_metrology_model_param`](set_metrology_model_param.md), world
coordinates are used for the fitting. Otherwise, image coordinates
are used. The XLD contours for the measured objects can be
obtained using [`get_metrology_object_result_contour`](get_metrology_object_result_contour.md).

## Attention

Note that all measure regions of all metrology objects
must be recomputed if the width or the height of the input
*`Image`* is not equal to the width and height stored in the
metrology object (e.g., set with [`set_metrology_model_image_size`](set_metrology_model_image_size.md)).
This leads to longer execution times of the operator.

Note further that `apply_metrology_model` ignores the domain
of *`Image`* for efficiency reasons (see also
[`measure_pos`](measure_pos.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MetrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2 / real)

Input image.

**`MetrologyHandle`** (input_control, state is modified)  metrology_model `→`  (handle)

Handle of the metrology model.

## Result

If the parameters are valid, the operator
`apply_metrology_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`add_metrology_object_generic`,
`add_metrology_object_circle_measure`,
`add_metrology_object_ellipse_measure`,
`add_metrology_object_line_measure`,
`add_metrology_object_rectangle2_measure`,
`align_metrology_model`,
`set_metrology_model_param`,
`set_metrology_object_param`

## Possible Successors

`get_metrology_object_result`,
`get_metrology_object_result_contour`,
`get_metrology_object_measures`

## See also

`set_metrology_object_fuzzy_param`,
`read_metrology_model`,
`write_metrology_model`

## Module

2D Metrology
