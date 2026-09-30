# MorphHat (Operator)

## Name

`MorphHat` — Compute the union of [`BottomHat`](bottom_hat.md) and [`TopHat`](top_hat.md).

## Warning

**`MorphHat` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.MorphHat(HObject region, HObject structElement, out HObject regionMorphHat)`

`HRegion HRegion.MorphHat(HRegion structElement)`

## Description

`MorphHat` computes the union of the regions that are
removed by an [`Opening`](opening.md) operation with the regions that are
added by a [`Closing`](closing.md) operation. Hence this is the union
of the results of [`TopHat`](top_hat.md) and [`BottomHat`](bottom_hat.md).
The position of *`structElement`* does not influence the
result.

Structuring elements (*`structElement`*) can be generated
with operators such as [`GenCircle`](gen_circle.md), [`GenRectangle1`](gen_rectangle1.md),
[`GenRectangle2`](gen_rectangle2.md), [`GenEllipse`](gen_ellipse.md),
[`DrawRegion`](draw_region.md), [`GenRegionPolygon`](gen_region_polygon.md),
[`GenRegionPoints`](gen_region_points.md), etc.

## Attention

The individual regions are processed separately.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be processed.

**`structElement`** (input_object)  region `→` [HRegion](HRegion.md)

Structuring element (position-invariant).

**`regionMorphHat`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Union of top hat and bottom hat.

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
  cout << "Red   = after segmentation " << endl;
  cout << "Blue  = after erosion " << endl;

  HByteImage img("monkey");
  HWindow    w;

  HRegion      circ   = HRegion::GenCircle (10, 10, 1.5);
  HRegionArray regs   = (img >= 128).Connection();
  HRegionArray tophat = regs.TopHat (circ);
  HRegionArray bothat = regs.BottomHat (circ);
  HRegionArray unionX = tophat.Union2 (bothat);

                        img.Display (w);      w.Click ();
  w.SetColor ("red");   regs.Display (w);     w.Click ();
  w.SetColor ("blue");  tophat.Display (w);   w.Click ();
  w.SetColor ("green"); bothat.Display (w);   w.Click ();
  w.SetColor ("white"); unionX.Display (w);   w.Click ();

  return(0);
}
```

## Result

`MorphHat` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty or no input region can be set via:

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

`TopHat`,
`BottomHat`,
`Union2`

## See also

`Opening`,
`Closing`

## Module

Foundation
