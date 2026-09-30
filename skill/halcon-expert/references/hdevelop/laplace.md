# laplace (Operator)

## Name

`laplace` — Calculate the Laplace operator by using finite differences.

## Signature

`laplace(Image : ImageLaplace : ResultType, MaskSize, FilterMask : )`

## Description

`laplace` filters the input images *`Image`* using a
Laplace operator. Depending on the parameter *`FilterMask`*
the following approximations of the Laplace operator are used:

- ***'n_4'*** —

  1
  1 -4 1
  1
- ***'n_8'*** —

  1 1 1
  1 -8 1
  1 1 1
- ***'n_8_isotropic'*** —

  10 22 10
  22 -128 22
  10 22 10

For the three filter masks the following normalizations of the
resulting gray values is applied, (i.e., by dividing the result by
the given divisor): *'n_4'* normalization by 1, *'n_8'*,
normalization by 2 and for *'n_8_isotropic'* normalization by 32.

For a Laplace operator with size 3x3, the
corresponding filter is applied directly, while for larger filter
sizes the input image is first smoothed using a Gaussian
filter (see [`gauss_image`](gauss_image.md)) or a binomial filter (see
[`binomial_filter`](binomial_filter.md)) of size *`MaskSize`*-2. The Gaussian
filter is selected for the above values of *`ResultType`*.
Here, *`MaskSize`* = 5, 7, 9, 11, or 13 must be used. The
binomial filter is selected by appending *'_binomial'* to the
above values of *`ResultType`*. Here, *`MaskSize`* can be
selected between 5 and 39. Furthermore, it is possible to select
different amounts of smoothing for the column and row direction by
passing two values in *`MaskSize`*. Here, the first value of
*`MaskSize`* corresponds to the mask width (smoothing in the
column direction), while the second value corresponds to the mask
height (smoothing in the row direction) of the binomial filter.
Therefore,

|  |
| --- |
| `laplace(O:R:'absolute',MaskSize,N:)` |

for *`MaskSize`* > *3* is equivalent to

|  |
| --- |
| `gauss_image(O:G:MaskSize-2:)` |
| `laplace(G:R:'absolute',3,N:)` |

and

|  |
| --- |
| `laplace(O:R:'absolute_binomial',MaskSize,N:)` |

is equivalent to

|  |
| --- |
| `binomial_filter(O:B:MaskSize-2,MaskSize-2:)` |
| `laplace(B:R:'absolute',3,N:)`. |

`laplace` either returns the absolute value of the Laplace
filtered image (*`ResultType`* = *'absolute'*) in a
byte or uint2 image or the signed result (*`ResultType`* =
*'signed'* or *'signed_clipped'*). Here, the output
image type has the same number of bytes per pixel as the input image
(i.e., int1 or int2) for *'signed_clipped'*, while the output
image has the next larger number of pixels (i.e., int2 or int4) for
*'signed'*.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2)

Input image.

**`ImageLaplace`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2 / int2 / int2 / int4)

Laplace-filtered result image.

**`ResultType`** (input_control)  string `→`  (string)

Type of the result image, whereas for byte and uint2
the absolute value is used.

Default:
'absolute'

List of values:
'absolute', 'absolute_binomial', 'signed', 'signed_binomial', 'signed_clipped', 'signed_clipped_binomial'

**`MaskSize`** (input_control)  integer(-array) `→`  (integer)

Size of filter mask.

Default:
3

List of values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39

**`FilterMask`** (input_control)  string `→`  (string)

Filter mask used in the Laplace operator

Default:
'n_4'

List of values:
'n_4', 'n_8', 'n_8_isotropic'

## Example (C)

```
read_image(&Image,"mreut");
laplace(Image,&Laplace,"signed",3,"n_8_isotropic");
zero_crossing(Laplace,&ZeroCrossings);
```

## Result

`laplace` returns 2 (
H_MSG_TRUE)
if all parameters are correct. If the
input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Successors

`zero_crossing`,
`dual_threshold`,
`threshold`

## Alternatives

`diff_of_gauss`,
`laplace_of_gauss`,
`derivate_gauss`

## See also

`highpass_image`,
`edges_image`

## Module

Foundation
