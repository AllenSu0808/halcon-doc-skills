# PartitionLines (Operator)

## Name

`PartitionLines` — Partition lines according to various criteria.

## Warning

**`PartitionLines` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.PartitionLines(HTuple rowBeginIn, HTuple colBeginIn, HTuple rowEndIn, HTuple colEndIn, HTuple feature, HTuple operation, HTuple min, HTuple max, out HTuple rowBeginOut, out HTuple colBeginOut, out HTuple rowEndOut, out HTuple colEndOut, out HTuple failRowBOut, out HTuple failColBOut, out HTuple failRowEOut, out HTuple failColEOut)`

`static void HMisc.PartitionLines(HTuple rowBeginIn, HTuple colBeginIn, HTuple rowEndIn, HTuple colEndIn, HTuple feature, string operation, HTuple min, HTuple max, out HTuple rowBeginOut, out HTuple colBeginOut, out HTuple rowEndOut, out HTuple colEndOut, out HTuple failRowBOut, out HTuple failColBOut, out HTuple failRowEOut, out HTuple failColEOut)`

`static void HMisc.PartitionLines(HTuple rowBeginIn, HTuple colBeginIn, HTuple rowEndIn, HTuple colEndIn, string feature, string operation, string min, string max, out HTuple rowBeginOut, out HTuple colBeginOut, out HTuple rowEndOut, out HTuple colEndOut, out HTuple failRowBOut, out HTuple failColBOut, out HTuple failRowEOut, out HTuple failColEOut)`

## Description

The operator `PartitionLines` divides lines into two sets
according to various criteria. For each input line the indicated
features (*`feature`*) are calculated. If each
(*`operation`* = *"and"*) or at least one
(*`operation`* = *"or"*) of the calculated features is within
the given limits (*`min`*,*`max`*) the line is
transferred into the first set (parameters *`rowBeginOut`* to
*`colEndOut`*), otherwise into the second set (parameters
*`failRowBOut`* to *`failColEOut`*).
The default values *"min"* and *"max"* of the parameters
*`min`* and *`max`* are used to leave bottom and top limit,
respectively, open.
$$\text{Condition:}Min_{i}\le Feature_{i}(Line)\le Max_{i}$$
Possible values for *`feature`*:

- **'length'** —

  (Euclidean) length of the line
- **'row'** —

  Line index of the center
- **'column'** —

  Column index of the center
- **'phi'** —

  Orientation of the line $\left(-\frac{\pi}{2} < \varphi \le \frac{\pi}{2}\right)$ ![figure](../assets/9c19d9d0a0968c31.svg)

## Attention

If only one feature is used the value of *`operation`* is
meaningless. Several features are processed according to the
sequence in which they are passed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rowBeginIn`** (input_control)  line.begin.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the starting points of the
input lines.

**`colBeginIn`** (input_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the starting points of the
input lines.

**`rowEndIn`** (input_control)  line.end.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the ending points of the
input lines.

**`colEndIn`** (input_control)  line.end.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the ending points of the
input lines.

**`feature`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Features to be used for selection.

List of values:
"column", "length", "phi", "row"

**`operation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Desired combination of the features.

List of values:
"and", "or"

**`min`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Lower limits of the features or 'min'.

Default:
"min"

**`max`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Upper limits of the features or 'max'.

Default:
"max"

**`rowBeginOut`** (output_control)  line.begin.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the starting points of the
lines fulfilling the conditions.

**`colBeginOut`** (output_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the starting points of the
lines fulfilling the conditions.

**`rowEndOut`** (output_control)  line.end.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the ending points of the
lines fulfilling the conditions.

**`colEndOut`** (output_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the ending points of the
lines fulfilling the conditions.

**`failRowBOut`** (output_control)  line.begin.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the starting points of the
lines not fulfilling the conditions.

**`failColBOut`** (output_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the starting points of the
lines not fulfilling the conditions.

**`failRowEOut`** (output_control)  line.end.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the ending points of the
lines not fulfilling the conditions.

**`failColEOut`** (output_control)  line.end.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the ending points of the
lines not fulfilling the conditions.

## Result

The operator `PartitionLines` returns the value 2 (
H_MSG_TRUE)
if the
parameter values are correct. Otherwise an exception is raised.

## Possible Predecessors

`SobelAmp`,
`EdgesImage`,
`Threshold`,
`HysteresisThreshold`,
`SplitSkeletonRegion`,
`SplitSkeletonLines`

## Possible Successors

`SetLineWidth`,
`DispLine`

## Alternatives

`LineOrientation`,
`LinePosition`,
`SelectLines`,
`SelectLinesLongest`

## See also

`SelectLines`,
`SelectLinesLongest`,
`DetectEdgeSegments`,
`SelectShape`

## Module

Foundation
