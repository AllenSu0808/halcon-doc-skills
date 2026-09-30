# CombineRoadsXld (Operator)

## Name

`CombineRoadsXld` — Combine road hypotheses from two resolution levels.

## Signature

`static void HOperatorSet.CombineRoadsXld(HObject edgePolygons, HObject modParallels, HObject extParallels, HObject centerLines, out HObject roadSides, HTuple maxAngleParallel, HTuple maxAngleColinear, HTuple maxDistanceParallel, HTuple maxDistanceColinear)`

`HXLDPoly HXLDPoly.CombineRoadsXld(HXLDModPara modParallels, HXLDExtPara extParallels, HXLDPoly centerLines, HTuple maxAngleParallel, HTuple maxAngleColinear, HTuple maxDistanceParallel, HTuple maxDistanceColinear)`

`HXLDPoly HXLDPoly.CombineRoadsXld(HXLDModPara modParallels, HXLDExtPara extParallels, HXLDPoly centerLines, double maxAngleParallel, double maxAngleColinear, double maxDistanceParallel, double maxDistanceColinear)`

`HXLDPoly HXLDModPara.CombineRoadsXld(HXLDPoly edgePolygons, HXLDExtPara extParallels, HXLDPoly centerLines, HTuple maxAngleParallel, HTuple maxAngleColinear, HTuple maxDistanceParallel, HTuple maxDistanceColinear)`

`HXLDPoly HXLDModPara.CombineRoadsXld(HXLDPoly edgePolygons, HXLDExtPara extParallels, HXLDPoly centerLines, double maxAngleParallel, double maxAngleColinear, double maxDistanceParallel, double maxDistanceColinear)`

## Description

`CombineRoadsXld` combines road hypotheses obtained from
two different resolution levels. The algorithm selects only those
hypotheses which mutually support each other in both resolution
levels. The parameters *`edgePolygons`*,
*`modParallels`* and *`extParallels`* correspond to
the road hypotheses from the highest resolution level. The
parameter *`centerLines`* is the result of road extraction in
a lower resolution level. Those of the polygons *`edgePolygons`*
are returned for which evidence of being roadsides is found in
both resolution levels. The parameters *`maxAngleParallel`*
and *`maxAngleColinear`* determine the angle, that may be formed
by two parallel collinear line segments, respectively. The
parameters *`maxDistanceParallel`* and
*`maxDistanceColinear`* determine the maximum allowed
distance of two parallel or collinear line segments, respectively.
The combination is done using a number of rules.

## Execution Information

- Multithreading type: mutually exclusive (runs in parallel with other non-exclusive operators, but not with itself).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`edgePolygons`** (input_object)  xld_poly-array `→` [HXLDPoly](HXLDPoly.md)

XLD polygons to be examined.

**`modParallels`** (input_object)  xld_mod_para-array `→` [HXLDModPara](HXLDModPara.md)

Modified parallels obtained from
*`edgePolygons`*.

**`extParallels`** (input_object)  xld_ext_para-array `→` [HXLDExtPara](HXLDExtPara.md)

Extended parallels obtained from
*`edgePolygons`*.

**`centerLines`** (input_object)  xld_poly-array `→` [HXLDPoly](HXLDPoly.md)

Road-center-line polygons to be examined.

**`roadSides`** (output_object)  xld_poly-array `→` [HXLDPoly](HXLDPoly.md)

Roadsides found.

**`maxAngleParallel`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum angle between two parallel line segments.

Default:
0.523598775598

Suggested values:
0.349065850399, 0.523598775598, 0.6981317008

Restriction:
`0 <= MaxAngleParallel <= pi / 2`

**`maxAngleColinear`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum angle between two collinear line segments.

Default:
0.261799387799

Suggested values:
0.174532925199, 0.261799387799, 0.349065850399

Restriction:
`0 <= MaxAngleColinear <= pi / 2`

**`maxDistanceParallel`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum distance between two parallel line segments.

Default:
40

Suggested values:
20, 30, 40, 50, 60

Restriction:
`MaxDistanceParallel > 0`

**`maxDistanceColinear`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum distance between two collinear line segments.

Default:
40

Suggested values:
20, 30, 40, 50, 60

Restriction:
`MaxDistanceColinear > 0`

## Possible Predecessors

`ModParallelsXld`,
`GenPolygonsXld`,
`AffineTransContourXld`

## Possible Successors

`GetPolygonXld`,
`GetLinesXld`

## See also

`LinesGauss`,
`LinesFacet`,
`GetChannelInfo`,
`EdgesSubPix`

## References

C. Steger, C. Glock, W. Eckstein, H. Mayer, B. Radig; “Model-based
Road Extraction from Images”; in “Automatic Extraction of
Man-Made Objects from Aerial and Space Images”; A. Gruen,
O. Kuebler, P. Agouris (Editors); Birkhäuser Verlag (1995),
pp. 275-284.
  
C. Heipke, C. Steger, R. Multhammer; “A Hierarchical Approach to
Automatic Road Extraction from Aerial Imagery”; in “Integrating
Photogrammetric Techniques with Scene Analysis and Machine Vision
II”; D. M. McKeown, Jr., I. J. Dowman (Editors); Proc. SPIE 2486
(1995), pp. 222-231.

## Module

Foundation
