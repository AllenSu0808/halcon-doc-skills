# equ_histo_image (Operator)

## Name

`equ_histo_image` — Histogram linearization of images

## Signature

`def equ_histo_image(image: HObject) -> HObject`

## Description

The operator `equ_histo_image` enhances the contrast. The
starting point is the histogram of the input images. The following
simple gray value transformation f(g) is carried out for byte
images:
$$f(g)=255\n\n\n\n\n\n\n\n\n\n\n\n\n$$ ![figure](../assets/f460536e4af119df.svg)
h(x) describes the relative frequency of the occurrence of the
gray value x. For uint2 images, the only difference is that the
value 255 is replaced with a different maximum value. The maximum
value is computed from the number of significant bits stored with
the input image, provided that this value is set. If not, the value
of the system parameter *"int2_bits"* is used (see
[`set_system`](set_system.md)), if this value is set (i.e., different from -1).
If none of the two values is set, the number of significant bits is
set to 16.

This transformation linearizes the cumulative histogram. Maxima in
the original histogram are “spreaded” and thus the contrast in
image regions with these frequently occurring gray values is
increased. Supposedly homogeneous regions receive more easily visible
structures. On the other hand, of course, the noise in the image
increases correspondingly. Minima in the original histogram are
dually “compressed”. The transformed histogram contains gaps, but
the remaining gray values used occur approximately at the same
frequency (“histogram equalization”).

## Attention

The operator `equ_histo_image` primarily serves for
optical processing of images for a human viewer. For example, the
(local) contrast spreading can lead to a detection of fictitious edges.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Image to be enhanced.

**`image_equ_histo`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Image with linearized gray values.

## Possible Successors

`disp_image`

## Alternatives

`equ_histo_image_rect`,
`scale_image`,
`scale_image_max`,
`illuminate`

## See also

`equ_histo_image_rect`,
`scale_image`

## References

R.C. Gonzales, P. Wintz: “Digital Image Processing”; Second edition;
Addison Wesley; 1987.

## Module

Foundation
