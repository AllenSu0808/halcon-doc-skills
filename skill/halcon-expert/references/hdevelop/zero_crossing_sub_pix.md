# zero_crossing_sub_pix (Operator)

## Name

`zero_crossing_sub_pix` — Extract zero crossings from an image with subpixel accuracy.

## Signature

`zero_crossing_sub_pix(Image : ZeroCrossings : : )`

## Description

`zero_crossing_sub_pix` extracts the zero crossings of the
input image *`Image`* with subpixel accuracy. The extracted
zero crossings are returned as XLD-contours in
*`ZeroCrossings`*. Thus, `zero_crossing_sub_pix` can be
used as a sub-pixel precise edge extractor if the input image is a
Laplace-filtered image (see [`laplace`](laplace.md),
[`laplace_of_gauss`](laplace_of_gauss.md), [`derivate_gauss`](derivate_gauss.md)).

For the extraction, the input image is regarded as a surface, in
which the gray values are interpolated bilinearly between the
centers of the individual pixels. Consistent with the surface thus
defined, zero crossing lines are extracted for each pixel and linked
into topologically sound contours. This means that the zero
crossing contours are correctly split at junction points. If the
image contains extended areas of constant gray value 0, only the
border of such areas is returned as zero crossings.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (int1 / int2 / int4 / real)

Input image.

**`ZeroCrossings`** (output_object)  xld_cont-array `→` object

Extracted zero crossings.

## Example (HDevelop)

```
* Detection zero crossings of the Laplacian-of-Gaussian
* of an aerial image
read_image(Image,'mreut')
derivate_gauss(Image,Laplace,3,'laplace')
zero_crossing_sub_pix(Laplace,ZeroCrossings)
dev_display(ZeroCrossings)

* Detection of edges, i.e, zero crossings of the Laplacian-of-Gaussian
* that have a large gradient magnitude, in an aerial image
read_image(Image,'mreut')
Sigma := 1.5
* Compensate the threshold for the fact that derivate_gauss(...,'gradient')
* calculates a Gaussian-smoothed gradient, in which the edge amplitudes
* are too small because of the Gaussian smoothing, to correspond to a true
* edge amplitude of 20.
Threshold := 20/(Sigma*sqrt(2*3.1415926))
derivate_gauss(Image,Gradient,Sigma,'gradient')
threshold(Gradient,Region,Threshold,255)
reduce_domain(Image,Region,ImageReduced)
derivate_gauss(ImageReduced,Laplace,Sigma,'laplace')
zero_crossing_sub_pix(Laplace,Edges)
dev_display(Edges)
```

## Result

`zero_crossing_sub_pix` usually returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`laplace`,
`laplace_of_gauss`,
`diff_of_gauss`,
`derivate_gauss`

## Alternatives

`zero_crossing`

## See also

`threshold_sub_pix`

## Module

2D Metrology
