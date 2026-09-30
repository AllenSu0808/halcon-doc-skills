# gen_psf_defocus (Operator)

## Name

`gen_psf_defocus` — Generate an impulse response of an uniform out-of-focus blurring.

## Signature

`gen_psf_defocus( : Psf : PSFwidth, PSFheight, Blurring : )`

## Description

`gen_psf_defocus` generates an impulse response (spatial domain)
of an uniform out-of-focus blurring and writes it into an image of
HALCON image type `real`.
*`Blurring`* specifies the extent of blurring by defining
the “blur radius” (out-of-focus blurring maps each image pixel on a small
circle with a radius of *`Blurring`* - specified in “number of
pixels”). If specified less than zero, the absolute value of
*`Blurring`* is used.
The result image of `gen_psf_defocus` encloses an spatial
domain impulse response of the specified blurring. Its representation
presumes the origin in the upper left corner. This results in the
following disposition of an NxM sized image:

- first rectangle (“upper left”):
  (image coordinates xb = 0..(N/2)-1, yb = 0..(M/2)-1)

  - conforms to the fourth quadrant of the Cartesian coordinate system,
  encloses values of the impulse response
  at position x = 0..N/2 and y = 0..-M/2
- second rectangle (“upper right”):
  (image coordinates xb = N/2..N-1, yb = 0..(M/2)-1)

  - conforms to the third quadrant of the Cartesian coordinate system,
  encloses values of the impulse response
  at position x = -N/2..-1 and y = -1..-M/2
- third rectangle (“lower left”):
  (image coordinates xb = 0..(N/2)-1, yb = M/2..M-1)

  - conforms to the first quadrant of the Cartesian coordinate system,
  encloses values of the impulse response
  at position x = 1..N/2 and y = M/2..0
- fourth rectangle (“lower right”):
  (image coordinates xb = N/2..N-1, yb = M/2..M-1)

  - conforms to the second quadrant of the Cartesian coordinate system,
  encloses values of the impulse response
  at position x = -N/2..-1 and y = M/2..1

This representation conforms to that of the impulse response parameter of
the HALCON-operator [`wiener_filter`](wiener_filter.md). So one can use
`gen_psf_defocus` to generate an impulse response for
Wiener filtering.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Psf`** (output_object)  image `→` object (real)

Impulse response of uniform out-of-focus blurring.

**`PSFwidth`** (input_control)  integer `→`  (integer)

Width of result image.

Default:
256

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
PSFwidth`

**`PSFheight`** (input_control)  integer `→`  (integer)

Height of result image.

Default:
256

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
PSFheight`

**`Blurring`** (input_control)  real `→`  (real)

Degree of Blurring.

Default:
5.0

Suggested values:
1.0, 5.0, 10.0, 15.0, 18.0

## Result

`gen_psf_defocus` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`simulate_motion`,
`gen_psf_motion`

## Possible Successors

`simulate_defocus`,
`wiener_filter`,
`wiener_filter_ni`

## See also

`simulate_defocus`,
`gen_psf_motion`,
`simulate_motion`,
`wiener_filter`,
`wiener_filter_ni`

## References

Reginald L. Lagendijk, Jan Biemond: Iterative Identification and Restoration
of Images, Kluwer Academic Publishers Boston/Dordrecht/London, 1991
  
M. Lückenhaus:“Grundlagen des Wiener-Filters und seine Anwendung in der
Bildanalyse”; Diplomarbeit;
Technische Universität München, Institut für Informatik;
Lehrstuhl Prof. Radig; 1995.

## Module

Foundation
