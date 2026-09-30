# closing (Operator)

## Name

`closing` — Close a region.

## Signature

`closing(Region, StructElement : RegionClosing : : )`

## Description

A `closing` operation is defined as a dilation followed
by a Minkowski subtraction. By applying `closing` to a
region, larger structures remain mostly intact, while small gaps
between adjacent regions and holes smaller than
*`StructElement`* are closed, and the regions' boundaries are
smoothed. All `closing` variants share the property that
separate regions are not merged, but remain separate objects. The
position of *`StructElement`* is meaningless, since a closing
operation is invariant with respect to the choice of the reference
point.

Structuring elements (*`StructElement`*) can be generated
with operators such as [`gen_circle`](gen_circle.md), [`gen_rectangle1`](gen_rectangle1.md),
[`gen_rectangle2`](gen_rectangle2.md), [`gen_ellipse`](gen_ellipse.md),
[`draw_region`](draw_region.md), [`gen_region_polygon`](gen_region_polygon.md),
[`gen_region_points`](gen_region_points.md), etc.

## Attention

`closing` is applied to each input region separately. If
gaps between different regions are to be closed, [`union1`](union1.md)
or [`union2`](union2.md) has to be called first.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be closed.

**`StructElement`** (input_object)  region `→` object

Structuring element (position-invariant).

**`RegionClosing`** (output_object)  region(-array) `→` object

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

`closing` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty or no input region can be set via:

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
`class_ndim_norm`,
`gen_circle`,
`gen_ellipse`,
`gen_rectangle1`,
`gen_rectangle2`,
`draw_region`,
`gen_region_points`,
`gen_region_polygon_filled`

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`closing_circle`

## See also

`dilation1`,
`erosion1`,
`opening`,
`minkowski_sub1`

## Module

Foundation
