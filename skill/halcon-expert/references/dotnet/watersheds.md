# Watersheds (Operator)

## Name

`Watersheds` — Extract watersheds and basins from an image.

## Signature

`static void HOperatorSet.Watersheds(HObject image, out HObject basins, out HObject watersheds)`

`HRegion HImage.Watersheds(out HRegion watersheds)`

## Description

`Watersheds` segments an image based on the topology of
the gray values. The image is interpreted as a “mountain range.”
Higher gray values correspond to “mountains,” while lower gray
values correspond to “valleys.” In the resulting mountain range
watersheds are extracted. These correspond to the bright ridges
between dark basins. On output, the parameter *`basins`*
contains these basins, while *`watersheds`* contains the
watersheds, which are at most one pixel wide.
*`watersheds`* always is a single
region per input image, while *`basins`* contains a separate
region for each basin.

It is advisable to apply a smoothing operator (e.g.,
[`BinomialFilter`](binomial_filter.md) or [`GaussFilter`](gauss_filter.md)) to the input image
before calling `Watersheds` in order to reduce the number of
output regions. A more sophisticated way to reduce the number of
output regions is to merge neighboring basins based on a threshold
criterion by using [`WatershedsThreshold`](watersheds_threshold.md) instead (for more
details please refer to the documentation of
[`WatershedsThreshold`](watersheds_threshold.md)).

## Attention

If the image contains many fine structures or is noisy, many output
regions result, and thus the runtime increases considerably.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`basins`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segmented basins.

**`watersheds`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Watersheds between the basins.

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
  HImage   image (argv[1]), gauss;
  HWindow  win;

  cout << "Gauss of original " << endl;
  gauss  = image.GaussImage (9);
  image.Display (win);

  HRegion        watersheds;
  HRegionArray   basins = gauss.Watersheds (&watersheds);

  win.SetColored (12);
  basins.Display (win);
  win.Click ();

  return (0);
}
```

## Result

`Watersheds` always returns 2 (
H_MSG_TRUE)
. The behavior with
respect to the input images and output regions can be determined by
setting the values of the flags *"no_object_result"*,
*"empty_region_result"*, and *"store_empty_region"*
with [`SetSystem`](set_system.md). If necessary, an exception is raised.

## Possible Predecessors

`BinomialFilter`,
`GaussFilter`,
`SmoothImage`,
`InvertImage`

## Possible Successors

`ExpandRegion`,
`SelectShape`,
`ReduceDomain`,
`Opening`

## Alternatives

`WatershedsThreshold`,
`Pouring`,
`WatershedsMarker`

## References

L. Vincent, P. Soille: “Watersheds in Digital Space: An Efficient
Algorithm Based on Immersion Simulations”; IEEE Transactions on Pattern
Analysis and Machine Intelligence; vol. 13, no. 6; pp. 583-598; 1991.

## Module

Foundation
