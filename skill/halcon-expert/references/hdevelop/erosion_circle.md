# erosion_circle (Operator)

## Name

`erosion_circle` — Erode a region with a circular structuring element.

## Signature

`erosion_circle(Region : RegionErosion : Radius : )`

## Description

`erosion_circle` applies a Minkowski subtraction with a
circular structuring element to the input regions *`Region`*.
Because the circular mask is symmetrical, this is identical to an
erosion. The size of the circle used as structuring element is
determined by *`Radius`*.

The operator results in reduced regions, smoothed region boundaries,
and the regions smaller than the circular mask are eliminated.
It is useful to select only values like 3.5,
5.5, etc. for *`Radius`* in order to avoid a translation
of a region, because integer radii result in a circle having a
non-integer center of gravity which is rounded to the next integer.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be eroded.

**`RegionErosion`** (output_object)  region(-array) `→` object

Eroded regions.

**`Radius`** (input_control)  real `→`  (real / integer)

Radius of the circular structuring element.

Default:
3.5

Suggested values:
1.5, 2.5, 3.5, 4.5, 5.5, 7.5, 9.5, 12.5, 15.5, 19.5, 25.5, 33.5, 45.5, 60.5, 110.5

Value range:
`0.5
≤
Radius
≤
511.5` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

## Example (C++)

```
#include "HIOStream.h"
#if !defined(USE_IOSTREAM_H)
using namespace std;
#endif
#include "HalconCpp.h"

main()
{
  cout << "Simulation of 'erosion_circle ()'" << endl;
  cout << "First = original image " << endl;
  cout << "Red   = after segmentation " << endl;
  cout << "Blue  = after erosion " << endl;

  HByteImage img("monkey");
  HWindow    w;

  HRegion      circ   = HRegion::GenCircle (10, 10, 1.5);
  HRegionArray regs   = (img >= 128).Connection();
  HRegionArray minsub = regs.MinkowskiSub1 (circ, 1);

                         img.Display (w);      w.Click ();
  w.SetColor ("red");   regs.Display (w);     w.Click ();
  w.SetColor ("blue");  minsub.Display (w);   w.Click ();

  return(0);
}
```

## Complexity

Let F1 be the area of an input region. Then the runtime complexity for one
region is:
$$O(2 \cdot Radius \cdot \sqrt{F1})$$ ![figure](../assets/562af9267be98e4a.svg)

## Result

`erosion_circle` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty or no input region can be
set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`watersheds`,
`class_ndim_norm`

## Possible Successors

`connection`,
`reduce_domain`,
`select_shape`,
`area_center`

## Alternatives

`minkowski_sub1`

## See also

`gen_circle`,
`dilation_circle`,
`closing_circle`,
`opening_circle`

## Module

Foundation
