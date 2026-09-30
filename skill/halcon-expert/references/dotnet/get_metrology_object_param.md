# GetMetrologyObjectParam (Operator)

## Name

`GetMetrologyObjectParam` — Get one or several parameters of a metrology model.

## Signature

`static void HOperatorSet.GetMetrologyObjectParam(HTuple metrologyHandle, HTuple index, HTuple genParamName, out HTuple genParamValue)`

`HTuple HMetrologyModel.GetMetrologyObjectParam(HTuple index, HTuple genParamName)`

`HTuple HMetrologyModel.GetMetrologyObjectParam(string index, HTuple genParamName)`

## Description

`GetMetrologyObjectParam` allows to access the parameters
that are used by a metrology object.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle
*`metrologyHandle`*. The parameter *`index`*
determines for which metrology objects the information is accessed.
With *`index`* set to *"all"*, the parameters of all
metrology objects are accessed. The names of the desired parameters
are passed in the generic parameter *`genParamName`*, the
corresponding values are returned in *`genParamValue`* in the
same order. All these general parameters can be set and changed at
any time with the operator [`SetMetrologyObjectParam`](set_metrology_object_param.md).
Parameters that describe the geometry of an object can only be set by
creating the metrology object with the operators
[`AddMetrologyObjectCircleMeasure`](add_metrology_object_circle_measure.md),
[`AddMetrologyObjectEllipseMeasure`](add_metrology_object_ellipse_measure.md),
[`AddMetrologyObjectLineMeasure`](add_metrology_object_line_measure.md), or
[`AddMetrologyObjectRectangle2Measure`](add_metrology_object_rectangle2_measure.md).

The following parameters can be accessed:

- Valid for all types of metrology objects:

  - ***"min_score"*, *"num_instances"*,
    *"instances_outside_measure_regions"*:** —

    The meaning and the use of these parameters is described with the
    operator [`SetMetrologyObjectParam`](set_metrology_object_param.md).
  - ***"rand_seed"*, *"distance_threshold"*,
    *"max_num_iterations"*:** —

    The meaning and the use of these parameters is described with the
    operator [`SetMetrologyObjectParam`](set_metrology_object_param.md).
  - ***"measure_length1"*, *"measure_length2"*:** —

    The meaning and the use of these parameters is described with the
    operator [`SetMetrologyObjectParam`](set_metrology_object_param.md).
  - ***"measure_sigma"*, *"measure_threshold"*,
    *"measure_transition"*, *"measure_select"*:** —

    The meaning and the use of these parameters is described with
    the operator [`MeasurePos`](measure_pos.md) by the parameters `sigma`,
    `threshold`, `transition`, and `select`.
  - ***"measure_interpolation"*:** —

    The meaning and the use of this parameter is described with the
    operator [`GenMeasureRectangle2`](gen_measure_rectangle2.md) by the parameter
    `interpolation`.
  - ***"measure_distance_min"*:** —

    Returns the minimum distance between the centers of the generated
    measure regions, which depends on the geometry of the object and
    the value of the input parameter *"measure_distance"* or
    the value of the input parameter *"num_measures"* of the
    operator [`SetMetrologyObjectParam`](set_metrology_object_param.md). For
    a metrology object circle or a metrology object line the
    distances between measure regions are uniformly distributed.
    Therefore, *"measure_distance_min"* and
    *"measure_distance_max"* return the same value.
  - ***"measure_distance_max"*:** —

    Returns the maximum distance between the centers of the generated
    measure regions, which depends on the geometry of the object and
    the value of the input parameter *"measure_distance"* or
    the value of the input parameter *"num_measures"* of the
    operator [`SetMetrologyObjectParam`](set_metrology_object_param.md). For
    a metrology object circle or a metrology object line the distances
    between measure regions are uniformly distributed. Therefore,
    *"measure_distance_min"* and *"measure_distance_max"*
    return the same value.
  - ***"num_measures"*:** —

    Returns the number of generated measure regions, which depends
    on the geometry of the object and the value of the input parameter
    *"measure_distance"* or the value of the input parameter
    *"num_measures"* of the operator
    [`SetMetrologyObjectParam`](set_metrology_object_param.md).
  - ***"object_type"*:** —

    Type of the geometric shape of
    the metrology object.
    For a metrology object of type circle, the output parameter
    *`genParamValue`* contains the value *"circle"*.
    For a metrology object of type ellipse, the output parameter
    *`genParamValue`* contains the value *"ellipse"*.
    For a metrology object of type line, the output parameter
    *`genParamValue`* contains the value *"line"*.
    For a metrology object of type rectangle, the output parameter
    *`genParamValue`* contains the value *"rectangle"*.
  - ***"object_params"*:** —

    The parameters of the geometric
    shape of the metrology object.
    For a metrology object of type circle, the output parameter
    *`genParamValue`* contains the geometry of the circle in
    the following order: *"row"*, *"column"*,
    *"radius"*. The meaning and the use of these
    parameters is described with the operator
    [`AddMetrologyObjectCircleMeasure`](add_metrology_object_circle_measure.md).
    For a metrology object of type ellipse, the output parameter
    *`genParamValue`* contains the geometry of the ellipse in
    the following order: *"row"*, *"column"*,
    *"phi"*, *"radius1"*, *"radius2"*. The
    meaning and the use of these parameters is described with the
    operator [`AddMetrologyObjectEllipseMeasure`](add_metrology_object_ellipse_measure.md).
    For a metrology object of type line, the output parameter
    *`genParamValue`* contains the geometry of the line in the
    following order: *"row_begin"*, *"column_begin"*,
    *"row_end"*, *"column_end"*. The meaning and the
    use of these parameters is described with the operator
    [`AddMetrologyObjectLineMeasure`](add_metrology_object_line_measure.md).
    For a metrology object of type rectangle, the output parameter
    *`genParamValue`* contains the geometry of the rectangle in
    the following order: *"row"*, *"column"*,
    *"phi"*, *"length1"*, *"length2"*. The
    meaning and the use of these parameters is described with the
    operator [`AddMetrologyObjectRectangle2Measure`](add_metrology_object_rectangle2_measure.md).
- Only valid for a metrology object of type circle:

  - ***"row"*, *"column"*, *"radius"*:** —

    These are parameters for a metrology object of type circle.
    The meaning and the use of these parameters is described with the
    operator [`AddMetrologyObjectCircleMeasure`](add_metrology_object_circle_measure.md).
- Only valid for a metrology object of type ellipse:

  - ***"row"*, *"column"*, *"phi"*,
    *"radius1"*, *"radius2"*:** —

    These are parameters
    for a metrology object of type ellipse. The meaning and the use
    of these parameters is described with the operator
    [`AddMetrologyObjectEllipseMeasure`](add_metrology_object_ellipse_measure.md).
- Only valid for a metrology object of type line:

  - ***"row_begin"*, *"column_begin"*,
    *"row_end"*, *"column_end"*:** —

    These are parameters
    for a metrology object of type line. The meaning and the use
    of these parameters is described with the operator
    [`AddMetrologyObjectLineMeasure`](add_metrology_object_line_measure.md).
- Only valid for a metrology object of type rectangle:

  - ***"row"*, *"column"*, *"phi"*,
    *"length1"*, *"length2"*:** —

    These are
    parameters for a metrology object of type rectangle. The meaning
    and the use of these parameters is described with the
    operator [`AddMetrologyObjectRectangle2Measure`](add_metrology_object_rectangle2_measure.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
"num_measures"

List of values:
"column", "column_begin", "column_end", "distance_threshold", "end_phi", "instances_outside_measure_regions", "length1", "length2", "max_num_iterations", "measure_distance_min", "measure_distance_min", "measure_interpolation", "measure_length1", "measure_length2", "measure_select", "measure_sigma", "measure_threshold", "measure_transition", "min_score", "num_instances", "num_measures", "object_params", "object_type", "phi", "point_order", "radius", "radius1", "radius2", "rand_seed", "row", "row_begin", "row_end", "start_phi", "x", "x_begin", "x_end", "y", "y_begin", "y_end"

**`genParamValue`** (output_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values of the generic parameters.

## Result

If the parameters are valid, the operator
`GetMetrologyObjectParam` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`GetMetrologyObjectIndices`,
`SetMetrologyObjectParam`

## Possible Successors

`SetMetrologyObjectParam`

## See also

`GetMetrologyObjectFuzzyParam`,
`GetMetrologyObjectNumInstances`

## Module

2D Metrology
