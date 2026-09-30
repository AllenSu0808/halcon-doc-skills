# EstimateNoise (Operator)

## Name

`EstimateNoise` — Estimate the image noise from a single image.

## Signature

`static void HOperatorSet.EstimateNoise(HObject image, HTuple method, HTuple percent, out HTuple sigma)`

`HTuple HImage.EstimateNoise(string method, HTuple percent)`

`double HImage.EstimateNoise(string method, double percent)`

## Description

The operator `EstimateNoise` estimates the standard deviation
of additive noise within the domain of the image that is passed in
*`image`*. The standard deviation is returned in
*`sigma`*.

To estimate the noise, one of the following four methods can be
selected in *`method`*:

- *"foerstner"*: If *`method`* is set to
  *"foerstner"*, first for each pixel a homogeneity measure is
  computed based on the first derivatives of the gray values of
  *`image`*. By thresholding the homogeneity measure one obtains the
  homogeneous regions in the image. The threshold is computed based on a
  starting value for the image noise. The starting value is obtained by
  applying the method *"immerkaer"* (see below) in the first step. It
  is assumed that the gray value fluctuations within the homogeneous regions
  are solely caused by the image noise. Furthermore it is assumed that the
  image noise is Gaussian distributed. The average homogeneity measure within
  the homogeneous regions is then used to calculate a refined estimate for
  the image noise. The refined estimate leads to a new threshold for the
  homogeneity. The described process is iterated until the estimated image
  noise remains constant between two successive iterations. Finally, the
  standard deviation of the estimated image noise is returned in
  *`sigma`*.

  Note that in some cases the iteration falsely converges to the value
  *0*. This happens, for example, if the gray value histogram of the
  input image contains gaps that are caused either by an automatic
  radiometric scaling of the camera or frame grabber, respectively, or by a
  manual spreading of the gray values using a scaling factor > 1.

  Also note that the result obtained by this method is independent
  of the value passed in *`percent`*.
- *"immerkaer"*: If *`method`* is set to
  *"immerkaer"*, first the following filter mask is applied
  to the input image:

  $$M = \left|\begin{array}{ccc}1 & -2 & 1\\-2 & 4 & -2\\1 & -2 & 1\end{array}\right|$$ ![figure](../assets/ac36caaf1e2b7da6.svg)

  The advantage of this method is that $M$ is almost insensitive to image
  structure but only depends on the noise in the image. Assuming a Gaussian
  distributed noise, its standard deviation is finally obtained as

  $$\text{Sigma} = \sqrt{\frac{\pi}{2 \cdot 6N}} \sum_{\text{Image}} |\text{Image} * M|,$$ ![figure](../assets/e49eca3fb53f86ce.svg)

  where $N$ is the number of image pixels to which $M$
  is applied. Note that the result obtained by this method is
  independent of the value passed in *`percent`*.
- *"least_squares"*: If *`method`* is set
  to *"least_squares"*, the fluctuations of the gray values
  with respect to a locally fitted gray value plane are used to
  estimate the image noise. First, a homogeneity measure is computed
  based on the first derivatives of the gray values of
  *`image`*. Homogeneous image regions are determined by
  selecting the *`percent`* percent most homogeneous pixels in
  the domain of the input image, i.e., pixels with small magnitudes
  of the first derivatives. For each homogeneous pixel a gray value
  plane is fitted to its 3x3 neighborhood. The
  differences between the gray values within the 3x3
  neighborhood and the locally fitted plane are used to estimate the
  standard deviation of the noise. Finally, the average standard
  deviation over all homogeneous pixels is returned in
  *`sigma`*.
- *"mean"*: If *`method`* is set to
  *"mean"*, the noise estimation is based on the difference
  between the input image and a noiseless version of the input
  image. First, a homogeneity measure is computed based on the first
  derivatives of the gray values of *`image`*. Homogeneous
  image regions are determined by selecting the *`percent`*
  percent most homogeneous pixels in the domain of the input image,
  i.e., pixels with small magnitudes of the first derivatives. A
  mean filter is applied to the homogeneous image regions in order
  to eliminate the noise. It is assumed that the difference between
  the input image and the thus obtained noiseless version of the
  image represents the image noise. Finally, the standard deviation
  of the differences is returned in *`sigma`*. It should be
  noted that this method requires large connected homogeneous image
  regions to be able to reliably estimate the noise.

Note that the methods *"foerstner"* and *"immerkaer"*
assume a Gaussian distribution of the image noise, whereas the
methods *"least_squares"* and*"mean"* can be applied
to images with arbitrarily distributed noise. In general, the method
*"foerstner"* returns the most accurate results while the
method *"immerkaer"* shows the fastest computation.

If the image noise could not be estimated reliably, the error 3175
is raised. This may happen if the image does not contain enough
homogeneous regions, if the image was artificially created, or if
the noise is not of Gaussian type. In order to avoid this error, it
might be useful in some cases to try one of the following
modifications in dependence of the estimation method that is passed
in *`method`*:

- Increase the size of the input image domain (useful
  for all methods).
- Increase the value of the parameter *`percent`*
  (useful for methods *"least_squares"* and *"mean"*).
- Use the method *"immerkaer"*, instead of the
  methods *"foerstner"*, *"least_squares"*, or
  *"mean"*. The method *"immerkaer"* does not rely on
  the existence of homogeneous image regions, and hence is almost
  always applicable.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method to estimate the image noise.

Default:
"foerstner"

List of values:
"foerstner", "immerkaer", "least_squares", "mean"

**`percent`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Percentage of used image points.

Default:
20

Suggested values:
1, 2, 5, 7, 10, 15, 20, 30, 40, 50

Restriction:
`0 < Percent && Percent <= 50.`

**`sigma`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Standard deviation of the image noise.

Assertion:
`Sigma >= 0`

## Example (HDevelop)

```
read_image (Image, 'combine')
estimate_noise (ImageNoise, 'foerstner', 20, SigmaFoerstner)
estimate_noise (ImageNoise, 'immerkaer', 20, SigmaImmerkaer)
estimate_noise (ImageNoise, 'least_squares', 20, SigmaLeastSquares)
estimate_noise (ImageNoise, 'mean', 20, SigmaMean)
```

## Result

If the parameters are valid, the operator `EstimateNoise`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised. If
the image noise could not be estimated reliably, the error 3175 is
raised.

## Possible Predecessors

`GrabImage`,
`GrabImageAsync`,
`ReadImage`,
`ReduceDomain`

## Possible Successors

`BinomialFilter`,
`GaussFilter`,
`MeanImage`,
`SmoothImage`

## Alternatives

`NoiseDistributionMean`,
`Intensity`,
`MinMaxGray`

## See also

`GaussDistribution`,
`AddNoiseDistribution`

## References

W. Förstner: “Image Preprocessing for Feature Extraction in Digital
Intensity, Color and Range Images“, Springer Lecture Notes on Earth
Sciences, Summer School on Data Analysis and the Statistical
Foundations of Geomatics, 1999
  
J. Immerkaer: “Fast Noise Variance Estimation“, Computer Vision
and Image Understanding, Vol. 64, No. 2, pp. 300-302, 1996

## Module

Foundation
