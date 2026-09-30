# LocalMin (Operator)

## Name

`LocalMin` — Detect all local minima in an image.

## Signature

`static void HOperatorSet.LocalMin(HObject image, out HObject localMinima)`

`HRegion HImage.LocalMin()`

## Description

`LocalMin` extracts all points from *`image`* having a gray
value smaller than the gray value of all its neighbors and returns them in
*`localMinima`*. The neighborhood used can be set by
`set_system(::'neighborhood',<4/8>)`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Image to be processed.

**`localMinima`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Extracted local minima as regions.

Number of elements:
LocalMinima == Image

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
  HRegionArray mins = cres.LocalMin ();

  win.SetColored (12);
  mins.Display (win);
  win.Click ();

  return (0);
}
```

## Possible Predecessors

`BinomialFilter`,
`GaussFilter`,
`SmoothImage`

## Possible Successors

`GetRegionPoints`,
`Connection`

## Alternatives

`GraySkeleton`,
`Lowlands`,
`LowlandsCenter`

## See also

`Monotony`,
`TopographicSketch`,
`CornerResponse`,
`TextureLaws`

## Module

Foundation
