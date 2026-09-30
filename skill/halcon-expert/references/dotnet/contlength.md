# Contlength (Operator)

## Name

`Contlength` — Contour length of a region.

## Signature

`static void HOperatorSet.Contlength(HObject regions, out HTuple contLength)`

`HTuple HRegion.Contlength()`

## Description

The operator `Contlength` calculates the total length of the contour
(sum of all connection components of the region) for each region of
*`regions`*. The distance between two neighboring contour
points parallel to the coordinate axes is rated 1, the distance in the diagonal
is rated $\sqrt{2}$ ![figure](../assets/102cc74656473d95.svg).

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in the length of their
contours.

If more than one region is passed the numerical values of the
contour length are stored in a tuple, the position of a value in the tuple
corresponding to the position of the region in the input tuple. In case of an
empty region the operator `Contlength` returns the value 0.

## Attention

The contour of holes is not calculated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be examined.

**`contLength`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Contour length of the input region(s).

Assertion:
`ContLength >= 0`

## Example (C++)

```
#include "HalconCpp.h"
#include <iostream>
using namespace HalconCpp;

int main (int argc, char *argv[])
{
  HWindow        w(10,10,512,512);
  HRegion        reg;
  int            NumOfElements = 3;

  std::cout << "Draw " << NumOfElements << " regions " << std::endl;
  GenEmptyObj(&reg);
  for (int i=0; i < NumOfElements; i++)
  {
    reg = reg.ConcatObj(w.DrawRegion());
  }

  HTuple circ = reg.Circularity ();
  HTuple cont = reg.Contlength ();

  for (int i = 0; i < NumOfElements; i++)
  {
    std::cout << "region " << i+1 << ": \tcircularity = " << circ[i].D() <<
                 "\tcontour length =" << cont[i].D() << std::endl;
  }
  std::cout << "Click into the graphics window to end." << std::endl;
  w.Click ();
  return(0);
}
```

## Result

The operator `Contlength` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Possible Successors

`GetRegionContour`

## Alternatives

`Compactness`

## See also

`AreaCenter`,
`GetRegionContour`

## Module

Foundation
