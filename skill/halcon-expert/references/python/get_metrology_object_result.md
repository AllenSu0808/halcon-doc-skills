# get_metrology_object_result (Operator)

## Name

`get_metrology_object_result` — Get the results of the measurement of a metrology model.

## Signature

`def get_metrology_object_result(metrology_handle: HHandle, index: MaybeSequence[Union[int, str]], instance: MaybeSequence[Union[int, str]], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float]]) -> Sequence[Union[float, int, str]]`

`def get_metrology_object_result_s(metrology_handle: HHandle, index: MaybeSequence[Union[int, str]], instance: MaybeSequence[Union[int, str]], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float]]) -> Union[float, int, str]`

## Description

`get_metrology_object_result` allows to access the results of a
measurement obtained by [`apply_metrology_model`](apply_metrology_model.md) for the metrology
objects of the metrology model *`metrology_handle`*.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The parameter *`index`* specifies for which metrology objects the
results are queried. For *`index`* set to *"all"*, the results
of all metrology objects are returned. With the parameter *`instance`*
it can be specified, which instances of the results are returned in
*`parameter`*. The results for all instances are
returned by setting *`instance`* to *"all"*. Different generic
parameters can be used to control the returned values in *`parameter`*.
The generic parameter names are passed in *`gen_param_name`*. The
corresponding values are passed in *`gen_param_value`*. The following
parameters and values are possible:

- ***"result_type"*:** —

  If *`gen_param_name`* is set to *"result_type"*, then
  *`gen_param_value`* allows to control
  how and what results are returned for a metrology object.
  All measured parameters of the queried metrology
  object can be queried at once, specific parameters can be queried
  individually or the score for the metrology object can be queried.

  - ***'Obtaining all parameters'*:** —

    If *`gen_param_value`* is set to *"all_param"*, then all
    measured parameters of a metrology object are returned. If
    camera parameters and a pose
    have been set (see [`set_metrology_model_param`](set_metrology_model_param.md)), the
    results are returned in metric coordinates, otherwise in pixels.

    For a *circle*, the return
    values are the coordinates of the center and the radius
    of the circle. The order is [*"row"*, *"column"*,
    *"radius"*] or [*"x"*, *"y"*,
    *"radius"*] respectively.

    For an *ellipse*, the return
    values are the coordinates of the center, the orientation of the major axis
    *"phi"*, the length of the larger half axis
    *"radius1"*, and the length of the smaller half axis
    *"radius2"* of the ellipse. The order is [*"row"*,
    *"column"*, *"phi"*, *"radius1"*,
    *"radius2"*] or [*"x"*,
    *"y"*, *"phi"*, *"radius1"*,
    *"radius2"*] respectively.

    For a *line*, the start and end
    point of the line is returned.
    The order is [*"row_begin"*, *"column_begin"*,
    *"row_end"*, *"column_end"*] or
    [*"x_begin"*, *"y_begin"*, *"x_end"*, *"y_end"*]

    For a *rectangle*, the return
    values are the coordinates of the center, the orientation of the main axis
    *"phi"*, the length of the larger half edge
    *"length1"*, and the length of the smaller half edge
    *"length2"* of the rectangle. The order is [*"row"*,
    *"column"*, *"phi"*, *"length1"*,
    *"length2"*] or [*"x"*,
    *"y"*, *"phi"*, *"length1"*,
    *"length2"*] respectively.
  - ***'Obtaining specific parameters'*:** —

    Measured object parameters can also be queried individually by providing
    the desired parameter name in *`gen_param_name`*.

    When *no camera parameters* and no measurement plane are set,
    the following parameters can be queried individually, depending on
    whether they are available for the respective object.
    Note that for lines, additionally
    the 3 parameters of the hessian normal form can be queried,
    i.e., the unit normal vector *"nrow"*, *"ncolumn"*
    and the orthogonal distance
    *"distance"* of the line from the origin of the coordinate system.
    The sign of the distance determines the side of the line on which
    the origin is located.

    List of values:
     *"row"*, *"column"*,
    *"radius"*, *"phi"* , *"radius1"*, *"radius2"*,
    *"length1"*, *"length2"*, *"row_begin"*,
    *"column_begin"*, *"row_end"*, *"column_end"*,
    *"nrow"*, *"ncolumn"*, *"distance"*

    If *camera parameters* and a measurement plane
    was set, the parameters are returned in metric coordinates,
    the following parameters can be queried individually, depending on
    whether they are available for the respective object.
    Note that for lines, additionally the 3 parameters of the hessian normal
    form can be queried, i.e., the unit normal vector
    *"nx"*, *"ny"* and the orthogonal distance
    *"distance"* of the line from the origin of the coordinate system.
    The sign of the distance determines the side of the line on which
    the origin is located.

    List of values:
     *"x"*, *"y"*,
    *"radius"*, *"phi"* , *"radius1"*, *"radius2"*,
    *"length1"*, *"length2"*, *"radius1"*,
    *"radius2"*, *"length1"*, *"length2"*,
    *"x_begin"*, *"y_begin"*, *"x_end"*,
    *"y_end"*, *"nx"*, *"ny"*, *"distance"*
  - ***'Obtaining the score'*:** —

    If *`gen_param_name`* is set to the *"score"*, the fitting
    scores are returned. The score represents
    the number of measurements that are used for the calculation of
    the results divided by the maximum number of measure regions.
- ***"used_edges"*:** —

  To query the edge points, that were actually
  used for a fitted metrology object, you can choose between following values
  for *`gen_param_value`*:

  - ***"row"*:** —

    Return the row coordinate of the edges that
    were used to fit the metrology object.
  - ***"column"*:** —

    Return the column coordinate of the edges that were used to fit the
    metrology object.
  - ***"amplitude"*:** —

    Return the edge amplitude of the edges that
    were used to fit the metrology object.

  List of values:
   *"row"*, *"column"*,
  *"amplitude"*
- ***"angle_direction"*:** —

  The parameter determines the rotation
  direction for angles that result from the fitting. Setting the
  parameter *"angle_direction"* to *"positive"* the angle is
  specified between the main axis of the object and
  the horizontal axis of the coordinate system in the mathematically
  positive direction (counterclockwise). Setting the parameter
  *"angle_direction"* to *"negative"* the angle is specified
  between the main axis of the object and the horizontal axis
  of the coordinate system in the mathematically negative direction
  (clockwise). The results of the angles are returned in radians.

  List of values:
   *"positive"*, *"negative"*

  Default:
   *"positive"*

It is possible to query the results of several metrology objects (see the
parameter *`index`*) and several instances (see the parameter
*`instance`*) of the metrology objects simultaneously. The results are
returned in the following order in *`parameter`*: 1st instance
of 1st metrology object, 2nd instance of 1st metrology object, etc., 1st
instance of 2nd metrology object, 2nd instance of 2nd metrology object,
etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrology_handle`** (input_control)  metrology_model `→` HHandle

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Index of the metrology object.

Default:
0

Suggested values:
"all", 0, 1, 2

**`instance`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Instance of the metrology object.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Name of the generic parameter.

Default:
"result_type"

List of values:
"angle_direction", "result_type", "used_edges"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, float]]

Value of the generic parameter.

Default:
"all_param"

Suggested values:
"all_param", "score", "true", "false", "row", "column", "amplitude", "radius", "phi", "radius1", "radius2", "length1", "length2", "row_begin", "column_begin", "row_end", "column_end", "nrow", "ncolumn", "distance", "x", "y", "x_begin", "y_begin", "x_end", "y_end", "nx", "ny", "positive", "negative"

**`parameter`** (output_control)  real(-array) `→` Sequence[Union[float, int, str]]

Result values.

## Result

If the parameters are valid, the operator
`get_metrology_object_result` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`apply_metrology_model`

## Possible Successors

`clear_metrology_model`

## See also

`get_metrology_object_result_contour`,
`get_metrology_object_measures`

## Module

2D Metrology
