# remove_obj (Operator)

## Name

`remove_obj` — Remove objects from an iconic object tuple.

## Signature

`def remove_obj(objects: HObject, index: MaybeSequence[int]) -> HObject`

## Description

`remove_obj` removes the elements referred by *`index`* from
the tuple *`objects`* and returns the rest in the tuple *`objects_reduced`*.
*`index`* determines the index of the elements to remove. Note that, in
contrast to control tuples, indices for the object tuple elements start at 1,
i.e. the first tuple element has got the index 1. Duplicates and indices
out of range are ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` HObject

Input object tuple.

**`objects_reduced`** (output_object)  object(-array) `→` HObject

Remaining object tuple.

**`index`** (input_control)  number(-array) `→` MaybeSequence[int]

Indices of the objects to be removed.

## Example (HDevelop)

```
gen_empty_obj (Images)
for Index := 1 to 10 by 1
  gen_image_const (Image, 'byte', Index, Index)
  concat_obj (Images, Image, Images)
endfor

remove_obj (Images, Images, [7, 4])
```

## Alternatives

`select_obj`

## See also

`count_obj`,
`select_obj`,
`copy_obj`,
`insert_obj`

## Module

Foundation
