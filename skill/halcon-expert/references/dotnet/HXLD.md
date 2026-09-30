# HXLD (Class)

## Name

`HXLD` — Represents an instance of an XLD object-(array).

## Base Class

`HObject` — Represents an instance of an iconic object(-array).
Base class for images, regions and XLDs

## Finalizer

This operator is not available as a class member but will be called automatically when the resources of the object instances are to be released. This occurs in the finalization stage of garbage collection, or upon an explicit call of the Dispose() method.

|  |  |  |
| --- | --- | --- |
| `ClearObj` |  | Delete an iconic object from the database. |

## Methods

|  |  |  |
| --- | --- | --- |
| `AreaCenterPointsXld` |  | Area and center of gravity (centroid) of contours and polygons treated as point clouds. |
| `AreaCenterXld` |  | Area and center of gravity (centroid) of contours and polygons. |
| `CircularityXld` |  | Shape factor for the circularity (similarity to a circle) of contours or polygons. |
| `CompactnessXld` |  | Shape factor for the compactness of contours or polygons. |
| `CompareObj` |  | Compare iconic objects regarding equality. |
| `ConcatObj` |  | Concatenate two iconic object tuples. |
| `ConvexityXld` |  | Shape factor for the convexity of contours or polygons. |
| `CopyObj` |  | Copy an iconic object in the database. |
| `DeserializeXld` |  | Deserialize a serialized XLD object. |
| `DiameterXld` |  | Maximum distance between two contour or polygon points. |
| `DispXld` |  | Display an XLD object. |
| `EccentricityPointsXld` |  | Anisometry of contours or polygons treated as point clouds. |
| `EccentricityXld` |  | Shape features derived from the ellipse parameters of contours or polygons. |
| `EllipticAxisPointsXld` |  | Parameters of the equivalent ellipse of contours or polygons treated as point clouds. |
| `EllipticAxisXld` |  | Parameters of the equivalent ellipse of contours or polygons. |
| `GenGridRectificationMap` |  | Compute the mapping between the distorted image and the rectified image based upon the points of a regular grid. |
| `GetCirclePose` |  | Determine the 3D pose of a circle from its perspective 2D projection. |
| `GetParallelsXld` |  | Return an XLD parallel's data (as lines). |
| `GetRectanglePose` |  | Determine the 3D pose of a rectangle from its perspective 2D projection |
| `HeightWidthRatioXld` |  | Compute the width, height, and aspect ratio of the enclosing rectangle parallel to the coordinate axes of contours or polygons. |
| `InsertObj` |  | Insert objects into an iconic object tuple. |
| `LengthXld` |  | Length of contours or polygons. |
| `MomentsAnyPointsXld` |  | Arbitrary geometric moments of contours or polygons treated as point clouds. |
| `MomentsAnyXld` |  | Arbitrary geometric moments of contours or polygons. |
| `MomentsPointsXld` |  | Geometric moments M20$M_{20}$, M02$M_{02}$, and M11$M_{11}$ of contours or polygons treated as point clouds. |
| `MomentsXld` |  | Geometric moments M20$M_{20}$, M02$M_{02}$, and M11$M_{11}$ of contours or polygons. |
| `ObjDiff` |  | Calculate the difference of two object tuples. |
| `OrientationPointsXld` |  | Calculate the orientation of contours or polygons treated as point clouds. |
| `OrientationXld` |  | Calculate the orientation of contours or polygons. |
| `PaintXld` |  | Paint XLD objects into an image. |
| `ReceiveXld` |  | Receive an XLD object over a socket connection. |
| `RectangularityXld` |  | Shape factor for the rectangularity of contours or polygons. |
| `RemoveObj` |  | Remove objects from an iconic object tuple. |
| `ReplaceObj` |  | Replaces one or more elements of an iconic object tuple. |
| `SelectObj` |  | Select objects from an object tuple. |
| `SelectShapeXld` |  | Select contours or polygons using shape features. |
| `SelectXldPoint` |  | Choose all contours or polygons containing a given point. |
| `SendXld` |  | Send an XLD object over a socket connection. |
| `SerializeXld` |  | Serialize an XLD object. |
| `ShapeTransXld` |  | Transform the shape of contours or polygons. |
| `SmallestCircleXld` |  | Smallest enclosing circle of contours or polygons. |
| `SmallestRectangle1Xld` |  | Enclosing rectangle parallel to the coordinate axes of contours or polygons. |
| `SmallestRectangle2Xld` |  | Smallest enclosing rectangle with arbitrary orientation of contours or polygons. |
| `TestClosedXld` |  | Test whether contours or polygons are closed. |
| `TestEqualObj` |  | Compare image objects regarding equality. |
| `TestSelfIntersectionXld` |  | Test XLD contours or polygons for self intersection. |
| `TestXldPoint` |  | Test whether one or more contours or polygons enclose the given point(s). |
