## Features

List of Operators ↓

This chapter contains operators that allow you to access the different
features of regions.

### List of Features

In the following, the available features are illustrated.

- ***`"area"`*:** —

  Area of the object

  ![figure](../assets/52483890b06cfc96.svg)
- ***`"row"`*:** —

  Row index of the center
- ***`"column"`*:** —

  Column index of the center
- ***`"row1"`*:** —

  Row index of upper left corner
- ***`"column1"`*:** —

  Column index of upper left corner
- ***`"row2"`*:** —

  Row index of lower right corner
- ***`"column2"`*:** —

  Column index of lower right corner
- ***`"width"`*:** —

  Width of the region (parallel to the coordinate axis)

  ![figure](../assets/ecd71a4af1e6a8f1.svg)
- ***`"height"`*:** —

  Height of the region (parallel to the coordinate axis)

  ![figure](../assets/b1b4807450e8fd5b.svg)
- ***`"circularity"`*:** —

  Circularity (see [`Circularity`](circularity.md))

  ![figure](../assets/3025e59798ffc74a.svg)
- ***`"compactness"`*:** —

  Compactness (see [`Compactness`](compactness.md))

  ![figure](../assets/950a144321bbe88f.svg)
- ***`"contlength"`*:** —

  Total length of contour (see operator [`Contlength`](contlength.md))

  ![figure](../assets/9487c16c2d10428b.svg)
- ***`"convexity"`*:** —

  Convexity (see [`Convexity`](convexity.md))

  ![figure](../assets/8edb3ce7bd9da40c.svg)
- ***`"rectangularity"`*:** —

  Rectangularity (see [`Rectangularity`](rectangularity.md))

  ![figure](../assets/3c3632a2b17fc088.svg)
- ***`"ra"`*:** —

  Main radius of the equivalent ellipse (see [`EllipticAxis`](elliptic_axis.md))

  ![figure](../assets/ff80b464b9590bfd.svg)
- ***`"rb"`*:** —

  Secondary radius of the equivalent ellipse (see [`EllipticAxis`](elliptic_axis.md))

  ![figure](../assets/19239c372993b7c6.svg)
- ***`"phi"`*:** —

  Orientation of the equivalent ellipse
  see [`EllipticAxis`](elliptic_axis.md))

  ![figure](../assets/94ef3d8a691ca58d.svg)
- ***`"anisometry"`*:** —

  Anisometry (see [`Eccentricity`](eccentricity.md))

  ![figure](../assets/24c64f90f06d1a4e.svg)
- ***`"bulkiness"`*:** —

  Bulkiness (see operator [`Eccentricity`](eccentricity.md))

  ![figure](../assets/121c790f74c650b2.svg)
- ***`"struct_factor"`*:** —

  Structure Factor (see operator [`Eccentricity`](eccentricity.md))

  ![figure](../assets/f09cb47ea04a915d.svg)
- ***`"outer_radius"`*:** —

  Radius of smallest surrounding circle (see [`SmallestCircle`](smallest_circle.md))

  ![figure](../assets/32e29a24b0a29aad.svg)
- ***`"inner_radius"`*:** —

  Radius of largest inner circle (see [`InnerCircle`](inner_circle.md))

  ![figure](../assets/8959125a34e0d66a.svg)
- ***`"inner_width"`*:** —

  Width of the largest axis-parallel rectangle that fits into the region
  (see [`InnerRectangle1`](inner_rectangle1.md))

  ![figure](../assets/5fdc707342d9766f.svg)
- ***`"inner_height"`*:** —

  Height of the largest axis-parallel rectangle that fits into the region
  (see [`InnerRectangle1`](inner_rectangle1.md))

  ![figure](../assets/301c8a20593b6b7b.svg)
- ***`"dist_mean"`*:** —

  Mean distance from the region border to the center (see operator
  [`Roundness`](roundness.md))

  ![figure](../assets/51b8bdc6e1565030.svg)
- ***`"dist_deviation"`*:** —

  Deviation of the distance from the region border to the center
  (see operator [`Roundness`](roundness.md))

  ![figure](../assets/6aa9b1dabf2c583f.svg)
- ***`"roundness"`*:** —

  Roundness (see operator [`Roundness`](roundness.md))

  ![figure](../assets/40a20c84829810ab.svg)
- ***`"num_sides"`*:** —

  Number of polygon sides (see operator [`Roundness`](roundness.md))

  ![figure](../assets/425fecc0a0f863aa.svg)
- ***`"connect_num"`*:** —

  Number of connection components (see operator [`ConnectAndHoles`](connect_and_holes.md))

  ![figure](../assets/5f3c9eaee2d5b304.svg)
- ***`"holes_num"`*:** —

  Number of holes (see operator [`ConnectAndHoles`](connect_and_holes.md))

  ![figure](../assets/589fbd646076b926.svg)
- ***`"area_holes"`*:** —

  Area of the holes of the object (see operator [`AreaHoles`](area_holes.md))

  ![figure](../assets/e29d02cdc4835e8d.svg)
- ***`"max_diameter"`*:** —

  Maximum diameter of the region (see operator [`DiameterRegion`](diameter_region.md))

  ![figure](../assets/10da3787700b9fb5.svg)
- ***`"orientation"`*:** —

  Orientation of the region (see operator [`OrientationRegion`](orientation_region.md))

  ![figure](../assets/7a53df9e28b06d93.svg)
- ***`"euler_number"`*:** —

  Euler number (see operator [`EulerNumber`](euler_number.md))

  ![figure](../assets/3d4099720bc78240.svg)
- ***`"rect2_phi"`*:** —

  Orientation of the smallest surrounding rectangle (see operator
  [`SmallestRectangle2`](smallest_rectangle2.md))

  ![figure](../assets/d6d866d7b3ebba95.svg)
- ***`"rect2_len1"`*:** —

  Half the length of the smallest surrounding rectangle
  (see operator [`SmallestRectangle2`](smallest_rectangle2.md))

  ![figure](../assets/4dea7e6c8a8cadc9.svg)
- ***`"rect2_len2"`*:** —

  Half the width of the smallest surrounding rectangle
  (see operator [`SmallestRectangle2`](smallest_rectangle2.md))

  ![figure](../assets/5ac8093b49878274.svg)
- ***`"moments_m11"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***`"moments_m20"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***`"moments_m02"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***`"moments_ia"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***`"moments_ib"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***`"moments_m11_invar"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndInvar`](moments_region_2nd_invar.md))
- ***`"moments_m20_invar"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndInvar`](moments_region_2nd_invar.md))
- ***`"moments_m02_invar"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndInvar`](moments_region_2nd_invar.md))
- ***`"moments_phi1"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndRelInvar`](moments_region_2nd_rel_invar.md))
- ***`"moments_phi2"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndRelInvar`](moments_region_2nd_rel_invar.md))
- ***`"moments_m21"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rd`](moments_region_3rd.md))
- ***`"moments_m12"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rd`](moments_region_3rd.md))
- ***`"moments_m03"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rd`](moments_region_3rd.md))
- ***`"moments_m30"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rd`](moments_region_3rd.md))
- ***`"moments_m21_invar"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md))
- ***`"moments_m12_invar"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md))
- ***`"moments_m03_invar"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md))
- ***`"moments_m30_invar"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md))
- ***`"moments_i1"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentral`](moments_region_central.md))
- ***`"moments_i2"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentral`](moments_region_central.md))
- ***`"moments_i3"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentral`](moments_region_central.md))
- ***`"moments_i4"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentral`](moments_region_central.md))
- ***`"moments_psi1"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentralInvar`](moments_region_central_invar.md))
- ***`"moments_psi2"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentralInvar`](moments_region_central_invar.md))
- ***`"moments_psi3"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentralInvar`](moments_region_central_invar.md))
- ***`"moments_psi4"`*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentralInvar`](moments_region_central_invar.md))

---

#### List of Operators

- [`AreaCenter`](area_center.md) — Area and center of regions.

- [`AreaHoles`](area_holes.md) — Compute the area of holes of regions.

- [`Circularity`](circularity.md) — Shape factor for the circularity (similarity to a circle) of a region.

- [`Compactness`](compactness.md) — Shape factor for the compactness of a region.

- [`ConnectAndHoles`](connect_and_holes.md) — Number of connection components and holes

- [`Contlength`](contlength.md) — Contour length of a region.

- [`Convexity`](convexity.md) — Shape factor for the convexity of a region.

- [`DiameterRegion`](diameter_region.md) — Maximal distance between two boundary points of a region.

- [`Eccentricity`](eccentricity.md) — Shape features derived from the ellipse parameters.

- [`EllipticAxis`](elliptic_axis.md) — Calculate the parameters of the equivalent ellipse.

- [`EulerNumber`](euler_number.md) — Calculate the Euler number.

- [`FindNeighbors`](find_neighbors.md) — Search direct neighbors.

- [`GetRegionIndex`](get_region_index.md) — Index of all regions containing a given pixel.

- [`GetRegionThickness`](get_region_thickness.md) — Access the thickness of a region along the main axis.

- [`HammingDistance`](hamming_distance.md) — Hamming distance between two regions.

- [`HammingDistanceNorm`](hamming_distance_norm.md) — Hamming distance between two regions using normalization.

- [`HeightWidthRatio`](height_width_ratio.md) — Compute the width, height, and aspect ratio of the surrounding
  rectangle parallel to the coordinate axes.

- [`InnerCircle`](inner_circle.md) — Largest inner circle of a region.

- [`InnerRectangle1`](inner_rectangle1.md) — Largest inner rectangle of a region.

- [`MomentsRegion2nd`](moments_region_2nd.md) — Calculate the geometric moments of regions.

- [`MomentsRegion2ndInvar`](moments_region_2nd_invar.md) — Geometric moments of regions.

- [`MomentsRegion2ndRelInvar`](moments_region_2nd_rel_invar.md) — Geometric moments of regions.

- [`MomentsRegion3rd`](moments_region_3rd.md) — Geometric moments of regions.

- [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md) — Geometric moments of regions.

- [`MomentsRegionCentral`](moments_region_central.md) — Geometric moments of regions.

- [`MomentsRegionCentralInvar`](moments_region_central_invar.md) — Geometric moments of regions.

- [`OrientationRegion`](orientation_region.md) — Orientation of a region.

- [`Rectangularity`](rectangularity.md) — Shape factor for the rectangularity of a region.

- [`RegionFeatures`](region_features.md) — Calculate shape features of regions.

- [`Roundness`](roundness.md) — Shape factors from contour.

- [`RunlengthDistribution`](runlength_distribution.md) — Distribution of runs needed for runlength encoding of a region.

- [`RunlengthFeatures`](runlength_features.md) — Characteristic values for runlength coding of regions.

- [`SelectRegionPoint`](select_region_point.md) — Choose all regions containing a given pixel.

- [`SelectRegionSpatial`](select_region_spatial.md) — Pose relation of regions.

- [`SelectShape`](select_shape.md) — Choose regions with the aid of shape features.

- [`SelectShapeProto`](select_shape_proto.md) — Choose regions having a certain relation to each other.

- [`SelectShapeStd`](select_shape_std.md) — Select regions of a given shape.

- [`SmallestCircle`](smallest_circle.md) — Smallest surrounding circle of a region.

- [`SmallestRectangle1`](smallest_rectangle1.md) — Surrounding rectangle parallel to the coordinate axes.

- [`SmallestRectangle2`](smallest_rectangle2.md) — Smallest surrounding rectangle with any orientation.

- [`SpatialRelation`](spatial_relation.md) — Pose relation of regions with regard to the coordinate axes.
