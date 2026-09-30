# SelectRegionPoint (Operator)

## Name

`SelectRegionPoint` — Choose all regions containing a given pixel.

## Signature

`static void HOperatorSet.SelectRegionPoint(HObject regions, out HObject destRegions, HTuple row, HTuple column)`

`HRegion HRegion.SelectRegionPoint(int row, int column)`

## Description

The operator `SelectRegionPoint` selects all regions from *`regions`*
containing the test pixel (*`row`*,*`column`*), i.e.:
$$|\texttt{Regions}[n]\cap\{(\texttt{Row},\texttt{Column})\}|=1$$

## Attention

If the regions overlap more than one region might contain the pixel.
In this case all these regions are returned.
If no region contains the indicated pixel the
empty tuple (= no region) is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions to be examined.

**`destRegions`** (output_object)  region-array `→` [HRegion](HRegion.md)

All regions containing the test pixel.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Line index of the test pixel.

Default:
100

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column index of the test pixel.

Default:
100

## Example (HDevelop)

```
read_image(Image,'fabrik')
regiongrowing(Image,Seg,3,3,5,0)
dev_set_color('red')
dev_set_draw('margin')
Button := 1
while (Button == 1)
  get_mbutton(WindowHandle,Row,Column,Button)
  select_region_point(Seg,Single,Row,Column)
  dev_display(Image)
  dev_display(Single)
endwhile
```

## Complexity

If F is the area of the region and N is the number of regions, the
mean runtime complexity is O(ln(sqrt(F)) * N).

## Result

The operator `SelectRegionPoint` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`TestRegionPoint`

## See also

`GetMbutton`,
`GetMposition`

## Module

Foundation
