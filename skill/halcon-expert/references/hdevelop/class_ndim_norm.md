# class_ndim_norm (Operator)

## Name

`class_ndim_norm` — Classify pixels using hyper-spheres or hyper-cubes.

## Signature

`class_ndim_norm(MultiChannelImage : Regions : Metric, SingleMultiple, Radius, Center : )`

## Description

`class_ndim_norm` classifies the pixels of the multi-channel
image given in *`MultiChannelImage`*. The result is returned
in *`Regions`* as one region per classification object. The
metric used (*'euclid'* or *'maximum'*) is determined by
*`Metric`*. This parameter must be set to the same value used
in [`learn_ndim_norm`](learn_ndim_norm.md). The parameter *`SingleMultiple`*
determines whether one region (*'single'*) or multiples regions
(*'multiple'*) are generated for each cluster.
*`Radius`* determines the
radii or half edge length of the clusters, respectively.
*`Center`* determines their centers.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`MultiChannelImage`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Multi channel input image.

**`Regions`** (output_object)  region-array `→` object

Classification result.

**`Metric`** (input_control)  string `→`  (string)

Metric to be used.

Default:
'euclid'

List of values:
'euclid', 'maximum'

**`SingleMultiple`** (input_control)  string `→`  (string)

Return one region or one region for each cluster.

Default:
'single'

List of values:
'multiple', 'single'

**`Radius`** (input_control)  number(-array) `→`  (real / integer)

Cluster radii or half edge lengths (returned by
[`learn_ndim_norm`](learn_ndim_norm.md)).

**`Center`** (input_control)  number(-array) `→`  (real / integer)

Coordinates of the cluster centers (returned by
[`learn_ndim_norm`](learn_ndim_norm.md)).

## Example (C++)

```
#include "HIOStream.h"
#if !defined(USE_IOSTREAM_H)
using namespace std;
#endif
#include "HalconCpp.h"
using namespace Halcon;

int main ()
{
  HImage   image ("meer"),
           t1, t2, t3,
           m1, m2, m3, m;

  HWindow  w;

  w.SetColor ("green");
  image.Display (w);

  cout << "Draw your region of interest " << endl;

  HRegion testreg = w.DrawRegion ();

  t1 = image.TextureLaws ("el", 2, 5);     m1 = t1.MeanImage (21, 21);
  t2 = image.TextureLaws ("es", 2, 5);     m2 = t2.MeanImage (21, 21);
  t3 = image.TextureLaws ("le", 2, 5);     m3 = t3.MeanImage (21, 21);

  m  = m1.Compose3 (m2, m3);

  Tuple Metric = "euclid";
  Tuple Radius = 20.0;
  Tuple MinNum = 5;
  Tuple NbrCha = 3;

  HRegion empty;
  Tuple cen, t;

  Radius = testreg.LearnNdimNorm (empty, m, Metric, Radius,
                                  MinNum, NbrCha, &cen, &t);
  Tuple RegMod = "multiple";

  HRegionArray reg = m.ClassNdimNorm (Metric, RegMod, Radius, cen, NbrCha);

  w.SetColored (12);
  reg.Display (w);
  cout << "Result of classification" << endl;
  return (0);
}
```

## Complexity

Let N be the number of clusters and A be the area of the input
region. Then the runtime complexity is O(N,A).

## Result

`class_ndim_norm` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*'no_object_result'*, *'empty_region_result'*, and
*'store_empty_region'* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`learn_ndim_norm`,
`compose2`,
`compose3`,
`compose4`,
`compose5`,
`compose6`,
`compose7`

## Possible Successors

`connection`,
`select_shape`,
`reduce_domain`,
`select_gray`

## Alternatives

`class_2dim_sup`,
`class_2dim_unsup`

## Module

Foundation
