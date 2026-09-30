# simulate_motion (Operator)

## Name

`simulate_motion` — Simulation of (linearly) motion blur.

## Signature

`def simulate_motion(image: HObject, blurring: float, angle: int, type: int) -> HObject`

## Description

`simulate_motion` simulates blurring caused by a relative motion
between the object and the camera during exposure. The simulated motion
moves along an even. *`angle`* fixes its direction by specifying
the angle between the motion direction and the x-axis (anticlockwise,
measured in degrees).
Simulation is done by a convolution of the image with a blurring specific
impulse response. The convolution is realized by multiplication in the
Fourier domain.
`simulate_motion` offers five prototypes of impulse responses
conforming to different acceleration behaviors. *`type`* allows
to choose one of the following PSF prototypes:

1. reverse ramp (crude model for acceleration)
2. reverse trapezoid (crude model for high acceleration)
3. square pulse (exact model for constant velocity), this is
   default
4. forward trapezoid (crude model for deceleration)
5. forward ramp (crude model for high deceleration)

(default value is 3.)

The simulated blurring affects all part of the image uniformly.
*`blurring`* controls the extent of blurring. It specifies the
number of pixels (lying one after another) that are affected by the
blurring. This number is determined by velocity of the motion and
exposure time. If *`blurring`* is a negative number, an adequate
blurring in reverse direction is simulated. If *`angle`* is a
negative number, it is interpreted clockwise. If *`angle`* exceeds
360 or falls below -360, it is transformed modulo(360) in an adequate number
between [0..360] resp. [-360..0].

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

image to be blurred.

**`moved_image`** (output_object)  image `→` HObject (real)

motion blurred image.

**`blurring`** (input_control)  real `→` float

extent of blurring.

Default:
20.0

Suggested values:
5.0, 10.0, 20.0, 30.0, 40.0

**`angle`** (input_control)  integer `→` int

Angle between direction of motion and x-axis
(anticlockwise).

Default:
0

Suggested values:
0, 45, 90, 180, 270

**`type`** (input_control)  integer `→` int

impulse response of motion blur.

Default:
3

List of values:
1, 2, 3, 4, 5

## Result

`simulate_motion` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty `simulate_motion` returns with
an error message.

## Possible Predecessors

`gen_psf_motion`,
`gen_psf_motion`

## Possible Successors

`simulate_defocus`,
`wiener_filter`,
`wiener_filter_ni`

## See also

`gen_psf_motion`,
`simulate_defocus`,
`gen_psf_defocus`

## References

Anil K. Jain:Fundamentals of Digital Image Processing, Prentice-Hall
International Inc., Englewood Cliffs, New Jersey, 1989
  
M. Lückenhaus:“Grundlagen des Wiener-Filters und seine Anwendung in
der Bildanalyse”; Diplomarbeit;
Technische Universität München, Institut für Informatik;
Lehrstuhl Prof. Radig; 1995.
  
Kha-Chye Tan, Hock Lim, B. T. G. Tan:“Restoration of Real-World
Motion-Blurred Images”;S. 291-299 in: CVGIP Graphical Models and
Image Processing, Vol. 53, No. 3, May 1991

## Module

Foundation
