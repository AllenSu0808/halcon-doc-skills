# simulate_defocus (Operator)

## Name

`simulate_defocus` — Simulate an uniform out-of-focus blurring of an image.

## Signature

`def simulate_defocus(image: HObject, blurring: float) -> HObject`

## Description

`simulate_defocus` simulates out-of-focus blurring of an image.
All parts of the image are blurred uniformly.
*`blurring`* specifies the extent of blurring by defining
the “blur radius” (out-of-focus blurring maps each image pixel on a small
circle with a radius of *`blurring`* - specified in “number of
pixels”). If specified less than null, the absolute value of
*`blurring`* is used. Simulation of blurring is done by a
convolution of the image with a blurring specific impulse response.
The convolution is realized by multiplication in the Fourier domain.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Image to blur.

**`defocused_image`** (output_object)  image(-array) `→` HObject (real)

Blurred image.

**`blurring`** (input_control)  real `→` float

Degree of blurring.

Default:
5.0

Suggested values:
1.0, 5.0, 10.0, 15.0, 18.0

## Result

`simulate_defocus` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty `simulate_defocus` returns with
an error message.

## Possible Predecessors

`gen_psf_defocus`,
`simulate_motion`,
`gen_psf_motion`

## Possible Successors

`wiener_filter`,
`wiener_filter_ni`

## See also

`gen_psf_defocus`,
`simulate_motion`,
`gen_psf_motion`

## References

Reginald L. Lagendijk, Jan Biemond: Iterative Identification and Restoration
of Images, Kluwer Academic Publishers Boston/Dordrecht/London, 1991
  
M. Lückenhaus:“Grundlagen des Wiener-Filters und seine Anwendung in der
Bildanalyse”; Diplomarbeit;
Technische Universität München, Institut für Informatik;
Lehrstuhl Prof. Radig; 1995.

## Module

Foundation
