# transpose_region (Operator)

## Name

`transpose_region` — Reflect a region about a point.

## Signature

`transpose_region(Region : Transposed : Row, Column : )`

## Description

`transpose_region` reflects a region about a point. The fixed
point is given by *`Column`* and *`Row`*. The image
P' of a point P is determined by the following requirement:

If P = S, then P' = S, i.e., the point S is the fixed point of
the mapping. If $P \neq S$ ![figure](../assets/60d3def307b099e6.svg), S is the center point of
a line segment connecting P and P'. Therefore, the following
equations result:
$$Column = \frac{x + x'}{2} \\\nRow = \frac{y + y'}{2}.$$ ![figure](../assets/c3a251b7920e0270.svg)
If *`Row`* and *`Column`* are set to the origin, the
in morphology often used transposition results. Hence
`transpose_region` is often used to reflect (transpose) a
structuring element.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region to be reflected.

**`Transposed`** (output_object)  region(-array) `→` object

Transposed region.

**`Row`** (input_control)  point.y `→`  (integer)

Row coordinate of the reference point.

Default:
0

Suggested values:
0, 64, 128, 256, 512

Value range:
`0
≤
Row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Column`** (input_control)  point.x `→`  (integer)

Column coordinate of the reference point.

Default:
0

Suggested values:
0, 64, 128, 256, 512

Value range:
`0
≤
Column
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let F be the area of the input region. Then the runtime
complexity for one region is
$$O\big(\sqrt{F}\big).$$ ![figure](../assets/e1d1bb78940914b4.svg)

## Result

`transpose_region` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty or no input region can be
set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## See also

`dilation1`,
`opening`,
`closing`

## Module

Foundation
