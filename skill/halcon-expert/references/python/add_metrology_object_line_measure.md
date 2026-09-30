# add_metrology_object_line_measure (Operator)

## Name

`add_metrology_object_line_measure` — Add a line to a metrology model.

## Signature

`def add_metrology_object_line_measure(metrology_handle: HHandle, row_begin: MaybeSequence[Union[int, float]], column_begin: MaybeSequence[Union[int, float]], row_end: MaybeSequence[Union[int, float]], column_end: MaybeSequence[Union[int, float]], measure_length_1: Union[int, float], measure_length_2: Union[int, float], measure_sigma: Union[int, float], measure_threshold: Union[int, float], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[float, int, str]]) -> int`

## Description

`add_metrology_object_line_measure` adds a metrology object of
type line to a metrology model and prepares the rectangular measure
regions. The handle of the model is passed in
*`metrology_handle`*.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The geometric shape of the metrology object of type line is described
by the coordinates of the start point (*`row_begin`*,
*`column_begin`*) and the coordinates of the end point
(*`row_end`*, *`column_end`*). The rectangular measure regions
lie *perpendicular* to the line. The half edge lengths of the
measure regions perpendicular and tangential to the line are set
in *`measure_length_1`* and *`measure_length_2`*.
The centers of the measure regions lie on the line. The
parameter *`measure_sigma`* specifies a standard deviation that
is used by the operator [`apply_metrology_model`](apply_metrology_model.md)
to smooth the gray values of the image. Salient edges can be
selected with the parameter *`measure_threshold`*, which
constitutes a threshold on the amplitude, i.e., the absolute
value of the first derivative of the edge.

Furthermore, you can adjust some generic parameters within
*`gen_param_name`* and *`gen_param_value`*. In particular,
all generic parameters that are available in the operator
[`set_metrology_object_param`](set_metrology_object_param.md) can be set. But note that
for a lot of applications the default values are sufficient and
no adjustment is necessary.

The operator
`add_metrology_object_line_measure` returns the index of the added
metrology object in the parameter *`index`*.

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

**`row_begin`** (input_control)  line.begin.y(-array) `→` MaybeSequence[Union[int, float]]

Row (or Y) coordinate of the start of the line.

**`column_begin`** (input_control)  line.begin.x(-array) `→` MaybeSequence[Union[int, float]]

Column (or X) coordinate of the start of the line.

**`row_end`** (input_control)  line.end.y(-array) `→` MaybeSequence[Union[int, float]]

Row (or Y) coordinate of the end of the line.

**`column_end`** (input_control)  line.end.x(-array) `→` MaybeSequence[Union[int, float]]

Column (or X) coordinate of the end of the line.

**`measure_length_1`** (input_control)  number `→` Union[int, float]

Half length of the measure regions
perpendicular to the boundary.

Default:
20.0

Suggested values:
10.0, 20.0, 30.0

Value range:
`1.0
≤
measure_length_1`

Minimum increment:
1.0

Recommended increment:
10.0

**`measure_length_2`** (input_control)  number `→` Union[int, float]

Half length of the measure regions tangential
to the boundary.

Default:
5.0

Suggested values:
3.0, 5.0, 10.0

Value range:
`1.0
≤
measure_length_2`

Minimum increment:
1.0

Recommended increment:
10.0

**`measure_sigma`** (input_control)  number `→` Union[int, float]

Sigma of the Gaussian function for the smoothing.

Default:
1.0

Suggested values:
0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0

Value range:
`0.4
≤
measure_sigma
≤
100.0`

Minimum increment:
0.01

Recommended increment:
0.1

**`measure_threshold`** (input_control)  number `→` Union[int, float]

Minimum edge amplitude.

Default:
30.0

Suggested values:
5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 90.0, 110.0

Value range:
`1
≤
measure_threshold
≤
255` (lin)

Minimum increment:
0.5

Recommended increment:
2

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Names of the generic parameters.

Default:
[]

List of values:
"distance_threshold", "instances_outside_measure_regions", "max_num_iterations", "measure_distance", "measure_interpolation", "measure_select", "measure_transition", "min_score", "num_instances", "num_measures", "rand_seed"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[float, int, str]]

Values of the generic parameters.

Default:
[]

Suggested values:
1, 2, 3, 4, 5, 10, 20, "all", "true", "false", "first", "last", "positive", "negative", "uniform", "nearest_neighbor", "bilinear", "bicubic"

**`index`** (output_control)  integer `→` int

Index of the created metrology object.

## Result

If the parameters are valid, the operator
`add_metrology_object_line_measure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`set_metrology_model_image_size`

## Possible Successors

`align_metrology_model`,
`apply_metrology_model`

## Alternatives

`add_metrology_object_generic`

## See also

`get_metrology_object_model_contour`,
`set_metrology_model_param`,
`add_metrology_object_circle_measure`,
`add_metrology_object_ellipse_measure`,
`add_metrology_object_rectangle2_measure`

## Module

2D Metrology
