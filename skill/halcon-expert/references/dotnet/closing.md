# Closing (Operator)

## Name

`Closing` — Close a region.

## Signature

`static void HOperatorSet.Closing(HObject region, HObject structElement, out HObject regionClosing)`

`HRegion HRegion.Closing(HRegion structElement)`

## Description

A `Closing` operation is defined as a dilation followed
by a Minkowski subtraction. By applying `Closing` to a
region, larger structures remain mostly intact, while small gaps
between adjacent regions and holes smaller than
*`structElement`* are closed, and the regions' boundaries are
smoothed. All `Closing` variants share the property that
separate regions are not merged, but remain separate objects. The
position of *`structElement`* is meaningless, since a closing
operation is invariant with respect to the choice of the reference
point.

Structuring elements (*`structElement`*) can be generated
with operators such as [`GenCircle`](gen_circle.md), [`GenRectangle1`](gen_rectangle1.md),
[`GenRectangle2`](gen_rectangle2.md), [`GenEllipse`](gen_ellipse.md),
[`DrawRegion`](draw_region.md), [`GenRegionPolygon`](gen_region_polygon.md),
[`GenRegionPoints`](gen_region_points.md), etc.

## Attention

`Closing` is applied to each input region separately. If
gaps between different regions are to be closed, [`Union1`](union1.md)
or [`Union2`](union2.md) has to be called first.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be closed.

**`structElement`** (input_object)  region `→` [HRegion](HRegion.md)

Structuring element (position-invariant).

**`regionClosing`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Closed regions.

## Example (C++)

```
#include "HIOStream.h"
#if !defined(USE_IOSTREAM_H)
using namespace std;
#endif
#include "HalconCpp.h"

main()
{
  cout << "Reproduction of 'closing ()' using " << endl;
  cout << "'dilation()' and 'minkowski_sub1()'" << endl;

  HByteImage img("monkey");
  HWindow    w;

  HRegion      circ = HRegion::GenCircle (10, 10, 1.5);
  HRegionArray regs = (img >= 128).Connection();

  HRegionArray dilreg = regs.Dilation1 (circ, 1);
  HRegionArray minsub = dilreg.MinkowskiSub1 (circ, 1);

                        img.Display (w);      w.Click ();
  w.SetColor ("red");   regs.Display (w);     w.Click ();
  w.SetColor ("green"); dilreg.Display (w);   w.Click ();
  w.SetColor ("blue");  minsub.Display (w);   w.Click ();

  return(0);
}
```

## Complexity

Let F1 be the area of the input region, and F2 be the area of
the structuring element. Then the runtime complexity for one region
is:
$$O\left(2\cdot \sqrt{F1}\cdot \sqrt{F2}\right)\,.$$ ![figure](../assets/df053ef6aed1f7b1.svg)

## Result

`Closing` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`Union1`,
`Watersheds`,
`ClassNdimNorm`,
`GenCircle`,
`GenEllipse`,
`GenRectangle1`,
`GenRectangle2`,
`DrawRegion`,
`GenRegionPoints`,
`GenRegionPolygonFilled`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`ClosingCircle`

## See also

`Dilation1`,
`Erosion1`,
`Opening`,
`MinkowskiSub1`

## Module

Foundation
