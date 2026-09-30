# LocalThreshold (Operator)

## Name

`LocalThreshold` — Segment an image using local thresholding.

## Signature

`static void HOperatorSet.LocalThreshold(HObject image, out HObject region, HTuple method, HTuple lightDark, HTuple genParamName, HTuple genParamValue)`

`HRegion HImage.LocalThreshold(string method, string lightDark, HTuple genParamName, HTuple genParamValue)`

`HRegion HImage.LocalThreshold(string method, string lightDark, string genParamName, int genParamValue)`

## Description

`LocalThreshold` segments a single-channel image *`image`*
using the thresholding method given in *`method`* and returns the
segmented region in *`region`*. Currently the operator offers only the
Method *"adapted_std_deviation"*. This algorithm is a text
binarization technique and provides good results for document images.

### Adaptive Thresholding

By selecting *`method`* = *"adapted_std_deviation"*, a
locally adaptive thresholding based on local mean and standard
deviation according to Sauvola (see the paper in References) is
invoked. The algorithm is able to segment document images even if
they are degraded, e.g., due to inhomogeneous illumination or noise.
It enables text binarization on an inhomogeneous background by taking
into account the local contrast.

For a segmentation of the dark foreground (see parameter
*`lightDark`*), for a pixel at position
`(r,c)`, a local threshold
`T(r,c)` is calculated within a window of size
*"mask_size"* x *"mask_size"* (see the generic
parameter *"mask_size"*) as follows:
$$T(r,c) = \mu(r,c)\left(1 + k\left(\frac{\sigma(r,c)}{R} - 1\right)\right)$$ ![figure](../assets/c9101652691743c8.svg)
where $\mu(r,c)$ is the local mean value
within the window and $\sigma(r,c)$ denotes
the corresponding standard deviation. The parameter
`R` (see *"range"*) is the assumed maximum
value of the standard deviation (`R` = 128 for
byte images) and `k` (see *"scale"*) a
parameter that controls how much the threshold value
`T(r,c)` differs from the mean value
$\mu(r,c)$. If there is high contrast in the
neighborhood of a point `(r,c)` the standard
deviation $\sigma(r,c)$ has a value close to
`R` which yields a threshold value
`T(r,c)` close to the local mean
$\mu(r,c)$. If the contrast is low, the local
threshold is below the local mean value. For dark text on light
background containing also darker regions, this lower threshold
enables the segmentation of the text even in darker areas.

The parameter *`lightDark`* controls, whether light or dark
structures are segmented.

- If *`lightDark`* = *"dark"*,
  dark structures on a light background are segmented. Every
  pixel `p(r,c)` whose gray value is smaller
  than the calculated local threshold
  `T(r,c)` is selected.
- If *`lightDark`* = *"light"*,
  light structures on a dark background are segmented. The result
  is essentially the same as if the image would have been inverted
  and then, *`lightDark`* was set to *"dark"*.

By setting *`genParamName`* to one of the following values, additional
parameters specific for the *"adapted_std_deviation"* method can be set
with *`genParamValue`*:

- ***"mask_size"*:** —

  specifies the mask size, i.e., the size of the neighborhood in
  which the local threshold is calculated. The smaller the window
  size the thinner the segmented strokes. *"mask_size"*
  must be set to a value that is larger than the stroke width of
  the characters or structures to be segmented. If
  *"mask_size"* is even, the next larger odd value is
  used.

  Suggested values:
   *15*, *21*, *31*.

  Default:
   *15*.
- ***"scale"*:** —

  sets the parameter `k` ($0\le k$), that controls how much the threshold
  value differs from the local mean value. Use smaller values for
  *"scale"* to also segment structures with a lower
  contrast to their background. Use larger values to suppress
  clutter.

  Suggested values:
   *0.2*, *0.3*, *0.5*.

  Default:
   *0.2*.
- ***"range"*:** —

  sets the maximum assumed value of standard deviation
  `R` . This parameter should be adapted based
  on the expected gray value range. As a rule of thumb, the
  value for *"range"* can be set to $range=0.5\cdot(MaxGray-MinGray)$, where MinGray and MaxGray are
  the minimum and maximum gray values in the image, which can be
  determined with [`MinMaxGray`](min_max_gray.md).

  Suggested values:
   *128*, *32767.5*.

  Default:
   *128* (for `byte` images),
  *32767.5* (for `uint2` images).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2)

Input Image.

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Segmented output region.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Segmentation method.

Default:
"adapted_std_deviation"

List of values:
"adapted_std_deviation"

**`lightDark`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Extract foreground or background?

Default:
"dark"

List of values:
"dark", "light"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

List of generic parameter names.

Default:
[]

List of values:
"mask_size", "range", "scale"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

List of generic parameter values.

Default:
[]

Suggested values:
0.2, 15, 30, 128.0

## Possible Successors

`Connection`,
`SelectShape`,
`SelectGray`

## Alternatives

`AutoThreshold`,
`BinaryThreshold`,
`CharThreshold`

## See also

`GrayHisto`,
`Threshold`

## References

J. Sauvola, M. Pietikäinen, “Adaptive document image binarization", Pattern
Recognition, 33, 225-236 (2000)

## Module

Foundation
