_base_ = ['fcaf3d_scannet-3d-18class.py']
voxel_size = 0.05

model = dict(
    voxel_size=voxel_size,
    backbone=dict(
        stride=1),
    neck_with_head=dict(
        voxel_size=voxel_size))
