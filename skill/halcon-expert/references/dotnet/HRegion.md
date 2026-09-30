# HRegion (Class)

## Name

`HRegion` — Represents an instance of a region object(-array).

## Base Class

`HObject` — Represents an instance of an iconic object(-array).
Base class for images, regions and XLDs

## Constructors

|  |  |  |
| --- | --- | --- |
| `GenRectangle1` |  | Create a rectangle parallel to the coordinate axes. |
| `GenEllipseSector` |  | Create an ellipse sector. |
| `GenCircleSector` |  | Create a circle sector. |
| `GenCircle` |  | Create a circle. |

## Finalizer

This operator is not available as a class member but will be called automatically when the resources of the object instances are to be released. This occurs in the finalization stage of garbage collection, or upon an explicit call of the Dispose() method.

|  |  |  |
| --- | --- | --- |
| `ClearObj` |  | Delete an iconic object from the database. |

## Methods

|  |  |  |
| --- | --- | --- |
| `AddChannels` |  | Add gray values to regions. |
| `AffineTransRegion` |  | Apply an arbitrary affine 2D transformation to regions. |
| `AppendOcrTrainf` |  | Add characters to a training file. |
| `AreaCenter` |  | Area and center of regions. |
| `AreaCenterGray` |  | Compute the area and center of gravity of a region in a gray value image. |
| `AreaHoles` |  | Compute the area of holes of regions. |
| `BackgroundSeg` |  | Determine the connected components of the background of given regions. |
| `BottomHat` |  | Compute the bottom hat of regions. |
| `Boundary` |  | Reduce a region to its boundary. |
| `Circularity` |  | Shape factor for the circularity (similarity to a circle) of a region. |
| `ClipRegion` |  | Clip a region to a rectangle. |
| `ClipRegionRel` |  | Clip a region relative to its smallest surrounding rectangle. |
| `CloseEdges` |  | Close edge gaps using the edge amplitude image. |
| `CloseEdgesLength` |  | Close edge gaps using the edge amplitude image. |
| `ClosestPointTransform` |  | Compute the closest-point transformation of a region. |
| `Closing` |  | Close a region. |
| `ClosingCircle` |  | Close a region with a circular structuring element. |
| `ClosingGolay` |  | Close a region with an element from the Golay alphabet. |
| `ClosingRectangle1` |  | Close a region with a rectangular structuring element. |
| `Compactness` |  | Shape factor for the compactness of a region. |
| `CompareObj` |  | Compare iconic objects regarding equality. |
| `Complement` |  | Return the complement of a region. |
| `ConcatObj` |  | Concatenate two iconic object tuples. |
| `ConnectAndHoles` |  | Number of connection components and holes |
| `Connection` |  | Compute connected components of a region. |
| `Contlength` |  | Contour length of a region. |
| `Convexity` |  | Shape factor for the convexity of a region. |
| `CoocFeatureImage` |  | Calculate a co-occurrence matrix and derive gray value features thereof. |
| `CopyObj` |  | Copy an iconic object in the database. |
| `CreateSheetOfLightModel` |  | Create a model to perform 3D-measurements using the sheet-of-light technique. |
| `DeserializeRegion` |  | Deserialize a serialized region. |
| `DiameterRegion` |  | Maximal distance between two boundary points of a region. |
| `Difference` |  | Calculate the difference of two regions. |
| `Dilation1` |  | Dilate a region. |
| `Dilation2` |  | Dilate a region (using a reference point). |
| `DilationCircle` |  | Dilate a region with a circular structuring element. |
| `DilationGolay` |  | Dilate a region with an element from the Golay alphabet. |
| `DilationRectangle1` |  | Dilate a region with a rectangular structuring element. |
| `DilationSeq` |  | Dilate a region sequentially. |
| `DispRegion` |  | Displays regions in a window. |
| `DistanceLr` |  | Calculate the distance between a line and a region. |
| `DistancePr` |  | Calculate the distance between a point and a region. |
| `DistanceRrMin` |  | Minimum distance between the contour pixels of two regions each. |
| `DistanceRrMinDil` |  | Minimum distance between two regions with the help of dilation. |
| `DistanceSr` |  | Calculate the distance between a line segment and one region. |
| `DistanceTransform` |  | Compute the distance transformation of a region. |
| `DoOcrMulti` |  | Classify characters. |
| `DoOcrMultiClassCnn` |  | Classify multiple characters with an CNN-based OCR classifier. |
| `DoOcrMultiClassKnn` |  | Classify multiple characters with an k-NN classifier. |
| `DoOcrMultiClassMlp` |  | Classify multiple characters with an OCR classifier. |
| `DoOcrMultiClassSvm` |  | Classify multiple characters with an SVM-based OCR classifier. |
| `DoOcrSingle` |  | Classify one character. |
| `DoOcrSingleClassCnn` |  | Classify a single character with an CNN-based OCR classifier. |
| `DoOcrSingleClassKnn` |  | Classify a single character with an OCR classifier. |
| `DoOcrSingleClassMlp` |  | Classify a single character with an OCR classifier. |
| `DoOcrSingleClassSvm` |  | Classify a single character with an SVM-based OCR classifier. |
| `DoOcrWordCnn` |  | Classify a related group of characters with an CNN-based OCR classifier. |
| `DoOcrWordKnn` |  | Classify a related group of characters with an OCR classifier. |
| `DoOcrWordMlp` |  | Classify a related group of characters with an OCR classifier. |
| `DoOcrWordSvm` |  | Classify a related group of characters with an OCR classifier. |
| `DragRegion1` |  | Interactive moving of a region. |
| `DragRegion2` |  | Interactive movement of a region with fixpoint specification. |
| `DragRegion3` |  | Interactive movement of a region with restriction of positions. |
| `DrawPolygon` |  | Interactive drawing of a polygon row. |
| `DrawRegion` |  | Interactive drawing of a closed region. |
| `Eccentricity` |  | Shape features derived from the ellipse parameters. |
| `EliminateRuns` |  | Eliminate runs of a given length. |
| `EllipticAxis` |  | Calculate the parameters of the equivalent ellipse. |
| `EllipticAxisGray` |  | Compute the orientation and major axes of a region in a gray value image. |
| `EntropyGray` |  | Determine the entropy and anisotropy of images. |
| `Erosion1` |  | Erode a region. |
| `Erosion2` |  | Erode a region (using a reference point). |
| `ErosionCircle` |  | Erode a region with a circular structuring element. |
| `ErosionGolay` |  | Erode a region with an element from the Golay alphabet. |
| `ErosionRectangle1` |  | Erode a region with a rectangular structuring element. |
| `ErosionSeq` |  | Erode a region sequentially. |
| `EulerNumber` |  | Calculate the Euler number. |
| `ExpandGray` |  | Fill gaps between regions (depending on gray value or color) or split overlapping regions. |
| `ExpandGrayRef` |  | Fill gaps between regions (depending on gray value or color) or split overlapping regions. |
| `ExpandRegion` |  | Fill gaps between regions or split overlapping regions. |
| `FillUp` |  | Fill up holes in regions. |
| `FillUpShape` |  | Fill up holes in regions having given shape features. |
| `FindNeighbors` |  | Search direct neighbors. |
| `FitSurfaceFirstOrder` |  | Calculate gray value moments and approximation by a first order surface (plane). |
| `FitSurfaceSecondOrder` |  | Calculate gray value moments and approximation by a second order surface. |
| `Fitting` |  | Perform a closing after an opening with multiple structuring elements. |
| `FuzzyEntropy` |  | Determine the fuzzy entropy of regions. |
| `FuzzyPerimeter` |  | Calculate the fuzzy perimeter of a region. |
| `GenCheckerRegion` |  | Create a checkered region. |
| `GenCircle` |  | Create a circle. |
| `GenCircleSector` |  | Create a circle sector. |
| `GenContourRegionXld` |  | Generate XLD contours from regions. |
| `GenContoursSkeletonXld` |  | Convert a skeleton into XLD contours. |
| `GenCoocMatrix` |  | Calculate the co-occurrence matrix of a region in an image. |
| `GenEllipse` |  | Create an ellipse. |
| `GenEllipseSector` |  | Create an ellipse sector. |
| `GenEmptyRegion` |  | Create an empty region. |
| `GenGridRegion` |  | Create a region from lines or pixels. |
| `GenRandomRegion` |  | Create a random region. |
| `GenRandomRegions` |  | Create random regions like circles, rectangles and ellipses. |
| `GenRectangle1` |  | Create a rectangle parallel to the coordinate axes. |
| `GenRectangle2` |  | Create a rectangle of any orientation. |
| `GenRegionHisto` |  | Convert a histogram into a region. |
| `GenRegionHline` |  | Store input lines described in Hesse normal form as regions. |
| `GenRegionLine` |  | Store input lines as regions. |
| `GenRegionPoints` |  | Store individual pixels as image region. |
| `GenRegionPolygon` |  | Store a polygon as a region. |
| `GenRegionPolygonFilled` |  | Store a polygon as a “filled” region. |
| `GenRegionRuns` |  | Create a region from a runlength coding. |
| `GenStructElements` |  | Generate standard structuring elements. |
| `GetIcon` |  | Query the icon for region output |
| `GetRegionChain` |  | Contour of an object as chain code. |
| `GetRegionContour` |  | Access the contour of an object. |
| `GetRegionConvex` |  | Access convex hull as contour. |
| `GetRegionIndex` |  | Index of all regions containing a given pixel. |
| `GetRegionPoints` |  | Access the pixels of a region. |
| `GetRegionPolygon` |  | Polygon approximation of a region. |
| `GetRegionRuns` |  | Access the runlength coding of a region. |
| `GetRegionThickness` |  | Access the thickness of a region along the main axis. |
| `GolayElements` |  | Generate the structuring elements of the Golay alphabet. |
| `GrabData` |  | Synchronous grab of images and preprocessed image data from the specified image acquisition device. |
| `GrabDataAsync` |  | Asynchronous grab of images and preprocessed image data from the specified image acquisition device. |
| `GrayFeatures` |  | Calculates gray value features for a set of regions. |
| `GrayHisto` |  | Calculate the gray value distribution. |
| `GrayHistoAbs` |  | Calculate the gray value distribution. |
| `GrayHistoRange` |  | Calculate the gray value distribution of a single channel image within a certain gray value range. |
| `GrayProjections` |  | Calculate horizontal and vertical gray-value projections. |
| `HammingChangeRegion` |  | Generate a region having a given Hamming distance. |
| `HammingDistance` |  | Hamming distance between two regions. |
| `HammingDistanceNorm` |  | Hamming distance between two regions using normalization. |
| `HeightWidthRatio` |  | Compute the width, height, and aspect ratio of the surrounding rectangle parallel to the coordinate axes. |
| `Histo2dim` |  | Calculate the histogram of two-channel gray value images. |
| `HitOrMiss` |  | Hit-or-miss operation for regions. |
| `HitOrMissGolay` |  | Hit-or-miss operation for regions using the Golay alphabet. |
| `HitOrMissSeq` |  | Hit-or-miss operation for regions using the Golay alphabet (sequential). |
| `HoughCircleTrans` |  | Return the Hough-Transform for circles with a given radius. |
| `HoughCircles` |  | Detect centers of circles for a specific radius using the Hough transform. |
| `HoughLineTrans` |  | Produce the Hough transform for lines within regions. |
| `HoughLines` |  | Detect lines in edge images with the help of the Hough transform and returns it in HNF. |
| `InnerCircle` |  | Largest inner circle of a region. |
| `InnerRectangle1` |  | Largest inner rectangle of a region. |
| `InsertObj` |  | Insert objects into an iconic object tuple. |
| `Intensity` |  | Calculate the mean and deviation of gray values. |
| `Interjacent` |  | Partition the image plane using given regions. |
| `Intersection` |  | Calculate the intersection of two regions. |
| `IntersectionRegionContourXld` |  | Intersect a contour with a region. |
| `JunctionsSkeleton` |  | Find junctions and end points in a skeleton. |
| `LearnNdimNorm` |  | Construct classes for class_ndim_normclass_ndim_normClassNdimNormClassNdimNormclass_ndim_norm. |
| `MergeRegionsLineScan` |  | Merge regions from line scan images. |
| `MinMaxGray` |  | Determine the minimum and maximum gray values within regions. |
| `MinkowskiAdd1` |  | Perform a Minkowski addition on a region. |
| `MinkowskiAdd2` |  | Dilate a region (using a reference point). |
| `MinkowskiSub1` |  | Erode a region. |
| `MinkowskiSub2` |  | Erode a region (using a reference point). |
| `MirrorRegion` |  | Reflect a region about an axis. |
| `MomentsGrayPlane` |  | Calculate gray value moments and approximation by a plane. |
| `MomentsRegion2nd` |  | Calculate the geometric moments of regions. |
| `MomentsRegion2ndInvar` |  | Geometric moments of regions. |
| `MomentsRegion2ndRelInvar` |  | Geometric moments of regions. |
| `MomentsRegion3rd` |  | Geometric moments of regions. |
| `MomentsRegion3rdInvar` |  | Geometric moments of regions. |
| `MomentsRegionCentral` |  | Geometric moments of regions. |
| `MomentsRegionCentralInvar` |  | Geometric moments of regions. |
| `MorphHat` |  | Compute the union of bottom_hatbottom_hatBottomHatBottomHatbottom_hat and top_hattop_hatTopHatTopHattop_hat. |
| `MorphSkeleton` |  | Compute the morphological skeleton of a region. |
| `MorphSkiz` |  | Thinning of a region. |
| `MoveRegion` |  | Translate a region. |
| `NoiseDistributionMean` |  | Determine the noise distribution of an image. |
| `ObjDiff` |  | Calculate the difference of two object tuples. |
| `Opening` |  | Open a region. |
| `OpeningCircle` |  | Open a region with a circular structuring element. |
| `OpeningGolay` |  | Open a region with an element from the Golay alphabet. |
| `OpeningRectangle1` |  | Open a region with a rectangular structuring element. |
| `OpeningSeg` |  | Separate overlapping regions. |
| `OrientationRegion` |  | Orientation of a region. |
| `OverpaintRegion` |  | Overpaint regions in an image. |
| `PaintRegion` |  | Paint regions into an image. |
| `PartitionDynamic` |  | Partition a region horizontally at positions of small vertical extent. |
| `PartitionRectangle` |  | Partition a region into rectangles of approximately equal size. |
| `PlaneDeviation` |  | Calculate the deviation of the gray values from the approximating image plane. |
| `PolarTransRegion` |  | Transform a region within an annular arc to polar coordinates. |
| `PolarTransRegionInv` |  | Transform a region in polar coordinates back to Cartesian coordinates. |
| `ProjectiveTransRegion` |  | Apply a projective transformation to a region. |
| `ProtectOcrTrainf` |  | Protection of training data. |
| `Pruning` |  | Prune the branches of a region. |
| `RankRegion` |  | Rank operator for regions. |
| `ReadRegion` |  | Read binary images or regions. |
| `ReceiveRegion` |  | Receive regions over a socket connection. |
| `Rectangularity` |  | Shape factor for the rectangularity of a region. |
| `RegionFeatures` |  | Calculate shape features of regions. |
| `RegionToBin` |  | Convert a region into a binary byte-image. |
| `RegionToLabel` |  | Convert regions to a label image. |
| `RegionToMean` |  | Paint regions with their average gray value. |
| `RemoveNoiseRegion` |  | Remove noise from a region. |
| `RemoveObj` |  | Remove objects from an iconic object tuple. |
| `ReplaceObj` |  | Replaces one or more elements of an iconic object tuple. |
| `Roundness` |  | Shape factors from contour. |
| `RunlengthDistribution` |  | Distribution of runs needed for runlength encoding of a region. |
| `RunlengthFeatures` |  | Characteristic values for runlength coding of regions. |
| `SegmentCharacters` |  | Segments characters in a given region of an image. |
| `SelectCharacters` |  | Selects characters from a given region. |
| `SelectGray` |  | Select regions based on gray value features. |
| `SelectMatchingLines` |  | Select those lines from a set of lines (in HNF) which fit best into a region. |
| `SelectObj` |  | Select objects from an object tuple. |
| `SelectRegionPoint` |  | Choose all regions containing a given pixel. |
| `SelectRegionSpatial` |  | Pose relation of regions. |
| `SelectShape` |  | Choose regions with the aid of shape features. |
| `SelectShapeProto` |  | Choose regions having a certain relation to each other. |
| `SelectShapeStd` |  | Select regions of a given shape. |
| `SendRegion` |  | Send regions over a socket connection. |
| `SerializeRegion` |  | Serialize a region. |
| `SetIcon` |  | Icon definition for region output. |
| `ShapeHistoAll` |  | Determine a histogram of features along all threshold values. |
| `ShapeHistoPoint` |  | Determine a histogram of features along all threshold values. |
| `ShapeTrans` |  | Transform the shape of a region. |
| `Skeleton` |  | Compute the skeleton of a region. |
| `SmallestCircle` |  | Smallest surrounding circle of a region. |
| `SmallestRectangle1` |  | Surrounding rectangle parallel to the coordinate axes. |
| `SmallestRectangle2` |  | Smallest surrounding rectangle with any orientation. |
| `SortRegion` |  | Sorting of regions with respect to their relative position. |
| `SpatialRelation` |  | Pose relation of regions with regard to the coordinate axes. |
| `SplitSkeletonLines` |  | Split lines represented by one pixel wide, non-branching lines. |
| `SplitSkeletonRegion` |  | Split lines represented by one pixel wide, non-branching regions. |
| `SymmDifference` |  | Calculate the symmetric difference of two regions. |
| `TestEqualObj` |  | Compare image objects regarding equality. |
| `TestEqualRegion` |  | Test whether the regions of two objects are identical. |
| `TestRegionPoint` |  | Test if the region contains a given point. |
| `TestRegionPoints` |  | Test if points are contained in regions. |
| `TestSubsetRegion` |  | Test whether a region is contained in another region. |
| `TestdOcrClassBox` |  | Test an OCR classifier. |
| `TextLineOrientation` |  | Determines the orientation of a text line or paragraph. |
| `TextLineSlant` |  | Determines the slant of characters of a text line or paragraph. |
| `Thickening` |  | Add the result of a hit-or-miss operation to a region. |
| `ThickeningGolay` |  | Add the result of a hit-or-miss operation to a region (using a Golay structuring element). |
| `ThickeningSeq` |  | Add the result of a hit-or-miss operation to a region (sequential). |
| `Thinning` |  | Remove the result of a hit-or-miss operation from a region. |
| `ThinningGolay` |  | Remove the result of a hit-or-miss operation from a region (using a Golay structuring element). |
| `ThinningSeq` |  | Remove the result of a hit-or-miss operation from a region (sequential). |
| `TopHat` |  | Compute the top hat of regions. |
| `TraindOcrClassBox` |  | Train an OCR classifier by the input of regions. |
| `TransposeRegion` |  | Reflect a region about a point. |
| `Union1` |  | Return the union of all input regions. |
| `Union2` |  | Return the union of two regions. |
| `WriteOcrTrainf` |  | Storing of training characters into a file. |
| `WriteRegion` |  | Write regions to a file. |
| `ZoomRegion` |  | Zoom a region. |
