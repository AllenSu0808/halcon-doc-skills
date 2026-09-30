## Binocular Stereo

#### List of Operators

- [`binocular_disparity`](binocular_disparity.md) — Compute the disparities of a rectified image pair using correlation
  techniques.

- [`binocular_disparity_mg`](binocular_disparity_mg.md) — Compute the disparities of a rectified stereo image pair using multigrid
  methods.

- [`binocular_disparity_ms`](binocular_disparity_ms.md) — Compute the disparities of a rectified stereo image pair using
  multi-scanline optimization.

- [`binocular_distance`](binocular_distance.md) — Compute the distance values for a rectified stereo image pair using
  correlation techniques.

- [`binocular_distance_mg`](binocular_distance_mg.md) — Compute the distance values for a rectified stereo image pair using
  multigrid methods.

- [`binocular_distance_ms`](binocular_distance_ms.md) — Compute the distance values for a rectified stereo image pair using
  multi-scanline optimization.

- [`disparity_image_to_xyz`](disparity_image_to_xyz.md) — Transform a disparity image into 3D points in a rectified stereo
  system.

- [`disparity_to_distance`](disparity_to_distance.md) — Transform a disparity value into a distance value in a rectified
  binocular stereo system.

- [`disparity_to_point_3d`](disparity_to_point_3d.md) — Transform an image point and its disparity into a 3D point in a
  rectified stereo system.

- [`distance_to_disparity`](distance_to_disparity.md) — Transform a distance value into a disparity in a rectified stereo
  system.

- [`essential_to_fundamental_matrix`](essential_to_fundamental_matrix.md) — Compute the fundamental matrix from an essential matrix.

- [`gen_binocular_proj_rectification`](gen_binocular_proj_rectification.md) — Compute the projective rectification of weakly calibrated binocular
  stereo images.

- [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md) — Generate transformation maps that describe the mapping of the images
  of a binocular camera pair to a common rectified image plane.

- [`intersect_lines_of_sight`](intersect_lines_of_sight.md) — Get a 3D point from the intersection of two lines of sight
  within a binocular camera system.

- [`match_essential_matrix_ransac`](match_essential_matrix_ransac.md) — Compute the essential matrix for a pair of stereo images by automatically
  finding correspondences between image points.

- [`match_fundamental_matrix_distortion_ransac`](match_fundamental_matrix_distortion_ransac.md) — Compute the fundamental matrix and the radial distortion coefficient
  for a pair of stereo images by automatically finding correspondences
  between image points.

- [`match_fundamental_matrix_ransac`](match_fundamental_matrix_ransac.md) — Compute the fundamental matrix for a pair of stereo images by
  automatically finding correspondences between image
  points.

- [`match_rel_pose_ransac`](match_rel_pose_ransac.md) — Compute the relative orientation between two cameras by automatically
  finding correspondences between image points.

- [`reconst3d_from_fundamental_matrix`](reconst3d_from_fundamental_matrix.md) — Compute the projective 3d reconstruction of points based on the fundamental
  matrix.

- [`rel_pose_to_fundamental_matrix`](rel_pose_to_fundamental_matrix.md) — Compute the fundamental matrix from the relative orientation of two
  cameras.

- [`vector_to_essential_matrix`](vector_to_essential_matrix.md) — Compute the essential matrix given image point correspondences
  and known camera matrices and reconstruct 3D points.

- [`vector_to_fundamental_matrix`](vector_to_fundamental_matrix.md) — Compute the fundamental matrix given a set of image point
  correspondences and reconstruct 3D points.

- [`vector_to_fundamental_matrix_distortion`](vector_to_fundamental_matrix_distortion.md) — Compute the fundamental matrix and the radial distortion coefficient
  given a set of image point correspondences and reconstruct 3D
  points.

- [`vector_to_rel_pose`](vector_to_rel_pose.md) — Compute the relative orientation between two cameras given image point
  correspondences and known camera parameters and reconstruct 3D space points.
