# Boundary (Operator)

## Name

`Boundary` — Reduce a region to its boundary.

## Signature

`static void HOperatorSet.Boundary(HObject region, out HObject regionBorder, HTuple boundaryType)`

`HRegion HRegion.Boundary(string boundaryType)`

## Description

`Boundary` computes the boundary of each input region in
*`region`* and returns them in *`regionBorder`*.
The parameter *`boundaryType`* determines the type of boundary
computation.

The contour computation is done using morphological operations.
The resulting output regions consist only of the minimal border of the input
regions. Their positions depend on the value of *`boundaryType`*,
accepting the following values:

- *"inner"*: The contour lies within the original region.
- *"inner_filled"*: The contour lies within the original
  region, holes in the interior of the input region are suppressed.
  Due to algorithm optimization this contours may slightly differ
  from corresponding ones obtained with *"inner"*.
- *"outer"*: The contour is one pixel outside of the original
  region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions for which the boundary is to be computed.

**`regionBorder`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Resulting boundaries.

**`boundaryType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Boundary type.

Default:
"inner"

List of values:
"inner", "inner_filled", "outer"

## Example (C++)

```
#include "HalconCpp.h"
using namespace Halcon;

main()
{
  HWindow  w;
  HRegion  circ1 = HRegion::GenCircle (20, 10, 10.5);

  circ1.Display (w);
  w.Click ();

  HRegion marg1 = circ1.Boundary ("inner");
  w.SetColor ("red");
  marg1.Display (w);
  w.Click ();

  return(0);
}
```

## Complexity

Let A be the area of the input region. Then the runtime
complexity for one region is
$$O\left(3\sqrt{A}\right) .$$ ![figure](../assets/362707851310c4ec.svg)

## Result

`Boundary` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`Union1`,
`Watersheds`,
`ClassNdimNorm`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`DilationCircle`,
`ErosionCircle`,
`Difference`

## See also

`FillUp`

## Module

Foundation
