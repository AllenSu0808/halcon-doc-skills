# local_max (Operator)

## Name

`local_max` — Detect all local maxima in an image.

## Signature

`local_max(Image : LocalMaxima : : )`

## Description

`local_max` extracts all points from *`Image`* having a gray
value larger than the gray value of all its neighbors and returns them in
*`LocalMaxima`*. The neighborhood used can be set by
`set_system(::'neighborhood',<4/8>)`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Input image.

**`LocalMaxima`** (output_object)  region(-array) `→` object

Extracted local maxima as a region.

Number of elements:
LocalMaxima == Image

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
  using namespace Halcon;
  if (argc != 2)
  {
    cout << "Usage : " << argv[0] << " <name of image>" << endl;
    return (-1);
  }

  HImage   image (argv[1]);
  HWindow  win;

  image.Display (win);

  HImage       cres = image.CornerResponse (5, 0.04);
  HRegionArray maxi = cres.LocalMax ();

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

`get_region_points`,
`connection`

## Alternatives

`nonmax_suppression_amp`,
`plateaus`,
`plateaus_center`

## See also

`monotony`,
`topographic_sketch`,
`corner_response`,
`texture_laws`

## Module

Foundation
