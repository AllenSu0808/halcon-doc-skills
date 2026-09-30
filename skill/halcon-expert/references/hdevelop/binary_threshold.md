# binary_threshold (Operator)

## Name

`binary_threshold` — Segment an image using binary thresholding.

## Signature

`binary_threshold(Image : Region : Method, LightDark : UsedThreshold)`

## Description

`binary_threshold` segments a single-channel *`Image`*
using an automatically determined global threshold and returns the
segmented region in *`Region`*. This is, e.g., useful for the
segmentation of characters on a homogeneously illuminated background.
`binary_threshold` also returns the used threshold in
*`UsedThreshold`*.

The used threshold is determined by the method that is given in
*`Method`*. Currently the operator provides the following two
methods: *'max_separability'* and *'smooth_histo'*.
Both methods should only be used for images that have a bimodal
histogram.

The method *'smooth_histo'* provides the same functionality
that has been provided by the operator [`bin_threshold`](bin_threshold.md). The
method *'max_separability'* tends to determine smaller values
for *`UsedThreshold`*. Furthermore, it is less sensitive to thin
isolated peaks in the histogram that are far from the rest of the
spectrum and often, it is faster than *'smooth_histo'*.

### Maximize separability

By selecting *`Method`* = *'max_separability'*, automatic
thresholding based on the gray-level histogram according to Otsu (see
the paper in References) is invoked. The algorithm first calculates
the histogram of the image and then uses statistical moments to find
the optimal threshold $T^{\ast}$ that divides the pixels
into foreground and background and maximizes the separability between
these two classes. This method is only available for byte and uint2
images.

- If *`LightDark`* = *'light'*
  all pixels with gray values greater or equal to $T^{\ast}$ are selected.
- If *`LightDark`* = *'dark'* all pixels
  with gray values smaller than $T^{\ast}$ are selected.

### Histogram smoothing

By selecting *`Method`* = *'smooth_histo'*
`binary_threshold` determines the threshold
$T^{\ast}$ in the following way: First, the relative
histogram of the gray values is determined. Then, relevant minima are
extracted from the histogram, which are used as parameters for a
thresholding operation. In order to reduce the number of minima, the
histogram is smoothed with a Gaussian, as in [`auto_threshold`](auto_threshold.md).
The mask size is enlarged until there is only one minimum in the
smoothed histogram. Then, the threshold $T^{\ast}$ is
set to the position of this minimum.

- If *`LightDark`* = *'light'*
  all pixels `p(r,c)` with gray values greater or
  equal to $T^{\ast}$ are selected.
- If *`LightDark`* = *'dark'* all pixels
  `p(r,c)`
  with gray values smaller than $T^{\ast}$ are selected.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2)

Input Image.

**`Region`** (output_object)  region(-array) `→` object

Segmented output region.

**`Method`** (input_control)  string `→`  (string)

Segmentation method.

Default:
'max_separability'

List of values:
'max_separability', 'smooth_histo'

**`LightDark`** (input_control)  string `→`  (string)

Extract foreground or background?

Default:
'dark'

List of values:
'dark', 'light'

**`UsedThreshold`** (output_control)  number(-array) `→`  (integer / string)

Used threshold.

## Possible Successors

`connection`,
`select_shape`,
`select_gray`

## Alternatives

`auto_threshold`,
`char_threshold`,
`local_threshold`

## See also

`gray_histo`,
`threshold`

## References

N. Otsu, “A threshold selection method from gray level histograms",
IEEE Trans. Syst. Man. Cybern., Vol. SMC-9, 62-66 (1979).

## Module

Foundation
