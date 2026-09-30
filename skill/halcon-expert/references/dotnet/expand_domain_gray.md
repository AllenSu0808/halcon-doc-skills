# ExpandDomainGray (Operator)

## Name

`ExpandDomainGray` — Expand the domain of an image and set the gray values in the
expanded domain.

## Signature

`static void HOperatorSet.ExpandDomainGray(HObject inputImage, out HObject expandedImage, HTuple expansionRange)`

`HImage HImage.ExpandDomainGray(int expansionRange)`

## Description

`ExpandDomainGray` expands the border gray values of the
domain outwards. The width of the expansion is set by the parameter
*`expansionRange`*, which describes the expansion radius in pixels.
All filters in HALCON which are applied to the image domain also include
the gray values of a certain number of pixels, depending on the filter size,
outside of the image domain in their calculation.
This may lead to undesirable side effects especially in the border region
of the domain. For example, if the foreground (domain) and the
background of the image differ strongly in brightness, the result of
a filter operation may lead to undesired darkening or brightening at
the border of the domain. In order to avoid this drawback, the
domain is artificially expanded by `ExpandDomainGray` in a preliminary
stage, copying the gray values of the border pixels to the outside
of the domain. In addition, the domain itself is also expanded to
reflect the newly set pixels. Therefore, in many cases it is
reasonable to reduce the domain again ([`ReduceDomain`](reduce_domain.md) or
[`ChangeDomain`](change_domain.md)) after using `ExpandDomainGray` and
call the filter operation afterwards.
*`expansionRange`* should be set to a value high enough to
make sure the whole region including its dilatation through the filter
mask has initialized values.
Usually this leads to *`expansionRange`* values of half the filter
length or greater.
In combination with the filter [`MeanImage`](mean_image.md)
on images of type real we recommend to determine the value for
*`expansionRange`* as shown in the example below.
For speed reasons this filter uses the values from pixels within the
smallest rectangle around the dilated region.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`inputImage`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int1 / int2 / uint2 / int4 / real)

Input image with domain to be expanded.

**`expandedImage`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / int1 / int2 / uint2 / int4 / real)

Output image with new gray values in the
expanded domain.

**`expansionRange`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Radius of the gray value expansion, measured in
pixels.

Default:
2

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16

Restriction:
`ExpansionRange >= 1`

## Example (HDevelop)

```
read_image(Fabrik, 'fabrik')
gen_rectangle2(Rectangle_Label,243,320,-1.55,62,28)
reduce_domain(Fabrik, Rectangle_Label, Fabrik_Label)
* Character extraction without gray value expansion:
MaskSize := 31
mean_image(Fabrik_Label,Label_Mean_normal,MaskSize, MaskSize)
dyn_threshold(Fabrik_Label,Label_Mean_normal,Characters_normal,10,'dark')
dev_display(Fabrik)
dev_display(Characters_normal)
* The characters in the border region are not extracted !
stop()
* Character extraction with gray value expansion:
get_domain (Fabrik_Label, Domain)
expand_domain_gray (Fabrik_Label, Expanded_Fabrik_Label, MaskSize)
get_domain (Expanded_Fabrik_Label, Expanded_Domain)
shape_trans (Expanded_Domain, RegionRect, 'rectangle1')
difference (RegionRect, Expanded_Domain, Region_Difference)
overpaint_region (Expanded_Fabrik_Label, Region_Difference, 0, 'fill')
reduce_domain (Expanded_Fabrik_Label, Domain, Reduced_Expanded_Fabrik_Label)
mean_image (Reduced_Expanded_Fabrik_Label, Label_Mean_Expanded,\
MaskSize, MaskSize)
dyn_threshold(Fabrik_Label,Label_Mean_Expanded,\
Characters_expanded,10,'dark')
dev_display(Fabrik)
dev_display(Characters_expanded)
```

## Complexity

Let L the perimeter of the domain. Then the runtime complexity is
approximately O(L)**`expansionRange`*.

## Result

`ExpandDomainGray` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`ReduceDomain`

## Possible Successors

`ReduceDomain`,
`MeanImage`,
`DynThreshold`

## See also

`ReduceDomain`,
`MeanImage`

## Module

Foundation
