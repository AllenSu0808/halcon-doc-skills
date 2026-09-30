# combine_roads_xld (Operator)

## Name

`combine_roads_xld` — Combine road hypotheses from two resolution levels.

## Signature

`def combine_roads_xld(edge_polygons: HObject, mod_parallels: HObject, ext_parallels: HObject, center_lines: HObject, max_angle_parallel: Union[float, int], max_angle_colinear: Union[float, int], max_distance_parallel: Union[float, int], max_distance_colinear: Union[float, int]) -> HObject`

## Description

`combine_roads_xld` combines road hypotheses obtained from
two different resolution levels. The algorithm selects only those
hypotheses which mutually support each other in both resolution
levels. The parameters *`edge_polygons`*,
*`mod_parallels`* and *`ext_parallels`* correspond to
the road hypotheses from the highest resolution level. The
parameter *`center_lines`* is the result of road extraction in
a lower resolution level. Those of the polygons *`edge_polygons`*
are returned for which evidence of being roadsides is found in
both resolution levels. The parameters *`max_angle_parallel`*
and *`max_angle_colinear`* determine the angle, that may be formed
by two parallel collinear line segments, respectively. The
parameters *`max_distance_parallel`* and
*`max_distance_colinear`* determine the maximum allowed
distance of two parallel or collinear line segments, respectively.
The combination is done using a number of rules.

## Execution Information

- Multithreading type: mutually exclusive (runs in parallel with other non-exclusive operators, but not with itself).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`edge_polygons`** (input_object)  xld_poly-array `→` HObject

XLD polygons to be examined.

**`mod_parallels`** (input_object)  xld_mod_para-array `→` HObject

Modified parallels obtained from
*`edge_polygons`*.

**`ext_parallels`** (input_object)  xld_ext_para-array `→` HObject

Extended parallels obtained from
*`edge_polygons`*.

**`center_lines`** (input_object)  xld_poly-array `→` HObject

Road-center-line polygons to be examined.

**`road_sides`** (output_object)  xld_poly-array `→` HObject

Roadsides found.

**`max_angle_parallel`** (input_control)  angle.rad `→` Union[float, int]

Maximum angle between two parallel line segments.

Default:
0.523598775598

Suggested values:
0.349065850399, 0.523598775598, 0.6981317008

Restriction:
`0 <= MaxAngleParallel <= pi / 2`

**`max_angle_colinear`** (input_control)  angle.rad `→` Union[float, int]

Maximum angle between two collinear line segments.

Default:
0.261799387799

Suggested values:
0.174532925199, 0.261799387799, 0.349065850399

Restriction:
`0 <= MaxAngleColinear <= pi / 2`

**`max_distance_parallel`** (input_control)  real `→` Union[float, int]

Maximum distance between two parallel line segments.

Default:
40

Suggested values:
20, 30, 40, 50, 60

Restriction:
`MaxDistanceParallel > 0`

**`max_distance_colinear`** (input_control)  real `→` Union[float, int]

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
