# replace_obj (Operator)

## Name

`replace_obj` — Replaces one or more elements of an iconic object tuple.

## Signature

`replace_obj(Objects, ObjectsReplace : Replaced : Index : )`

## Description

`replace_obj` replaces one or more elements of the
iconic input tuple *`Objects`* and returns them with *`Replaced`*.
At this, *`Index`* determines the indices of the elements
and *`ObjectsReplace`* the corresponding objects to replace.
The parameter *`Index`* must contain one or more integer values
(any floating point number must represent an integer value without
fraction). Indices of iconic object elements start at 1.
If *`ObjectsReplace`* contains only
one value, this value will be replaced at all indices of *`Index`*.
If a value of *`Index`* is greater than the length of the iconic input
object tuple *`Objects`*, *`Replaced`* will be extended
accordingly and initialized with empty regions.

### Exception: Empty input object

If either *`Index`* or *`ObjectsReplace`* is empty and the other is
not, an exception is raised. If both are empty, the output object tuple
*`Replaced`* corresponds to the input *`Objects`*. If both are not
empty, but the input *`Objects`* is, the empty object will be
extended as described above.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Objects`** (input_object)  object(-array) `→` object

Iconic Input Object.

**`ObjectsReplace`** (input_object)  object(-array) `→` object

Element(s) to replace.

**`Replaced`** (output_object)  object(-array) `→` object

Tuple with replaced elements.

**`Index`** (input_control)  number(-array) `→`  (integer)

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
