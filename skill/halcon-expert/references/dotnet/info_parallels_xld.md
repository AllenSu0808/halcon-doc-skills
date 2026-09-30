# InfoParallelsXld (Operator)

## Name

`InfoParallelsXld` — Return information about the gray values of the area enclosed by XLD
parallels.

## Signature

`static void HOperatorSet.InfoParallelsXld(HObject parallels, HObject image, out HTuple qualityMin, out HTuple qualityMax, out HTuple grayMin, out HTuple grayMax, out HTuple standardMin, out HTuple standardMax)`

`void HXLDPara.InfoParallelsXld(HImage image, out double qualityMin, out double qualityMax, out int grayMin, out int grayMax, out double standardMin, out double standardMax)`

## Description

`InfoParallelsXld` calculates various gray value
features of the area enclosed by the XLD parallels
*`parallels`*. The input image *`image`* is used to
get the gray values needed for this. The algorithm used in this
operator is very similar to the one used in
[`ModParallelsXld`](mod_parallels_xld.md). The operator returns ranges for the
quality factor (*`qualityMin`* and *`qualityMax`*, see
[`GenParallelsXld`](gen_parallels_xld.md) for the corresponding calculation),
the mean gray value (*`grayMin`* and *`grayMax`*), and
the standard deviation with respect to the mean gray value
(*`standardMin`* and *`standardMax`*).

This operator serves to determine appropriate thresholds for
[`ModParallelsXld`](mod_parallels_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`parallels`** (input_object)  xld_para-array `→` [HXLDPara](HXLDPara.md)

Input XLD Parallels.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Corresponding gray value image.

**`qualityMin`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum quality factor.

**`qualityMax`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum quality factor.

**`grayMin`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum mean gray value.

**`grayMax`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum mean gray value.

**`standardMin`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum standard deviation.

**`standardMax`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum standard deviation.

## Possible Predecessors

`GenParallelsXld`

## Possible Successors

`ModParallelsXld`

## See also

`Intensity`,
`MinMaxGray`

## Module

Foundation
