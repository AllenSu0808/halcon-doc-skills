# get_metrology_object_param (Operator)

## Name

`get_metrology_object_param` — Get one or several parameters of a metrology model.

## Signature

`get_metrology_object_param( : : MetrologyHandle, Index, GenParamName : GenParamValue)`

## Description

`get_metrology_object_param` allows to access the parameters
that are used by a metrology object.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle
*`MetrologyHandle`*. The parameter *`Index`*
determines for which metrology objects the information is accessed.
With *`Index`* set to *'all'*, the parameters of all
metrology objects are accessed. The names of the desired parameters
are passed in the generic parameter *`GenParamName`*, the
corresponding values are returned in *`GenParamValue`* in the
same order. All these general parameters can be set and changed at
any time with the operator [`set_metrology_object_param`](set_metrology_object_param.md).
Parameters that describe the geometry of an object can only be set by
creating the metrology object with the operators
[`add_metrology_object_circle_measure`](add_metrology_object_circle_measure.md),
[`add_metrology_object_ellipse_measure`](add_metrology_object_ellipse_measure.md),
[`add_metrology_object_line_measure`](add_metrology_object_line_measure.md), or
[`add_metrology_object_rectangle2_measure`](add_metrology_object_rectangle2_measure.md).

The following parameters can be accessed:

- Valid for all types of metrology objects:

  - ***'min_score'*, *'num_instances'*,
    *'instances_outside_measure_regions'*:** —

    The meaning and the use of these parameters is described with the
    operator [`set_metrology_object_param`](set_metrology_object_param.md).
  - ***'rand_seed'*, *'distance_threshold'*,
    *'max_num_iterations'*:** —

    The meaning and the use of these parameters is described with the
    operator [`set_metrology_object_param`](set_metrology_object_param.md).
  - ***'measure_length1'*, *'measure_length2'*:** —

    The meaning and the use of these parameters is described with the
    operator [`set_metrology_object_param`](set_metrology_object_param.md).
  - ***'measure_sigma'*, *'measure_threshold'*,
    *'measure_transition'*, *'measure_select'*:** —

    The meaning and the use of these parameters is described with
    the operator [`measure_pos`](measure_pos.md) by the parameters `Sigma`,
    `Threshold`, `Transition`, and `Select`.
  - ***'measure_interpolation'*:** —

    The meaning and the use of this parameter is described with the
    operator [`gen_measure_rectangle2`](gen_measure_rectangle2.md) by the parameter
    `Interpolation`.
  - ***'measure_distance_min'*:** —

    Returns the minimum distance between the centers of the generated
    measure regions, which depends on the geometry of the object and
    the value of the input parameter *'measure_distance'* or
    the value of the input parameter *'num_measures'* of the
    operator [`set_metrology_object_param`](set_metrology_object_param.md). For
    a metrology object circle or a metrology object line the
    distances between measure regions are uniformly distributed.
    Therefore, *'measure_distance_min'* and
    *'measure_distance_max'* return the same value.
  - ***'measure_distance_max'*:** —

    Returns the maximum distance between the centers of the generated
    measure regions, which depends on the geometry of the object and
    the value of the input parameter *'measure_distance'* or
    the value of the input parameter *'num_measures'* of the
    operator [`set_metrology_object_param`](set_metrology_object_param.md). For
    a metrology object circle or a metrology object line the distances
    between measure regions are uniformly distributed. Therefore,
    *'measure_distance_min'* and *'measure_distance_max'*
    return the same value.
  - ***'num_measures'*:** —

    Returns the number of generated measure regions, which depends
    on the geometry of the object and the value of the input parameter
    *'measure_distance'* or the value of the input parameter
    *'num_measures'* of the operator
    [`set_metrology_object_param`](set_metrology_object_param.md).
  - ***'object_type'*:** —

    Type of the geometric shape of
    the metrology object.
    For a metrology object of type circle, the output parameter
    *`GenParamValue`* contains the value *'circle'*.
    For a metrology object of type ellipse, the output parameter
    *`GenParamValue`* contains the value *'ellipse'*.
    For a metrology object of type line, the output parameter
    *`GenParamValue`* contains the value *'line'*.
    For a metrology object of type rectangle, the output parameter
    *`GenParamValue`* contains the value *'rectangle'*.
  - ***'object_params'*:** —

    The parameters of the geometric
    shape of the metrology object.
    For a metrology object of type circle, the output parameter
    *`GenParamValue`* contains the geometry of the circle in
    the following order: *'row'*, *'column'*,
    *'radius'*. The meaning and the use of these
    parameters is described with the operator
    [`add_metrology_object_circle_measure`](add_metrology_object_circle_measure.md).
    For a metrology object of type ellipse, the output parameter
    *`GenParamValue`* contains the geometry of the ellipse in
    the following order: *'row'*, *'column'*,
    *'phi'*, *'radius1'*, *'radius2'*. The
    meaning and the use of these parameters is described with the
    operator [`add_metrology_object_ellipse_measure`](add_metrology_object_ellipse_measure.md).
    For a metrology object of type line, the output parameter
    *`GenParamValue`* contains the geometry of the line in the
    following order: *'row_begin'*, *'column_begin'*,
    *'row_end'*, *'column_end'*. The meaning and the
    use of these parameters is described with the operator
    [`add_metrology_object_line_measure`](add_metrology_object_line_measure.md).
    For a metrology object of type rectangle, the output parameter
    *`GenParamValue`* contains the geometry of the rectangle in
    the following order: *'row'*, *'column'*,
    *'phi'*, *'length1'*, *'length2'*. The
    meaning and the use of these parameters is described with the
    operator [`add_metrology_object_rectangle2_measure`](add_metrology_object_rectangle2_measure.md).
- Only valid for a metrology object of type circle:

  - ***'row'*, *'column'*, *'radius'*:** —

    These are parameters for a metrology object of type circle.
    The meaning and the use of these parameters is described with the
    operator [`add_metrology_object_circle_measure`](add_metrology_object_circle_measure.md).
- Only valid for a metrology object of type ellipse:

  - ***'row'*, *'column'*, *'phi'*,
    *'radius1'*, *'radius2'*:** —

    These are parameters
    for a metrology object of type ellipse. The meaning and the use
    of these parameters is described with the operator
    [`add_metrology_object_ellipse_measure`](add_metrology_object_ellipse_measure.md).
- Only valid for a metrology object of type line:

  - ***'row_begin'*, *'column_begin'*,
    *'row_end'*, *'column_end'*:** —

    These are parameters
    for a metrology object of type line. The meaning and the use
    of these parameters is described with the operator
    [`add_metrology_object_line_measure`](add_metrology_object_line_measure.md).
- Only valid for a metrology object of type rectangle:

  - ***'row'*, *'column'*, *'phi'*,
    *'length1'*, *'length2'*:** —

    These are
    parameters for a metrology object of type rectangle. The meaning
    and the use of these parameters is described with the
    operator [`add_metrology_object_rectangle2_measure`](add_metrology_object_rectangle2_measure.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MetrologyHandle`** (input_control)  metrology_model `→`  (handle)

Handle of the metrology model.

**`Index`** (input_control)  integer(-array) `→`  (string / integer)

Index of the metrology objects.

Default:
'all'

Suggested values:
'all', 0, 1, 2

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters.

Default:
'num_measures'

List of values:
'column', 'column_begin', 'column_end', 'distance_threshold', 'end_phi', 'instances_outside_measure_regions', 'length1', 'length2', 'max_num_iterations', 'measure_distance_min', 'measure_distance_min', 'measure_interpolation', 'measure_length1', 'measure_length2', 'measure_select', 'measure_sigma', 'measure_threshold', 'measure_transition', 'min_score', 'num_instances', 'num_measures', 'object_params', 'object_type', 'phi', 'point_order', 'radius', 'radius1', 'radius2', 'rand_seed', 'row', 'row_begin', 'row_end', 'start_phi', 'x', 'x_begin', 'x_end', 'y', 'y_begin', 'y_end'

**`GenParamValue`** (output_control)  attribute.value-array `→`  (string / real / integer)

Values of the generic parameters.

## Result

If the parameters are valid, the operator
`get_metrology_object_param` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`get_metrology_object_indices`,
`set_metrology_object_param`

## Possible Successors

`set_metrology_object_param`

## See also

`get_metrology_object_fuzzy_param`,
`get_metrology_object_num_instances`

## Module

2D Metrology
