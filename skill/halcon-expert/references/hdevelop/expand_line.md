# expand_line (Operator)

## Name

`expand_line` — Expand a region starting at a given line.

## Warning

**`expand_line` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`expand_line(Image : RegionExpand : Coordinate, ExpandType, RowColumn, Threshold : )`

## Description

`expand_line` generates a region by expansion, starting at a given line
(row or column). The expansion is terminated when the current gray value
differs by more than *`Threshold`* from the mean gray value along the
line (*`ExpandType`* = *'mean'*) or from the previously added
gray value (*`ExpandType`* = *'gradient'*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte)

Input image.

**`RegionExpand`** (output_object)  region(-array) `→` object

Extracted segments.

**`Coordinate`** (input_control)  integer `→`  (integer)

Row or column coordinate.

Default:
256

Suggested values:
16, 64, 128, 200, 256, 300, 400, 511

Restriction:
`Coordinate >= 0`

**`ExpandType`** (input_control)  string `→`  (string)

Stopping criterion.

Default:
'gradient'

List of values:
'gradient', 'mean'

**`RowColumn`** (input_control)  string `→`  (string)

Segmentation mode (row or column).

Default:
'row'

List of values:
'column', 'row'

**`Threshold`** (input_control)  number `→`  (real / integer)

Threshold for the expansion.

Default:
3.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 13.0, 17.0, 20.0, 30.0

Value range:
`0
≤
Threshold
≤
255` (lin)

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
using namespace Halcon;

int main (int argc, char *argv[])
{
  HImage   image (argv[1]),
           gauss;
  HWindow  win;

  win.SetDraw ("margin");
  win.SetColored (12);

  image.Display (win);

  gauss = image.GaussImage (5);

  HRegionArray reg = gauss.ExpandLine (100, "mean", "row", 5.0);

  reg.Display (win);
  win.Click ();

  return (0);
}
```

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`anisotropic_diffusion`,
`median_image`,
`affine_trans_image`,
`rotate_image`

## Possible Successors

`intersection`,
`opening`,
`closing`

## Alternatives

`regiongrowing_mean`,
`expand_gray`,
`expand_gray_ref`

## Module

Foundation
