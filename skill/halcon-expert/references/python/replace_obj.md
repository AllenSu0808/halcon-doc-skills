# replace_obj (Operator)

## Name

`replace_obj` — Replaces one or more elements of an iconic object tuple.

## Signature

`def replace_obj(objects: HObject, objects_replace: HObject, index: MaybeSequence[int]) -> HObject`

## Description

`replace_obj` replaces one or more elements of the
iconic input tuple *`objects`* and returns them with *`replaced`*.
At this, *`index`* determines the indices of the elements
and *`objects_replace`* the corresponding objects to replace.
The parameter *`index`* must contain one or more integer values
(any floating point number must represent an integer value without
fraction). Indices of iconic object elements start at 1.
If *`objects_replace`* contains only
one value, this value will be replaced at all indices of *`index`*.
If a value of *`index`* is greater than the length of the iconic input
object tuple *`objects`*, *`replaced`* will be extended
accordingly and initialized with empty regions.

### Exception: Empty input object

If either *`index`* or *`objects_replace`* is empty and the other is
not, an exception is raised. If both are empty, the output object tuple
*`replaced`* corresponds to the input *`objects`*. If both are not
empty, but the input *`objects`* is, the empty object will be
extended as described above.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` HObject

Iconic Input Object.

**`objects_replace`** (input_object)  object(-array) `→` HObject

Element(s) to replace.

**`replaced`** (output_object)  object(-array) `→` HObject

Tuple with replaced elements.

**`index`** (input_control)  number(-array) `→` MaybeSequence[int]

Index/Indices of elements to be replaced.

## Example (HDevelop)

```
gen_empty_obj (Images)
for Index := 1 to 10 by 1
  gen_image_const (Image, 'byte', Index, Index)
  concat_obj (Images, Image, Images)
endfor
gen_empty_obj (Replace)

replace_obj (Images, Replace, Images, 1)
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
