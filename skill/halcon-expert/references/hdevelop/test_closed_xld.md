# test_closed_xld (Operator)

## Name

`test_closed_xld` — Test whether contours or polygons are closed.

## Signature

`test_closed_xld(XLD : : : IsClosed)`

## Description

`test_closed_xld` tests each contour or polygon in
*`XLD`*, whether it is closed and returns the result in
*`IsClosed`*. If the contour contour or polygon is closed, the
respective return value is 1, otherwise 0. A contour or polygon is
closed, if its last point is equal to its first point.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` object

Contours or polygons to be tested.

**`IsClosed`** (output_control)  integer(-array) `→`  (integer)

Tuple with Boolean numbers.

## Possible Predecessors

`gen_contour_region_xld`,
`edges_sub_pix`

## Module

Foundation
