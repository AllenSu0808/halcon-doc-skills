# HObjectModel3D (Class)

## Name

`HObjectModel3D` — Represents an instance of a 3D object model.

## Constructors

|  |  |  |
| --- | --- | --- |
| `GenEmptyObjectModel3d` |  | Create an empty 3D object model. |
| `GenObjectModel3dFromPoints` |  | Create a 3D object model that represents a point cloud from a set of 3D points. |
| `XyzToObjectModel3d` |  | Transform 3D points from images to a 3D object model. |
| `ReadObjectModel3d` |  | Read a 3D object model from a file. |

## Methods

|  |  |  |
| --- | --- | --- |
| `AddDeformableSurfaceModelSample` |  | Add a sample deformation to a deformable surface model |
| `AffineTransObjectModel3d` |  | Apply an arbitrary affine 3D transformation to 3D object models. |
| `AreaObjectModel3d` |  | Calculate the area of all faces of a 3D object model. |
| `ClearObjectModel3d` |  | Free the memory of a 3D object model. |
| `ConnectionObjectModel3d` |  | Determine the connected components of the 3D object model. |
| `ConvexHullObjectModel3d` |  | Calculate the convex hull of a 3D object model. |
| `CopyObjectModel3d` |  | Copy a 3D object model. |
| `CreateDeformableSurfaceModel` |  | Create the data structure needed to perform deformable surface-based matching. |
| `CreateSurfaceModel` |  | Create the data structure needed to perform surface-based matching. |
| `DeserializeObjectModel3d` |  | Deserialize a serialized 3D object model. |
| `DispObjectModel3d` |  | Display 3D object models. |
| `DistanceObjectModel3d` |  | Compute the distances of the points of one 3D object model to another 3D object model. |
| `EdgesObjectModel3d` |  | Find edges in a 3D object model. |
| `FindBox3d` |  | Find boxes in 3D data. |
| `FindDeformableSurfaceModel` |  | Find the best match of a deformable surface model in a 3D scene. |
| `FindSurfaceModel` |  | Find the best matches of a surface model in a 3D scene. |
| `FindSurfaceModelImage` |  | Find the best matches of a surface model in a 3D scene and images. |
| `FitPrimitivesObjectModel3d` |  | Fit 3D primitives into a set of 3D points. |
| `FuseObjectModel3d` |  | Fuse 3D object models into a surface. |
| `GenBoxObjectModel3d` |  | Create a 3D object model that represents a box. |
| `GenCylinderObjectModel3d` |  | Create a 3D object model that represents a cylinder. |
| `GenEmptyObjectModel3d` |  | Create an empty 3D object model. |
| `GenObjectModel3dFromPoints` |  | Create a 3D object model that represents a point cloud from a set of 3D points. |
| `GenPlaneObjectModel3d` |  | Create a 3D object model that represents a plane. |
| `GenSphereObjectModel3d` |  | Create a 3D object model that represents a sphere. |
| `GenSphereObjectModel3dCenter` |  | Create a 3D object model that represents a sphere from x,y,z coordinates. |
| `GetDispObjectModel3dInfo` |  | Get the depth or the index of a displayed 3D object model. |
| `GetObjectModel3dParams` |  | Return attributes of 3D object models. |
| `GetSheetOfLightResultObjectModel3d` |  | Get the result of a calibrated measurement performed with the sheet-of-light technique as a 3D object model. |
| `IntersectPlaneObjectModel3d` |  | Intersect a 3D object model with a plane. |
| `MaxDiameterObjectModel3d` |  | Calculate the maximal diameter of a 3D object model. |
| `MomentsObjectModel3d` |  | Calculates the mean or the central moment of second order for a 3D object model. |
| `ObjectModel3dToXyz` |  | Transform 3D points from a 3D object model to images. |
| `PrepareObjectModel3d` |  | Prepare a 3D object model for a certain operation. |
| `ProjectObjectModel3d` |  | Project a 3D object model into image coordinates. |
| `ProjectiveTransObjectModel3d` |  | Apply an arbitrary projective 3D transformation to 3D object models. |
| `ReadObjectModel3d` |  | Read a 3D object model from a file. |
| `ReconstructSurfaceStereo` |  | Reconstruct surface from calibrated multi-view stereo images. |
| `ReconstructSurfaceStructuredLight` |  | Reconstruct a surface from a decoded structured light setup. |
| `ReduceObjectModel3dByView` |  | Remove points from a 3D object model by projecting it to a virtual view and removing all points outside of a given region. |
| `RefineDeformableSurfaceModel` |  | Refine the position and deformation of a deformable surface model in a 3D scene. |
| `RefineSurfaceModelPose` |  | Refine the pose of a surface model in a 3D scene. |
| `RefineSurfaceModelPoseImage` |  | Refine the pose of a surface model in a 3D scene and in images. |
| `RegisterObjectModel3dGlobal` |  | Improve the relative transformations between 3D object models based on their overlaps. |
| `RegisterObjectModel3dPair` |  | Search for a transformation between two 3D object models. |
| `RemoveObjectModel3dAttrib` |  | Remove attributes of a 3D object model. |
| `RemoveObjectModel3dAttribMod` |  | Remove attributes of a 3D object model. |
| `RenderObjectModel3d` |  | Render 3D object models to get an image. |
| `RigidTransObjectModel3d` |  | Apply a rigid 3D transformation to 3D object models. |
| `SampleObjectModel3d` |  | Sample a 3D object model. |
| `SceneFlowCalib` |  | Compute the calibrated scene flow between two stereo image pairs. |
| `SegmentObjectModel3d` |  | Segment a set of 3D points into sub-sets with similar characteristics. |
| `SelectObjectModel3d` |  | Select 3D object models from an array of 3D object models according to global features. |
| `SelectPointsObjectModel3d` |  | Apply a threshold to an attribute of 3D object models. |
| `SerializeObjectModel3d` |  | Serialize a 3D object model. |
| `SetObjectModel3dAttrib` |  | Set attributes of a 3D object model. |
| `SetObjectModel3dAttribMod` |  | Set attributes of a 3D object model. |
| `SimplifyObjectModel3d` |  | Simplify a triangulated 3D object model. |
| `SmallestBoundingBoxObjectModel3d` |  | Calculate the smallest bounding box around the points of a 3D object model. |
| `SmallestSphereObjectModel3d` |  | Calculate the smallest sphere around the points of a 3D object model. |
| `SmoothObjectModel3d` |  | Smooth the 3D points of a 3D object model. |
| `SurfaceNormalsObjectModel3d` |  | Calculate the 3D surface normals of a 3D object model. |
| `TriangulateObjectModel3d` |  | Create a surface triangulation for a 3D object model. |
| `UnionObjectModel3d` |  | Combine several 3D object models to a new 3D object model. |
| `VolumeObjectModel3dRelativeToPlane` |  | Calculate the volume of a 3D object model. |
| `WriteObjectModel3d` |  | Writes a 3D object model to a file. |
| `XyzToObjectModel3d` |  | Transform 3D points from images to a 3D object model. |
