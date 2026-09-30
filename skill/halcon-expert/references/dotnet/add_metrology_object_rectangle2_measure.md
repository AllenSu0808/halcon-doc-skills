# AddMetrologyObjectRectangle2Measure (Operator)

## Name

`AddMetrologyObjectRectangle2Measure` — Add a rectangle to a metrology model.

## Signature

`static void HOperatorSet.AddMetrologyObjectRectangle2Measure(HTuple metrologyHandle, HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, HTuple measureLength1, HTuple measureLength2, HTuple measureSigma, HTuple measureThreshold, HTuple genParamName, HTuple genParamValue, out HTuple index)`

`int HMetrologyModel.AddMetrologyObjectRectangle2Measure(HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, HTuple measureLength1, HTuple measureLength2, HTuple measureSigma, HTuple measureThreshold, HTuple genParamName, HTuple genParamValue)`

`int HMetrologyModel.AddMetrologyObjectRectangle2Measure(double row, double column, double phi, double length1, double length2, double measureLength1, double measureLength2, double measureSigma, double measureThreshold, HTuple genParamName, HTuple genParamValue)`

## Description

`AddMetrologyObjectRectangle2Measure` adds a metrology
object of type rectangle to a metrology model and prepares the
rectangular measure regions. The handle of the model is
passed in *`metrologyHandle`*.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The geometric shape of the metrology object of type rectangle is
specified by its center (*`row`*, *`column`*), the orientation
of the main axis *`phi`*, and the half edge lengths *`length1`*
and *`length2`*. The input value for *`phi`* is mapped
automatically to the interval $]-\pi,\pi]$. The
rectangular measure regions lie *perpendicular* to the
boundary of the rectangle. The half edge lengths of the measure
regions perpendicular and tangential to the boundary of the
rectangle are set in *`measureLength1`* and
*`measureLength2`*. The centers of the measure regions lie on
the boundary of the rectangle. The parameter *`measureSigma`*
specifies a standard deviation that is used by the operator
[`ApplyMetrologyModel`](apply_metrology_model.md) to smooth the gray values of the
image. Salient edges can be selected with the parameter
*`measureThreshold`*, which constitutes a threshold on the
amplitude, i.e., the absolute value of the first derivative of
the edge.

Furthermore, you can adjust some generic parameters within
*`genParamName`* and *`genParamValue`*. In particular,
all generic parameters that are available in the operator
[`SetMetrologyObjectParam`](set_metrology_object_param.md) can be set. But note that
for a lot of applications the default values are sufficient and
no adjustment is necessary.

The operator `AddMetrologyObjectRectangle2Measure` returns the
index of the added metrology object within the metrology model in the
parameter *`index`*.

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

**`row`** (input_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row (or Y) coordinate of the center of the rectangle.

**`column`** (input_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column (or X) coordinate of the center of the rectangle.

**`phi`** (input_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Orientation of the main axis [rad].

**`length1`** (input_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Length of the larger half edge of the rectangle.

**`length2`** (input_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Length of the smaller half edge of the rectangle.

**`measureLength1`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Half length of the measure regions perpendicular
to the boundary.

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

Restriction:
`MeasureLength1 < Length1 && MeasureLength1 < Length2`

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
`AddMetrologyObjectRectangle2Measure` returns the value 2 (
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
`AddMetrologyObjectLineMeasure`

## Module

2D Metrology
