# pouring (Operator)

## Name

`pouring` — Segment an image by “pouring water” over it.

## Signature

`pouring(Image : Regions : Mode, MinGray, MaxGray : )`

## Description

`pouring` regards the input image as a “mountain range.”
Larger gray values correspond to mountain peaks, while smaller gray
values correspond to valley bottoms. `pouring` segments
the input image in several steps. First, the local maxima are
extracted, i.e., pixels which either alone or in the form of an
extended plateau have larger gray values than their immediate
neighbors (in 4-neighborhood). In the next step, the maxima thus
found are the starting points for an expansion until “valley
bottoms” are reached. The expansion is done as long as there are
chains of pixels in which the gray value becomes smaller (like water
running downhill from the maxima in all directions). Again, the
4-neighborhood is used, but with a weaker condition (smaller or
equal). This means that points at valley bottoms may belong to
more than one maximum. These areas are at first not assigned to a
region, but rather are split among all competing segments in the
last step. The split is done by a uniform expansion of all involved
segments, until all ambiguous pixels were assigned. The parameter
*`Mode`* determines which steps are executed. The following
values are possible:

- ***'all'*** —

  This is the normal mode of operation. All steps of the
  segmentation are performed. The regions are assigned to maxima,
  and overlapping regions are split.
- ***'maxima'*** —

  The segmentation only extracts the local maxima of the input
  image. No corresponding regions are extracted.
- ***'regions'*** —

  The segmentation extracts the local maxima of the input image
  and the corresponding regions, which are uniquely determined.
  Areas that were assigned to more than one maximum are not
  split.

In order to prevent the algorithm from splitting a uniform
background that is different from the rest of the image, the
parameters *`MinGray`* and *`MaxGray`* determine gray
value thresholds for regions in the image that should be regarded as
background. All parts of the image having a gray value smaller
than *`MinGray`* or larger than *`MaxGray`* are
disregarded for the extraction of the maxima as well as for the
assignment of regions. For a complete segmentation of the image,
*`MinGray`* = 0 and *`MaxGray`* = 255 should be
selected. *`MinGray`* < *`MaxGray`*
must be observed.

## Execution Information

- Multithreading type: mutually exclusive (runs in parallel with other non-exclusive operators, but not with itself).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Input image.

**`Regions`** (output_object)  region-array `→` object

Segmented regions.

**`Mode`** (input_control)  string `→`  (string)

Mode of operation.

Default:
'all'

List of values:
'all', 'maxima', 'regions'

**`MinGray`** (input_control)  integer `→`  (integer)

All gray values smaller than this threshold are
disregarded.

Default:
0

Suggested values:
0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110

Value range:
`0
≤
MinGray
≤
254` (lin)

Minimum increment:
1

Recommended increment:
10

**`MaxGray`** (input_control)  integer `→`  (integer)

All gray values larger than this threshold are
disregarded.

Default:
255

Suggested values:
100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 255

Value range:
`1
≤
MaxGray
≤
255` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`MaxGray > MinGray`

## Example (HDevelop)

```
* Segment a filtered image
read_image(Image,'particle')
mean_image(Image,Mean,11,11)
pouring(Mean,Seg,'all',0,255)
dev_display(Mean)
dev_set_colored(12)
dev_display(Seg)

* Segment an image while masking the dark background
read_image(Image,'particle')
mean_image(Image,ImageMean,15,15)
pouring(Mean,Seg,'all',90,255)
dev_display(Mean)
dev_set_colored(12)
dev_display(Seg)
```

## Complexity

Let $N$ be the number of pixels in the input image and $M$
be the number of found segments, where the enclosing rectangle of the
segment $i$ contains $m_{i}$ pixels. Furthermore, let
$K_{i}$ be the number of chords in segment $i$.
Then the runtime complexity is
$$O(3\ast N+sum_{M}(3\ast m_{i})+sum_{M}(K_{i})).$$

## Result

`pouring` usually returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`mean_image`

## Alternatives

`watersheds`,
`local_max`,
`watersheds_threshold`,
`watersheds_marker`

## See also

`histo_2dim`,
`expand_region`,
`expand_gray`,
`expand_gray_ref`

## Module

Foundation
