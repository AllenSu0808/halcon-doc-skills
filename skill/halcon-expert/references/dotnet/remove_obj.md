# RemoveObj (Operator)

## Name

`RemoveObj` — Remove objects from an iconic object tuple.

## Signature

`static void HOperatorSet.RemoveObj(HObject objects, out HObject objectsReduced, HTuple index)`

`HObject HObject.RemoveObj(HTuple index)`

`HObject HObject.RemoveObj(int index)`

`HImage HImage.RemoveObj(HTuple index)`

`HImage HImage.RemoveObj(int index)`

`HRegion HRegion.RemoveObj(HTuple index)`

`HRegion HRegion.RemoveObj(int index)`

`HXLD HXLD.RemoveObj(HTuple index)`

`HXLD HXLD.RemoveObj(int index)`

`HXLDCont HXLDCont.RemoveObj(HTuple index)`

`HXLDCont HXLDCont.RemoveObj(int index)`

`HXLDPoly HXLDPoly.RemoveObj(HTuple index)`

`HXLDPoly HXLDPoly.RemoveObj(int index)`

`HXLDPara HXLDPara.RemoveObj(HTuple index)`

`HXLDPara HXLDPara.RemoveObj(int index)`

`HXLDModPara HXLDModPara.RemoveObj(HTuple index)`

`HXLDModPara HXLDModPara.RemoveObj(int index)`

`HXLDExtPara HXLDExtPara.RemoveObj(HTuple index)`

`HXLDExtPara HXLDExtPara.RemoveObj(int index)`

## Description

`RemoveObj` removes the elements referred by *`index`* from
the tuple *`objects`* and returns the rest in the tuple *`objectsReduced`*.
*`index`* determines the index of the elements to remove. Note that, in
contrast to control tuples, indices for the object tuple elements start at 1,
i.e. the first tuple element has got the index 1. Duplicates and indices
out of range are ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` [HObject](HObject.md)

Input object tuple.

**`objectsReduced`** (output_object)  object(-array) `→` [HObject](HObject.md)

Remaining object tuple.

**`index`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

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

`SelectObj`

## See also

`CountObj`,
`SelectObj`,
`CopyObj`,
`InsertObj`

## Module

Foundation
