# GenRandomRegion (Operator)

## Name

`GenRandomRegion` — Create a random region.

## Signature

`static void HOperatorSet.GenRandomRegion(out HObject regionRandom, HTuple width, HTuple height)`

`void HRegion.GenRandomRegion(int width, int height)`

## Description

The operator `GenRandomRegion` returns a random region.
During this process every pixel in the image area
[0...*`width`*-1]
[0...*`height`*-1] is adapted into the region with
the probability 0.5.
The created region can be imagined as the
threshold formation in an image with noise.

This procedure is particularly important for the creation of uncorrelated
binary patterns.

The random pattern is generated using the C function “nrand48()”.
See the parameter *"seed_rand"* of [`SetSystem`](set_system.md) for
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

**`regionRandom`** (output_object)  region `→` [HRegion](HRegion.md)

Created random region with expansion
*`width`* x *`height`*.

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

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

If the parameter values are correct, the operator `GenRandomRegion`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`PaintRegion`,
`ReduceDomain`

## See also

`GenCheckerRegion`,
`AddNoiseDistribution`,
`AddNoiseWhite`,
`ReduceDomain`

## Module

Foundation
