# add_metrology_object_line_measure (Operator)

## Name

`add_metrology_object_line_measure` — Add a line to a metrology model.

## Signature

`add_metrology_object_line_measure( : : MetrologyHandle, RowBegin, ColumnBegin, RowEnd, ColumnEnd, MeasureLength1, MeasureLength2, MeasureSigma, MeasureThreshold, GenParamName, GenParamValue : Index)`

## Description

`add_metrology_object_line_measure` adds a metrology object of
type line to a metrology model and prepares the rectangular measure
regions. The handle of the model is passed in
*`MetrologyHandle`*.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The geometric shape of the metrology object of type line is described
by the coordinates of the start point (*`RowBegin`*,
*`ColumnBegin`*) and the coordinates of the end point
(*`RowEnd`*, *`ColumnEnd`*). The rectangular measure regions
lie *perpendicular* to the line. The half edge lengths of the
measure regions perpendicular and tangential to the line are set
in *`MeasureLength1`* and *`MeasureLength2`*.
The centers of the measure regions lie on the line. The
parameter *`MeasureSigma`* specifies a standard deviation that
is used by the operator [`apply_metrology_model`](apply_metrology_model.md)
to smooth the gray values of the image. Salient edges can be
selected with the parameter *`MeasureThreshold`*, which
constitutes a threshold on the amplitude, i.e., the absolute
value of the first derivative of the edge.

Furthermore, you can adjust some generic parameters within
*`GenParamName`* and *`GenParamValue`*. In particular,
all generic parameters that are available in the operator
[`set_metrology_object_param`](set_metrology_object_param.md) can be set. But note that
for a lot of applications the default values are sufficient and
no adjustment is necessary.

The operator
`add_metrology_object_line_measure` returns the index of the added
metrology object in the parameter *`Index`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MetrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MetrologyHandle`** (input_control, state is modified)  metrology_model `→`  (handle)

Handle of the metrology model.

**`RowBegin`** (input_control)  line.begin.y(-array) `→`  (real / integer)

Row (or Y) coordinate of the start of the line.

**`ColumnBegin`** (input_control)  line.begin.x(-array) `→`  (real / integer)

Column (or X) coordinate of the start of the line.

**`RowEnd`** (input_control)  line.end.y(-array) `→`  (real / integer)

Row (or Y) coordinate of the end of the line.

**`ColumnEnd`** (input_control)  line.end.x(-array) `→`  (real / integer)

Column (or X) coordinate of the end of the line.

**`MeasureLength1`** (input_control)  number `→`  (real / integer)

Half length of the measure regions
perpendicular to the boundary.

Default:
20.0

Suggested values:
10.0, 20.0, 30.0

Value range:
`1.0
≤
MeasureLength1`

Minimum increment:
1.0

Recommended increment:
10.0

**`MeasureLength2`** (input_control)  number `→`  (real / integer)

Half length of the measure regions tangential
to the boundary.

Default:
5.0

Suggested values:
3.0, 5.0, 10.0

Value range:
`1.0
≤
MeasureLength2`

Minimum increment:
1.0

Recommended increment:
10.0

**`MeasureSigma`** (input_control)  number `→`  (real / integer)

Sigma of the Gaussian function for the smoothing.

Default:
1.0

Suggested values:
0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0

Value range:
`0.4
≤
MeasureSigma
≤
100.0`

Minimum increment:
0.01

Recommended increment:
0.1

**`MeasureThreshold`** (input_control)  number `→`  (real / integer)

Minimum edge amplitude.

Default:
30.0

Suggested values:
5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 90.0, 110.0

Value range:
`1
≤
MeasureThreshold
≤
255` (lin)

Minimum increment:
0.5

Recommended increment:
2

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters.

Default:
[]

List of values:
'distance_threshold', 'instances_outside_measure_regions', 'max_num_iterations', 'measure_distance', 'measure_interpolation', 'measure_select', 'measure_transition', 'min_score', 'num_instances', 'num_measures', 'rand_seed'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string)

Values of the generic parameters.

Default:
[]

Suggested values:
1, 2, 3, 4, 5, 10, 20, 'all', 'true', 'false', 'first', 'last', 'positive', 'negative', 'uniform', 'nearest_neighbor', 'bilinear', 'bicubic'

**`Index`** (output_control)  integer `→`  (integer)

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
