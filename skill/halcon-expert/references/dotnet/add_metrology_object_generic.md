# AddMetrologyObjectGeneric (Operator)

## Name

`AddMetrologyObjectGeneric` — Add a metrology object to a metrology model.

## Signature

`static void HOperatorSet.AddMetrologyObjectGeneric(HTuple metrologyHandle, HTuple shape, HTuple shapeParam, HTuple measureLength1, HTuple measureLength2, HTuple measureSigma, HTuple measureThreshold, HTuple genParamName, HTuple genParamValue, out HTuple index)`

`int HMetrologyModel.AddMetrologyObjectGeneric(HTuple shape, HTuple shapeParam, HTuple measureLength1, HTuple measureLength2, HTuple measureSigma, HTuple measureThreshold, HTuple genParamName, HTuple genParamValue)`

`int HMetrologyModel.AddMetrologyObjectGeneric(string shape, HTuple shapeParam, double measureLength1, double measureLength2, double measureSigma, double measureThreshold, HTuple genParamName, HTuple genParamValue)`

## Description

`AddMetrologyObjectGeneric` adds a metrology object
of type *`shape`* to a metrology model and prepares the
rectangular measure regions.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The handle of the model is
passed in *`metrologyHandle`*.

*`shape`* specifies which type of object is added to the
metrology model. The operator `AddMetrologyObjectGeneric`
returns the index of the added metrology object in the parameter
*`index`*.
Note that `AddMetrologyObjectGeneric` provides the
functionality of the operators [`AddMetrologyObjectCircleMeasure`](add_metrology_object_circle_measure.md),
[`AddMetrologyObjectEllipseMeasure`](add_metrology_object_ellipse_measure.md),
[`AddMetrologyObjectRectangle2Measure`](add_metrology_object_rectangle2_measure.md) and
[`AddMetrologyObjectLineMeasure`](add_metrology_object_line_measure.md) in one operator.

### Possible shapes

Depending on the object specified in *`shape`* the following values
are expected:

- ***"circle"*:** —

  The geometric shape of the metrology object of type circle is
  specified by its center (Row, Column) and radius.

  *`shapeParam`*=*[Row, Column, Radius]*
- ***"rectangle2"*:** —

  The geometric shape of the metrology object of type rectangle is
  specified by its center (Row, Column), the orientation
  of the main axis Phi, and the half edge lengths Length1
  and Length2. The input value for Phi is mapped
  automatically to the interval $]-\pi,\pi]$.

  *`shapeParam`*=*[Row, Column, Phi, Length1, Length2]*
- ***"ellipse"*:** —

  The geometric shape of the metrology object of type ellipse is specified
  by its center (Row, Column), the orientation of the
  main axis Phi, the length of the larger half axis
  Radius1, and the length of the smaller half axis
  Radius2. The input value for Phi is mapped
  automatically to the interval $]-\pi,\pi]$.

  *`shapeParam`*=*[Row, Column, Phi, Radius1, Radius2]*
- ***"line"*:** —

  The geometric shape of the metrology object of type line is described
  by the coordinates of its start point (RowBegin, ColumnBegin) and the
  coordinates of its end point (RowEnd, ColumnEnd).

  *`shapeParam`*=*[RowBegin, ColumnBegin, RowEnd, ColumnEnd]*

### Definition of measure regions

`AddMetrologyObjectGeneric` also prepares the
rectangular measure regions. The rectangular measure regions lie
*perpendicular* to the boundary of the object. The half edge lengths of
the measure regions perpendicular and tangential to the boundary of the
object are set in *`measureLength1`* and
*`measureLength2`*. The centers of the measure regions lie on
the boundary of the object. The parameter *`measureSigma`*
specifies a standard deviation that is used by the operator
[`ApplyMetrologyModel`](apply_metrology_model.md) to smooth the gray values of the
image. Salient edges can be selected with the parameter
*`measureThreshold`*, which constitutes a threshold on the
amplitude, i.e., the absolute value of the first derivative of
the edge.

### Generic parameters

Generic parameters and their values can be specified using
*`genParamName`* and *`genParamValue`*.
All generic parameters that are available in the operator
[`SetMetrologyObjectParam`](set_metrology_object_param.md) can also be set in
`AddMetrologyObjectGeneric`. But note that
for a lot of applications the default values are sufficient and
no adjustment is necessary. Furthermore, the following values for
*`genParamName`* and *`genParamValue`* are
available only for *`shape`* =
*"circle"* and *"ellipse"*:

- ***"start_phi"*:** —

  The parameter specifies the angle at
  the start point of a circular or elliptic arc.
  For an ellipse, the angle at the start point
  is measured relative to the positive main axis
  and corresponds to the smallest surrounding circle
  of the ellipse. The actual start point of the ellipse is the
  intersection of the ellipse with the orthogonal projection of the
  corresponding circle point onto the main axis. To create a
  closed circle or ellipse the value of the parameter *"start_phi"* is
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
  specifies the angle at the end point of a circular or elliptic arc.
  For an ellipse, the angle at the end point
  is measured relative to the positive main axis
  and corresponds to the smallest surrounding circle
  of the ellipse. The actual end point of the ellipse is the
  intersection of the ellipse with the orthogonal projection of the
  corresponding circle point onto the main axis.
  To create a closed circle or ellipse the value of the parameter
  *"start_phi"*
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
  of the circular or elliptic arc. For the value *"positive"*,
  the arc is defined between *"start_phi"* and *"end_phi"*
  in mathematically positive direction (counterclockwise).
  For the value *"negative"*, the arc is defined
  between *"start_phi"* and *"end_phi"* in
  mathematically negative direction (clockwise).

  List of values:
   *"positive"*, *"negative"*

  Default:
   *"positive"*

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

**`shape`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Type of the metrology object to be added.

Default:
"circle"

List of values:
"circle", "ellipse", "line", "rectangle2"

**`shapeParam`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long)

Parameters of the metrology object to be added.

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
measureLength1
≤
511.0` (lin)

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
measureLength2
≤
511.0` (lin)

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
100` (lin)

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
create_metrology_model (MetrologyHandle)
read_image (Image, 'fabrik')
get_image_size (Image, Width, Height)
set_metrology_model_image_size (MetrologyHandle, Width, Height)
LinePar := [45,360,415,360]
RectPar1 := [270,232,rad(0),30,25]
RectPar2 := [360,230,rad(0),30,25]
LinePar := [45,360,415,360]
RectPar3 := [245,320,rad(-90),70,35]
* Add two rectangles
add_metrology_object_generic (MetrologyHandle, 'rectangle2', \
                             [RectPar1,RectPar2], 20, 5, 1, 30, [], [], \
                             Indices)
* Add a rectangle and a line
add_metrology_object_generic (MetrologyHandle, ['rectangle2','line'], \
                             [RectPar3,LinePar], 20, 5, 1, 30, [], [], \
                             Index)
get_metrology_object_model_contour (Contour, MetrologyHandle, 'all', 1.5)
apply_metrology_model (Image, MetrologyHandle)
get_metrology_object_result_contour (Contour1, MetrologyHandle, 'all', \
                                    'all', 1.5)
```

## Result

If the parameters are valid, the operator
`AddMetrologyObjectGeneric` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`SetMetrologyModelImageSize`,
`SetMetrologyModelParam`

## Possible Successors

`AlignMetrologyModel`,
`ApplyMetrologyModel`,
`SetMetrologyModelParam`

## See also

`GetMetrologyObjectModelContour`

## Module

2D Metrology
