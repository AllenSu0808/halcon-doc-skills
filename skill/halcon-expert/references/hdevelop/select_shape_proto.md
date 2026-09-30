# select_shape_proto (Operator)

## Name

`select_shape_proto` — Choose regions having a certain relation to each other.

## Signature

`select_shape_proto(Regions, Pattern : SelectedRegions : Feature, Min, Max : )`

## Description

The operator `select_shape_proto` selects regions based on
certain relations between the regions. Every region from
*`Regions`* is compared to the union of regions from
*`Pattern`*. The limits (*`Min`* and *`Max`*) are
specified absolutely or in percent (0..100), depending on the
feature. Possible values for *`Feature`* are:

- ***'distance_dilate'*** —

  The minimum distance in the maximum norm from the edge of
  *`Pattern`* to the edge of every region from *`Regions`*
  is determined (see [`distance_rr_min_dil`](distance_rr_min_dil.md)).
- ***'distance_contour'*** —

  The minimum Euclidean distance from the edge of *`Pattern`* to
  the edge of every region from *`Regions`* is determined. (see
  [`distance_rr_min`](distance_rr_min.md)).
- ***'distance_center'*** —

  The Euclidean distance from the center of *`Pattern`* to the
  center of every region from *`Regions`* is determined.
- ***'covers'*** —

  It is examined how well the region *`Pattern`* fits into the
  regions from *`Regions`*. If there is no shift so that
  *`Pattern`* is a subset of *`Regions`* the overlap is 0.
  If *`Pattern`* corresponds to the region after a corresponding
  shift the overlap is 100. Otherwise the area of the opening of
  *`Regions`* with *`Pattern`* is put into relation with the
  area of *`Regions`* (in percent).
- ***'fits'*** —

  It is examined whether *`Pattern`* can be shifted in such a way
  that it fits in *`Regions`*. If this is possible the
  corresponding region is copied from *`Regions`*. The
  parameters *`Min`* and *`Max`* are ignored.
- ***'overlaps_abs'*** —

  The area of the intersection of *`Pattern`* and every region in
  *`Regions`* is computed.
- ***'overlaps_rel'*** —

  The area of the intersection of *`Pattern`* and every region in
  *`Regions`* is computed. The relative overlap is the ratio of
  the area of the intersection, and the area of the respective region in
  *`Regions`* (in percent).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions to be examined.

**`Pattern`** (input_object)  region(-array) `→` object

Region compared to *`Regions`*.

**`SelectedRegions`** (output_object)  region(-array) `→` object

Regions fulfilling the condition.

**`Feature`** (input_control)  string(-array) `→`  (string)

Shape features to be checked.

Default:
'covers'

List of values:
'covers', 'distance_center', 'distance_contour', 'distance_dilate', 'fits', 'overlaps_abs', 'overlaps_rel'

**`Min`** (input_control)  number `→`  (real / integer)

Lower border of feature.

Default:
50.0

Suggested values:
0.0, 1.0, 5.0, 10.0, 20.0, 30.0, 50.0, 60.0, 70.0, 80.0, 90.0, 95.0, 99.0, 100.0, 200.0, 400.0

Value range:
`0.0
≤
Min`

Minimum increment:
0.001

Recommended increment:
5.0

**`Max`** (input_control)  number `→`  (real / integer)

Upper border of the feature.

Default:
100.0

Suggested values:
0.0, 10.0, 20.0, 30.0, 50.0, 60.0, 70.0, 80.0, 90.0, 95.0, 99.0, 100.0, 200.0, 300.0, 400.0

Value range:
`0.0
≤
Max`

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
