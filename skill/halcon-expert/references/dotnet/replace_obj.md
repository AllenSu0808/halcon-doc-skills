# ReplaceObj (Operator)

## Name

`ReplaceObj` — Replaces one or more elements of an iconic object tuple.

## Signature

`static void HOperatorSet.ReplaceObj(HObject objects, HObject objectsReplace, out HObject replaced, HTuple index)`

`HObject HObject.ReplaceObj(HObject objectsReplace, HTuple index)`

`HObject HObject.ReplaceObj(HObject objectsReplace, int index)`

`HImage HImage.ReplaceObj(HImage objectsReplace, HTuple index)`

`HImage HImage.ReplaceObj(HImage objectsReplace, int index)`

`HRegion HRegion.ReplaceObj(HRegion objectsReplace, HTuple index)`

`HRegion HRegion.ReplaceObj(HRegion objectsReplace, int index)`

`HXLD HXLD.ReplaceObj(HXLD objectsReplace, HTuple index)`

`HXLD HXLD.ReplaceObj(HXLD objectsReplace, int index)`

`HXLDCont HXLDCont.ReplaceObj(HXLDCont objectsReplace, HTuple index)`

`HXLDCont HXLDCont.ReplaceObj(HXLDCont objectsReplace, int index)`

`HXLDPoly HXLDPoly.ReplaceObj(HXLDPoly objectsReplace, HTuple index)`

`HXLDPoly HXLDPoly.ReplaceObj(HXLDPoly objectsReplace, int index)`

`HXLDPara HXLDPara.ReplaceObj(HXLDPara objectsReplace, HTuple index)`

`HXLDPara HXLDPara.ReplaceObj(HXLDPara objectsReplace, int index)`

`HXLDModPara HXLDModPara.ReplaceObj(HXLDModPara objectsReplace, HTuple index)`

`HXLDModPara HXLDModPara.ReplaceObj(HXLDModPara objectsReplace, int index)`

`HXLDExtPara HXLDExtPara.ReplaceObj(HXLDExtPara objectsReplace, HTuple index)`

`HXLDExtPara HXLDExtPara.ReplaceObj(HXLDExtPara objectsReplace, int index)`

## Description

`ReplaceObj` replaces one or more elements of the
iconic input tuple *`objects`* and returns them with *`replaced`*.
At this, *`index`* determines the indices of the elements
and *`objectsReplace`* the corresponding objects to replace.
The parameter *`index`* must contain one or more integer values
(any floating point number must represent an integer value without
fraction). Indices of iconic object elements start at 1.
If *`objectsReplace`* contains only
one value, this value will be replaced at all indices of *`index`*.
If a value of *`index`* is greater than the length of the iconic input
object tuple *`objects`*, *`replaced`* will be extended
accordingly and initialized with empty regions.

### Exception: Empty input object

If either *`index`* or *`objectsReplace`* is empty and the other is
not, an exception is raised. If both are empty, the output object tuple
*`replaced`* corresponds to the input *`objects`*. If both are not
empty, but the input *`objects`* is, the empty object will be
extended as described above.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` [HObject](HObject.md)

Iconic Input Object.

**`objectsReplace`** (input_object)  object(-array) `→` [HObject](HObject.md)

Element(s) to replace.

**`replaced`** (output_object)  object(-array) `→` [HObject](HObject.md)

Tuple with replaced elements.

**`index`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

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

`SelectObj`

## See also

`CountObj`,
`SelectObj`,
`CopyObj`,
`InsertObj`

## Module

Foundation
