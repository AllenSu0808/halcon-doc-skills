# info_parallels_xld (Operator)

## Name

`info_parallels_xld` — Return information about the gray values of the area enclosed by XLD
parallels.

## Signature

`def info_parallels_xld(parallels: HObject, image: HObject) -> Tuple[float, float, int, int, float, float]`

## Description

`info_parallels_xld` calculates various gray value
features of the area enclosed by the XLD parallels
*`parallels`*. The input image *`image`* is used to
get the gray values needed for this. The algorithm used in this
operator is very similar to the one used in
[`mod_parallels_xld`](mod_parallels_xld.md). The operator returns ranges for the
quality factor (*`quality_min`* and *`quality_max`*, see
[`gen_parallels_xld`](gen_parallels_xld.md) for the corresponding calculation),
the mean gray value (*`gray_min`* and *`gray_max`*), and
the standard deviation with respect to the mean gray value
(*`standard_min`* and *`standard_max`*).

This operator serves to determine appropriate thresholds for
[`mod_parallels_xld`](mod_parallels_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`parallels`** (input_object)  xld_para-array `→` HObject

Input XLD Parallels.

**`image`** (input_object)  singlechannelimage `→` HObject (byte)

Corresponding gray value image.

**`quality_min`** (output_control)  real `→` float

Minimum quality factor.

**`quality_max`** (output_control)  real `→` float

Maximum quality factor.

**`gray_min`** (output_control)  integer `→` int

Minimum mean gray value.

**`gray_max`** (output_control)  integer `→` int

Maximum mean gray value.

**`standard_min`** (output_control)  real `→` float

Minimum standard deviation.

**`standard_max`** (output_control)  real `→` float

Maximum standard deviation.

## Possible Predecessors

`gen_parallels_xld`

## Possible Successors

`mod_parallels_xld`

## See also

`intensity`,
`min_max_gray`

## Module

Foundation
