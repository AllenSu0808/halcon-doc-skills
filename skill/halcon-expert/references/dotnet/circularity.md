# Circularity (Operator)

## Name

`Circularity` — Shape factor for the circularity (similarity to a circle) of a region.

## Signature

`static void HOperatorSet.Circularity(HObject regions, out HTuple circularity)`

`HTuple HRegion.Circularity()`

## Description

The operator `Circularity` calculates the similarity of
the input region with a circle.

- **Calculation:** —

  If F is the area of the region and max is the maximum distance from
  the center to all contour pixels, the shape factor C
  is defined as:

  $$C' = \frac{F}{\left(\max^2 * \pi\right)}$$ ![figure](../assets/5bf532d52a381335.svg)

  C = min(1,C')

The shape factor C of a circle is 1. If the region
is long or has holes, C is smaller than 1.
The operator `Circularity` especially responds to large bulges,
holes and unconnected regions. The value of C is clipped to 1.0,
because the pixel area of a region can only be an approximation of a
real circle's area. This approximation error is bigger for small
regions than for large regions.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their circularity.

In case of an empty region the operator `Circularity` returns the
value 0 (if no other behavior was set (see [`SetSystem`](set_system.md))).
If more than one region is passed the numerical values of the shape
factor are stored in a tuple, the position of a value in the tuple corresponding
to the position of the region in the input tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be examined.

**`circularity`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Circularity of the input region(s).

Assertion:
`0 <= Circularity && Circularity <= 1.0`

## Example (HDevelop)

```
* Comparison between shape factors of rectangle, circle and ellipse:
gen_rectangle1(R1,10,10,20,20)
gen_rectangle2(R2,100,100,0.0,100,20)
gen_ellipse(E100,100,100,0.0,100,20)
gen_circle(C,100,100,20)
circularity(R1,M_R1)
circularity(R2,M_R2)
circularity(E100,M_E)
circularity(C,M_C)
fwrite_string(FileId,['quadrate:  ',M_R1])
fnew_line(FileId)
fwrite_string(FileId,['rectangle: ',M_R2])
fnew_line(FileId)
fwrite_string(FileId,['ellipse:   ',M_E])
fnew_line(FileId)
fwrite_string(FileId,['circle:    ',M_C])
fnew_line(FileId)
```

## Result

The operator `Circularity` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`Roundness`,
`Compactness`,
`Convexity`,
`Eccentricity`

## See also

`AreaCenter`,
`SelectShape`

## Module

Foundation
