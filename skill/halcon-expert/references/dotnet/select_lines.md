# SelectLines (Operator)

## Name

`SelectLines` — Select lines according to various criteria.

## Warning

**`SelectLines` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.SelectLines(HTuple rowBeginIn, HTuple colBeginIn, HTuple rowEndIn, HTuple colEndIn, HTuple feature, HTuple operation, HTuple min, HTuple max, out HTuple rowBeginOut, out HTuple colBeginOut, out HTuple rowEndOut, out HTuple colEndOut)`

`static void HMisc.SelectLines(HTuple rowBeginIn, HTuple colBeginIn, HTuple rowEndIn, HTuple colEndIn, HTuple feature, string operation, HTuple min, HTuple max, out HTuple rowBeginOut, out HTuple colBeginOut, out HTuple rowEndOut, out HTuple colEndOut)`

`static void HMisc.SelectLines(HTuple rowBeginIn, HTuple colBeginIn, HTuple rowEndIn, HTuple colEndIn, string feature, string operation, string min, string max, out HTuple rowBeginOut, out HTuple colBeginOut, out HTuple rowEndOut, out HTuple colEndOut)`

## Description

The operator `SelectLines` chooses lines according to
various criteria. For every input line the indicated features
(*`feature`*) are calculated. If each
(*`operation`* = *"and"*) or at least one
(*`operation`* = *"or"*) of the calculated features is within
the given limits (*`min`*,*`max`*) the line is
transferred into the output.
The default values *"min"* and *"max"* of the parameters
*`min`* and *`max`* are used to leave bottom and top limits,
respectively, open.

Condition:
$$Min_{i}\le Feature_{i}(Line)\le Max_{i}$$

Possible values for *`feature`*:

- ***"length"*** —

  (Euclidean) length of the line
- ***"row"*** —

  Line index of the center
- ***"column"*** —

  Column index of the center
- ***"phi"*** —

  Orientation of the line
  ($-\frac{\pi}{2} < \varphi \le \frac{\pi}{2}$ ![figure](../assets/a9d6b4537501996b.svg))

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

Default:
"length"

List of values:
"column", "length", "phi", "row"

**`operation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Desired combination of the features.

Default:
"and"

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
output lines.

**`colBeginOut`** (output_control)  line.begin.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the starting points of the
output lines.

**`rowEndOut`** (output_control)  line.end.y-array `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of the ending points of the
output lines.

**`colEndOut`** (output_control)  line.end.x-array `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of the ending points of the
output lines.

## Result

The operator `SelectLines` returns the value 2 (
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
`PartitionLines`

## See also

`PartitionLines`,
`SelectLinesLongest`,
`DetectEdgeSegments`,
`SelectShape`

## Module

Foundation
