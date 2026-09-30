# AreaCenter (Operator)

## Name

`AreaCenter` — Area and center of regions.

## Signature

`static void HOperatorSet.AreaCenter(HObject regions, out HTuple area, out HTuple row, out HTuple column)`

`HTuple HRegion.AreaCenter(out HTuple row, out HTuple column)`

`int HRegion.AreaCenter(out double row, out double column)`

## Description

The operator `AreaCenter` calculates the area and the center
of the input regions. The area is defined as the number of
pixels of a region. The center is calculated as the mean value
of the line or column coordinates, respectively, of all pixels.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their area.

If more than one region is passed the results are stored in tuples,
the index of a value in the tuple corresponding to the index of the
input region. In case of empty region all parameters have the value 0.0
if no other behavior was set (see [`SetSystem`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be examined.

**`area`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Area of the region.

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Line index of the center.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column index of the center.

## Example (C++)

```
#include "HIOStream.h"
#if !defined(USE_IOSTREAM_H)
using namespace std;
#endif
#include "HalconCpp.h"
using namespace Halcon;

main()
{
  Tuple   area, row, column;

  HImage   img ("monkey");
  HWindow  w;

  img.Display (w);
  w.Click ();

  HRegionArray   reg = (img >= 164).Connection ();

  reg.Display (w);
  w.Click ();

  area = reg.AreaCenter (&row, &column);

  for (int i = 0; i < reg.Num (); i++)
  {
    cout << "Row    [" << i << "]" << "= " << row[i].D ();
    cout << "\t\tColumn [" << i << "]" << "= " << column[i].D () << endl;
  }

  cout << "Total number of regions: " << reg.Num () << endl;
  return(0);
}
```

## Complexity

If F is the area of a region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `AreaCenter` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## See also

`SelectShape`

## Module

Foundation
