# ExpandGrayRef (Operator)

## Name

`ExpandGrayRef` — Fill gaps between regions (depending on gray value or color) or split
overlapping regions.

## Signature

`static void HOperatorSet.ExpandGrayRef(HObject regions, HObject image, HObject forbiddenArea, out HObject regionExpand, HTuple iterations, HTuple mode, HTuple refGray, HTuple threshold)`

`HRegion HImage.ExpandGrayRef(HRegion regions, HRegion forbiddenArea, HTuple iterations, string mode, HTuple refGray, HTuple threshold)`

`HRegion HImage.ExpandGrayRef(HRegion regions, HRegion forbiddenArea, string iterations, string mode, int refGray, int threshold)`

`HRegion HRegion.ExpandGrayRef(HImage image, HRegion forbiddenArea, HTuple iterations, string mode, HTuple refGray, HTuple threshold)`

`HRegion HRegion.ExpandGrayRef(HImage image, HRegion forbiddenArea, string iterations, string mode, int refGray, int threshold)`

## Description

`ExpandGrayRef` closes gaps between the input regions,
which resulted from the suppression of small regions in a
segmentation operator, (mode *"image"*), for example, or
separates overlapping regions *"region"*). Both uses result
from the expansion of regions. The operator works by adding a one
pixel wide “strip” to a region, in which the gray values or color
are different from a reference gray value or color by at most
*`threshold`* (in each channel). For images of type
*"cyclic"* (e.g., direction images), also points with a gray
value difference of at least 255 - *`threshold`* are added
to the output region.

The expansion takes place only in regions, which are designated as
not “forbidden” (parameter *`forbiddenArea`*). The number
of iterations is determined by the parameter *`iterations`*.
By passing *"maximal"*, `ExpandGrayRef` iterates
until convergence, i.e., until no more changes occur. By passing 0
for this parameter, all non-overlapping regions are returned. The
two modes of operation (*"image"* and *"region"*)
are different in the following ways:

- ***"image"*** —

  The input regions are expanded iteratively until they
  touch another region or the image border, or the expansion
  stops because of too high gray value differences. Because
  `ExpandGrayRef` processes all regions
  simultaneously, gaps between regions are distributed
  evenly to all regions with a similar gray value.
  Overlapping regions are split by distributing the area of
  overlap evenly to both regions.
- ***"region"*** —

  No expansion of the input regions is performed. Instead,
  only overlapping regions are split by distributing the
  area of overlap evenly to regions having a matching gray
  value or color.

## Attention

Because regions are only expanded into areas having a matching gray
value or color, usually gaps will remain between the output regions,
i.e., the segmentation is not complete.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions for which the gaps are to be closed, or which
are to be separated.

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / cyclic)

Image (possibly multi-channel) for gray value or color
comparison.

**`forbiddenArea`** (input_object)  region `→` [HRegion](HRegion.md)

Regions in which no expansion takes place.

**`regionExpand`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Expanded or separated regions.

**`iterations`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Number of iterations.

Default:
"maximal"

Suggested values:
"maximal", 1, 2, 3, 4, 5, 7, 10, 15, 20, 30, 50, 70, 100, 150, 200, 300, 500

Value range:
`1
≤
iterations
≤
500` (lin)

Minimum increment:
1

Recommended increment:
1

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Expansion mode.

Default:
"image"

List of values:
"image", "region"

**`refGray`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Reference gray value or color for comparison.

Default:
128

Suggested values:
1, 10, 20, 50, 100, 128, 200, 255

Value range:
`1
≤
refGray
≤
255` (lin)

Minimum increment:
1

Recommended increment:
10

**`threshold`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Maximum difference between the reference gray value
or color and a candidate for expansion.

Default:
32

Suggested values:
4, 10, 15, 20, 25, 30, 40

Value range:
`1
≤
threshold
≤
255` (lin)

Minimum increment:
1

Recommended increment:
5

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
  HImage   image (argv[1]);
  HRegion  empty_region;
  HWindow  win;

  win.SetDraw ("margin");
  win.SetColored (12);

  image.Display (win);

  HRegionArray seg = (image >= 100).Connection ();
  seg.Display (win);

  Tuple iter = "maximal";
  Tuple mode = "image";
  Tuple refg = 128;
  Tuple thrs = 32;

  HRegionArray exp = seg.ExpandGrayRef (image, empty_region,
                                        iter, mode, refg, thrs);
  exp.Display (win);
  win.Click ();

  return (0);
}
```

## Result

`ExpandGrayRef` always returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`,
the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`,
and the behavior in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Connection`,
`Regiongrowing`,
`Pouring`,
`ClassNdimNorm`

## Possible Successors

`SelectShape`

## See also

`ExpandGray`,
`ExpandRegion`

## Module

Foundation
