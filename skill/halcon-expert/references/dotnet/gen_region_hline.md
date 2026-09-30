# GenRegionHline (Operator)

## Name

`GenRegionHline` — Store input lines described in Hesse normal form as regions.

## Signature

`static void HOperatorSet.GenRegionHline(out HObject regions, HTuple orientation, HTuple distance)`

`void HRegion.GenRegionHline(HTuple orientation, HTuple distance)`

`void HRegion.GenRegionHline(double orientation, double distance)`

## Description

The operator `GenRegionHline` stores the lines described in Hesse
normal form as regions. A line is determined by the distance from the line
to the origin (*`distance`*, corresponds to the length of the normal
vector) and the direction of the normal vector (*`orientation`*,
corresponds to the orientation of the line $\pm\pi/2$).
The directions were defined in such a way that
at *`orientation`* = 0 the normal vector lies in the direction of
the X axis, which corresponds to a vertical line.
At *`orientation`* = $\pi/2$
the normal vector points in the direction
of the Y axis, i.e. a horizontal line is described.

## Attention

The lines are clipped to the current maximum image format.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Created regions (one for every line), clipped to
maximum image format.

Number of elements:
Regions == Distance

**`orientation`** (input_control)  hesseline.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Orientation of the normal vector in radians.

Number of elements:
Orientation == Distance

Default:
0.0

Suggested values:
-0.78, 0.0, 0.78, 1.57

Value range:
`orientation` (lin)

Recommended increment:
0.02

**`distance`** (input_control)  hesseline.distance(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Distance from the line to the coordinate origin (0.0).

Default:
200

Suggested values:
10, 50, 100, 200, 300, 400

Value range:
`distance` (lin)

Recommended increment:
1

## Result

The operator `GenRegionHline` always returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`GenRegionLine`

## See also

`HoughLines`

## Module

Foundation
