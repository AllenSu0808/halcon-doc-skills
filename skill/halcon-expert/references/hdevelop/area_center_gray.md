# area_center_gray (Operator)

## Name

`area_center_gray` — Compute the area and center of gravity of a region in a gray value
image.

## Signature

`area_center_gray(Regions, Image : : : Area, Row, Column)`

## Description

`area_center_gray` computes the area and center of gravity of
the regions *`Regions`* that have gray values which are defined
by the image *`Image`*. This operator is similar to
[`area_center`](area_center.md), but in contrast to that operator, the gray
values of the image are taken into account while computing the area
and center of gravity.

The area A of a region R in the image with the gray values
g(r,c) is defined as $$A = \sum_{(r,c)\in R} g(r,c).$$ ![figure](../assets/b7611c07f867ba7d.svg) This means that the area is defined by the volume of the gray
value function g(r,c). The center of gravity is defined by the
first two normalized moments of the gray values g(r,c), i.e., by
$(m_{1,0},m_{0,1})$, where $$m_{p,q} = \frac{1}{A} \sum_{(r,c) \in R} r^{p}_{c^{q}} g(r,c).$$ ![figure](../assets/450d502147041494.svg)

Note, that in the case where the *`Area`* is zero the row and
column coordinates of the center of gravity are also set to zero.

## Attention

Note that the operator `area_center_gray` only considers
the given *`Regions`* and ignores any previously set domain
of the input image *`Image`*.
`area_center_gray` can be executed on OpenCL devices if the device
supports the cl_khr_fp64 and cl_khr_int64_base_atomics OpenCL extensions.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Region(s) to be examined.

**`Image`** (input_object)  singlechannelimage `→` object (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / real*) **allowed for compute devices*

Gray value image.

**`Area`** (output_control)  real(-array) `→`  (real)

Gray value volume of the region.

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the gray value center of gravity.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of the gray value center of gravity.

## Result

`area_center_gray` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution. If the input is empty the
behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`area_center`

## See also

`area_center_xld`,
`elliptic_axis_gray`

## Module

Foundation
