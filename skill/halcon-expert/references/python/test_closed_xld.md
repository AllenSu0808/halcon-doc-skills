# test_closed_xld (Operator)

## Name

`test_closed_xld` — Test whether contours or polygons are closed.

## Signature

`def test_closed_xld(xld: HObject) -> Sequence[int]`

`def test_closed_xld_s(xld: HObject) -> int`

## Description

`test_closed_xld` tests each contour or polygon in
*`xld`*, whether it is closed and returns the result in
*`is_closed`*. If the contour contour or polygon is closed, the
respective return value is 1, otherwise 0. A contour or polygon is
closed, if its last point is equal to its first point.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be tested.

**`is_closed`** (output_control)  integer(-array) `→` Sequence[int]

Tuple with Boolean numbers.

## Possible Predecessors

`gen_contour_region_xld`,
`edges_sub_pix`

## Module

Foundation
