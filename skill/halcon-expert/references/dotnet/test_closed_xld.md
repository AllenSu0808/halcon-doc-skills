# TestClosedXld (Operator)

## Name

`TestClosedXld` — Test whether contours or polygons are closed.

## Signature

`static void HOperatorSet.TestClosedXld(HObject XLD, out HTuple isClosed)`

`HTuple HXLD.TestClosedXld()`

## Description

`TestClosedXld` tests each contour or polygon in
*`XLD`*, whether it is closed and returns the result in
*`isClosed`*. If the contour contour or polygon is closed, the
respective return value is 1, otherwise 0. A contour or polygon is
closed, if its last point is equal to its first point.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be tested.

**`isClosed`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Tuple with Boolean numbers.

## Possible Predecessors

`GenContourRegionXld`,
`EdgesSubPix`

## Module

Foundation
