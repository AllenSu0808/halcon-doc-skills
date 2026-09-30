# insert_obj (Operator)

## Name

`insert_obj` — Insert objects into an iconic object tuple.

## Signature

`insert_obj(Objects, ObjectsInsert : ObjectsExtended : Index : )`

## Description

`insert_obj` inserts the elements of *`ObjectsInsert`* at
*`Index`* into the object tuple *`Objects`* and returns the
result in *`ObjectsExtended`*.

*`Index`* must contain a single integer value. Note that, in contrast
to control tuples, indices of object tuple elements start at 1. The length
of *`ObjectsExtended`* is the sum of the length of *`Objects`*
and *`ObjectsInsert`*.
It is allowed to mix images, regions and XLDs in *`Objects`* and
*`ObjectsInsert`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Objects`** (input_object)  object(-array) `→` object

Input object tuple.

**`ObjectsInsert`** (input_object)  object(-array) `→` object

Object tuple to insert.

**`ObjectsExtended`** (output_object)  object(-array) `→` object

Extended object tuple.

**`Index`** (input_control)  number `→`  (integer)

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

Typical runtime complexity: O(|*`Objects`*| + |*`ObjectsInsert`*|).

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
