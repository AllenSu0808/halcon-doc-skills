# HCamPar (Class)

## Name

`HCamPar` — Represents internal camera parameters.

## Methods

|  |  |  |
| --- | --- | --- |
| `AddScene3dCamera` |  | Add a camera to a 3D scene. |
| `BinocularCalibration` |  | Determine all camera parameters of a binocular stereo system. |
| `BinocularDistance` |  | Compute the distance values for a rectified stereo image pair using correlation techniques. |
| `BinocularDistanceMg` |  | Compute the distance values for a rectified stereo image pair using multigrid methods. |
| `BinocularDistanceMs` |  | Compute the distance values for a rectified stereo image pair using multi-scanline optimization. |
| `CamMatToCamPar` |  | Compute the internal camera parameters from a camera matrix. |
| `CamParPoseToHomMat3d` |  | Convert internal camera parameters and a 3D pose into a 3×4 projection matrix. |
| `CamParToCamMat` |  | Compute a camera matrix from internal camera parameters. |
| `CameraCalibration` |  | Determine all camera parameters by a simultaneous minimization process. |
| `ChangeRadialDistortionCamPar` |  | Determine new camera parameters in accordance to the specified radial distortion. |
| `ChangeRadialDistortionContoursXld` |  | Change the radial distortion of contours. |
| `ChangeRadialDistortionImage` |  | Change the radial distortion of an image. |
| `ChangeRadialDistortionPoints` |  | Change the radial distortion of pixel coordinates. |
| `CreateCalibDescriptorModel` |  | Create a descriptor model for calibrated perspective matching. |
| `CreatePlanarCalibDeformableModel` |  | Create a deformable model for calibrated perspective matching. |
| `CreatePlanarCalibDeformableModelXld` |  | Prepare a deformable model for planar calibrated matching from XLD contours. |
| `CreateShapeModel3d` |  | Prepare a 3D object model for matching. |
| `DeserializeCamPar` |  | Deserialize the serialized internal camera parameters. |
| `DispCaltab` |  | Project and visualize the 3D model of the calibration plate in the image. |
| `DispObjectModel3d` |  | Display 3D object models. |
| `DisparityImageToXyz` |  | Transform a disparity image into 3D points in a rectified stereo system. |
| `DisparityToDistance` |  | Transform a disparity value into a distance value in a rectified binocular stereo system. |
| `DisparityToPoint3d` |  | Transform an image point and its disparity into a 3D point in a rectified stereo system. |
| `DistanceToDisparity` |  | Transform a distance value into a disparity in a rectified stereo system. |
| `FindCalibDescriptorModel` |  | Find the best matches of a calibrated descriptor model in an image and return their 3D pose. |
| `FindMarksAndPose` |  | Extract rectangularly arranged 2D calibration marks from the image and calculate initial values for the external camera parameters. |
| `GenBinocularRectificationMap` |  | Generate transformation maps that describe the mapping of the images of a binocular camera pair to a common rectified image plane. |
| `GenImageToWorldPlaneMap` |  | Generate a projection map that describes the mapping between the image plane and the plane z=0 of a world coordinate system. |
| `GenRadialDistortionMap` |  | Generate a projection map that describes the mapping of images corresponding to a changing radial distortion. |
| `GetCirclePose` |  | Determine the 3D pose of a circle from its perspective 2D projection. |
| `GetLineOfSight` |  | Compute the line of sight corresponding to a point in the image. |
| `GetRectanglePose` |  | Determine the 3D pose of a rectangle from its perspective 2D projection |
| `HandEyeCalibration` |  | Perform a hand-eye calibration. |
| `ImagePointsToWorldPlane` |  | Transform image points into the plane z=0 of a world coordinate system. |
| `ImageToWorldPlane` |  | Rectify an image by transforming it into the plane z=0 of a world coordinate system. |
| `IntersectLinesOfSight` |  | Get a 3D point from the intersection of two lines of sight within a binocular camera system. |
| `MatchRelPoseRansac` |  | Compute the relative orientation between two cameras by automatically finding correspondences between image points. |
| `ObjectModel3dToXyz` |  | Transform 3D points from a 3D object model to images. |
| `Project3dPoint` |  | Project 3D points into (sub-)pixel image coordinates. |
| `ProjectObjectModel3d` |  | Project a 3D object model into image coordinates. |
| `ProjectShapeModel3d` |  | Project the edges of a 3D shape model into image coordinates. |
| `RadialDistortionSelfCalibration` |  | Calibrate the radial distortion. |
| `ReadCamPar` |  | Read internal camera parameters from a file. |
| `ReduceObjectModel3dByView` |  | Remove points from a 3D object model by projecting it to a virtual view and removing all points outside of a given region. |
| `RelPoseToFundamentalMatrix` |  | Compute the fundamental matrix from the relative orientation of two cameras. |
| `RenderObjectModel3d` |  | Render 3D object models to get an image. |
| `SceneFlowCalib` |  | Compute the calibrated scene flow between two stereo image pairs. |
| `SerializeCamPar` |  | Serialize the internal camera parameters. |
| `SetCalibDataCamParam` |  | Set type and initial parameters of a camera in a calibration data model. |
| `SetCameraSetupCamParam` |  | Define type, parameters, and relative pose of a camera in a camera setup model. |
| `SimCaltab` |  | Simulate an image with calibration plate. |
| `VectorToPose` |  | Compute an absolute pose out of point correspondences between world and image coordinates. |
| `VectorToRelPose` |  | Compute the relative orientation between two cameras given image point correspondences and known camera parameters and reconstruct 3D space points. |
| `WriteCamPar` |  | Write internal camera parameters into a file. |
