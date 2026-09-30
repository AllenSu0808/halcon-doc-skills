# GenPsfMotion (Operator)

## Name

`GenPsfMotion` — Generate an impulse response of a (linearly) motion blurring.

## Signature

`static void HOperatorSet.GenPsfMotion(out HObject psf, HTuple PSFwidth, HTuple PSFheight, HTuple blurring, HTuple angle, HTuple type)`

`void HImage.GenPsfMotion(int PSFwidth, int PSFheight, double blurring, int angle, int type)`

## Description

`GenPsfMotion` generates an impulse response (spatial domain)
of a blurring caused by a relative motion between the object and the camera
during exposure. The generated impulse response is output into an image of
HALCON image type `real`. *`PSFwidth`* and *`PSFheight`*
define the width and height of the output image.
The blurring motion moves along an even. *`angle`* fixes its
direction by specifying the angle between the motion direction and the
x-axis (anticlockwise, measured in degrees).
To specify different velocity behavior five PSF prototypes can be
generated. *`type`* switches between the following prototypes:

1. reverse ramp (crude model for acceleration)
2. reverse trapezoid (crude model for high acceleration)
3. square pulse (exact model for constant velocity), this is
   default
4. forward trapezoid (crude model for deceleration)
5. forward ramp (crude model for high deceleration)

(default value is 3.)

The blurring affects all part of the image uniformly.
*`blurring`* controls the extent of blurring. It specifies the
number of pixels (lying one after another) that are affected by the
blurring. This number is determined by velocity of the motion and
exposure time. If *`blurring`* is a negative number, an adequate
blurring in reverse direction is simulated. If *`angle`* is a
negative number, it is interpreted clockwise. If *`angle`* exceeds
360 or falls below -360, it is transformed modulo(360) in an adequate number
between [0..360] resp. [-360..0].
The result image of `GenPsfMotion` encloses an spatial
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
the HALCON-operator [`WienerFilter`](wiener_filter.md). So one can use
`GenPsfMotion` to generate an impulse response for
Wiener filtering a motion blurred image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`psf`** (output_object)  image `→` [HImage](HImage.md) (real)

Impulse response of motion-blur.

**`PSFwidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of impulse response image.

Default:
256

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
PSFwidth`

**`PSFheight`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of impulse response image.

Default:
256

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
PSFheight`

**`blurring`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Degree of motion-blur.

Default:
20.0

Suggested values:
5.0, 10.0, 20.0, 30.0, 40.0

**`angle`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Angle between direction of motion and x-axis
(anticlockwise).

Default:
0

Suggested values:
0, 45, 90, 180, 270

**`type`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

PSF prototype resp. type of motion.

Default:
3

List of values:
1, 2, 3, 4, 5

## Result

`GenPsfMotion` returns 2 (
H_MSG_TRUE)
if all parameters are correct.

## Possible Predecessors

`SimulateDefocus`,
`GenPsfDefocus`

## Possible Successors

`SimulateMotion`,
`WienerFilter`,
`WienerFilterNi`

## See also

`SimulateMotion`,
`SimulateDefocus`,
`GenPsfDefocus`,
`WienerFilter`,
`WienerFilterNi`

## References

Anil K. Jain:Fundamentals of Digital Image Processing, Prentice-Hall
International Inc., Englewood Cliffs, New Jersey, 1989
  
M. Lückenhaus:“Grundlagen des Wiener-Filters und seine Anwendung
in der Bildanalyse”; Diplomarbeit;
Technische Universität München, Institut für Informatik;
Lehrstuhl Prof. Radig; 1995.
  
Kha-Chye Tan, Hock Lim, B. T. G. Tan:“Restoration of Real-World
Motion-Blurred Images”;S. 291-299 in: CVGIP Graphical Models and
Image Processing, Vol. 53, No. 3, May 1991

## Module

Foundation
