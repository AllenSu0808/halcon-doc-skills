# remove_obj (Operator)

## Name

`remove_obj` — Remove objects from an iconic object tuple.

## Signature

`remove_obj(Objects : ObjectsReduced : Index : )`

## Description

`remove_obj` removes the elements referred by *`Index`* from
the tuple *`Objects`* and returns the rest in the tuple *`ObjectsReduced`*.
*`Index`* determines the index of the elements to remove. Note that, in
contrast to control tuples, indices for the object tuple elements start at 1,
i.e. the first tuple element has got the index 1. Duplicates and indices
out of range are ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Objects`** (input_object)  object(-array) `→` object

Input object tuple.

**`ObjectsReduced`** (output_object)  object(-array) `→` object

Remaining object tuple.

**`Index`** (input_control)  number(-array) `→`  (integer)

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
