# ObjDiff (Operator)

## Name

`ObjDiff` — Calculate the difference of two object tuples.

## Signature

`static void HOperatorSet.ObjDiff(HObject objects, HObject objectsSub, out HObject objectsDiff)`

`HObject HObject.ObjDiff(HObject objectsSub)`

`HImage HImage.ObjDiff(HImage objectsSub)`

`HRegion HRegion.ObjDiff(HRegion objectsSub)`

`HXLD HXLD.ObjDiff(HXLD objectsSub)`

`HXLDCont HXLDCont.ObjDiff(HXLDCont objectsSub)`

`HXLDPoly HXLDPoly.ObjDiff(HXLDPoly objectsSub)`

`HXLDPara HXLDPara.ObjDiff(HXLDPara objectsSub)`

`HXLDModPara HXLDModPara.ObjDiff(HXLDModPara objectsSub)`

`HXLDExtPara HXLDExtPara.ObjDiff(HXLDExtPara objectsSub)`

## Description

`ObjDiff` calculates the set-theoretic difference of
two object tuples:
(objects in Objects) - (objects in ObjectsSub)
The resulting object tuple *`objectsDiff`*
is defined as the input tuple
*`objects`* with all objects from *`objectsSub`* removed.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Attention

Image matrices and XLDs are not compared regarding their contents. Thus,
two images or XLDs, respectively, are “equal” if they are located
at the same place in the storage.
By contrast, regions that are not located at the same place in the
storage are compared regarding their actual contents.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` [HObject](HObject.md)

Object tuple 1.

**`objectsSub`** (input_object)  object(-array) `→` [HObject](HObject.md)

Object tuple 2.

**`objectsDiff`** (output_object)  object(-array) `→` [HObject](HObject.md)

Objects from *`objects`* that are not part of
*`objectsSub`*.

## Result

`ObjDiff` always returns 2 (
H_MSG_TRUE)
.

## See also

`TestEqualObj`,
`CountObj`,
`CopyObj`,
`SelectObj`

## Module

Foundation
