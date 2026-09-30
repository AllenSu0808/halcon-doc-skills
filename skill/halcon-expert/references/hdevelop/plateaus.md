# plateaus (Operator)

## Name

`plateaus` — Detect all gray value plateaus.

## Signature

`plateaus(Image : Plateaus : : )`

## Description

`plateaus` extracts all points from *`Image`* with a gray value
greater or equal to the gray value of its neighbors (8-neighborhood) and
returns them in *`Plateaus`*. Each maximum is returned as a separate
region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input image.

**`Plateaus`** (output_object)  region-array `→` object

Extracted plateaus as regions (one region for
each plateau).

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
  HRegionArray maxi = cres.Plateaus ();

  win.SetColored (12);
  maxi.Display (win);
  win.Click ();

  return (0);
}
```

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`

## Possible Successors

`area_center`,
`get_region_points`,
`select_shape`

## Alternatives

`plateaus_center`,
`nonmax_suppression_amp`,
`local_max`

## See also

`monotony`,
`topographic_sketch`,
`corner_response`,
`texture_laws`

## Module

Foundation
