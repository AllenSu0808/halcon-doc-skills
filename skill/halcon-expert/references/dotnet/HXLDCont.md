# HXLDCont (Class)

## Name

`HXLDCont` — Represents an instance of an XLD contour object(-array).

## Base Class

`HXLD` — Represents an instance of an XLD object-(array).

## Constructors

|  |  |  |
| --- | --- | --- |
| `GenContourRegionXld` |  | Generate XLD contours from regions. |
| `GenContourPolygonXld` |  | Generate an XLD contour from a polygon (given as tuples). |

## Finalizer

This operator is not available as a class member but will be called automatically when the resources of the object instances are to be released. This occurs in the finalization stage of garbage collection, or upon an explicit call of the Dispose() method.

|  |  |  |
| --- | --- | --- |
| `ClearObj` |  | Delete an iconic object from the database. |

## Methods

|  |  |  |
| --- | --- | --- |
| `AddNoiseWhiteContourXld` |  | Add noise to XLD contours. |
| `AffineTransContourXld` |  | Apply an arbitrary affine 2D transformation to XLD contours. |
| `ChangeRadialDistortionContoursXld` |  | Change the radial distortion of contours. |
| `ClipContoursXld` |  | Clip an XLD contour. |
| `ClipEndPointsContoursXld` |  | Clip the end points of an XLD contour. |
| `CloseContoursXld` |  | Close an XLD contour. |
| `CompareObj` |  | Compare iconic objects regarding equality. |
| `ConcatObj` |  | Concatenate two iconic object tuples. |
| `ContourPointNumXld` |  | Return the number of points in an XLD contour. |
| `ContourToWorldPlaneXld` |  | Transform an XLD contour into the plane z=0 of a world coordinate system. |
| `CopyObj` |  | Copy an iconic object in the database. |
| `CreateAnisoShapeModelXld` |  | Prepare an anisotropically scaled shape model for matching from XLD contours. |
| `CreateLocalDeformableModelXld` |  | Prepare a deformable model for local deformable matching from XLD contours. |
| `CreatePlanarCalibDeformableModelXld` |  | Prepare a deformable model for planar calibrated matching from XLD contours. |
| `CreatePlanarUncalibDeformableModelXld` |  | Prepare a deformable model for planar uncalibrated matching from XLD contours. |
| `CreateScaledShapeModelXld` |  | Prepare an isotropically scaled shape model for matching from XLD contours. |
| `CreateShapeModelXld` |  | Prepare a shape model for matching from XLD contours. |
| `CropContoursXld` |  | Crop an XLD contour. |
| `DeserializeXld` |  | Deserialize a serialized XLD object. |
| `DifferenceClosedContoursXld` |  | Compute the difference of closed contours. |
| `DistEllipseContourPointsXld` |  | Compute the distances of all contour points to an ellipse. |
| `DistEllipseContourXld` |  | Compute the distance of contours to an ellipse. |
| `DistRectangle2ContourPointsXld` |  | Compute the distances of all contour points to a rectangle. |
| `DistanceCc` |  | Calculate the distance between two contours. |
| `DistanceCcMin` |  | Calculate the minimum distance between two contours. |
| `DistanceCcMinPoints` |  | Calculate the minimum distance between two contours and the points used for the calculation. |
| `DistanceContoursXld` |  | Calculate the pointwise distance from one contour to another. |
| `DistanceLc` |  | Calculate the distance between a line and one contour. |
| `DistancePc` |  | Calculate the distance between a point and one contour. |
| `DistanceSc` |  | Calculate the distance between a line segment and one contour. |
| `DrawNurbs` |  | Interactive drawing of a NURBS curve. |
| `DrawNurbsInterp` |  | Interactive drawing of a NURBS curve using interpolation. |
| `DrawNurbsInterpMod` |  | Interactive modification of a NURBS curve using interpolation. |
| `DrawNurbsMod` |  | Interactive modification of a NURBS curve. |
| `DrawXld` |  | Interactive drawing of a contour. |
| `DrawXldMod` |  | Interactive modification of a contour. |
| `FitCircleContourXld` |  | Approximate XLD contours by circles. |
| `FitEllipseContourXld` |  | Approximate XLD contours by ellipses or elliptic arcs. |
| `FitLineContourXld` |  | Approximate XLD contours by line segments. |
| `FitRectangle2ContourXld` |  | Fit rectangles to XLD contours. |
| `GenCircleContourXld` |  | Create XLD contours corresponding to circles or circular arcs. |
| `GenContourNurbsXld` |  | Transform a NURBS curve into an XLD contour. |
| `GenContourPolygonRoundedXld` |  | Generate an XLD contour with rounded corners from a polygon (given as tuples). |
| `GenContourPolygonXld` |  | Generate an XLD contour from a polygon (given as tuples). |
| `GenCrossContourXld` |  | Generate one XLD contour in the shape of a cross for each input point. |
| `GenEllipseContourXld` |  | Create an XLD contour that corresponds to an elliptic arc. |
| `GenGridRectificationMap` |  | Compute the mapping between the distorted image and the rectified image based upon the points of a regular grid. |
| `GenParallelContourXld` |  | Compute the parallel contour of an XLD contour. |
| `GenPolygonsXld` |  | Approximate XLD contours by polygons. |
| `GenRectangle2ContourXld` |  | Create an XLD contour in the shape of a rectangle. |
| `GenRegionContourXld` |  | Create a region from an XLD contour. |
| `GetContourAngleXld` |  | Calculate the direction of an XLD contour for each contour point. |
| `GetContourAttribXld` |  | Return point attribute values of an XLD contour. |
| `GetContourGlobalAttribXld` |  | Return global attributes values of an XLD contour. |
| `GetContourXld` |  | Return the coordinates of an XLD contour. |
| `GetRegressParamsXld` |  | Return XLD contour parameters. |
| `InsertObj` |  | Insert objects into an iconic object tuple. |
| `IntersectionClosedContoursXld` |  | Intersect closed contours. |
| `IntersectionRegionContourXld` |  | Intersect a contour with a region. |
| `LocalMaxContoursXld` |  | Select XLD contours with a local maximum of gray values. |
| `MergeContLineScanXld` |  | Merge XLD contours from successive line scan images. |
| `ObjDiff` |  | Calculate the difference of two object tuples. |
| `PolarTransContourXld` |  | Transform a contour in an annular arc to polar coordinates. |
| `PolarTransContourXldInv` |  | Transform a contour in polar coordinates back to Cartesian coordinates |
| `ProjectiveTransContourXld` |  | Apply a projective transformation to an XLD contour. |
| `QueryContourAttribsXld` |  | Return the names of the defined attributes of an XLD contour. |
| `QueryContourGlobalAttribsXld` |  | Return the names of the defined global attributes of an XLD contour. |
| `RadialDistortionSelfCalibration` |  | Calibrate the radial distortion. |
| `ReadContourXldArcInfo` |  | Read XLD contours to a file in ARC/INFO generate format. |
| `ReadContourXldDxf` |  | Read XLD contours from a DXF file. |
| `RegressContoursXld` |  | Calculate the parameters of a regression line to an XLD contour. |
| `RemoveObj` |  | Remove objects from an iconic object tuple. |
| `ReplaceObj` |  | Replaces one or more elements of an iconic object tuple. |
| `SegmentContourAttribXld` |  | Segment XLD contour parts whose local attributes fulfill given conditions. |
| `SegmentContoursXld` |  | Segment XLD contours into line segments and circular or elliptic arcs. |
| `SelectContoursXld` |  | Select XLD contours according to several features. |
| `SelectObj` |  | Select objects from an object tuple. |
| `SelectShapeXld` |  | Select contours or polygons using shape features. |
| `SelectXldPoint` |  | Choose all contours or polygons containing a given point. |
| `SerializeXld` |  | Serialize an XLD object. |
| `ShapeTransXld` |  | Transform the shape of contours or polygons. |
| `SmoothContoursXld` |  | Smooth an XLD contour. |
| `SortContoursXld` |  | Sort contours with respect to their relative position. |
| `SymmDifferenceClosedContoursXld` |  | Compute the symmetric difference of closed contours. |
| `TestEqualObj` |  | Compare image objects regarding equality. |
| `TrainGenericShapeModel` |  | Train a shape model for matching. |
| `Union2ClosedContoursXld` |  | Compute the union of closed contours. |
| `UnionAdjacentContoursXld` |  | Compute the union of contours whose end points are close together. |
| `UnionCocircularContoursXld` |  | Compute the union of contours that belong to the same circle. |
| `UnionCollinearContoursExtXld` |  | Compute the union of collinear contours (operator with extended functionality). |
| `UnionCollinearContoursXld` |  | Unite approximately collinear contours. |
| `UnionCotangentialContoursXld` |  | Compute the union of cotangential contours. |
| `UnionStraightContoursHistoXld` |  | Compute the union of neighboring straight contours that have a similar distance from a given line. |
| `UnionStraightContoursXld` |  | Compute the union of neighboring straight contours that have a similar direction. |
| `WriteContourXldArcInfo` |  | Write XLD contours to a file in ARC/INFO generate format. |
| `WriteContourXldDxf` |  | Write XLD contours to a file in DXF format. |
