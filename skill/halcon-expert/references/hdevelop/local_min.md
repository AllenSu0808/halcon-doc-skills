# local_min (Operator)

## Name

`local_min` — Detect all local minima in an image.

## Signature

`local_min(Image : LocalMinima : : )`

## Description

`local_min` extracts all points from *`Image`* having a gray
value smaller than the gray value of all its neighbors and returns them in
*`LocalMinima`*. The neighborhood used can be set by
`set_system(::'neighborhood',<4/8>)`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Image to be processed.

**`LocalMinima`** (output_object)  region(-array) `→` object

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

`binomial_filter`,
`gauss_filter`,
`smooth_image`

## Possible Successors

`get_region_points`,
`connection`

## Alternatives

`gray_skeleton`,
`lowlands`,
`lowlands_center`

## See also

`monotony`,
`topographic_sketch`,
`corner_response`,
`texture_laws`

## Module

Foundation
