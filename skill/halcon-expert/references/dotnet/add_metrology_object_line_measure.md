# AddMetrologyObjectLineMeasure (Operator)

## Name

`AddMetrologyObjectLineMeasure` — Add a line to a metrology model.

## Signature

`static void HOperatorSet.AddMetrologyObjectLineMeasure(HTuple metrologyHandle, HTuple rowBegin, HTuple columnBegin, HTuple rowEnd, HTuple columnEnd, HTuple measureLength1, HTuple measureLength2, HTuple measureSigma, HTuple measureThreshold, HTuple genParamName, HTuple genParamValue, out HTuple index)`

`int HMetrologyModel.AddMetrologyObjectLineMeasure(HTuple rowBegin, HTuple columnBegin, HTuple rowEnd, HTuple columnEnd, HTuple measureLength1, HTuple measureLength2, HTuple measureSigma, HTuple measureThreshold, HTuple genParamName, HTuple genParamValue)`

`int HMetrologyModel.AddMetrologyObjectLineMeasure(double rowBegin, double columnBegin, double rowEnd, double columnEnd, double measureLength1, double measureLength2, double measureSigma, double measureThreshold, HTuple genParamName, HTuple genParamValue)`

## Description

`AddMetrologyObjectLineMeasure` adds a metrology object of
type line to a metrology model and prepares the rectangular measure
regions. The handle of the model is passed in
*`metrologyHandle`*.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The geometric shape of the metrology object of type line is described
by the coordinates of the start point (*`rowBegin`*,
*`columnBegin`*) and the coordinates of the end point
(*`rowEnd`*, *`columnEnd`*). The rectangular measure regions
lie *perpendicular* to the line. The half edge lengths of the
measure regions perpendicular and tangential to the line are set
in *`measureLength1`* and *`measureLength2`*.
The centers of the measure regions lie on the line. The
parameter *`measureSigma`* specifies a standard deviation that
is used by the operator [`ApplyMetrologyModel`](apply_metrology_model.md)
to smooth the gray values of the image. Salient edges can be
selected with the parameter *`measureThreshold`*, which
constitutes a threshold on the amplitude, i.e., the absolute
value of the first derivative of the edge.

Furthermore, you can adjust some generic parameters within
*`genParamName`* and *`genParamValue`*. In particular,
all generic parameters that are available in the operator
[`SetMetrologyObjectParam`](set_metrology_object_param.md) can be set. But note that
for a lot of applications the default values are sufficient and
no adjustment is necessary.

The operator
`AddMetrologyObjectLineMeasure` returns the index of the added
metrology object in the parameter *`index`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- metrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`metrologyHandle`** (input_control, state is modified)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`rowBegin`** (input_control)  line.begin.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row (or Y) coordinate of the start of the line.

**`columnBegin`** (input_control)  line.begin.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column (or X) coordinate of the start of the line.

**`rowEnd`** (input_control)  line.end.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row (or Y) coordinate of the end of the line.

**`columnEnd`** (input_control)  line.end.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column (or X) coordinate of the end of the line.

**`measureLength1`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Half length of the measure regions
perpendicular to the boundary.

Default:
20.0

Suggested values:
10.0, 20.0, 30.0

Value range:
`1.0
≤
measureLength1`

Minimum increment:
1.0

Recommended increment:
10.0

**`measureLength2`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Half length of the measure regions tangential
to the boundary.

Default:
5.0

Suggested values:
3.0, 5.0, 10.0

Value range:
`1.0
≤
measureLength2`

Minimum increment:
1.0

Recommended increment:
10.0

**`measureSigma`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Sigma of the Gaussian function for the smoothing.

Default:
1.0

Suggested values:
0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0

Value range:
`0.4
≤
measureSigma
≤
100.0`

Minimum increment:
0.01

Recommended increment:
0.1

**`measureThreshold`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum edge amplitude.

Default:
30.0

Suggested values:
5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 90.0, 110.0

Value range:
`1
≤
measureThreshold
≤
255` (lin)

Minimum increment:
0.5

Recommended increment:
2

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
[]

List of values:
"distance_threshold", "instances_outside_measure_regions", "max_num_iterations", "measure_distance", "measure_interpolation", "measure_select", "measure_transition", "min_score", "num_instances", "num_measures", "rand_seed"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the generic parameters.

Default:
[]

Suggested values:
1, 2, 3, 4, 5, 10, 20, "all", "true", "false", "first", "last", "positive", "negative", "uniform", "nearest_neighbor", "bilinear", "bicubic"

**`index`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the created metrology object.

## Result

If the parameters are valid, the operator
`AddMetrologyObjectLineMeasure` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`SetMetrologyModelImageSize`

## Possible Successors

`AlignMetrologyModel`,
`ApplyMetrologyModel`

## Alternatives

`AddMetrologyObjectGeneric`

## See also

`GetMetrologyObjectModelContour`,
`SetMetrologyModelParam`,
`AddMetrologyObjectCircleMeasure`,
`AddMetrologyObjectEllipseMeasure`,
`AddMetrologyObjectRectangle2Measure`

## Module

2D Metrology
