# dilation_rectangle1 (Operator)

## Name

`dilation_rectangle1` — Dilate a region with a rectangular structuring element.

## Signature

`dilation_rectangle1(Region : RegionDilation : Width, Height : )`

## Description

`dilation_rectangle1` applies a dilation with a rectangular
structuring element to the input regions *`Region`*. The size
of the structuring rectangle is *`Width`* x
*`Height`*. The operator results in enlarged regions, and the
holes smaller than the rectangular mask in the interior of the
regions are closed.

`dilation_rectangle1` is a very fast operation because the
height of the rectangle enters only logarithmically into the runtime
complexity, while the width does not enter at all. This leads to
excellent runtime efficiency, even in the case of very large
rectangles (edge length > 100).

## Attention

`dilation_rectangle1` is applied to each input region
separately. If gaps between different regions are to be closed,
[`union1`](union1.md) or [`union2`](union2.md) has to be called first.

To enlarge a region by the same amount in all directions,
*`Width`* and *`Height`* must be odd. If this is not the
case, the region is dilated by a larger amount at the right or at
the bottom, respectively, than at the left or at the top.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be dilated.

**`RegionDilation`** (output_object)  region(-array) `→` object

Dilated regions.

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the structuring rectangle.

Default:
11

Suggested values:
1, 2, 3, 4, 5, 11, 15, 21, 31, 51, 71, 101, 151, 201

Value range:
`1
≤
Width
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the structuring rectangle.

Default:
11

Suggested values:
1, 2, 3, 4, 5, 11, 15, 21, 31, 51, 71, 101, 151, 201

Value range:
`1
≤
Height
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

## Example (C++)

```
#include "HIOStream.h"
#if !defined(USE_IOSTREAM_H)
using namespace std;
#endif
#include "HalconCpp.h"

main()
{
  cout << "Reproduction of 'dilation_rectangle ()'" << endl;
  cout << "First = original image " << endl;
  cout << "Blue  = after dilation " << endl;
  cout << "Red   = after segmentation " << endl;

  HByteImage img("monkey");
  HWindow    w;

  HRegionArray regs   = (img >= 220).Connection();
  HRegionArray dilreg = regs.DilationRectangle1 (2, 4);

                        img.Display (w);      w.Click ();
  w.SetColor ("blue");  dilreg.Display (w);   w.Click ();
  w.SetColor ("red");   regs.Display (w);     w.Click ();

  return(0);
}
```

## Complexity

Let F1 be the area of an input region and H be the height of the
rectangle. Then the runtime complexity for one region is:
$$O\left(\sqrt{F1 \cdot id(H)}\right) .$$ ![figure](../assets/064fbbe19d75b278.svg)

## Result

`dilation_rectangle1` returns 2 (
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
`dilation_circle`

## See also

`gen_rectangle1`,
`gen_region_polygon_filled`

## Module

Foundation
