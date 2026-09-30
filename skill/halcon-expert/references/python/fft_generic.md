# fft_generic (Operator)

## Name

`fft_generic` — Compute the fast Fourier transform of an image.

## Signature

`def fft_generic(image: HObject, direction: str, exponent: int, norm: str, mode: str, result_type: str) -> HObject`

## Description

`fft_generic` computes the fast Fourier transform of the input
image *`image`*. Because several definitions of the forward
and reverse transforms exist in the literature, this operator allows
the user to select the most convenient definition.

The general definition of a Fourier transform is as follows:
$$F(m,n) = \frac{1}{c} \sum_{k=0}^{M-1} \sum_{l=0}^{N-1} e^{s2\pi i(km/M + ln/N)} f(k,l)$$ ![figure](../assets/134e19f876dbb7b3.svg)
Opinions vary on whether the sign s in the exponent should
be set to 1 or -1 for the forward transform, i.e., the transform for
going to the frequency domain. There is also disagreement on the
magnitude of the normalizing factor c. This is sometimes
set to 1 for the forward transform, sometimes to M*N, and
sometimes (in case of the unitary FFT) to
$\sqrt{MN}$ ![figure](../assets/269a5f99826e3f83.svg). Especially in image processing
applications the DC term is shifted to the center of the image.

`fft_generic` allows to select these choices individually.
The parameter *`direction`* allows to select the logical
direction of the FFT. (This parameter is not unnecessary; it is
needed to discern how to shift the image if the DC term should rest
in the center of the image.) Possible values are *"to_freq"*
and *"from_freq"*. The parameter *`exponent`* is used
to determine the sign of the exponent. It can be set to 1 or -1.
The normalizing factor can be set with *`norm`*, and can take
on the values *"none"*, *"sqrt"* and *"n"*.
The parameter *`mode`* determines the location of the DC term
of the FFT. It can be set to *"dc_center"* or
*"dc_edge"*.

In any case, the user must ensure the consistent use of the
parameters. This means that the normalizing factors used for the
forward and backward transform must yield M*N when
multiplied, the exponents must be of opposite sign, and
*`mode`* must be equal for both transforms.

A consistent combination is, for example
*"(to_freq,-1,n,dc_edge)"* for the forward transform and
*"(from_freq,1,none,dc_edge)"* for the reverse transform.
In this case, the FFT can be interpreted as interpolation with
trigonometric basis functions. Another possible combination is
*"(to_freq,-1,sqrt,dc_center)"* and
*"(from_freq,1,sqrt,dc_center)"*.

The parameter *`result_type`* can be used to specify the result
image type of the reverse transform (*`direction`* =
*"from_freq"*). In the forward transform (*`direction`*
= *"to_freq"*), *`result_type`* must be set to
*"complex"*.

## Attention

The transformation is always performed for the entire image, i.e., the
domain of the image is ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Input image.

**`image_fft`** (output_object)  image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Fourier-transformed image.

**`direction`** (input_control)  string `→` str

Calculate forward or reverse transform.

Default:
"to_freq"

List of values:
"from_freq", "to_freq"

**`exponent`** (input_control)  integer `→` int

Sign of the exponent.

Default:
-1

List of values:
-1, 1

**`norm`** (input_control)  string `→` str

Normalizing factor of the transform.

Default:
"sqrt"

List of values:
"n", "none", "sqrt"

**`mode`** (input_control)  string `→` str

Location of the DC term in the frequency domain.

Default:
"dc_center"

List of values:
"dc_center", "dc_edge"

**`result_type`** (input_control)  string `→` str

Image type of the output image.

Default:
"complex"

List of values:
"byte", "complex", "cyclic", "direction", "int1", "int2", "int4", "real", "uint2"

## Example (C)

```
/* simulation of fft_image */
void my_fft(Hobject In, Hobject *Out)
{
  fft_generic(In,Out,"to_freq",-1,"sqrt","dc_center","complex");
}

/* simulation of fft_image_inv */
void my_fft_image_inv(Hobject In, Hobject *Out)
{
  fft_generic(In,Out,"from_freq",1,"sqrt","dc_center","byte");
}
```

## Result

`fft_generic` returns 2 (
H_MSG_TRUE)
if all parameters are correct. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`optimize_fft_speed`,
`read_fft_optimization_data`

## Possible Successors

`convol_fft`,
`correlation_fft`,
`phase_correlation_fft`,
`convol_gabor`,
`convert_image_type`,
`power_byte`,
`power_real`,
`power_ln`,
`phase_deg`,
`phase_rad`,
`energy_gabor`

## Alternatives

`fft_image`,
`fft_image_inv`,
`rft_generic`

## Module

Foundation
