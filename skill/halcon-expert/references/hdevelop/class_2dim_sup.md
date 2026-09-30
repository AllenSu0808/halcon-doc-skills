# class_2dim_sup (Operator)

## Name

`class_2dim_sup` — Segment an image using two-dimensional pixel classification.

## Signature

`class_2dim_sup(ImageCol, ImageRow, FeatureSpace : RegionClass2Dim : : )`

## Description

`class_2dim_sup` classifies the points in two-channel images
using a two-dimensional feature space. For each point, two gray
values (one from each image) are used as features. The feature
space is represented by the input region. The classification is
done as follows:

A point from the input region of an image is accepted if the point
$(g_{r},g_{c})$, which is determined by the respective gray
values, is contained in the region *`FeatureSpace`*. $g_{r}$
is here a gray value from the image *`ImageRow`*, while $g_{c}$
is the corresponding gray value from *`ImageCol`*.

Let $P$ be a point with the coordinates $P=(R,C)$,
$g_{r}$ be the
gray value at position $(R,C)$ in the image *`ImageRow`*, and
$g_{c}$ be the gray value at position $(R,C)$ in the image
*`ImageCol`*. Then the point $P$ is aggregated into the
output region if
$$(g_{r},g_{c})\in\texttt{FeatureSpace}$$
$g_{r}$ is interpreted as row coordinate and $g_{c}$ as
column coordinate.

For the generation of *`FeatureSpace`*, see
[`histo_2dim`](histo_2dim.md). The feature space can be modified by
applying region transformation operators, such as [`rank_region`](rank_region.md),
[`dilation1`](dilation1.md), [`shape_trans`](shape_trans.md),
[`elliptic_axis`](elliptic_axis.md), etc., before calling
`class_2dim_sup`.

The parameters *`ImageCol`* and *`ImageRow`* must
contain an equal number of images with the same size.
The image points are taken from the intersection of the domains of
both images (see [`reduce_domain`](reduce_domain.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`ImageCol`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1)

Input image (first channel).

**`ImageRow`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1)

Input image (second channel).

**`FeatureSpace`** (input_object)  region(-array) `→` object

Region defining the feature space.

**`RegionClass2Dim`** (output_object)  region(-array) `→` object

Classified regions.

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

  HRegion   feats, cd2reg;
  HImage    image (argv[1]),
            text1, text2,
            mean1, mean2,
            histo;

  HWindow   win;
  Hlong      nc;

  if ((nc = image.CountChannels ()) != 3)
  {
    cout << argv[1] << " is not a rgb-image " << endl;
    return (-2);
  }

  image.Display (win);

  win.SetColor ("green");
  cout << "Draw the region of interrest " << endl;

  HRegion  region = win.DrawRegion ();

  text1 = image.TextureLaws ("el", 2, 5);
  mean1 = text1.MeanImage (21, 21);
  text2 = mean1.TextureLaws ("es", 2, 5);
  mean2 = text2.MeanImage (21, 21);

  histo = region.Histo2dim (mean1, mean2);
  feats = histo.Threshold (1.0, 1000000.0);

  win.SetDraw ("fill");
  win.SetColor ("red");

  feats.Display (win);

  cout << "Charakteristics area in red" << endl;

  cd2reg = mean1.Class2dimSup (mean2, feats);

  win.SetColor ("blue");
  cd2reg.Display (win);

  cout << "Result of classification in blue " << endl;
  win.Click ();
  return (0);
}
```

## Complexity

Let A be the area of the input region. Then the runtime
complexity is O(256^2 + A).

## Result

`class_2dim_sup` returns 2 (
H_MSG_TRUE)
. If all parameters are correct, the
behavior with respect to the input images and output regions can be
determined by setting the values of the flags *'no_object_result'*,
*'empty_region_result'*, and *'store_empty_region'*
with [`set_system`](set_system.md). If necessary, an exception is raised.

## Possible Predecessors

`histo_2dim`,
`threshold`,
`draw_region`,
`dilation1`,
`opening`,
`shape_trans`

## Possible Successors

`connection`,
`select_shape`,
`select_gray`

## Alternatives

`class_ndim_norm`,
`threshold`

## See also

`histo_2dim`

## Module

Foundation
