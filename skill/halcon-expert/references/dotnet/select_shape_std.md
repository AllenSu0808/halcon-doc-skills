# SelectShapeStd (Operator)

## Name

`SelectShapeStd` — Select regions of a given shape.

## Signature

`static void HOperatorSet.SelectShapeStd(HObject regions, out HObject selectedRegions, HTuple shape, HTuple percent)`

`HRegion HRegion.SelectShapeStd(string shape, double percent)`

## Description

The operator `SelectShapeStd` compares the shape of the
given regions with default shapes. If the region has a similar shape
it is adopted into the output. Possible values for *`shape`*
are:

- ***"max_area"*** —

  The largest region is selected.
- ***"rectangle1"*** —

  The surrounding rectangle parallel to the coordinate axes is
  determined via the operator [`SmallestRectangle1`](smallest_rectangle1.md). If the
  area difference in percent
  is larger than *`percent`* the region is adopted.
- ***"rectangle2"*** —

  The smallest surrounding rectangle with any orientation is
  determined via the operator [`SmallestRectangle2`](smallest_rectangle2.md). If the
  area difference in percent
  is larger than *`percent`* the region is adopted. Note that as a more
  robust alternative the operator [`SelectShape`](select_shape.md) with `feature`
  set to *"rectangularity"* can be used instead.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input regions to be selected.

**`selectedRegions`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Regions with desired shape.

**`shape`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Shape features to be checked.

Default:
"max_area"

List of values:
"max_area", "rectangle1", "rectangle2"

**`percent`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Similarity measure.

Default:
70.0

Suggested values:
10.0, 30.0, 50.0, 60.0, 70.0, 80.0, 90.0, 95.0, 100.0

Value range:
`0.0
≤
percent
≤
100.0` (lin)

Minimum increment:
0.1

Recommended increment:
10.0

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`SmallestRectangle1`,
`SmallestRectangle2`

## Alternatives

`Intersection`,
`Complement`,
`AreaCenter`,
`SelectShape`

## See also

`SmallestRectangle1`,
`SmallestRectangle2`,
`Rectangularity`

## Module

Foundation
