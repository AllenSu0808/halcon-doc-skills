# SelectShapeProto (Operator)

## Name

`SelectShapeProto` — Choose regions having a certain relation to each other.

## Signature

`static void HOperatorSet.SelectShapeProto(HObject regions, HObject pattern, out HObject selectedRegions, HTuple feature, HTuple min, HTuple max)`

`HRegion HRegion.SelectShapeProto(HRegion pattern, HTuple feature, HTuple min, HTuple max)`

`HRegion HRegion.SelectShapeProto(HRegion pattern, string feature, double min, double max)`

## Description

The operator `SelectShapeProto` selects regions based on
certain relations between the regions. Every region from
*`regions`* is compared to the union of regions from
*`pattern`*. The limits (*`min`* and *`max`*) are
specified absolutely or in percent (0..100), depending on the
feature. Possible values for *`feature`* are:

- ***"distance_dilate"*** —

  The minimum distance in the maximum norm from the edge of
  *`pattern`* to the edge of every region from *`regions`*
  is determined (see [`DistanceRrMinDil`](distance_rr_min_dil.md)).
- ***"distance_contour"*** —

  The minimum Euclidean distance from the edge of *`pattern`* to
  the edge of every region from *`regions`* is determined. (see
  [`DistanceRrMin`](distance_rr_min.md)).
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

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`pattern`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region compared to *`regions`*.

**`selectedRegions`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Regions fulfilling the condition.

**`feature`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Shape features to be checked.

Default:
"covers"

List of values:
"covers", "distance_center", "distance_contour", "distance_dilate", "fits", "overlaps_abs", "overlaps_rel"

**`min`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`max`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

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

## Example (C++)

```
#include "HIOStream.h"
#if !defined(USE_IOSTREAM_H)
using namespace std;
#endif
#include "HalconCpp.h"
using namespace Halcon;

int main (int argc, char *argv[])
{
  if (argc < 2)
  {
    cout << "Usage: " << argv[0] << " <radius of circle>" << endl;
    exit (1);
  }

  double   rad = atof (argv[1]);
  HImage   img ("monkey");
  HWindow  w;

  img.Display (w);

  HRegion       circ = HRegion::GenCircle (100, 100, rad);
  HRegionArray  reg  = img.Regiongrowing (3, 3, 5, 0);
  HRegionArray  seg  = reg.SelectShapeProto (circ, "fits", 0, 0);

  w.SetColor  ("red");
  seg.Display (w);
  w.Click ();
  return(0);
}
```

## Result

The operator `SelectShapeProto` returns the value 2 (
H_MSG_TRUE)
if
the input is not empty. The behavior in case of empty input (no
input regions available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`Connection`,
`DrawRegion`,
`GenCircle`,
`GenRectangle1`,
`GenRectangle2`,
`GenEllipse`

## Possible Successors

`SelectGray`,
`ShapeTrans`,
`ReduceDomain`,
`CountObj`

## Alternatives

`SelectShape`

## See also

`Opening`,
`Erosion1`,
`DistanceRrMinDil`,
`DistanceRrMin`

## Module

Foundation
