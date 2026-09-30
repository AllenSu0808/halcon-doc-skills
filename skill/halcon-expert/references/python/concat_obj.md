# concat_obj (Operator)

## Name

`concat_obj` — Concatenate two iconic object tuples.

## Signature

`def concat_obj(objects_1: HObject, objects_2: HObject) -> HObject`

## Description

`concat_obj` concatenates the two tuples of iconic objects
*`objects_1`* and *`objects_2`* into a new tuple of iconic objects
*`objects_concat`*. Hence, this tuple contains all the iconic
objects of the two input tuples:

*`objects_concat`* = [*`objects_1`*,*`objects_2`*]

In *`objects_concat`*, the objects of *`objects_1`* are stored
first, followed by the objects of *`objects_2`*, i.e., the order
of the objects is preserved. Note that only references to the
corresponding images and regions are stored in *`objects_concat`*,
i.e., no new memory is allocated. Furthermore, this means that
modifications of input images, e.g., with [`set_grayval`](set_grayval.md),
[`overpaint_gray`](overpaint_gray.md), or [`overpaint_region`](overpaint_region.md) directly affect
the images of the output tuple *`objects_concat`* and vice versa.

`concat_obj` should not be confused with
[`union1`](union1.md) or [`union2`](union2.md), in which regions are
merged, i.e., in which the number of objects is modified.

`concat_obj` can be used to concatenate objects of different
image object types (e.g., images and XLD contours) into a single
object. This is only recommended if it is necessary to accumulate
in a single object variable, for example, the results of an image
processing sequence. It should be noted that the only operators
that can handle such object tuples of mixed type are
`concat_obj`, [`copy_obj`](copy_obj.md), [`select_obj`](select_obj.md), and
[`disp_obj`](disp_obj.md).

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects_1`** (input_object)  object(-array) `→` HObject

Object tuple 1.

**`objects_2`** (input_object)  object(-array) `→` HObject

Object tuple 2.

**`objects_concat`** (output_object)  object-array `→` HObject

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
O(|*`objects_1`*| + |*`objects_2`*|);

Memory complexity of the result objects:
O(|*`objects_1`*| + |*`objects_2`*|)

## Result

`concat_obj` returns 2 (
H_MSG_TRUE)
if all objects are contained in
the HALCON database. If the input is empty the behavior can be
set via `set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## See also

`count_obj`,
`copy_obj`,
`select_obj`,
`disp_obj`

## Module

Foundation
