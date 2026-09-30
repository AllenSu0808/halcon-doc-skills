# gen_random_region (Operator)

## Name

`gen_random_region` — Create a random region.

## Signature

`def gen_random_region(width: int, height: int) -> HObject`

## Description

The operator `gen_random_region` returns a random region.
During this process every pixel in the image area
[0...*`width`*-1]
[0...*`height`*-1] is adapted into the region with
the probability 0.5.
The created region can be imagined as the
threshold formation in an image with noise.

This procedure is particularly important for the creation of uncorrelated
binary patterns.

The random pattern is generated using the C function “nrand48()”.
See the parameter *"seed_rand"* of [`set_system`](set_system.md) for
information on the used random seed.

## Attention

If *`width`* and *`height`* are chosen large
(> 100) the created region may require much storage space due to
the internally used runlength coding.
The gray values of the output region are undefined.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region_random`** (output_object)  region `→` HObject

Created random region with expansion
*`width`* x *`height`*.

**`width`** (input_control)  extent.x `→` int

Maximum horizontal expansion of random region.

Default:
128

Suggested values:
16, 32, 50, 64, 100, 128, 256, 300, 400, 512

Value range:
`width` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Width > 0`

**`height`** (input_control)  extent.y `→` int

Maximum vertical expansion of random region.

Default:
128

Suggested values:
16, 32, 50, 64, 100, 128, 256, 300, 400, 512

Value range:
`height` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Height > 0`

## Complexity

The worst case for the storage complexity for the
created region (in byte) is: O(Width * Height * 2).

## Result

If the parameter values are correct, the operator `gen_random_region`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`paint_region`,
`reduce_domain`

## See also

`gen_checker_region`,
`add_noise_distribution`,
`add_noise_white`,
`reduce_domain`

## Module

Foundation
