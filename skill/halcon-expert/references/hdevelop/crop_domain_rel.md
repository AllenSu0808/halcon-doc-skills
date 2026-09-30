# crop_domain_rel (Operator)

## Name

`crop_domain_rel` — Cut out an image area relative to the domain.

## Signature

`crop_domain_rel(Image : ImagePart : Top, Left, Bottom, Right : )`

## Description

`crop_domain_rel` cuts a rectangular area from the input
images. The area is determined by the surrounding rectangle of the
domain of the input image. The rectangle can be influenced by the
control parameters to modify at the top (*`Top`*), at the left
(*`Left`*), at the bottom (*`Bottom`*), and at the right
(*`Right`*). Positive values results in a smaller, negative
values in a larger size. If all parameters are set to zero, the
region remains unchanged.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Input image.

**`ImagePart`** (output_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Image area.

**`Top`** (input_control)  integer `→`  (integer)

Number of rows clipped at the top.

Default:
-1

Suggested values:
-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

**`Left`** (input_control)  integer `→`  (integer)

Number of columns clipped at the left.

Default:
-1

Suggested values:
-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

**`Bottom`** (input_control)  integer `→`  (integer)

Number of rows clipped at the bottom.

Default:
-1

Suggested values:
-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

**`Right`** (input_control)  integer `→`  (integer)

Number of columns clipped at the right.

Default:
-1

Suggested values:
-20, -10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

## Result

`crop_domain_rel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`reduce_domain`,
`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Alternatives

`crop_domain`,
`crop_rectangle1`

## See also

`smallest_rectangle1`,
`intersection`,
`gen_rectangle1`,
`clip_region`

## Module

Foundation
