# HPose (Class)

## Name

`HPose` — Represents a rigid 3D transformation with 7 parameters (3 for the
rotation, 3 for the translation, 1 for the representation type).

## Constructors

|  |  |  |
| --- | --- | --- |
| `CreatePose` |  | Create a 3D pose. |

## Methods

|  |  |  |
| --- | --- | --- |
| `BinocularCalibration` |  | Determine all camera parameters of a binocular stereo system. |
| `BinocularDistance` |  | Compute the distance values for a rectified stereo image pair using correlation techniques. |
| `BinocularDistanceMg` |  | Compute the distance values for a rectified stereo image pair using multigrid methods. |
| `BinocularDistanceMs` |  | Compute the distance values for a rectified stereo image pair using multi-scanline optimization. |
| `CamParPoseToHomMat3d` |  | Convert internal camera parameters and a 3D pose into a 3×4 projection matrix. |
| `CameraCalibration` |  | Determine all camera parameters by a simultaneous minimization process. |
| `ContourToWorldPlaneXld` |  | Transform an XLD contour into the plane z=0 of a world coordinate system. |
| `ConvertPoseType` |  | Change the representation type of a 3D pose. |
| `CreateCalibDescriptorModel` |  | Create a descriptor model for calibrated perspective matching. |
| `CreateCamPoseLookAtPoint` |  | Create a 3D camera pose from camera center and viewing direction. |
| `CreatePlanarCalibDeformableModel` |  | Create a deformable model for calibrated perspective matching. |
| `CreatePlanarCalibDeformableModelXld` |  | Prepare a deformable model for planar calibrated matching from XLD contours. |
| `CreatePose` |  | Create a 3D pose. |
| `DeserializePose` |  | Deserialize a serialized pose. |
| `DispObjectModel3d` |  | Display 3D object models. |
| `DisparityImageToXyz` |  | Transform a disparity image into 3D points in a rectified stereo system. |
| `DisparityToDistance` |  | Transform a disparity value into a distance value in a rectified binocular stereo system. |
| `DisparityToPoint3d` |  | Transform an image point and its disparity into a 3D point in a rectified stereo system. |
| `DistanceToDisparity` |  | Transform a distance value into a disparity in a rectified stereo system. |
| `FindCalibDescriptorModel` |  | Find the best matches of a calibrated descriptor model in an image and return their 3D pose. |
| `FindMarksAndPose` |  | Extract rectangularly arranged 2D calibration marks from the image and calculate initial values for the external camera parameters. |
| `GenBinocularRectificationMap` |  | Generate transformation maps that describe the mapping of the images of a binocular camera pair to a common rectified image plane. |
| `GenImageToWorldPlaneMap` |  | Generate a projection map that describes the mapping between the image plane and the plane z=0 of a world coordinate system. |
| `GetPoseType` |  | Get the representation type of a 3D pose. |
| `HandEyeCalibration` |  | Perform a hand-eye calibration. |
| `ImageToWorldPlane` |  | Rectify an image by transforming it into the plane z=0 of a world coordinate system. |
| `IntersectLinesOfSight` |  | Get a 3D point from the intersection of two lines of sight within a binocular camera system. |
| `MatchRelPoseRansac` |  | Compute the relative orientation between two cameras by automatically finding correspondences between image points. |
| `PoseAverage` |  | Compute the average of a set of poses. |
| `PoseCompose` |  | Combine 3D poses given in two tuples. |
| `PoseInvert` |  | Invert each pose in a tuple of 3D poses. |
| `PoseToHomMat3d` |  | Convert a 3D pose into a homogeneous transformation matrix. |
| `ProjectObjectModel3d` |  | Project a 3D object model into image coordinates. |
| `ProjectShapeModel3d` |  | Project the edges of a 3D shape model into image coordinates. |
| `ReadPose` |  | Read a 3D pose from a text file. |
| `ReduceObjectModel3dByView` |  | Remove points from a 3D object model by projecting it to a virtual view and removing all points outside of a given region. |
| `RelPoseToFundamentalMatrix` |  | Compute the fundamental matrix from the relative orientation of two cameras. |
| `RenderObjectModel3d` |  | Render 3D object models to get an image. |
| `SceneFlowCalib` |  | Compute the calibrated scene flow between two stereo image pairs. |
| `SerializePose` |  | Serialize a pose. |
| `SetCameraSetupCamParam` |  | Define type, parameters, and relative pose of a camera in a camera setup model. |
| `SetOriginPose` |  | Translate the origin of a 3D pose. |
| `SimCaltab` |  | Simulate an image with calibration plate. |
| `TransPoseShapeModel3d` |  | Transform a pose that refers to the coordinate system of a 3D object model to a pose that refers to the reference coordinate system of a 3D shape model and vice versa. |
| `VectorToPose` |  | Compute an absolute pose out of point correspondences between world and image coordinates. |
| `VectorToRelPose` |  | Compute the relative orientation between two cameras given image point correspondences and known camera parameters and reconstruct 3D space points. |
| `WritePose` |  | Write a 3D pose to a text file. |
