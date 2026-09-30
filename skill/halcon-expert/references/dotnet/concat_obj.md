# ConcatObj (Operator)

## Name

`ConcatObj` — Concatenate two iconic object tuples.

## Signature

`static void HOperatorSet.ConcatObj(HObject objects1, HObject objects2, out HObject objectsConcat)`

`HObject HObject.ConcatObj(HObject objects2)`

`HImage HImage.ConcatObj(HImage objects2)`

`HRegion HRegion.ConcatObj(HRegion objects2)`

`HXLD HXLD.ConcatObj(HXLD objects2)`

`HXLDCont HXLDCont.ConcatObj(HXLDCont objects2)`

`HXLDPoly HXLDPoly.ConcatObj(HXLDPoly objects2)`

`HXLDPara HXLDPara.ConcatObj(HXLDPara objects2)`

`HXLDModPara HXLDModPara.ConcatObj(HXLDModPara objects2)`

`HXLDExtPara HXLDExtPara.ConcatObj(HXLDExtPara objects2)`

## Description

`ConcatObj` concatenates the two tuples of iconic objects
*`objects1`* and *`objects2`* into a new tuple of iconic objects
*`objectsConcat`*. Hence, this tuple contains all the iconic
objects of the two input tuples:

*`objectsConcat`* = [*`objects1`*,*`objects2`*]

In *`objectsConcat`*, the objects of *`objects1`* are stored
first, followed by the objects of *`objects2`*, i.e., the order
of the objects is preserved. Note that only references to the
corresponding images and regions are stored in *`objectsConcat`*,
i.e., no new memory is allocated. Furthermore, this means that
modifications of input images, e.g., with [`SetGrayval`](set_grayval.md),
[`OverpaintGray`](overpaint_gray.md), or [`OverpaintRegion`](overpaint_region.md) directly affect
the images of the output tuple *`objectsConcat`* and vice versa.

`ConcatObj` should not be confused with
[`Union1`](union1.md) or [`Union2`](union2.md), in which regions are
merged, i.e., in which the number of objects is modified.

`ConcatObj` can be used to concatenate objects of different
image object types (e.g., images and XLD contours) into a single
object. This is only recommended if it is necessary to accumulate
in a single object variable, for example, the results of an image
processing sequence. It should be noted that the only operators
that can handle such object tuples of mixed type are
`ConcatObj`, [`CopyObj`](copy_obj.md), [`SelectObj`](select_obj.md), and
[`DispObj`](disp_obj.md).

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects1`** (input_object)  object(-array) `→` [HObject](HObject.md)

Object tuple 1.

**`objects2`** (input_object)  object(-array) `→` [HObject](HObject.md)

Object tuple 2.

**`objectsConcat`** (output_object)  object-array `→` [HObject](HObject.md)

Concatenated objects.

## Example (C)

```
/* generate a tuple of a circle and a rectangle */

gen_circle(&Circle,200.0,400.0,23.0);
gen_rectangle1(&Rectangle,23.0,44.0,203.0,201.0);
concat_obj(Circle,Rectangle,&CircleAndRectangle);
disp_region(CircleAndRectangle,WindowHandle);
```

## Complexity

Runtime complexity:
O(|*`objects1`*| + |*`objects2`*|);

Memory complexity of the result objects:
O(|*`objects1`*| + |*`objects2`*|)

## Result

`ConcatObj` returns 2 (
H_MSG_TRUE)
if all objects are contained in
the HALCON database. If the input is empty the behavior can be
set via `set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## See also

`CountObj`,
`CopyObj`,
`SelectObj`,
`DispObj`

## Module

Foundation
