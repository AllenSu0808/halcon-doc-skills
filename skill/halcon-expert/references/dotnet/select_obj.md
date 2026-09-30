# SelectObj (Operator)

## Name

`SelectObj` — Select objects from an object tuple.

## Signature

`static void HOperatorSet.SelectObj(HObject objects, out HObject objectSelected, HTuple index)`

`HObject HObject.SelectObj(HTuple index)`

`HObject HObject.SelectObj(int index)`

`HImage HImage.SelectObj(HTuple index)`

`HImage HImage.SelectObj(int index)`

`HRegion HRegion.SelectObj(HTuple index)`

`HRegion HRegion.SelectObj(int index)`

`HXLD HXLD.SelectObj(HTuple index)`

`HXLD HXLD.SelectObj(int index)`

`HXLDCont HXLDCont.SelectObj(HTuple index)`

`HXLDCont HXLDCont.SelectObj(int index)`

`HXLDPoly HXLDPoly.SelectObj(HTuple index)`

`HXLDPoly HXLDPoly.SelectObj(int index)`

`HXLDPara HXLDPara.SelectObj(HTuple index)`

`HXLDPara HXLDPara.SelectObj(int index)`

`HXLDModPara HXLDModPara.SelectObj(HTuple index)`

`HXLDModPara HXLDModPara.SelectObj(int index)`

`HXLDExtPara HXLDExtPara.SelectObj(HTuple index)`

`HXLDExtPara HXLDExtPara.SelectObj(int index)`

## Description

`SelectObj` copies the iconic objects with the indices given
by *`index`* (starting with 1) from the iconic input object
tuple *`objects`* to the output object *`objectSelected`*.
No new storage is allocated for the regions and images. Instead,
new objects containing references to the existing objects are
created. The number of objects in an object tuple can be queried
with the operator [`CountObj`](count_obj.md).

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` [HObject](HObject.md)

Input objects.

**`objectSelected`** (output_object)  object(-array) `→` [HObject](HObject.md)

Selected objects.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indices of the objects to be selected.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 100, 200, 500, 1000, 2000, 5000

Restriction:
`Index >= 1`

## Example (C)

```
/* Access to all Regions */

count_obj(Regions,&Num);
for (i=1; i<=Num; i++)
{
  select_obj(Regions,&Single,i);
  T_get_region_polygon(Single,5.0,&Row,&Column);
  T_disp_polygon(WindowHandleTuple,Row,Column);
  destroy_tuple(Row);
  destroy_tuple(Column);
}
```

## Complexity

Runtime complexity: O(|*`objects`*|)

## Result

`SelectObj` returns 2 (
H_MSG_TRUE)
if all objects are contained in
the HALCON database and all parameters are correct. If the input
is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`CountObj`

## Alternatives

`CopyObj`

## See also

`CountObj`,
`ConcatObj`,
`ObjToInteger`

## Module

Foundation
