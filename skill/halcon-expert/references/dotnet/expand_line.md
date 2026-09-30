# ExpandLine (Operator)

## Name

`ExpandLine` — Expand a region starting at a given line.

## Warning

**`ExpandLine` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.ExpandLine(HObject image, out HObject regionExpand, HTuple coordinate, HTuple expandType, HTuple rowColumn, HTuple threshold)`

`HRegion HImage.ExpandLine(int coordinate, string expandType, string rowColumn, HTuple threshold)`

`HRegion HImage.ExpandLine(int coordinate, string expandType, string rowColumn, double threshold)`

## Description

`ExpandLine` generates a region by expansion, starting at a given line
(row or column). The expansion is terminated when the current gray value
differs by more than *`threshold`* from the mean gray value along the
line (*`expandType`* = *"mean"*) or from the previously added
gray value (*`expandType`* = *"gradient"*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Input image.

**`regionExpand`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Extracted segments.

**`coordinate`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Row or column coordinate.

Default:
256

Suggested values:
16, 64, 128, 200, 256, 300, 400, 511

Restriction:
`Coordinate >= 0`

**`expandType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Stopping criterion.

Default:
"gradient"

List of values:
"gradient", "mean"

**`rowColumn`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Segmentation mode (row or column).

Default:
"row"

List of values:
"column", "row"

**`threshold`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Threshold for the expansion.

Default:
3.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 13.0, 17.0, 20.0, 30.0

Value range:
`0
≤
threshold
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

`BinomialFilter`,
`GaussFilter`,
`SmoothImage`,
`AnisotropicDiffusion`,
`MedianImage`,
`AffineTransImage`,
`RotateImage`

## Possible Successors

`Intersection`,
`Opening`,
`Closing`

## Alternatives

`RegiongrowingMean`,
`ExpandGray`,
`ExpandGrayRef`

## Module

Foundation
