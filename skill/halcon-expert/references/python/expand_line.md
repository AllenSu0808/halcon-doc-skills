# expand_line (Operator)

## Name

`expand_line` — Expand a region starting at a given line.

## Warning

**`expand_line` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def expand_line(image: HObject, coordinate: int, expand_type: str, row_column: str, threshold: Union[int, float]) -> HObject`

## Description

`expand_line` generates a region by expansion, starting at a given line
(row or column). The expansion is terminated when the current gray value
differs by more than *`threshold`* from the mean gray value along the
line (*`expand_type`* = *"mean"*) or from the previously added
gray value (*`expand_type`* = *"gradient"*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Input image.

**`region_expand`** (output_object)  region(-array) `→` HObject

Extracted segments.

**`coordinate`** (input_control)  integer `→` int

Row or column coordinate.

Default:
256

Suggested values:
16, 64, 128, 200, 256, 300, 400, 511

Restriction:
`Coordinate >= 0`

**`expand_type`** (input_control)  string `→` str

Stopping criterion.

Default:
"gradient"

List of values:
"gradient", "mean"

**`row_column`** (input_control)  string `→` str

Segmentation mode (row or column).

Default:
"row"

List of values:
"column", "row"

**`threshold`** (input_control)  number `→` Union[int, float]

Threshold for the expansion.

Default:
3.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 13.0, 17.0, 20.0, 30.0

Value range:
`0
≤
threshold
≤
255` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`anisotropic_diffusion`,
`median_image`,
`affine_trans_image`,
`rotate_image`

## Possible Successors

`intersection`,
`opening`,
`closing`

## Alternatives

`regiongrowing_mean`,
`expand_gray`,
`expand_gray_ref`

## Module

Foundation
