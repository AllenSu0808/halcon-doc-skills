# CropDomainRel (Operator)

## Name

`CropDomainRel` — Cut out an image area relative to the domain.

## Signature

`static void HOperatorSet.CropDomainRel(HObject image, out HObject imagePart, HTuple top, HTuple left, HTuple bottom, HTuple right)`

`HImage HImage.CropDomainRel(int top, int left, int bottom, int right)`

## Description

`CropDomainRel` cuts a rectangular area from the input
images. The area is determined by the surrounding rectangle of the
domain of the input image. The rectangle can be influenced by the
control parameters to modify at the top (*`top`*), at the left
(*`left`*), at the bottom (*`bottom`*), and at the right
(*`right`*). Positive values results in a smaller, negative
values in a larger size. If all parameters are set to zero, the
region remains unchanged.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Input image.

**`imagePart`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Image area.

**`top`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of rows clipped at the top.

Default:
-1

Suggested values:
-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

**`left`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of columns clipped at the left.

Default:
-1

Suggested values:
-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

**`bottom`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of rows clipped at the bottom.

Default:
-1

Suggested values:
-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

**`right`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of columns clipped at the right.

Default:
-1

Suggested values:
-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

## Result

`CropDomainRel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`ReduceDomain`,
`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Alternatives

`CropDomain`,
`CropRectangle1`

## See also

`SmallestRectangle1`,
`Intersection`,
`GenRectangle1`,
`ClipRegion`

## Module

Foundation
