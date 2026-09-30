# combine_roads_xld (Operator)

## Name

`combine_roads_xld` — Combine road hypotheses from two resolution levels.

## Signature

`combine_roads_xld(EdgePolygons, ModParallels, ExtParallels, CenterLines : RoadSides : MaxAngleParallel, MaxAngleColinear, MaxDistanceParallel, MaxDistanceColinear : )`

## Description

`combine_roads_xld` combines road hypotheses obtained from
two different resolution levels. The algorithm selects only those
hypotheses which mutually support each other in both resolution
levels. The parameters *`EdgePolygons`*,
*`ModParallels`* and *`ExtParallels`* correspond to
the road hypotheses from the highest resolution level. The
parameter *`CenterLines`* is the result of road extraction in
a lower resolution level. Those of the polygons *`EdgePolygons`*
are returned for which evidence of being roadsides is found in
both resolution levels. The parameters *`MaxAngleParallel`*
and *`MaxAngleColinear`* determine the angle, that may be formed
by two parallel collinear line segments, respectively. The
parameters *`MaxDistanceParallel`* and
*`MaxDistanceColinear`* determine the maximum allowed
distance of two parallel or collinear line segments, respectively.
The combination is done using a number of rules.

## Execution Information

- Multithreading type: mutually exclusive (runs in parallel with other non-exclusive operators, but not with itself).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`EdgePolygons`** (input_object)  xld_poly-array `→` object

XLD polygons to be examined.

**`ModParallels`** (input_object)  xld_mod_para-array `→` object

Modified parallels obtained from
*`EdgePolygons`*.

**`ExtParallels`** (input_object)  xld_ext_para-array `→` object

Extended parallels obtained from
*`EdgePolygons`*.

**`CenterLines`** (input_object)  xld_poly-array `→` object

Road-center-line polygons to be examined.

**`RoadSides`** (output_object)  xld_poly-array `→` object

Roadsides found.

**`MaxAngleParallel`** (input_control)  angle.rad `→`  (real / integer)

Maximum angle between two parallel line segments.

Default:
0.523598775598

Suggested values:
0.349065850399, 0.523598775598, 0.6981317008

Restriction:
`0 <= MaxAngleParallel <= pi / 2`

**`MaxAngleColinear`** (input_control)  angle.rad `→`  (real / integer)

Maximum angle between two collinear line segments.

Default:
0.261799387799

Suggested values:
0.174532925199, 0.261799387799, 0.349065850399

Restriction:
`0 <= MaxAngleColinear <= pi / 2`

**`MaxDistanceParallel`** (input_control)  real `→`  (real / integer)

Maximum distance between two parallel line segments.

Default:
40

Suggested values:
20, 30, 40, 50, 60

Restriction:
`MaxDistanceParallel > 0`

**`MaxDistanceColinear`** (input_control)  real `→`  (real / integer)

Maximum distance between two collinear line segments.

Default:
40

Suggested values:
20, 30, 40, 50, 60

Restriction:
`MaxDistanceColinear > 0`

## Possible Predecessors

`mod_parallels_xld`,
`gen_polygons_xld`,
`affine_trans_contour_xld`

## Possible Successors

`get_polygon_xld`,
`get_lines_xld`

## See also

`lines_gauss`,
`lines_facet`,
`get_channel_info`,
`edges_sub_pix`

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
