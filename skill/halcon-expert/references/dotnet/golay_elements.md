# GolayElements (Operator)

## Name

`GolayElements` — Generate the structuring elements of the Golay alphabet.

## Warning

**`GolayElements` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GolayElements(out HObject structElement1, out HObject structElement2, HTuple golayElement, HTuple rotation, HTuple row, HTuple column)`

`HRegion HRegion.GolayElements(string golayElement, int rotation, int row, int column)`

## Description

`GolayElements` generates the structuring elements from
the Golay alphabet. The parameter *`golayElement`*
determines the name of the structuring element, while
*`rotation`* determines its rotation. The structuring
elements are intended for use in [`HitOrMiss`](hit_or_miss.md): In
*`structElement1`* the structuring element for the foreground
is returned, while in *`structElement2`* the structuring
element for the background is returned. *`row`* and
*`column`* determine the reference point of the structuring
element.

The rotations are numbered from 0 to 15. This does not mean,
however, that there are 16 different rotations: Even values denote
rotations of the foreground elements, while odd values denote
rotations of the background elements.

For `GolayElements` only even values are accepted, and
determine the Golay element for *`structElement1`*. The next
larger odd value is used for *`structElement2`*. There are
no rotations for the Golay elements 'h' and 'i'. Therefore, only
the values 0 and 1 are possible as “rotations” (and hence only 0
for `GolayElements`). The element 'e' has only four
possible rotations, and hence the rotation must be between 0 and 7
(for `GolayElements` the values 0, 2, 4, or 6 must be
used).

The tables below show the elements of the Golay alphabet with all
possible rotations. The characters used have the following meaning:
* Foreground pixel
o Background pixel
. Don't care pixel
The names of the elements and their rotation numbers are displayed
below the respective element. The elements with even number contain
the foreground pixels, while the elements with odd numbers contain
the background pixels.
* * *
* * *
* * *
h(0,1)
o o o
o o o
o o o
i(0,1)
. . . o o . o o o . o o
o * o o * . o * o . * o
o o o o o . . . . . o o
e(0,1) e(2,3) e(4,5) e(6,7)
o * * o
o o o . . o * . o * . . * * * . . * o . * o . .
. * . * . * . o * * o * . * . o . * . o . * . * o * * o . * *
* * * * . . * . o . . o o o o o . . o . * . . *
* o o *
l(0,1) l(2,3) l(4,5) l(6,7) l(8,9) l(10,11) l(12,13) l(14,15)
* * . .
* . . * . . * * * . . * . . * o . . . o . . . o
* * o * . * . . . * . . . * . * o * * . . * . * . * . * . * . .
* . . . . o . o . o . . . . * . . * * * * * . .
. . * *
m(0,1) m(2,3) m(4,5) m(6,7) m(8,9) m(10,11) m(12,13) m(14,15)
o o . .
o . . o . . o o o . . o . . o * . . . * . . . *
o * * o . * . . . * . . . * . o * * o . . * . o . * . o . * . .
o . . . . * . * . * . . . . o . . o o o o o . .
. . o o
d(0,1) d(2,3) d(4,5) d(6,7) d(8,9) d(10,11) d(12,13) d(14,15)
* * o o
* o o o * o * o * o * o o o * * . o o * o o . *
o * * * * * . o o * o o . * * * * * o o . * * * o * o * * * . o
* o o o . * o * o * . o o o * o * o * o * o * o
o o * *
f(0,1) f(2,3) f(4,5) f(6,7) f(8,9) f(10,11) f(12,13) f(14,15)
* o o *
* * * o . * o o * o . o o o o o . o * o o * . o
o * o o . * . * o * * o . * . * o * o * . * . o * * o * . * . o
o o o o . o o o * o . * * * * * . o * o o o . o
o * * o
f2(0,1) f2(2,3) f2(4,5) f2(6,7) f2(8,9) f2(10,11)f2(12,13) f2(14,15)
* . . o
* * o . . * . . * . . . . . . . . . o . . * . .
. * . . . * . o . * * . . * . * . * . o . * . . * * . * . * . .
. . . . . . . . o . . * o * * * . . * . . . . .
. o * .
k(0,1) k(2,3) k(4,5) k(6,7) k(8,9) k(10,11) k(12,13) k(14,15)
* . . * * * * * . . * . . . . .
* o . * . . . o . . . * . o * . . . . o . . . .
* . . * . o . . . . . . . o . * . . * . . o * * * * * o . .
. . . . . . . . * * . .
. . * *
c(0,1) c(2,3) c(4,5) c(6,7) c(8,9) c(10,11) c(12,13) c(14,15)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`structElement1`** (output_object)  region `→` [HRegion](HRegion.md)

Structuring element for the foreground.

**`structElement2`** (output_object)  region `→` [HRegion](HRegion.md)

Structuring element for the background.

**`golayElement`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the structuring element.

Default:
"l"

List of values:
"c", "d", "e", "f", "f2", "h", "i", "k", "l", "m"

**`rotation`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Rotation of the Golay element. Depending on the
element, not all rotations are valid.

Default:
0

List of values:
0, 2, 4, 6, 8, 10, 12, 14

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the reference point.

Default:
16

Suggested values:
0, 16, 32, 128, 256

Value range:
`0
≤
row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of the reference point.

Default:
16

Suggested values:
0, 16, 32, 128, 256

Value range:
`0
≤
column
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

`GolayElements` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. Otherwise, an exception is raised.

## Possible Successors

`HitOrMiss`

## Alternatives

`GenRegionPoints`,
`GenStructElements`,
`GenRegionPolygonFilled`

## See also

`DilationGolay`,
`ErosionGolay`,
`OpeningGolay`,
`ClosingGolay`,
`HitOrMissGolay`,
`ThickeningGolay`

## References

J. Serra: “Image Analysis and Mathematical Morphology”. Volume I.
Academic Press, 1982

## Module

Foundation
