# SegmentImageMser (Operator)

## Name

`SegmentImageMser` — Segment image using Maximally Stable Extremal Regions (MSER).

## Signature

`static void HOperatorSet.SegmentImageMser(HObject image, out HObject MSERDark, out HObject MSERLight, HTuple polarity, HTuple minArea, HTuple maxArea, HTuple delta, HTuple genParamName, HTuple genParamValue)`

`HRegion HImage.SegmentImageMser(out HRegion MSERLight, string polarity, HTuple minArea, HTuple maxArea, HTuple delta, HTuple genParamName, HTuple genParamValue)`

`HRegion HImage.SegmentImageMser(out HRegion MSERLight, string polarity, int minArea, int maxArea, int delta, HTuple genParamName, HTuple genParamValue)`

## Description

`SegmentImageMser` segments an image into regions of
homogenous gray values using the approach of Maximally Stable Extremal
Regions (MSER). The segmentation process determines if a region is
homogenous by observing the local region surrounding. Therefore, the
operator is particularly suited to robustly segment objects in front
of inhomogeneous background or in applications with changing
illumination.

**Parameters**

- ***`polarity`*** —

  The *`polarity`* determines the type of the regions that are extracted.

  | Value | Meaning |
  | --- | --- |
  | *"dark"* | Only MSERs that are darker than their surroundings are extracted |
  | *"light"* | Only MSERs that are lighter than their surroundings are extracted |
  | *"both"* (default) | Both types of MSERs are extracted |
- ***`minArea`*, *`maxArea`*** —

  The values *`minArea`* and *`maxArea`* restrict the size
  of the returned MSERs.

  Note that very small values of *`minArea`*, e.g., values
  smaller than 5, can increase the runtime significantly, especially
  for noisy images.

  If *`maxArea`* is set to an empty tuple (default), the MSERs are
  restricted to be true subsets of the connected components of the
  input domain.
- ***`delta`*** —

  The value of *`delta`* influences the selectivity of the
  algorithm. Larger values lead to fewer MSERs. Smaller values lead
  to more MSERs.

  Please read the description of the segmentation process below to
  help understand the effect of this parameter.

The following generic parameters can be used to fine-tune the
segmentation of MSERs. The generic parameters can be set with
*`genParamName`* and *`genParamValue`*.

- ***"max_variation"*:** —

  The maximum variation of a component's area within the range of
  $\pm$ *`delta`* thresholds. Larger values lead
  to more MSERs. Smaller values lead to fewer MSERs.

  Please read the description of the segmentation process below for a
  definition of 'variation' and to help understand the effect of this
  generic parameter.

  Suggested values:
   *0.1*, *0.2*, *0.5*,
  *1.0*, *2.0*, *5.0*

  Default:
   *0.2*

  Restriction:
   real values lager than or equal to *0.0*.
- ***"min_diversity"*:** —

  The minimum relative difference of the sizes of two overlapping
  MSERs. Smaller values lead to more overlapping MSERs. Larger values
  lead to fewer overlapping MSERs.

  Please read the description of the segmentation process below for a
  definition of 'diversity' and to help understand the effect of this
  generic parameter.

  Setting *"min_diversity"* very close to *0.0* may increase the
  runtime.

  Suggested values:
   *0.1*, *0.5*, *0.8*,
  *1.0*, *2.0*, *5.0*

  Default:
   *0.8*

  Restriction:
   real values larger than or equal to *0.0*.
- ***"may_touch_border"*:** —

  Controls if regions that touch the border of the input domain are
  returned (*"true"*) or rejected (*"false"*).

  List of values:
   *"false"*, *"true"*

  Default:
   *"false"* if a full domain is used,
  *"true"* if the input domain is reduced.
- ***"min_gray"*, *"max_gray"*:** —

  The values *"min_gray"* and *"max_gray"* reduce the input
  domain dynamically by applying a [`Threshold`](threshold.md) to the input image.
  All pixels outside the specified gray value range are ignored in the
  segmentation process. This may reduce the runtime considerably.

  Please note, that if *`image`* has a full domain and the domain is
  reduced by the settings of *"min_gray"* or *"max_gray"*,
  the default behavior of *"may_touch_border"* may lead to more
  result regions than without restricted gray value range.

  Default:
   *"min_gray"*: 0, *"max_gray"*: *255* for
  byte images, *65535* for uint2 images

  Restriction:
   integer values larger than or equal to *0*.

**Segmentation Process**

In a first step, the image is segmented with all threshold values t,
from 0 to the maximal present gray value.

To illustrate this, the following example input image with twelve gray
values (0...11) is used. On the right, the boundaries of the resulting
threshold regions are shown.

|  |  |
| --- | --- |
| figure Example input image with twelve gray values reaching from 0 (= black) to 11 (= white) | figure Boundaries of the threshold regions for all thresholds (t = 0...11) |

The resulting threshold regions are split into their connected
components (4-connected neighborhood) and the area increase of the individual
components is monitored over the increasing thresholds. The area of each
individual component increases monotonically with each (increasing)
threshold. An MSER is a component whose area does not vary significantly
within the range of $\pm$ *`delta`* thresholds. To be
accepted as an MSER, the variation of the component's area within the
range of $\pm$ *`delta`* thresholds must be a
local minimum and it must be lower than *"max_variation"*.
Furthermore, the diversity of overlapping MSERs must be greater than
*"min_diversity"* (see below).

The variation of a component's area is defined by

$$\mathrm{Variation}_t = \frac{\mathrm{area}_{t+\Delta} - \mathrm{area}_{t-\Delta}}{\mathrm{area}_t}$$ ![figure](../assets/3718293fce12e67d.svg)
where
$$area_{t-\Delta} = area_0, \quad t - \Delta < 0 \\\narea_{t+\Delta} = area_{t_{max}}, \quad t + \Delta > t_{max}$$ ![figure](../assets/aa885e1f2ce03576.svg)

Decreasing the value of *"max_variation"* will reduce the
number of accepted regions.

In our example, each threshold region consists of only one component.
Therefore, the terms 'threshold region' and 'component' are used
synonymously hereinafter. The following table shows the area of the
threshold regions and their variations for *`delta`* set to 1 and
for *`delta`* set to 2.

| Threshold value t | Threshold region | Area of the threshold region | Variation of the area (for *`delta`* = 1) | Variation of the area (for *`delta`* = 2) |
| --- | --- | --- | --- | --- |
| 0 | figure | 320 | **0.28** | **0.53** |
| 1 | figure | 410 | 0.41 | 0.54 |
| 2 | figure | 490 | 0.27 | 0.49 |
| 3 | figure | 540 | 0.13 | 0.31 |
| 4 | figure | 560 | **0.07** | **0.25** |
| 5 | figure | 580 | 0.12 | 0.29 |
| 6 | figure | 630 | 0.21 | 0.38 |
| 7 | figure | 710 | 0.24 | 0.44 |
| 8 | figure | 800 | 0.23 | **0.41** |
| 9 | figure | 890 | **0.18** | 1.67 |
| 10 | figure | 960 | 1.36 | 1.46 |
| 11 | figure | 2200 | **0.56** | **0.60** |

The area of the threshold regions increases with the threshold value
t. If *`delta`* is set to 1, the local minima of the variation
are obtained for the threshold values t = 0, t = 4, t = 9, and t = 11.
Therefore, the threshold regions for t = 0, t = 4, t = 9, and t = 11
are MSER candidates. If *`delta`* is set to 2, the MSER
candidates correspond to the threshold regions for t = 0, t = 4, t =
8, t = 11.

Per default, the connected components of
the image domain will not be returned as MSER. This behavior can
be altered by explicitly setting *`maxArea`* to a value larger
than the area of the input domain and *"may_touch_border"* to
*"true"*. In our example, the default behavior eliminates the
MSER candidates that correspond to the threshold regions for t = 11.

The following figure shows the resulting MSER candidates for
*`delta`* = 1 and for *`delta`* = 2 (with *"max_variation"*
set to 1.0), overlaid over the input image.

| MSER candidates for Delta = 1 | MSER candidates for Delta = 2 |
| --- | --- |
| figure corresponds to t = 0 | figure corresponds to t = 0 |
| figure corresponds to t = 4 | figure corresponds to t = 4 |
| figure corresponds to t = 9 | figure corresponds to t = 8 |

The MSER segmentation does not divide the image into disjunct regions,
but rather determines all MSERs within the input image. Hence for one
image, multiple mutual overlapping regions may be returned as MSER
candidates. Since the MSERs are calculated by continuously increasing
the threshold t, two regions that overlap each other always consist of
a larger region that completely contains the smaller one. The
'diversity' measures, how much the areas of two overlapping MSERs
differ. It is calculated as the relative difference of the areas of
the two MSER candidates:
$$\text{diversity}_{i} = \frac{\text{area}_{i+1} - \text{area}_{i}}{\text{area}_{i}}$$ ![figure](../assets/a8016b6d9b55a198.svg)
where
$area_{i}$: is the area of the currently examined MSER candidate
and $area_{i+1}$: is the area of the MSER candidate that
contains the currently examined MSER candidate.

If the diversity of an MSER candidate is smaller than
*"min_diversity"*, it is discarded. Hence the parameter
*"min_diversity"* is used to control the amount of overlapping
regions. Higher values of *"min_diversity"* reduce the number
of overlapping regions and lower values increase it. Note that the
largest MSER candidates, i.e., those candidates that are not contained
in another MSER candidate are always kept.

|  | MSER candidate index i | Threshold value t | Area of the threshold region | Diversity of the MSER candidate |
| --- | --- | --- | --- | --- |
|  | 0 | 0 | 320 | 0.75 |
| **Delta=1** | 1 | 4 | 560 | 0.59 |
|  | 2 | 9 | 890 | N/A |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 0 | 0 | 320 | 0.75 |
| **Delta=2** | 1 | 4 | 560 | 0.43 |
|  | 2 | 8 | 800 | N/A |

First, the MSER candidate with the smallest diversity is eliminated if
its diversity is less than *"min_diversity"*. In our example,
the value for *"min_diversity"* is set to 0.5. For delta = 2,
the MSER candidate with the diversity of 0.43 is eliminated. Then, the
diversity is recalculated for the remaining MSER candidates. In our
example, this yields a diversity of 1.5 for the MSER candidate 0. Now,
all remaining MSER candidates have a diversity greater than 0.5 and
are therefore accepted as MSERs.

The segmentation process calculates MSERs for each connected component
of the input domain independently.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`MSERDark`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segmented dark MSERs.

**`MSERLight`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segmented light MSERs.

**`polarity`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

The polarity of the returned MSERs.

Default:
"both"

List of values:
"both", "dark", "light"

**`minArea`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Minimal size of an MSER.

Default:
10

Suggested values:
1, 10, 100, 10000

Value range:
`1
≤
minArea`

**`maxArea`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / double)

Maximal size of an MSER.

Default:
[]

Suggested values:
1, 10, 100, 10000

Value range:
`1
≤
maxArea`

**`delta`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Amount of thresholds for which a region needs to be
stable.

Default:
15

Suggested values:
5, 10, 20, 50

Value range:
`1
≤
delta
≤
65535`

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

List of generic parameter names.

Default:
[]

List of values:
"max_gray", "max_variation", "may_touch_border", "min_diversity", "min_gray"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long)

List of generic parameter values.

Default:
[]

Suggested values:
0.5, 0.8, "true", "false", 30, 50, 200, 230

## Example (HDevelop)

```
read_image (Image,'pellets')
segment_image_mser (Image, MSERDark, MSERLight, 'light',\
                    1000, 10000, 3, [],[])
```

## Result

`SegmentImageMser` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Successors

`SelectShape`,
`SelectGray`

## Alternatives

`AutoThreshold`,
`BinaryThreshold`,
`CharThreshold`,
`LocalThreshold`,
`Watersheds`,
`Regiongrowing`

## References

J. Matas, O. Chum, M. Urban, and T. Pajdla: “Robust wide baseline stereo
from maximally stable extremal regions.”; Proc. of British Machine Vision
Conference, pages 384-396; 2002.

## Module

Foundation
