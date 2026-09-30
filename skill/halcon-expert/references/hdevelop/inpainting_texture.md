# inpainting_texture (Operator)

## Name

`inpainting_texture` — Perform an inpainting by texture propagation.

## Signature

`inpainting_texture(Image, Region : InpaintedImage : MaskSize, SearchSize, Anisotropy, PostIteration, Smoothness : )`

## Description

The operator `inpainting_texture` is used for removing large
objects and image errors from the region *`Region`* of the
input image *`Image`*. Image blocks of side length
*`MaskSize`* are copied from the intact part of the image to
the border of the computation area, until that area has been filled
up with new gray values. This process is called image inpainting.
Hence, the computation area is also referred to as the inpainting
area and is reduced with every inserted rectangle, starting with
*`Region`*. Let the center of the current block be at the point
x. Since x is always chosen from the border of the inpainting
area the current block overlaps with the known or already filled-in
gray values. The gray value correlation with the overlapping part
of this block is used to determine which other image block fits at
the position x. As the correlation function, the sum of the
squared gray value differences is used. The image blocks that are
taken into account for the correlation, and hence as candidates for
the data source of the next inpainting step, are called comparison
blocks. The search area for suitable gray value patterns in which
the centers of the comparison blocks is searched is limited to a
square of side length 2**`SearchSize`*
around the point x.

On the one hand, the order in which the pixels of *`Region`*
are filled in depends on the size of the overlapping area and thus
the number of pixels available for the correlation. On the other
hand, the absolute value of the derivative of the gray value
function tangential to the border of the computation area is also
considered. The larger the value of the parameter
*`Anisotropy`* is, the more the points in which the derivative
is large are preferred. This way it can be achieved that, e.g.,
straight lines which are represented by large gradients, are
continued through the entire computation area without being
interrupted by the inpainting of image structures from other parts
of the border when the size of the inpainting area becomes small. On
the other hand, a large value of *`Anisotropy`* also means that
possible phantom edges, i.e., unwanted random structures that have
developed during the inpainting process, are also propagated and the
magnitude of those image disturbances is increased.

To confine the formation of such artifacts, the original algorithm
can be extended by a post-iteration step that selects smooth and
inconspicuous image patches as data sources for the inpainting. If
the parameter *`PostIteration`* is set to *'min_grad'*
the sum of the squares of the gray value gradients is minimized on
the comparison blocks. With the value
*'min_range_extension'*, the growth of the gray value
interval of the comparison blocks with respect to the reference
block around the point x is minimized. If *`PostIteration`*
has the value *'none'* no post-iteration is performed. The
choice of feasible blocks for this minimization process is
determined by the parameter *`Smoothness`*, which is an upper
limit to the permitted increase of the mean absolute gray value
difference between the comparison blocks and the reference block
with respect to the block that was selected by the original
algorithm. With increasing value of *`Smoothness`*, the
inpainting result becomes smoother and loses structure. The matching
accuracy of the selected comparison blocks decreases. If
*`Smoothness`* is set to *0*, the post-iteration only
considers comparison blocks with an equally high correlation to the
reference block.

If the inpainting process cannot be completed because there are
points x, for which no complete block of intact gray value
information is contained in the search area of size
*`SearchSize`*, the remaining pixels keep their initial gray
value and the ROI of the output image *`InpaintedImage`* is
reduced by the region that could not be processed. If the structure
size of the ROI of *`Image`* or of the computation area
*`Region`* is smaller than *`MaskSize`*, the execution
time of the algorithm can increase extremely. Hence, it is
recommended to only use clearly structured input regions.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Input image.

**`Region`** (input_object)  region `→` object

Inpainting region.

**`InpaintedImage`** (output_object)  image(-array) `→` object (byte / uint2 / real)

Output image.

**`MaskSize`** (input_control)  integer `→`  (integer)

Size of the inpainting blocks.

Default:
9

Suggested values:
7, 9, 11, 15, 21

Restriction:
`MaskSize >= 3 && odd(MaskSize)`

**`SearchSize`** (input_control)  integer `→`  (integer)

Size of the search window.

Default:
30

Suggested values:
15, 30, 50, 100, 1000

Restriction:
`2 * SearchSize > MaskSize`

**`Anisotropy`** (input_control)  real `→`  (real)

Influence of the edge amplitude on the
inpainting order.

Default:
1.0

Suggested values:
0.0, 0.01, 0.1, 0.5, 1.0, 10.0

Restriction:
`Anisotropy >= 0`

**`PostIteration`** (input_control)  string `→`  (string)

Post-iteration for artifact reduction.

Default:
'none'

List of values:
'min_grad', 'min_range_extension', 'none'

**`Smoothness`** (input_control)  real `→`  (real)

Gray value tolerance for post-iteration.

Default:
1.0

Suggested values:
0.0, 0.1, 0.2, 0.5, 1.0

Restriction:
`Smoothness >= 0`

## Module

Foundation
