# PlateausCenter (Operator)

## Name

`PlateausCenter` — Detect the centers of all gray value plateaus.

## Signature

`static void HOperatorSet.PlateausCenter(HObject image, out HObject plateaus)`

`HRegion HImage.PlateausCenter()`

## Description

`PlateausCenter` extracts all points from *`image`* with a gray
value greater or equal to the gray value of its neighbors (8-neighborhood)
and returns them in *`plateaus`*. If more than one of these points are
connected (plateau), their center of gravity is returned. Each plateau
center is returned as a separate region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input image.

**`plateaus`** (output_object)  region-array `→` [HRegion](HRegion.md)

Centers of gravity of the extracted plateaus as
regions (one region for each plateau).

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
  if (argc != 2)
  {
    cout << "Usage : " << argv[0] << " <name of image>" << endl;
    return (-1);
  }

  HImage   image (argv[1]);
  HWindow  win;

  image.Display (win);

  HImage       cres = image.CornerResponse (5, 0.04);
  HRegionArray maxi = cres.PlateausCenter ();

  win.SetColored (12);
  maxi.Display (win);
  win.Click ();

  return (0);
}
```

## Possible Predecessors

`BinomialFilter`,
`GaussFilter`,
`SmoothImage`

## Possible Successors

`AreaCenter`,
`GetRegionPoints`,
`SelectShape`

## Alternatives

`Plateaus`,
`NonmaxSuppressionAmp`,
`LocalMax`

## See also

`Monotony`,
`TopographicSketch`,
`CornerResponse`,
`TextureLaws`

## Module

Foundation
