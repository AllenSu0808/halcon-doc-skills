## Filters

List of Sections ↓

Filters are an important part of nearly every machine vision application.
They can, for instance, be used to smooth images (e.g., [`mean_image`](mean_image.md)),
extract sub-pixel precise edges (e.g., [`edges_sub_pix`](edges_sub_pix.md)) or
process the frequency domain of images (e.g., [`fft_image`](fft_image.md)).

Usually, filter operations are applied using filter masks, which are moved
across the input image pixelwise. For each pixel a new value is
calculated based on its neighborhood. The neighborhood is determined by
shape and size of the filter mask (see the scheme below).

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/ba0e06c5d291f4fe.svg) | ![figure](../assets/3fe188ecaa75f765.svg) | ![figure](../assets/e0a26119842f1f89.svg) | ![figure](../assets/ad681ba1f8d0f277.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

(1) Image with a filter mask of size 3x3 pixels (orange).
(2) For the computation of the new pixel value of the pixel located at the
center point of the mask all the pixel values within the mask are
taken into account.
(3) The mask is moved across the image pixel by pixel.
(4) In this case a median filter (see [`median_rect`](median_rect.md))
is used for the computation of the resulting image.

You can tell from the working principle of filter masks, the treatment of
pixels along the image or domain border requires special attention, as part
of the filter mask exceeds the domain.
In the following sections some consequential issues will be discussed.

### Applying Filter Masks on Reduced Image Domains

If a filter that is using a mask is applied on an image with a reduced
domain, the result along the domain boundary might be surprising because
gray values lying outside the boundary are used as input for the filter
process (see scheme below).

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/fba5a39750b0c89c.svg) | ![figure](../assets/8a7861c22d71ab42.svg) | ![figure](../assets/0b7c5b32fda5f02f.svg) | ![figure](../assets/6367672f8729098d.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

(1) Image with a region (yellow) to which the image domain shall be reduced
to.
(2) The image domain is reduced to the chosen region using
[`reduce_domain`](reduce_domain.md).
(3) For the computation of a new value for the pixel in the center of the
mask all the pixel values within the mask are taken into account.
For pixels along the domain border this also includes pixels from outside
the domain.
(4) Result image after the application of a median filter
(see [`median_rect`](median_rect.md)).

To understand this, the definition of domains in this context must be
considered: For a filter, a domain defines for which input pixels
output pixels must be calculated. But pixels outside the domain (which
lie within the image matrix) might be used for processing nevertheless.

### Problems Caused by Gray Values Outside of the Input Image Domain

Another point to notice is the handling of pixels outside the input
image domain.
The parameter *`"init_new_image"`* of [`set_system`](set_system.md) determines
how those pixels are treated. If the pixels are initialized with 0,
consecutive runs will yield identical results. Otherwise, those pixels
remain undefined.
While this enhances the program runtime, undefined pixels can differ
from system to system, for example if parallelization is activated or not.
It is merely guaranteed that the values are consistent if the program is
executed repeatedly on systems with the same configuration.
In certain cases, these 'undefined' pixels might lead to problems.
Expanding the resulting image to the full domain with
[`full_domain`](full_domain.md) will lead to artifacts appearing outside of
the former image domain.

### Problems Caused when Applying Filters Consecutively

When two or more filters are applied consecutively on the same domain, the
undefined or unexpected values (as described in the paragraphs above)
have a higher impact on the result image.
This is because with every following filter the error increases, starting
from the border to the middle. In the following, four strategies for
solving those problems are presented.

![figure](../assets/29edf838eaf2f5fa.svg)

Artifacts at the domain border after applying two consecutive filters.

1. Errors caused by undefined pixels can easily be prevented by, e.g.,
   choosing a dilated domain (see [Morphology / Region](toc_morphology_region.md)) according to
   the filter mask.
   If multiple filters are applied consecutively, the
   image domain can be dilated in advance, considering the filter sizes to
   be used. For instance, when using a cascade of rectangular filters of
   arbitrary dimensions, the width and length dimension
   $dim_{d}$ of the dilation mask can be calculated considering
   the individual filter mask dimensions $dim_{i}$ and the number
   of filter operations $n$:

   $\operatorname{dim}_{d} = \left(\sum_{i=1}^{n} \operatorname{dim}_{i}\right) - (n-1)$ ![figure](../assets/2d3128959034de59.svg).

   After the filters were applied, the image domain can be reduced to its
   original size (e.g., with [`reduce_domain`](reduce_domain.md)).
2. Another option is to set the domain exactly to the size of the
   interesting part within the image and then calling the operator
   [`expand_domain_gray`](expand_domain_gray.md) before applying a filter. This operator copies the
   pixels inside of the border to the outside of the border
   and therefore avoids errors caused by pixels that are undefined outside of
   the domain. Subsequently, the domain can again be reduced to its original
   size. This process should be repeated for every following filter operation.
   Note, however, that this option increases the runtime significantly.

   ![figure](../assets/f68faebd2cf7100d.svg)

   The result of [`expand_domain_gray`](expand_domain_gray.md) looks as if the boundary is copied
   multiple times and added at the outside.
3. If runtime is not an issue, the operator [`full_domain`](full_domain.md) can be
   called before applying the first filter to the image. That way, the whole
   image is defined as domain and undefined pixels are avoided completely.
4. Another possibility of getting an image without undefined pixels is by
   calling the operator [`crop_domain`](crop_domain.md) before applying a filter.
   The operator [`crop_domain`](crop_domain.md) crops the image to the size of the
   domain, which means that the domain then covers a complete smaller image.
   Note, however, that for the cropped image the coordinate system has changed
   in relation to the original image, which will influence all following
   applications depending on the image coordinate system (e.g., calculating the
   center of gravity).

---

#### List of Sections

- [Arithmetic](toc_filters_arithmetic.md)
- [Bit](toc_filters_bit.md)
- [Color](toc_filters_color.md)
- [Edges](toc_filters_edges.md)
- [Enhancement](toc_filters_enhancement.md)
- [FFT](toc_filters_fft.md)
- [Geometric Transformations](toc_filters_geometrictransformations.md)
- [Inpainting](toc_filters_inpainting.md)
- [Lines](toc_filters_lines.md)
- [Match](toc_filters_match.md)
- [Misc](toc_filters_misc.md)
- [Noise](toc_filters_noise.md)
- [Optical Flow](toc_filters_opticalflow.md)
- [Points](toc_filters_points.md)
- [Scene Flow](toc_filters_sceneflow.md)
- [Smoothing](toc_filters_smoothing.md)
- [Texture Inspection](toc_filters_texture.md)
- [Wiener Filter](toc_filters_wienerfilter.md)
