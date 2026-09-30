# set_metrology_object_param (Operator)

## Name

`set_metrology_object_param` — Set parameters for the metrology objects of a metrology model.

## Signature

`def set_metrology_object_param(metrology_handle: HHandle, index: MaybeSequence[Union[str, int]], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[str, float, int]]) -> None`

## Description

`set_metrology_object_param` is used to set or change the
different parameters of a metrology object.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle
*`metrology_handle`*. The parameter *`index`* specifies
the metrology objects for which the parameters are set. The parameters
of all metrology objects are set if the parameter *`index`* is
set to *"all"*. All parameters can also
be set when creating a metrology object with
[`add_metrology_object_generic`](add_metrology_object_generic.md),
[`add_metrology_object_circle_measure`](add_metrology_object_circle_measure.md),
[`add_metrology_object_ellipse_measure`](add_metrology_object_ellipse_measure.md),
[`add_metrology_object_line_measure`](add_metrology_object_line_measure.md), or
[`add_metrology_object_rectangle2_measure`](add_metrology_object_rectangle2_measure.md).
The current configuration of the metrology model can be accessed
with [`get_metrology_object_param`](get_metrology_object_param.md). All parameters that can be
set with `set_metrology_object_param` can be reset with
[`reset_metrology_object_param`](reset_metrology_object_param.md).

In the following all generic parameters with the default values
are listed. But note that
for a lot of applications the default values are sufficient and
no adjustment is necessary. The following values for
*`gen_param_name`* and *`gen_param_value`* are possible -
ordered by different categories:

**Creating measure regions:**

- ***"measure_length1"*:** —

  The value of this parameter
  specifies the half length of the measure regions perpendicular
  to the metrology object boundary. It is equivalent to the measure
  tolerance. The unit of this value is pixel.

  Suggested values:
   *10.0*, *20.0*, *30.0*

  Default:
   *20.0*

  Restriction:
   *"measure_length1"* >= *1.0*
- ***"measure_length2"*:** —

  The value of this parameter
  specifies the half length of the measure regions tangential to the
  metrology object boundary. The unit of this value is pixel.

  Suggested values:
   *3.0*, *5.0*, *10.0*

  Default:
   *5.0*

  Restriction:
   *"measure_length2"* >= *0.0*
- ***"measure_distance"*:** —

  The value of this parameter
  specifies the desired distance between the centers of two measure regions.
  If the value leads to too few measure regions, the parameter has no
  influence and the number of measure regions will be increased to
  the minimum required number of measure regions (circle = 3,
  ellipse = 5, line = 2, rectangle = 2 per side = 8).
  The unit of this value is pixel.

  If this value is set, the parameter *"num_measures"* has no
  influence.

  Suggested values:
   *5.0*, *15.0*, *20.0*,
  *30.0*

  Default:
   *10.0*
- ***"num_measures"*:** —

  The value of this parameter
  specifies the desired number of measure regions.

  The minimum number of measure regions depends on the type of the
  metrology object:

  - Line: 2 measure regions
  - Circle: 3 measure regions
  - Circular arc: 4 measure regions
  - Ellipse: 5 measure regions
  - Elliptic arc: 6 measure regions
  - Rectangle: 8 measure regions (2 regions each side)

  If the chosen value is too low, *"num_measures"* is automatically
  set to the respective minimum value.

  If this value is set, the parameter
  *"measure_distance"* has no influence.

  Suggested values:
   *8*, *10*, *16*,
  *20*, *30*, *50*,
  *100*

**Edge detection:**

- ***"measure_sigma"*:** —

  The parameter specifies the sigma for the Gaussian smoothing. The
  meaning, the use, and the default value of this parameter are
  described with the operator [`measure_pos`](measure_pos.md) by the parameter
  `sigma`.
- ***"measure_threshold"*:** —

  The parameter specifies the minimum edge amplitude. The meaning,
  the use, and the default value of this parameter are
  described with the operator [`measure_pos`](measure_pos.md) by the parameter
  `threshold`.
- ***"measure_select"*:** —

  The parameter specifies the selection of end points of the edges.
  The meaning, the use, and the default value of this parameter are
  described with the operator [`measure_pos`](measure_pos.md) by the parameter
  `select`.
- ***"measure_transition"*:** —

  The parameter specifies the use of dark/light or light/dark edges.
  The meaning and the use of the values *"all"*,
  *"positive"*, and *"negative"* for the parameter
  *"measure_transition"* is described with the operator
  [`measure_pos`](measure_pos.md) by the parameter `transition`.
  Additionally, *"measure_transition"* can be set to the value
  *"uniform"*. Then, all positive edges (dark/light edges) and
  all negative edges (light/dark edges) are detected by the edge
  detection but when fitting the geometric shapes, the edges with
  different edge types are used separately, i.e., for each instance of
  a geometric shape either only the positive edges or the negative
  edges are used.

  The measure direction within the measure regions is from the
  inside to the outside of the metrology object for objects of the types
  circle, ellipse, or rectangle. For metrology objects of the type line
  measure direction within the measure regions is from the left to the
  right, seen from the first point of the line (see
  `row_begin` and `column_begin` of the
  operator [`add_metrology_object_line_measure`](add_metrology_object_line_measure.md)).

  List of values:
   *"all"*, *"negative"*,
  *"positive"*, *"uniform"*

  Default:
   *"all"*
- ***"measure_interpolation"*:** —

  The parameter specifies the type of interpolation to be used.
  The meaning, the use and the default value of this parameter is
  described with the operator [`gen_measure_rectangle2`](gen_measure_rectangle2.md) by the
  parameter `interpolation`.

**Fitting the geometric shapes:**

- ***"min_score"*:** —

  The parameter determines
  what score a potential instance must at least have to be regarded
  as a valid instance of the metrology object. The
  score is the number of detected edges that are used to compute the
  results divided by the maximum number of measure regions (see
  [`apply_metrology_model`](apply_metrology_model.md)). If it can be expected that all
  edges of the metrology object are present, the parameter
  *"min_score"* can be set to a value as high as *0.8* or
  even *0.9*. Note that in images with a high degree of clutter
  or strong background texture the parameter *"min_score"* should
  be set to a value not much lower than *0.7* since otherwise
  false instances of a metrology object could be found.

  Suggested values:
   *0.5*, *0.7*, *0.9*

  Default:
   *0.7*
- ***"num_instances"*:** —

  The parameter specifies
  the maximum number of successfully fitted instances of each metrology
  object after which the fitting will stop (see
  [`apply_metrology_model`](apply_metrology_model.md)). Successfully fitted instances of
  the metrology objects must have a score of at least the value of
  *"min_score"*.

  Suggested values:
   *1*, *2*, *3*, *4*

  Default:
   *1*
- ***"distance_threshold"*:** —

  [`apply_metrology_model`](apply_metrology_model.md) uses a randomized search
  algorithm (RANSAC) to fit the geometric shapes. An edge point is
  considered to be part of a fitted geometric shape, if the distance of
  the edge point to the geometric shape does not exceed the
  value of *"distance_threshold"*.

  Suggested values:
   *0*, *1.0*, *2.0*,
  *3.5*, *5.0*

  Default:
   *3.5*
- ***"max_num_iterations"*:** —

  The RANSAC algorithm estimates the number of iterations necessary for
  fitting the requested geometric shape. The estimation is based on the
  extracted edge data and the complexity of the shape.
  When setting the value of the parameter *"max_num_iterations"*,
  an upper limit for the computed number of iterations is defined. The
  number of iterations is still estimated by the RANSAC algorithm but cannot
  exceed the value of *"max_num_iterations"*. Setting this
  parameter can be helpful, if the quality of the fitting is not as
  important as observing time limits. However, if
  *"max_num_iterations"* is set too low, the algorithm will return
  low-quality or no results.

  By default, *"max_num_iterations"* is set to -1, indicating that
  no additional upper limit is set for the number of iterations of the
  RANSAC algorithm.

  Suggested values:
   *10*, *100*, *1000*

  Default:
   *-1*
- ***"rand_seed"*:** —

  The parameter specifies the seed for
  the random number generator for the RANSAC algorithm that is
  used by the selection of the edges the in operator
  [`apply_metrology_model`](apply_metrology_model.md). If
  the value of the parameter *"rand_seed"* is set to a number
  unequal to the value *0*, the operator yields the same result
  on every call with the same parameters, because the internally used
  random number generator is initialized with the value of the
  parameter *"rand_seed"*.

  If the parameter *"rand_seed"* is set to the value
  *0*, the random number generator is initialized with the
  current time. In this case, the results are not reproducible.

  Suggested values:
   *0*, *1*, *42*

  Default:
   *42*
- ***"instances_outside_measure_regions"*:** —

  The parameter
  specifies the validation of the results of measurements. If the value
  of the parameter *"instances_outside_measure_regions"* is
  set to the value *"false"*, only resulting instances of an
  metrology object are valid that are inside the major
  axis of the measure regions of this metrology object. Instances
  which are not valid are not stored. If the value of the parameter
  *"instances_outside_measure_regions"* is set to the value
  *"true"*, all instances of a metrology object are valid.

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- metrology_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`metrology_handle`** (input_control, state is modified)  metrology_model `→` HHandle

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[Union[str, int]]

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic parameters.

Default:
"num_instances"

List of values:
"distance_threshold", "instances_outside_measure_regions", "max_num_iterations", "measure_distance", "measure_interpolation", "measure_length1", "measure_length2", "measure_select", "measure_sigma", "measure_threshold", "measure_transition", "min_score", "num_instances", "num_measures", "rand_seed"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[str, float, int]]

Values of the generic parameters.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 10, 20, "all", "true", "false", "first", "last", "positive", "negative", "uniform", "nearest_neighbor", "bilinear", "bicubic"

## Result

If the parameters are valid, the operator
`set_metrology_object_param` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`get_metrology_object_param`

## Possible Successors

`apply_metrology_model`,
`reset_metrology_object_param`,
`get_metrology_object_param`

## See also

`set_metrology_object_fuzzy_param`

## Module

2D Metrology
