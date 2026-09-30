# insert_obj (Operator)

## Name

`insert_obj` — Insert objects into an iconic object tuple.

## Signature

`def insert_obj(objects: HObject, objects_insert: HObject, index: int) -> HObject`

## Description

`insert_obj` inserts the elements of *`objects_insert`* at
*`index`* into the object tuple *`objects`* and returns the
result in *`objects_extended`*.

*`index`* must contain a single integer value. Note that, in contrast
to control tuples, indices of object tuple elements start at 1. The length
of *`objects_extended`* is the sum of the length of *`objects`*
and *`objects_insert`*.
It is allowed to mix images, regions and XLDs in *`objects`* and
*`objects_insert`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` HObject

Input object tuple.

**`objects_insert`** (input_object)  object(-array) `→` HObject

Object tuple to insert.

**`objects_extended`** (output_object)  object(-array) `→` HObject

Extended object tuple.

**`index`** (input_control)  number `→` int

Index to insert objects.

## Example (HDevelop)

```
gen_image_const (Image1, 'byte', 1, 1)
gen_image_const (Image3, 'byte', 3, 3)
concat_obj (Image1, Image3, Images)
gen_image_const (Image, 'byte', 2, 2)
insert_obj (Images, Image, Images, 2)
```

## Complexity

Typical runtime complexity: O(|*`objects`*| + |*`objects_insert`*|).

## Possible Predecessors

`count_obj`

## Possible Successors

`count_obj`

## Alternatives

`concat_obj`

## See also

`count_obj`,
`select_obj`,
`copy_obj`,
`remove_obj`

## Module

Foundation
