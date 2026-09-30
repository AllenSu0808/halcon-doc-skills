# select_shape_proto (Operator)

## Name

`select_shape_proto` — Choose regions having a certain relation to each other.

## Signature

`def select_shape_proto(regions: HObject, pattern: HObject, feature: MaybeSequence[str], min: Union[int, float], max: Union[int, float]) -> HObject`

## Description

The operator `select_shape_proto` selects regions based on
certain relations between the regions. Every region from
*`regions`* is compared to the union of regions from
*`pattern`*. The limits (*`min`* and *`max`*) are
specified absolutely or in percent (0..100), depending on the
feature. Possible values for *`feature`* are:

- ***"distance_dilate"*** —

  The minimum distance in the maximum norm from the edge of
  *`pattern`* to the edge of every region from *`regions`*
  is determined (see [`distance_rr_min_dil`](distance_rr_min_dil.md)).
- ***"distance_contour"*** —

  The minimum Euclidean distance from the edge of *`pattern`* to
  the edge of every region from *`regions`* is determined. (see
  [`distance_rr_min`](distance_rr_min.md)).
- ***"distance_center"*** —

  The Euclidean distance from the center of *`pattern`* to the
  center of every region from *`regions`* is determined.
- ***"covers"*** —

  It is examined how well the region *`pattern`* fits into the
  regions from *`regions`*. If there is no shift so that
  *`pattern`* is a subset of *`regions`* the overlap is 0.
  If *`pattern`* corresponds to the region after a corresponding
  shift the overlap is 100. Otherwise the area of the opening of
  *`regions`* with *`pattern`* is put into relation with the
  area of *`regions`* (in percent).
- ***"fits"*** —

  It is examined whether *`pattern`* can be shifted in such a way
  that it fits in *`regions`*. If this is possible the
  corresponding region is copied from *`regions`*. The
  parameters *`min`* and *`max`* are ignored.
- ***"overlaps_abs"*** —

  The area of the intersection of *`pattern`* and every region in
  *`regions`* is computed.
- ***"overlaps_rel"*** —

  The area of the intersection of *`pattern`* and every region in
  *`regions`* is computed. The relative overlap is the ratio of
  the area of the intersection, and the area of the respective region in
  *`regions`* (in percent).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions to be examined.

**`pattern`** (input_object)  region(-array) `→` HObject

Region compared to *`regions`*.

**`selected_regions`** (output_object)  region(-array) `→` HObject

Regions fulfilling the condition.

**`feature`** (input_control)  string(-array) `→` MaybeSequence[str]

Shape features to be checked.

Default:
"covers"

List of values:
"covers", "distance_center", "distance_contour", "distance_dilate", "fits", "overlaps_abs", "overlaps_rel"

**`min`** (input_control)  number `→` Union[int, float]

Lower border of feature.

Default:
50.0

Suggested values:
0.0, 1.0, 5.0, 10.0, 20.0, 30.0, 50.0, 60.0, 70.0, 80.0, 90.0, 95.0, 99.0, 100.0, 200.0, 400.0

Value range:
`0.0
≤
min`

Minimum increment:
0.001

Recommended increment:
5.0

**`max`** (input_control)  number `→` Union[int, float]

Upper border of the feature.

Default:
100.0

Suggested values:
0.0, 10.0, 20.0, 30.0, 50.0, 60.0, 70.0, 80.0, 90.0, 95.0, 99.0, 100.0, 200.0, 300.0, 400.0

Value range:
`0.0
≤
max`

Minimum increment:
0.001

Recommended increment:
5.0

## Result

The operator `select_shape_proto` returns the value 2 (
H_MSG_TRUE)
if
the input is not empty. The behavior in case of empty input (no
input regions available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`connection`,
`draw_region`,
`gen_circle`,
`gen_rectangle1`,
`gen_rectangle2`,
`gen_ellipse`

## Possible Successors

`select_gray`,
`shape_trans`,
`reduce_domain`,
`count_obj`

## Alternatives

`select_shape`

## See also

`opening`,
`erosion1`,
`distance_rr_min_dil`,
`distance_rr_min`

## Module

Foundation
