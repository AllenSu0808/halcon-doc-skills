## Binocular Stereo

#### List of Operators

- [`BinocularDisparity`](binocular_disparity.md) — Compute the disparities of a rectified image pair using correlation
  techniques.

- [`BinocularDisparityMg`](binocular_disparity_mg.md) — Compute the disparities of a rectified stereo image pair using multigrid
  methods.

- [`BinocularDisparityMs`](binocular_disparity_ms.md) — Compute the disparities of a rectified stereo image pair using
  multi-scanline optimization.

- [`BinocularDistance`](binocular_distance.md) — Compute the distance values for a rectified stereo image pair using
  correlation techniques.

- [`BinocularDistanceMg`](binocular_distance_mg.md) — Compute the distance values for a rectified stereo image pair using
  multigrid methods.

- [`BinocularDistanceMs`](binocular_distance_ms.md) — Compute the distance values for a rectified stereo image pair using
  multi-scanline optimization.

- [`DisparityImageToXyz`](disparity_image_to_xyz.md) — Transform a disparity image into 3D points in a rectified stereo
  system.

- [`DisparityToDistance`](disparity_to_distance.md) — Transform a disparity value into a distance value in a rectified
  binocular stereo system.

- [`DisparityToPoint3d`](disparity_to_point_3d.md) — Transform an image point and its disparity into a 3D point in a
  rectified stereo system.

- [`DistanceToDisparity`](distance_to_disparity.md) — Transform a distance value into a disparity in a rectified stereo
  system.

- [`EssentialToFundamentalMatrix`](essential_to_fundamental_matrix.md) — Compute the fundamental matrix from an essential matrix.

- [`GenBinocularProjRectification`](gen_binocular_proj_rectification.md) — Compute the projective rectification of weakly calibrated binocular
  stereo images.

- [`GenBinocularRectificationMap`](gen_binocular_rectification_map.md) — Generate transformation maps that describe the mapping of the images
  of a binocular camera pair to a common rectified image plane.

- [`IntersectLinesOfSight`](intersect_lines_of_sight.md) — Get a 3D point from the intersection of two lines of sight
  within a binocular camera system.

- [`MatchEssentialMatrixRansac`](match_essential_matrix_ransac.md) — Compute the essential matrix for a pair of stereo images by automatically
  finding correspondences between image points.

- [`MatchFundamentalMatrixDistortionRansac`](match_fundamental_matrix_distortion_ransac.md) — Compute the fundamental matrix and the radial distortion coefficient
  for a pair of stereo images by automatically finding correspondences
  between image points.

- [`MatchFundamentalMatrixRansac`](match_fundamental_matrix_ransac.md) — Compute the fundamental matrix for a pair of stereo images by
  automatically finding correspondences between image
  points.

- [`MatchRelPoseRansac`](match_rel_pose_ransac.md) — Compute the relative orientation between two cameras by automatically
  finding correspondences between image points.

- [`Reconst3dFromFundamentalMatrix`](reconst3d_from_fundamental_matrix.md) — Compute the projective 3d reconstruction of points based on the fundamental
  matrix.

- [`RelPoseToFundamentalMatrix`](rel_pose_to_fundamental_matrix.md) — Compute the fundamental matrix from the relative orientation of two
  cameras.

- [`VectorToEssentialMatrix`](vector_to_essential_matrix.md) — Compute the essential matrix given image point correspondences
  and known camera matrices and reconstruct 3D points.

- [`VectorToFundamentalMatrix`](vector_to_fundamental_matrix.md) — Compute the fundamental matrix given a set of image point
  correspondences and reconstruct 3D points.

- [`VectorToFundamentalMatrixDistortion`](vector_to_fundamental_matrix_distortion.md) — Compute the fundamental matrix and the radial distortion coefficient
  given a set of image point correspondences and reconstruct 3D
  points.

- [`VectorToRelPose`](vector_to_rel_pose.md) — Compute the relative orientation between two cameras given image point
  correspondences and known camera parameters and reconstruct 3D space points.
