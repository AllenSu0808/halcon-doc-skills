# select_shape_std (Operator)

## Name

`select_shape_std` — Select regions of a given shape.

## Signature

`select_shape_std(Regions : SelectedRegions : Shape, Percent : )`

## Description

The operator `select_shape_std` compares the shape of the
given regions with default shapes. If the region has a similar shape
it is adopted into the output. Possible values for *`Shape`*
are:

- ***'max_area'*** —

  The largest region is selected.
- ***'rectangle1'*** —

  The surrounding rectangle parallel to the coordinate axes is
  determined via the operator [`smallest_rectangle1`](smallest_rectangle1.md). If the
  area difference in percent
  is larger than *`Percent`* the region is adopted.
- ***'rectangle2'*** —

  The smallest surrounding rectangle with any orientation is
  determined via the operator [`smallest_rectangle2`](smallest_rectangle2.md). If the
  area difference in percent
  is larger than *`Percent`* the region is adopted. Note that as a more
  robust alternative the operator [`select_shape`](select_shape.md) with `Feature`
  set to *'rectangularity'* can be used instead.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Input regions to be selected.

**`SelectedRegions`** (output_object)  region(-array) `→` object

Regions with desired shape.

**`Shape`** (input_control)  string `→`  (string)

Shape features to be checked.

Default:
'max_area'

List of values:
'max_area', 'rectangle1', 'rectangle2'

**`Percent`** (input_control)  real `→`  (real)

Similarity measure.

Default:
70.0

Suggested values:
10.0, 30.0, 50.0, 60.0, 70.0, 80.0, 90.0, 95.0, 100.0

Value range:
`0.0
≤
Percent
≤
100.0` (lin)

Minimum increment:
0.1

Recommended increment:
10.0

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`smallest_rectangle1`,
`smallest_rectangle2`

## Alternatives

`intersection`,
`complement`,
`area_center`,
`select_shape`

## See also

`smallest_rectangle1`,
`smallest_rectangle2`,
`rectangularity`

## Module

Foundation
