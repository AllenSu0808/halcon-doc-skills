# dilation_circle (Operator)

## Name

`dilation_circle` — Dilate a region with a circular structuring element.

## Signature

`dilation_circle(Region : RegionDilation : Radius : )`

## Description

`dilation_circle` applies a Minkowski addition with a
circular structuring element to the input regions *`Region`*.
Because the circular mask is symmetrical, this is identical to a
dilation. The size of the circle used as structuring element is
determined by *`Radius`*.

The operator results in enlarged regions, smoothed
region boundaries, and the holes smaller than the
circular mask in the interior of the region are closed. It is useful to select
only values like 3.5, 5.5, etc. for *`Radius`* in order
to avoid a translation of a region, because integer radii result in
the circle having a non-integer center of gravity which is rounded
to the next integer.

## Attention

`dilation_circle` is applied to each input region
separately. If gaps between different regions are to be closed,
[`union1`](union1.md) or [`union2`](union2.md) has to be called first.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be dilated.

**`RegionDilation`** (output_object)  region(-array) `→` object

Dilated regions.

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
  cout << "Reproduction of 'dilation_circle ()'" << endl;
  cout << "First = original image " << endl;
  cout << "Blue  = after dilation " << endl;
  cout << "Red   = before dilation " << endl;

  HByteImage img("monkey");
  HWindow    w;

  HRegion      circ   = HRegion::GenCircle (10, 10, 1.5);
  HRegionArray regs   = (img >= 128).Connection();
  HRegionArray minadd = regs.MinkowskiAdd1 (circ, 1);

                        img.Display (w);      w.Click ();
  w.SetColor ("blue");  minadd.Display (w);   w.Click ();
  w.SetColor ("red");   regs.Display (w);     w.Click ();

  return(0);
}
```

## Complexity

Let F1 be the area of an input region. Then the runtime complexity for one
region is:
$$O(2 \cdot Radius \cdot \sqrt{F1})$$ ![figure](../assets/562af9267be98e4a.svg)

## Result

`dilation_circle` returns 2 (
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
`connection`,
`union1`,
`watersheds`,
`class_ndim_norm`

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`minkowski_add1`,
`minkowski_add2`,
`expand_region`,
`dilation1`,
`dilation2`,
`dilation_rectangle1`

## See also

`gen_circle`,
`erosion_circle`,
`closing_circle`,
`opening_circle`

## Module

Foundation
