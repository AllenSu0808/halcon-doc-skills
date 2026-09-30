# Class2dimUnsup (Operator)

## Name

`Class2dimUnsup` — Segment two images by clustering.

## Signature

`static void HOperatorSet.Class2dimUnsup(HObject image1, HObject image2, out HObject classes, HTuple threshold, HTuple numClasses)`

`HRegion HImage.Class2dimUnsup(HImage image2, int threshold, int numClasses)`

## Description

`Class2dimUnsup` performs a classification with two
single-channel images. First, a two-dimensional histogram of the two
images is computed ([`Histo2dim`](histo_2dim.md)). In this histogram,
the first maximum is extracted; it serves as the first cluster
center. The histogram is computed with the intersection of the
domains of both images (see [`ReduceDomain`](reduce_domain.md)). After this,
all pixels in the images that are at most *`threshold`*
pixels from the cluster center in the maximum norm, are determined.
These pixels form one output region. Next, the pixels thus
classified are deleted from the histogram so that they are not taken
into account for the next class. In this modified histogram, again
the maximum is extracted; it again serves as a cluster center. The
above steps are repeated *`numClasses`* times; thus,
*`numClasses`* output regions result. Only pixels defined in
both images are returned.

## Attention

Both input images must have the same size.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image1`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

First input image.

**`image2`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Second input image.

**`classes`** (output_object)  region-array `→` [HRegion](HRegion.md)

Classification result.

**`threshold`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Threshold (maximum distance to the cluster's center).

Default:
15

Suggested values:
0, 2, 5, 8, 12, 17, 20, 30, 50, 70

**`numClasses`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of classes (cluster centers).

Default:
5

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 30, 40, 50

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
    cout << "Usage : " << argv[0] << " 'image' " << endl;
    return (-1);
  }

  HImage   colimg (argv[1]),
           green, blue;

  HWindow  w;
  Hlong     nc;

  if ((nc = colimg.CountChannels ()) != 3)
  {
    cout << argv[1] << " is not a rgb-image " << endl;
    return (-2);
  }

  colimg.Display (w);

  HImage        red = colimg.Decompose3 (&green, &blue);
  HRegionArray  seg = red.Class2dimUnsup (green, 15, 5);

  w.SetDraw ("margin");
  w.SetColored (12);
  seg.Display (w);
  w.Click ();

  return (0);
}
```

## Result

`Class2dimUnsup` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior with respect to the input images and output regions
can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`Decompose2`,
`Decompose3`,
`MedianImage`,
`AnisotropicDiffusion`,
`ReduceDomain`

## Possible Successors

`SelectShape`,
`SelectGray`,
`Connection`

## Alternatives

`Threshold`,
`Histo2dim`,
`Class2dimSup`,
`ClassNdimNorm`

## Module

Foundation
