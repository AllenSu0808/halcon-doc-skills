# LinePosition (Operator)

## Name

`LinePosition` — Calculate the center of gravity, length, and orientation of a line.

## Signature

`static void HOperatorSet.LinePosition(HTuple rowBegin, HTuple colBegin, HTuple rowEnd, HTuple colEnd, out HTuple rowCenter, out HTuple colCenter, out HTuple length, out HTuple phi)`

`static void HMisc.LinePosition(HTuple rowBegin, HTuple colBegin, HTuple rowEnd, HTuple colEnd, out HTuple rowCenter, out HTuple colCenter, out HTuple length, out HTuple phi)`

`static void HMisc.LinePosition(double rowBegin, double colBegin, double rowEnd, double colEnd, out double rowCenter, out double colCenter, out double length, out double phi)`

## Description

The operator `LinePosition` returns the center
(*`rowCenter`*, *`colCenter`*), the (Euclidean) length
(*`length`*) and the orientation (-pi/2 < *`phi`* <=
pi/2)
of the given lines. If more than one line is to be treated the line
and column indices can be passed as tuples. In this case the output
parameters, of course, are also tuples.

The routine is applied, for example, to model lines in order to
determine search regions for the edge detection
([`DetectEdgeSegments`](detect_edge_segments.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rowBegin`** (input_control)  line.begin.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the starting points of the
input lines.

**`colBegin`** (input_control)  line.begin.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the starting points of the
input lines.

**`rowEnd`** (input_control)  line.end.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the ending points of the
input lines.

**`colEnd`** (input_control)  line.end.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the ending points of the
input lines.

**`rowCenter`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the centers of gravity of the
input lines.

**`colCenter`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the centers of gravity of the
input lines.

**`length`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Euclidean length of the input lines.

**`phi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of the input lines.

## Result

`LinePosition` always returns the value 2 (
H_MSG_TRUE)
.

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

`LineOrientation`

## See also

`LineOrientation`,
`DetectEdgeSegments`

## Module

Foundation
