# zero_crossing (Operator)

## Name

`zero_crossing` — Extract zero crossings from an image.

## Signature

`zero_crossing(Image : RegionCrossing : : )`

## Description

`zero_crossing` returns the zero crossings of the input
image as a region. A pixel is accepted as a zero crossing if its
gray value (in *`Image`*) is zero, or if at least one of its
neighbors of the 4-neighborhood has a different sign.

This operator is intended to be used after edge operators returning
the second derivative of the image (e.g., [`laplace_of_gauss`](laplace_of_gauss.md)),
which were possibly followed by a smoothing operator. In this case,
the zero crossings are (candidates for) edges.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (int1 / int2 / int4 / real)

Input image.

**`RegionCrossing`** (output_object)  region(-array) `→` object

Zero crossings.

## Result

`zero_crossing` usually returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`laplace`,
`laplace_of_gauss`,
`derivate_gauss`

## Possible Successors

`connection`,
`skeleton`,
`boundary`,
`select_shape`,
`fill_up`

## Alternatives

`threshold`,
`dual_threshold`,
`zero_crossing_sub_pix`

## Module

Foundation
