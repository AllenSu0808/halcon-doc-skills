# GammaImage (Operator)

## Name

`GammaImage` — Perform a gamma encoding or decoding of an image.

## Signature

`static void HOperatorSet.GammaImage(HObject image, out HObject gammaImage, HTuple gamma, HTuple offset, HTuple threshold, HTuple maxGray, HTuple encode)`

`HImage HImage.GammaImage(double gamma, double offset, double threshold, HTuple maxGray, string encode)`

`HImage HImage.GammaImage(double gamma, double offset, double threshold, double maxGray, string encode)`

## Description

`GammaImage` performs a general gamma encoding or decoding of
the input image *`image`* and returns the resulting image in
*`gammaImage`*. A generalized gamma encoding can be described
as follows:
$$G' = \left\{ \begin{array}{ll} m\big((1 + o)(G/m)\gamma - o\big), & t < G/m \le 1 \\ sG, & 0 \le G/m \le t \end{array} \right.$$ ![figure](../assets/fb8da76cde11b090.svg)
Here, G' is the gamma-encoded gray value, G is the linear gray
value, $\gamma=\texttt{Gamma}$, o =
*`offset`*, m = *`maxGray`*, t = *`threshold`*,
and s is a factor that is computed from *`gamma`*,
*`offset`*, *`threshold`*, and *`maxGray`* in such a
way that the linear and exponential parts of the transformation are
continuous.

Analogously, a generalized gamma decoding can be described as follows:
$$G = {\begin{cases} m\left(\frac{G'/m+o}{1+o}\right)^{1/\gamma}, & t' < G'/m \le 1 \\ G'/s, & 0 \le G'/m \le t' \end{cases}}$$ ![figure](../assets/a752e13e95c89248.svg)
where the variables have identical meanings as for the gamma
encoding and $t^{\prime}=st$.

For example, the gamma encoding or decoding required by the sRGB
standard can be obtained by setting *`gamma`* = 1.0/2.4,
*`offset`* = 0.055, and *`threshold`* = 0.0031308.
Similarly, the gamma encoding or decoding required by the HDTV video
standard can be obtained by setting *`gamma`* = 0.45,
*`offset`* = 0.099, and *`threshold`* = 0.018. In any
case, *`maxGray`* should be set as appropriate for the image
type of *`image`* (e.g., 255.0 for byte images).

## Attention

`GammaImage` can be executed on an OpenCL device for byte, uint2 and
real images. As the operation is performed in single precision floating
point instead of double precision as on the CPU, the result of the OpenCL
implementation can vary slightly from that of the CPU implementation.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / uint2* / real*) **allowed for compute devices*

Input image.

**`gammaImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Output image.

**`gamma`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Gamma coefficient of the exponential part of the
transformation.

Default:
0.416666666667

Suggested values:
0.416666666667, 0.45

**`offset`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Offset of the exponential part of the transformation.

Default:
0.055

Suggested values:
0.055, 0.099

**`threshold`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Gray value for which the transformation switches from
linear to exponential.

Default:
0.0031308

Suggested values:
0.0031308, 0.018

**`maxGray`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum gray value of the input image type.

Default:
255.0

Suggested values:
1.0, 255.0, 511.0, 1023.0, 4095.0, 16383.0, 65535.0

**`encode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

If *"true"*, perform a gamma encoding,
otherwise a gamma decoding.

Default:
"true"

List of values:
"false", "true"

## Alternatives

`PowImage`

## See also

`SqrtImage`,
`ExpImage`,
`LogImage`

## References

Erik Reinhard, Erum Arif Khan, Ahmet Oguz Akyüz, Garret M. Johnson:
“Color Imaging: Fundamentals and Applications.” A K Peters, Ltd.,
2008.
  
CEI/IEC 61966-2-1:1999: “Colour management -- Default RGB colour
space -- sRGB.”
  
ITU-R BT.709-5: “Parameter values for the HDTV standards for
production and international programme exchange.”

## Module

Foundation
