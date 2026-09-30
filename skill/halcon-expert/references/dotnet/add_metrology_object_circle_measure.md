# AddMetrologyObjectCircleMeasure (Operator)

## Name

`AddMetrologyObjectCircleMeasure` — Add a circle or a circular arc to a metrology model.

## Signature

`static void HOperatorSet.AddMetrologyObjectCircleMeasure(HTuple metrologyHandle, HTuple row, HTuple column, HTuple radius, HTuple measureLength1, HTuple measureLength2, HTuple measureSigma, HTuple measureThreshold, HTuple genParamName, HTuple genParamValue, out HTuple index)`

`int HMetrologyModel.AddMetrologyObjectCircleMeasure(HTuple row, HTuple column, HTuple radius, HTuple measureLength1, HTuple measureLength2, HTuple measureSigma, HTuple measureThreshold, HTuple genParamName, HTuple genParamValue)`

`int HMetrologyModel.AddMetrologyObjectCircleMeasure(double row, double column, double radius, double measureLength1, double measureLength2, double measureSigma, double measureThreshold, HTuple genParamName, HTuple genParamValue)`

## Description

`AddMetrologyObjectCircleMeasure` adds a metrology object
of type circle or circular arc to a metrology model and prepares the
rectangular measure regions. The handle of the model is
passed in *`metrologyHandle`*.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The geometric shape of the metrology object of type circle is
specified by its center (*`row`*, *`column`*) and
*`radius`*. The rectangular measure regions lie
*perpendicular* to the boundary of the circle. The half edge
lengths of the measure regions are set in *`measureLength1`*
and *`measureLength2`*. The centers of the measure regions
lie on the boundary of the circle. The parameter *`measureSigma`*
specifies the standard deviation that is used by operator
[`ApplyMetrologyModel`](apply_metrology_model.md) to smooth the gray values of the image.
Salient edges can be selected with the parameter
*`measureThreshold`*, which constitutes a threshold on the
amplitude, i.e., the absolute value of the first derivative of the
edge. The operator `AddMetrologyObjectCircleMeasure`
returns the index of the added metrology object in parameter
*`index`*.

Furthermore, you can adjust some generic parameters with
*`genParamName`* and *`genParamValue`*. The following
values for *`genParamName`* and *`genParamValue`* are
available:

- ***"start_phi"*:** —

  The parameter specifies the angle at
  the start point of a circular arc. To create a
  closed circle the value of the parameter *"start_phi"* is
  set to 0 and the value of the parameter *"end_phi"*
  is set to $2\pi$ (with positive point order).
  The input value is mapped automatically
  to the interval $[0,2\pi]$.

  Suggested values:
   *0.0*, *0.78*,
  *6.28318*

  Default:
   *0.0*
- ***"end_phi"*:** —

  The parameter
  specifies the angle at the end point of a circular arc. To create
  a closed circle the value of the parameter *"start_phi"*
  is set to 0 and the value of the parameter
  *"end_phi"* is set to $2\pi$ (with positive
  point order). The input value is mapped internally
  automatically to the interval $[0,2\pi]$.

  Suggested values:
   *0.0*, *0.78*,
  *6.28318*

  Default:
   *6.28318*
- ***"point_order"*:** —

  The parameter specifies the direction
  of the circular arc. For the value *"positive"*, the circular
  arc is defined between *"start_phi"* and *"end_phi"*
  in mathematically positive direction (counterclockwise).
  For the value *"negative"*, the circular arc is defined
  between *"start_phi"* and *"end_phi"* in
  mathematically negative direction (clockwise).

  List of values:
   *"positive"*, *"negative"*

  Default:
   *"positive"*

Additionally all generic parameters, that are available for the
operator [`SetMetrologyObjectParam`](set_metrology_object_param.md) can be set. But note
that for a lot of applications the default values are sufficient
and no adjustment is necessary.

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

**`row`** (input_control)  circle.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate (or Y) of the center of the circle or
circular arc.

**`column`** (input_control)  circle.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column (or X) coordinate of the center of the circle or
circular arc.

**`radius`** (input_control)  circle.radius(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle or circular arc.

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
`MeasureLength1 < Radius`

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
"distance_threshold", "end_phi", "instances_outside_measure_regions", "max_num_iterations", "measure_distance", "measure_interpolation", "measure_select", "measure_transition", "min_score", "num_instances", "num_measures", "point_order", "rand_seed", "start_phi"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the generic parameters.

Default:
[]

Suggested values:
1, 2, 3, 4, 5, 10, 20, "all", "true", "false", "first", "last", "positive", "negative", "uniform", "nearest_neighbor", "bilinear", "bicubic"

**`index`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the created metrology object.

## Example (HDevelop)

```
read_image (Image, 'rings_and_nuts')
create_metrology_model (MetrologyHandle)
get_image_size (Image, Width, Height)
set_metrology_model_image_size (MetrologyHandle, Width, Height)
add_metrology_object_circle_measure (MetrologyHandle, 120, 130, 35, 10, 2, \
                              1, 30, ['measure_distance'], [40], Index)
apply_metrology_model (Image, MetrologyHandle)
get_metrology_object_result (MetrologyHandle, Index, 'all', 'result_type', \
                      'all_param', Circle)
get_metrology_object_result_contour (Contour, MetrologyHandle, Index, \
                                    'all', 1.5)
```

## Result

If the parameters are valid, the operator
`AddMetrologyObjectCircleMeasure`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

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
`AddMetrologyObjectEllipseMeasure`,
`AddMetrologyObjectLineMeasure`,
`AddMetrologyObjectRectangle2Measure`

## Module

2D Metrology
