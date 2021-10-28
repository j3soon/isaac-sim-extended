# Isaac Sim Commands

Isaac Sim Version: `2021.1.1-beta.9+2021.1.141.a62eacb5.teamcity`

## Redo

Base class for all **Commands**.

## Undo

Base class for all **Commands**.

## AddReferenceCommand

Base class for all **Commands**.

## AddReference

Base class for all **Commands**.

## AddRelationshipTargetCommand

Add target to a relationship

## AddRelationshipTarget

Add target to a relationship

## BindMaterialCommand

Bind material undoable **Command**.

Args:
- prim_path (str or list): Path(s) to prim or collection
- material_path (str): Path to material to bind.
- strength (float): Strength.

## BindMaterial

Bind material undoable **Command**.

Args:
- prim_path (str or list): Path(s) to prim or collection
- material_path (str): Path to material to bind.
- strength (float): Strength.

## ChangeAttributesColorSpaceCommand

Change attribute color space undoable **Command**.

Args:
- attributes (List[str]): attributes to set color space on.
- color_space: Value of metadata to change to.

## ChangeAttributesColorSpace

Change attribute color space undoable **Command**.

Args:
- attributes (List[str]): attributes to set color space on.
- color_space: Value of metadata to change to.

## ChangeMetadataCommand

Change object metadata undoable **Command**.

Args:
- object_paths (List[str]): Object paths, can be attribute or prim.
- key: Key of metadata to change.
- value: Value of metadata to change to.

## ChangeMetadata

Change object metadata undoable **Command**.

Args:
- object_paths (List[str]): Object paths, can be attribute or prim.
- key: Key of metadata to change.
- value: Value of metadata to change to.

## ChangeMetadataInPrimsCommand

Change prim metadata undoable **Command**.

Args:
- prim_paths (List[str]): Prim paths.
- key: Key of metadata to change.
- value: Value of metadata to change to.

## ChangeMetadataInPrims

Change prim metadata undoable **Command**.

Args:
- prim_paths (List[str]): Prim paths.
- key: Key of metadata to change.
- value: Value of metadata to change to.

## ChangePropertyCommand

Change prim property undoable **Command**.

Args:
- prop_path (str): Prim property path.
- value: Value to change to.
- prev: Value to undo to.
- timecode: The timecode to set property value to.
- type_to_create_if_not_exist: If not None AND property does not already exist, a new property will be created with given type and value.

## ChangeProperty

Change prim property undoable **Command**.

Args:
- prop_path (str): Prim property path.
- value: Value to change to.
- prev: Value to undo to.
- timecode: The timecode to set property value to.
- type_to_create_if_not_exist: If not None AND property does not already exist, a new property will be created with given type and value.

## ClearRefinementOverridesCommand

Clear Refinement Overrides  **Command**.

## ClearRefinementOverrides

Clear Refinement Overrides  **Command**.

## CopyPrimCommand

Copy primitive undoable **Command**.

Args:
- path_from (str): Path to copy from.
- path_to (str): Path to copy to. If `None` next free path is generated.
- duplicate_layers (bool): Duplicate layers on copy.
- combine_layers (bool): Combine layers on copy.
- exclusive_select (bool): If to exclusively select (clear old selections) the newly create object.

## CopyPrim

Copy primitive undoable **Command**.

Args:
- path_from (str): Path to copy from.
- path_to (str): Path to copy to. If `None` next free path is generated.
- duplicate_layers (bool): Duplicate layers on copy.
- combine_layers (bool): Combine layers on copy.
- exclusive_select (bool): If to exclusively select (clear old selections) the newly create object.

## CopyPrimsCommand

Copy multiple primitives undoable **Command**.

Args:
- paths_from List[str]: Paths to copy from.
- paths_to List[str]: Paths to copy to. If `None` or length smaller than paths_from, then next free path is generated for missing paths.
- duplicate_layers (bool): Duplicate layers on copy.
- combine_layers (bool): Combine layers on copy.

## CopyPrims

Copy multiple primitives undoable **Command**.

Args:
- paths_from List[str]: Paths to copy from.
- paths_to List[str]: Paths to copy to. If `None` or length smaller than paths_from, then next free path is generated for missing paths.
- duplicate_layers (bool): Duplicate layers on copy.
- combine_layers (bool): Combine layers on copy.

## CreateAudioPrimFromAssetPathCommand

Create reference undoable **Command**.

It creates a new Audio prim.

Args:
- usd_context (omni.usd.UsdContext): UsdContext this command to run on.
- path_to (Sdf.Path): Path to create a new prim.
- asset_path (str): The asset it's necessary to add to references.

## CreateAudioPrimFromAssetPath

Create reference undoable **Command**.

It creates a new Audio prim.

Args:
- usd_context (omni.usd.UsdContext): UsdContext this command to run on.
- path_to (Sdf.Path): Path to create a new prim.
- asset_path (str): The asset it's necessary to add to references.

## CreateDefaultXformOnPrimCommand

Create DefaultXform On Prim undoable **Command**.

Args:
- prim_path (str): Path of the primitive to be create xform attribtues

## CreateDefaultXformOnPrim

Create DefaultXform On Prim undoable **Command**.

Args:
- prim_path (str): Path of the primitive to be create xform attribtues

## CreateInstanceCommand

Instance primitive undoable **Command**.

It creates a new prim, adds the master object to references, and flags this prim as instanceable. It the prim is
Xform, this command copies the transforms from the current frame. If the source prim is already instanceable, it
tries to find master prim of this prim and uses it, so it's perfectly safe to press Ctrl-I multiple times.

Args:
- path_from (str): Path to instance from.

## CreateInstance

Instance primitive undoable **Command**.

It creates a new prim, adds the master object to references, and flags this prim as instanceable. It the prim is
Xform, this command copies the transforms from the current frame. If the source prim is already instanceable, it
tries to find master prim of this prim and uses it, so it's perfectly safe to press Ctrl-I multiple times.

Args:
- path_from (str): Path to instance from.

## CreateInstancesCommand

Instance multiple primitives undoable **Command**.

Args:
- paths_from List[str]: Paths to instance from.

## CreateInstances

Instance multiple primitives undoable **Command**.

Args:
- paths_from List[str]: Paths to instance from.

## CreateMdlMaterialPrimCommand

Create Mdl Material undoable **Command**.

Args:
- mtl_url (str):
- mtl_name (str):
- mtl_path (str):
- select_new_prim (bool):

## CreateMdlMaterialPrim

Create Mdl Material undoable **Command**.

Args:
- mtl_url (str):
- mtl_name (str):
- mtl_path (str):
- select_new_prim (bool):

## CreatePreviewSurfaceMaterialPrimCommand

Create Preview Surface Material undoable **Command**.

Args:
- mtl_path (str):
- select_new_prim (bool):

## CreatePreviewSurfaceMaterialPrim

Create Preview Surface Material undoable **Command**.

Args:
- mtl_path (str):
- select_new_prim (bool):

## CreatePreviewSurfaceTextureMaterialPrimCommand

Create Preview Surface Texture Material undoable **Command**.

Args:
- mtl_path (str):
- select_new_prim (bool):

## CreatePreviewSurfaceTextureMaterialPrim

Create Preview Surface Texture Material undoable **Command**.

Args:
- mtl_path (str):
- select_new_prim (bool):

## CreatePrimCommand

Create primitive undoable **Command**. It is same as `CreatePrimWithDefaultXformCommand`.
Kept for backward compatibility.

Args:
- prim_type (str): Primitive type, e.g. "Sphere", "Cube" etc.
- prim_path (str): Path of the primitive to be created at. If None is provided, it will be placed at stage root or under default prim using Type name.
- select_new_prim (bool) : Whether to select the prim after it's created.
- attributes (Dict[str, object]): optional attributes dict to set after creation.

## CreatePrim

Create primitive undoable **Command**. It is same as `CreatePrimWithDefaultXformCommand`.
Kept for backward compatibility.

Args:
- prim_type (str): Primitive type, e.g. "Sphere", "Cube" etc.
- prim_path (str): Path of the primitive to be created at. If None is provided, it will be placed at stage root or under default prim using Type name.
- select_new_prim (bool) : Whether to select the prim after it's created.
- attributes (Dict[str, object]): optional attributes dict to set after creation.

## CreatePrimCommandBase

Base class to create a prim (and remove when undo)

Args:
- usd_context (omni.usd.UsdContext): UsdContext this command to run on.
- path_to (Sdf.Path): Path to create a new prim.
- asset_path (str): The asset it's necessary to add to references.

## CreatePrimWithDefaultXformCommand

Create primitive undoable **Command**.

Args:
- prim_type (str): Primitive type, e.g. "Sphere", "Cube" etc.
- prim_path (str): Path of the primitive to be created at. If None is provided, it will be placed at stage root or under default prim using Type name.
- select_new_prim (bool) : Whether to select the prim after it's created.
- attributes (Dict[str, object]): optional attributes dict to set after creation.

## CreatePrimWithDefaultXform

Create primitive undoable **Command**.

Args:
- prim_type (str): Primitive type, e.g. "Sphere", "Cube" etc.
- prim_path (str): Path of the primitive to be created at. If None is provided, it will be placed at stage root or under default prim using Type name.
- select_new_prim (bool) : Whether to select the prim after it's created.
- attributes (Dict[str, object]): optional attributes dict to set after creation.

## CreatePrimsCommand

Create multiple primitives undoable **Command**.

Example of command which calls other commands. Undo/Redo grouping handled automatically.

Args:
- prim_types (List[str]): List of primitive types to create, e.g ["Sphere", "Cone"].

## CreatePrims

Create multiple primitives undoable **Command**.

Example of command which calls other commands. Undo/Redo grouping handled automatically.

Args:
- prim_types (List[str]): List of primitive types to create, e.g ["Sphere", "Cone"].

## CreateReferenceCommand

Create reference undoable **Command**.

It creates a new prim and adds the asset and path as references.

Args:
- usd_context (omni.usd.UsdContext): UsdContext this command to run on.
- path_to (Sdf.Path): Path to create a new prim.
- asset_path (str): The asset it's necessary to add to references.
- prim_path (Sdf.Path): The prim in asset to reference.
- instanceable (bool): Whether to set the prim instanceable. It works together with `/persistent/app/stage/instanceableOnCreatingReference` setting.

## CreateReference

Create reference undoable **Command**.

It creates a new prim and adds the asset and path as references.

Args:
- usd_context (omni.usd.UsdContext): UsdContext this command to run on.
- path_to (Sdf.Path): Path to create a new prim.
- asset_path (str): The asset it's necessary to add to references.
- prim_path (Sdf.Path): The prim in asset to reference.
- instanceable (bool): Whether to set the prim instanceable. It works together with `/persistent/app/stage/instanceableOnCreatingReference` setting.

## DeletePrimsCommand

Delete primitives undoable **Command**.

Args:
- paths (List[str]): Paths to prims to delete.

## DeletePrims

Delete primitives undoable **Command**.

Args:
- paths (List[str]): Paths to prims to delete.

## MovePrimCommand

Move primitive undoable **Command**.

Args:
- path_from (str): Path to move prim from.
- path_to(str): Path to move prim to.
- time_code(Usd.TimeCode): Current timecode of the stage.
- keep_world_transform(bool): True to keep world transform after prim path is moved. False to keep local transfrom only.
- on_move_fn(Callable): Function to call when prim is renamed

## MovePrim

Move primitive undoable **Command**.

Args:
- path_from (str): Path to move prim from.
- path_to(str): Path to move prim to.
- time_code(Usd.TimeCode): Current timecode of the stage.
- keep_world_transform(bool): True to keep world transform after prim path is moved. False to keep local transfrom only.
- on_move_fn(Callable): Function to call when prim is renamed

## MovePrimsCommand

Move primitives undoable **Command**.

Args:
- paths_to_move Dict[str, str]: dictionary contaning entry of path_from : path_to.
- time_code(Usd.TimeCode): Current timecode of the stage.
- keep_world_transform(bool): True to keep world transform after prim path is moved. False to keep local transfrom only.

## MovePrims

Move primitives undoable **Command**.

Args:
- paths_to_move Dict[str, str]: dictionary contaning entry of path_from : path_to.
- time_code(Usd.TimeCode): Current timecode of the stage.
- keep_world_transform(bool): True to keep world transform after prim path is moved. False to keep local transfrom only.

## ReferenceCommandBase

Base class for all **Commands**.

## RelationshipTargetBase

Base class for all **Commands**.

## RemoveReferenceCommand

Base class for all **Commands**.

## RemoveReference

Base class for all **Commands**.

## RemoveRelationshipTargetCommand

Remove target from a relationship

## RemoveRelationshipTarget

Remove target from a relationship

## ReplaceReferenceCommand

Base class for all **Commands**.

## ReplaceReference

Base class for all **Commands**.

## ReplaceReferencesCommand

Clears/Add references undoable **Command**.

NOTE: THIS COMMAND HAS A LOT OF ISSUES AND IS DEPRECATED. PLEASE USE ReplaceReferenceCommand instead!

Args:
- path (str): Prim path.
- old_url(str): Url to be replaced.
- new_url(str): Replacement url.

## ReplaceReferences

Clears/Add references undoable **Command**.

NOTE: THIS COMMAND HAS A LOT OF ISSUES AND IS DEPRECATED. PLEASE USE ReplaceReferenceCommand instead!

Args:
- path (str): Prim path.
- old_url(str): Url to be replaced.
- new_url(str): Replacement url.

## SelectPrimsCommand

Select primitives undoable **Command**.

Args:
- old_selected_paths (List[str]): Old selected prim paths.
- new_selected_paths (List[str]): Prim paths to be selected.
- expand_in_stage (bool, DEPRECATED): Whether to expand the path in Stage Window on selection.
- This param is left for compatibility.

## SelectPrims

Select primitives undoable **Command**.

Args:
- old_selected_paths (List[str]): Old selected prim paths.
- new_selected_paths (List[str]): Prim paths to be selected.
- expand_in_stage (bool, DEPRECATED): Whether to expand the path in Stage Window on selection.
- This param is left for compatibility.

## SetMaterialStrengthCommand

Set material binding strength undoable **Command**.

Args:
- rel: Material binding relationship.
- strength (float): Strength.

## SetMaterialStrength

Set material binding strength undoable **Command**.

Args:
- rel: Material binding relationship.
- strength (float): Strength.

## ToggleVisibilitySelectedPrimsCommand

Toggles the visiblity of the selected primitives undoable **Command**.

Args:
- selected_paths (List[str]): Old selected prim paths.

## ToggleVisibilitySelectedPrims

Toggles the visiblity of the selected primitives undoable **Command**.

Args:
- selected_paths (List[str]): Old selected prim paths.

## TransformPrimCommand

Transform primitive undoable **Command**.

Args:
- path (str): Prim path.
- new_transform_matrix: New transform matrix.
- old_transform_matrix: Optional old transform matrix to undo to. If `None` use current transform.

## TransformPrim

Transform primitive undoable **Command**.

Args:
- path (str): Prim path.
- new_transform_matrix: New transform matrix.
- old_transform_matrix: Optional old transform matrix to undo to. If `None` use current transform.

## TransformPrimSRTCommand

Transform primitive undoable **Command**.

Args:
- path (str): Prim path.
- new_translation (Gf.Vec3d): New local translation.
- new_rotation_euler (Gf.Vec3d): New local rotation euler angles (in degree).
- new_scale (Gf.Vec3d): New scale.
- new_rotation_order (Gf.Vec3i): New rotation order (e.g. (0, 1, 2) means XYZ). Set to None to stay the same.
- old_translation (Gf.Vec3d): Old local translation. Leave to None to use current value.
- old_rotation_euler (Gf.Vec3d): Old local rotation euler angles. Leave to None to use current value.
- old_rotation_order (Gf.Vec3i): Old local rotation order. Leave to None to use current value.
- old_scale (Gf.Vec3d): Old scale. Leave to None to use current value.
- time_code (Usd.TimeCode): TimeCode to set transform to.
- had_transform_at_key (bool): If there's key for transfrom.
- usd_context_name (str): Usd context name to run the command on.

## TransformPrimSRT

Transform primitive undoable **Command**.

Args:
- path (str): Prim path.
- new_translation (Gf.Vec3d): New local translation.
- new_rotation_euler (Gf.Vec3d): New local rotation euler angles (in degree).
- new_scale (Gf.Vec3d): New scale.
- new_rotation_order (Gf.Vec3i): New rotation order (e.g. (0, 1, 2) means XYZ). Set to None to stay the same.
- old_translation (Gf.Vec3d): Old local translation. Leave to None to use current value.
- old_rotation_euler (Gf.Vec3d): Old local rotation euler angles. Leave to None to use current value.
- old_rotation_order (Gf.Vec3i): Old local rotation order. Leave to None to use current value.
- old_scale (Gf.Vec3d): Old scale. Leave to None to use current value.
- time_code (Usd.TimeCode): TimeCode to set transform to.
- had_transform_at_key (bool): If there's key for transfrom.
- usd_context_name (str): Usd context name to run the command on.

## TransformPrimsCommand

Transform multiple primitives undoable **Command**.

Undo/Redo grouping handled automatically.

Args:
- prims_to_transform: List of primitive to transform in a tuple of (path, new_transform, old_transform).

## TransformPrims

Transform multiple primitives undoable **Command**.

Undo/Redo grouping handled automatically.

Args:
- prims_to_transform: List of primitive to transform in a tuple of (path, new_transform, old_transform).

## TransformPrimsSRTCommand

Transform multiple primitives undoable **Command**.

Undo/Redo grouping handled automatically.

Args:
- prims_to_transform: List of primitive to transform in a tuple of
-                     (path,
-                     new_translation,
-                     new_rotation_euler,
-                     new_rotation_order,
-                     new_scale,
-                     old_translation,
-                     old_rotation_euler,
-                     old_rotation_order,
-                     old_scale,
-                     time_code,
-                     had_transform_at_key).

## TransformPrimsSRT

Transform multiple primitives undoable **Command**.

Undo/Redo grouping handled automatically.

Args:
- prims_to_transform: List of primitive to transform in a tuple of
-                     (path,
-                     new_translation,
-                     new_rotation_euler,
-                     new_rotation_order,
-                     new_scale,
-                     old_translation,
-                     old_rotation_euler,
-                     old_rotation_order,
-                     old_scale,
-                     time_code,
-                     had_transform_at_key).

## UnhideAllPrimsCommand

Base class for all **Commands**.

## UnhideAllPrims

Base class for all **Commands**.

## AddCollisionGroupCommand

Wrapper for omni.physx.utils.addCollisionGroup. Creates a UsdPhysics.CollisionGroup prim.

Args:
- stage: USD stage.
- path: Path of the primitive to be created at. 

## AddCollisionGroup

Wrapper for omni.physx.utils.addCollisionGroup. Creates a UsdPhysics.CollisionGroup prim.

Args:
- stage: USD stage.
- path: Path of the primitive to be created at. 

## AddD6PhysicsJointComponentCommand

Base class for all **Commands**.

## AddD6PhysicsJointComponent

Base class for all **Commands**.

## AddDistancePhysicsJointComponentCommand

Base class for all **Commands**.

## AddDistancePhysicsJointComponent

Base class for all **Commands**.

## AddFixedPhysicsJointComponentCommand

Base class for all **Commands**.

## AddFixedPhysicsJointComponent

Base class for all **Commands**.

## AddGroundPlaneCommand

Wrapper for omni.physx.physicsUtils.add_ground_plane. Adds a zero-thick plane to prevent physics-enabled prims from     falling to infinity. Creates an UsdGeom.Xform with a UsdGeom.Mesh and a PhysxSchema.Plane child primitives.

Args:
- stage: USD stage.
- planePath: Path for the root xform to be created at. Finds first free path.
- axis: Up axis.
- size: Halfsize of one side.
- position: Center of the plane.
- color: Display color.

Returns:
- Path where the plane was actually created.

## AddGroundPlane

Wrapper for omni.physx.physicsUtils.add_ground_plane. Adds a zero-thick plane to prevent physics-enabled prims from     falling to infinity. Creates an UsdGeom.Xform with a UsdGeom.Mesh and a PhysxSchema.Plane child primitives.

Args:
- stage: USD stage.
- planePath: Path for the root xform to be created at. Finds first free path.
- axis: Up axis.
- size: Halfsize of one side.
- position: Center of the plane.
- color: Display color.

Returns:
- Path where the plane was actually created.

## AddMaterialCommand

Wrapper for omni.physx.utils.addMaterial. Creates a UsdShade.Material prim and adds a UsdPhysics.MaterialAPI to it.

Args:
- stage: USD stage.
- path: Path of the primitive to be created at. 
- density: Physics material param.
- staticFriction: Physics material param.
- dynamicFriction: Physics material param.
- restitution: Physics material param.

## AddMaterial

Wrapper for omni.physx.utils.addMaterial. Creates a UsdShade.Material prim and adds a UsdPhysics.MaterialAPI to it.

Args:
- stage: USD stage.
- path: Path of the primitive to be created at. 
- density: Physics material param.
- staticFriction: Physics material param.
- dynamicFriction: Physics material param.
- restitution: Physics material param.

## AddPairFilterCommand

Wrapper for omni.physx.utils.addPairFilter. Filters out collisions between primitives using UsdPhysics.FilteredPairsAPI.

Args:
- stage: USD stage.
- primPaths: List of paths. 

## AddPairFilter

Wrapper for omni.physx.utils.addPairFilter. Filters out collisions between primitives using UsdPhysics.FilteredPairsAPI.

Args:
- stage: USD stage.
- primPaths: List of paths. 

## AddPhysicsComponentCommand

Add physics component command. See omni.physx.commands source for currently valid component names.

Args:
- usd_prim: USD prim to apply a component to.
- str: Component name.

## AddPhysicsComponent

Add physics component command. See omni.physx.commands source for currently valid component names.

Args:
- usd_prim: USD prim to apply a component to.
- str: Component name.

## AddPhysicsSceneCommand

Wrapper for omni.physx.utils.addPhysicsScene. Adds a UsdPhysics.Scene prim with default params.

Args:
- stage: USD stage.
- path: Path of the primitive to be created at. 

## AddPhysicsScene

Wrapper for omni.physx.utils.addPhysicsScene. Adds a UsdPhysics.Scene prim with default params.

Args:
- stage: USD stage.
- path: Path of the primitive to be created at. 

## AddPrismaticPhysicsJointComponentCommand

Base class for all **Commands**.

## AddPrismaticPhysicsJointComponent

Base class for all **Commands**.

## AddRevolutePhysicsJointComponentCommand

Base class for all **Commands**.

## AddRevolutePhysicsJointComponent

Base class for all **Commands**.

## AddSphericalPhysicsJointComponentCommand

Base class for all **Commands**.

## AddSphericalPhysicsJointComponent

Base class for all **Commands**.

## ApplyAPISchemaCommand

Undoable Apply API command.

Args:
- api: API class.
- prim: Target primitive.
- api_prefix: Prefix of a multiple-apply API.
- multiple_api_token: Token of a multiple-apply API.

## ApplyAPISchema

Undoable Apply API command.

Args:
- api: API class.
- prim: Target primitive.
- api_prefix: Prefix of a multiple-apply API.
- multiple_api_token: Token of a multiple-apply API.

## ChangeAttributeCommand

Change prim property undoable **Command**.

Args:
- attr (attribute): Attribute to change.
- value: Value to change to.
- value: Value to undo to.

## ChangeAttribute

Change prim property undoable **Command**.

Args:
- attr (attribute): Attribute to change.
- value: Value to change to.
- value: Value to undo to.

## Command

Base class for all **Commands**.

## 

Base class for all **Commands**.

## CreateJointCommand

Wrapper for omni.physx.utils.createJoint. Connects two primitives with a physical joints.

Args:
- stage: Path of the target primitive.
- joint_type: Fixed, Revolute, Prismatic, Spherical or Distance. If left blank a D6 Joint is used.
- from_prim: From primitive.
- to_prim: To primitive.

Returns: 
- Joint primitive.

## CreateJoint

Wrapper for omni.physx.utils.createJoint. Connects two primitives with a physical joints.

Args:
- stage: Path of the target primitive.
- joint_type: Fixed, Revolute, Prismatic, Spherical or Distance. If left blank a D6 Joint is used.
- from_prim: From primitive.
- to_prim: To primitive.

Returns: 
- Joint primitive.

## CreateJointsCommand

Wrapper for omni.physx.utils.createJoints. Connects a list of primitives with their parent or a pseudo-root with physical joints.

Args:
- stage: Path of the target primitive.
- joint_type: Fixed, Revolute, Prismatic, Spherical or Distance. If left blank a D6 Joint is used.
- paths: A list of paths.
- join_to_parent: Connect primitives to their parents if True, otherwise to a scene pseudo-root.

Returns: 
- Joint primitives.

## CreateJoints

Wrapper for omni.physx.utils.createJoints. Connects a list of primitives with their parent or a pseudo-root with physical joints.

Args:
- stage: Path of the target primitive.
- joint_type: Fixed, Revolute, Prismatic, Spherical or Distance. If left blank a D6 Joint is used.
- paths: A list of paths.
- join_to_parent: Connect primitives to their parents if True, otherwise to a scene pseudo-root.

Returns: 
- Joint primitives.

## PhysicsCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## Physics

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## RemoveAttributeCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## RemoveAttribute

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## RemoveD6PhysicsJointComponentCommand

Base class for all **Commands**.

## RemoveD6PhysicsJointComponent

Base class for all **Commands**.

## RemoveDistancePhysicsJointComponentCommand

Base class for all **Commands**.

## RemoveDistancePhysicsJointComponent

Base class for all **Commands**.

## RemoveFixedPhysicsJointComponentCommand

Base class for all **Commands**.

## RemoveFixedPhysicsJointComponent

Base class for all **Commands**.

## RemovePairFilterCommand

Wrapper for omni.physx.utils.removePairFilter. Removes UsdPhysics.FilteredPairsAPI from primitives.

Args:
- stage: USD stage.
- primPaths: List of paths. 

## RemovePairFilter

Wrapper for omni.physx.utils.removePairFilter. Removes UsdPhysics.FilteredPairsAPI from primitives.

Args:
- stage: USD stage.
- primPaths: List of paths. 

## RemovePhysicsComponentCommand

Remove physics component. See omni.physx.commands source for currently valid components.

Args:
- usd_prim: USD prim to apply a component to.
- str: Component name. 

## RemovePhysicsComponent

Remove physics component. See omni.physx.commands source for currently valid components.

Args:
- usd_prim: USD prim to apply a component to.
- str: Component name. 

## RemovePrismaticPhysicsJointComponentCommand

Base class for all **Commands**.

## RemovePrismaticPhysicsJointComponent

Base class for all **Commands**.

## RemoveRelationshipCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## RemoveRelationship

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## RemoveRevolutePhysicsJointComponentCommand

Base class for all **Commands**.

## RemoveRevolutePhysicsJointComponent

Base class for all **Commands**.

## RemoveRigidBodyCommand

Wrapper for omni.physx.utils.removeRigidBody.

Args:
- path: Path of the target primitive.

## RemoveRigidBody

Wrapper for omni.physx.utils.removeRigidBody.

Args:
- path: Path of the target primitive.

## RemoveSphericalPhysicsJointComponentCommand

Base class for all **Commands**.

## RemoveSphericalPhysicsJointComponent

Base class for all **Commands**.

## RemoveStaticColliderCommand

Wrapper for omni.physx.utils.removeStaticCollider.

Args:
- path: Path of the target primitive.

## RemoveStaticCollider

Wrapper for omni.physx.utils.removeStaticCollider.

Args:
- path: Path of the target primitive.

## SetRigidBodyCommand

Wrapper for omni.physx.utils.setRigidBody. Applies UsdPhysics.RigidBodyAPI and a UsdPhysics.CollisionAPI to target prim.     Applies UsdPhysics.MeshCollisionAPI and PhysxSchema.PhysxMeshCollisionAPI if it's a mesh. Collision API's are also applied to     the whole subtree if the target prim is an xform.

Args:
- path: Path of the target primitive.
- approximationShape: Physics param.
- kinematic: Physics param.

## SetRigidBody

Wrapper for omni.physx.utils.setRigidBody. Applies UsdPhysics.RigidBodyAPI and a UsdPhysics.CollisionAPI to target prim.     Applies UsdPhysics.MeshCollisionAPI and PhysxSchema.PhysxMeshCollisionAPI if it's a mesh. Collision API's are also applied to     the whole subtree if the target prim is an xform.

Args:
- path: Path of the target primitive.
- approximationShape: Physics param.
- kinematic: Physics param.

## SetStaticColliderCommand

Wrapper for omni.physx.utils.setStaticCollider. Applies Collision APIs (UsdPhysics.CollisionAPI,  UsdPhysics.MeshCollisionAPI     PhysxSchema.PhysxMeshCollisionAPI) to a target prim and its subtree.

Args:
- path: Path of the target primitive.
- approximationShape: Physics param.

## SetStaticCollider

Wrapper for omni.physx.utils.setStaticCollider. Applies Collision APIs (UsdPhysics.CollisionAPI,  UsdPhysics.MeshCollisionAPI     PhysxSchema.PhysxMeshCollisionAPI) to a target prim and its subtree.

Args:
- path: Path of the target primitive.
- approximationShape: Physics param.

## UnapplyAPISchemaCommand

Undoable Unapply API command.

Args:
- api: API class.
- prim: Target primitive.
- api_prefix: Prefix of a multiple-apply API.
- multiple_api_token: Token of a multiple-apply API.

## UnapplyAPISchema

Undoable Unapply API command.

Args:
- api: API class.
- prim: Target primitive.
- api_prefix: Prefix of a multiple-apply API.
- multiple_api_token: Token of a multiple-apply API.

## DuplicateFromActiveViewportCameraCommand

Duplicates Viewport's actively bound camera and bind active camera to the duplicated one.

Args:
- viewport_name (str): name of the viewport to set active camera (for multi-viewport).

## DuplicateFromActiveViewportCamera

Duplicates Viewport's actively bound camera and bind active camera to the duplicated one.

Args:
- viewport_name (str): name of the viewport to set active camera (for multi-viewport).

## SetActiveViewportCameraCommand

Sets Viewport's actively bound camera to given camera at give path.

Args:
- new_active_cam_path (Union[str, Sdf.Path): new camera path to bind to viewport.
- viewport_name (str): name of the viewport to set active camera (for multi-viewport).

## SetActiveViewportCamera

Sets Viewport's actively bound camera to given camera at give path.

Args:
- new_active_cam_path (Union[str, Sdf.Path): new camera path to bind to viewport.
- viewport_name (str): name of the viewport to set active camera (for multi-viewport).

## SelectVariantPrimCommand

Base class for all **Commands**.

## SelectVariantPrim

Base class for all **Commands**.

## ToolbarPauseButtonClickedCommand

On clicked toolbar pause button **Command**.

## ToolbarPauseButtonClicked

On clicked toolbar pause button **Command**.

## ToolbarPlayButtonClickedCommand

On clicked toolbar play button **Command**.

## ToolbarPlayButtonClicked

On clicked toolbar play button **Command**.

## ToolbarPlayFilterCheckedCommand

Change settings depending on the status of play filter checkboxes **Command**.

Args:
- path: Path to the setting to change.
- enabled: New value to change to.

## ToolbarPlayFilterChecked

Change settings depending on the status of play filter checkboxes **Command**.

Args:
- path: Path to the setting to change.
- enabled: New value to change to.

## ToolbarPlayFilterSelectAllCommand

Sets all play filter settings to True **Command**.

Args:
- settings: Paths to the settings.

## ToolbarPlayFilterSelectAll

Sets all play filter settings to True **Command**.

Args:
- settings: Paths to the settings.

## ToolbarStopButtonClickedCommand

On clicked toolbar stop button **Command**.

## ToolbarStopButtonClicked

On clicked toolbar stop button **Command**.

## TransformJointCommand

Base class for all **Commands**.

## TransformJoint

Base class for all **Commands**.

## BindMaterialExtCommand

Base class for all **Commands**.

## BindMaterialExt

Base class for all **Commands**.

## PhysXVehicleAddDroneCameraCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleAddDroneCamera

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleAddFollowCameraCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleAddFollowCamera

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleControllerEnableAutoReverseCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleControllerEnableAutoReverse

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleControllerEnableInputCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleControllerEnableInput

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleControllerEnableMouseCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleControllerEnableMouse

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleSetRelationshipCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleSetRelationship

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleTireFrictionTableAddCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleTireFrictionTableAdd

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleTireFrictionTableAddEntryCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleTireFrictionTableAddEntry

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleTireFrictionTableChangeEntryCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleTireFrictionTableChangeEntry

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleTireFrictionTableRemoveEntryCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleTireFrictionTableRemoveEntry

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleUpdateAllCamerasCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleUpdateAllCameras

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleWheelSimTransformsAutocomputeCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleWheelSimTransformsAutocompute

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleWizardCreateCommand

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## PhysXVehicleWizardCreate

Base class for physics commands. Adds an execute helper to not force the user to use only keyword arguments

## IsaacSimDestroyPrim

Command to set a delete a prim. This variant has less overhead than other commands as it doesn't store an undo operation

Typical usage example:

.. code-block:: python

    omni.kit.commands.execute(
        "IsaacSimDestroyPrim",
        prim_path="/World/Prim,
    )

## IsaacSimScalePrim

Command to set a scale of a prim

Typical usage example:

.. code-block:: python

    omni.kit.commands.execute(
        "IsaacSimScalePrim",
        prim_path="/World/Prim,
        scale=(1.5, 1.5, 1.5),
    )

## IsaacSimSpawnPrim

Command to spawn a new prim in the stage and set its transform. This uses dynamic_control to properly handle physics objects and articulation

Typical usage example:

.. code-block:: python

    omni.kit.commands.execute(
        "IsaacSimSpawnPrim",
        usd_path="/path/to/file.usd",
        prim_path="/World/Prim,
        translation=(0, 0, 0),
        rotation=(0, 0, 0, 1),
    )

## IsaacSimTeleportPrim

Command to set a transform of a prim. This uses dynamic_control to properly handle physics objects and articulation

Typical usage example:

.. code-block:: python

    omni.kit.commands.execute(
        "IsaacSimTeleportPrim",
        prim_path="/World/Prim,
        translation=(0, 0, 0),
        rotation=(0, 0, 0, 1),
    )

## RobotEngineBridgeCreateCamera

Base class for all **Commands**.

## RobotEngineBridgeCreateCommand

Base class for all **Commands**.

## RobotEngineBridgeCreate

Base class for all **Commands**.

## RobotEngineBridgeCreateContactMonitor

Base class for all **Commands**.

## RobotEngineBridgeCreateDifferentialBase

Base class for all **Commands**.

## RobotEngineBridgeCreateHolonomicBase

Base class for all **Commands**.

## RobotEngineBridgeCreateJointControl

Base class for all **Commands**.

## RobotEngineBridgeCreateLidar

Base class for all **Commands**.

## RobotEngineBridgeCreateOccupancyGridMap

Base class for all **Commands**.

## RobotEngineBridgeCreatePolylineVisualizer

Base class for all **Commands**.

## RobotEngineBridgeCreatePoseTree

Base class for all **Commands**.

## RobotEngineBridgeCreatePrim

Base class for all **Commands**.

## RobotEngineBridgeCreateRigidBodySink

Base class for all **Commands**.

## RobotEngineBridgeCreateScenarioFromMessage

Base class for all **Commands**.

## RobotEngineBridgeCreateScissorLift

Base class for all **Commands**.

## RobotEngineBridgeCreateSurfaceGripper

Base class for all **Commands**.

## RobotEngineBridgeCreateTeleport

Base class for all **Commands**.

## RobotEngineBridgeCreateTwoFingerGripper

Base class for all **Commands**.

## RobotEngineBridgeCreateUltrasonic

Base class for all **Commands**.

## RobotEngineBridgeCreateVehicle

Base class for all **Commands**.

## RangeSensorCreateGeneric

Commands class to create a generic range sensor.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "RangeSensorCreateGeneric",
        path="/GenericSensor",
        parent=None,
        min_range=0.4,
        max_range=100.0,
        draw_points=False,
        draw_lines=False,
        sampling_rate=60,
    )

## RangeSensorCreateLidar

Commands class to create a lidar sensor.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "RangeSensorCreateLidar",
        path="/Lidar",
        parent=None,
        min_range=0.4,
        max_range=100.0,
        draw_points=False,
        draw_lines=False,
        horizontal_fov=360.0,
        vertical_fov=30.0,
        horizontal_resolution=0.4,
        vertical_resolution=4.0,
        rotation_rate=20.0,
        high_lod=False,
        yaw_offset=0.0,
        enable_semantics=False,
    )

## RangeSensorCreatePrim

Base class for all **Commands**.

## RangeSensorCreateUltrasonicArray

Commands class to create an ultrasonic array.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "RangeSensorCreateUltrasonicArray",
        path="/UltrasonicArray",
        parent=None,
        min_range=0.4,
        max_range=3.0,
        draw_points=False,
        draw_lines=False,
        horizontal_fov=15.0,
        vertical_fov=10.0,
        horizontal_resolution=0.5,
        vertical_resolution=0.5,
        num_bins=224,
        emitter_prims=[],
        firing_group_prims=[],
    )

## RangeSensorCreateUltrasonicEmitter

Commands class to create an ultrasonic emitter.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "RangeSensorCreateUltrasonicEmitter",
        path="/UltrasonicEmitter",
        parent=None,
        per_ray_intensity=1.0,
        yaw_offset=0.0,
        adjacency_list=[],
    )

## RangeSensorCreateUltrasonicFiringGroup

Commands class to create an ultrasonic firing group.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "RangeSensorCreateUltrasonicFiringGroup",
        path="/UltrasonicFiringGroup",
        parent=None,
        emitter_modes=[],
        receiver_modes=[],
    )

## URDFCreateImportConfig

Returns an ImportConfig object that can be used while parsing and importing.
Should be used with `URDFParseFile` and `URDFParseAndImportFile` commands

Returns:
    :obj:`omni.isaac.urdf._urdf.ImportConfig`: Parsed URDF stored in an internal structure.

## URDFParseAndImportFile

This command parses and imports a given urdf and returns a UrdfRobot object

Args: 
- arg0 (:obj:`str`): The absolute path to where the urdf file is

- arg1 (:obj:`omni.isaac.urdf._urdf.ImportConfig`): Import Configuration

Returns:
- :obj:`str`: Path to the robot on the USD stage. 

## URDFParseFile

This command parses a given urdf and returns a UrdfRobot object

Args:
- arg0 (:obj:`str`): The absolute path to where the urdf file is

- arg1 (:obj:`omni.isaac.urdf._urdf.ImportConfig`): Import Configuration

Returns:
- :obj:`omni.isaac.urdf._urdf.UrdfRobot`: Parsed URDF stored in an internal structure.

## RobotEngineBridgeCreateApplication

Base class for all **Commands**.

## RobotEngineBridgeDestroyApplication

Base class for all **Commands**.

## RobotEngineBridgeInitStageLoader

Base class for all **Commands**.

## RobotEngineBridgeTickComponent

Base class for all **Commands**.

## RestoreDefaultRenderSettingCommand

Restore default setting for Renderer **Command**.

Args:
- path: Path to the setting to be reset.

## RestoreDefaultRenderSetting

Restore default setting for Renderer **Command**.

Args:
- path: Path to the setting to be reset.

## RestoreDefaultRenderSettingSectionCommand

Restore default settings for the whole section **Command**.

Args:
- path: Path to the settings section to be reset.

## RestoreDefaultRenderSettingSection

Restore default settings for the whole section **Command**.

Args:
- path: Path to the settings section to be reset.

## SetCurrentRenderer

Sets the current renderer
Args:
- renderer_name: name of the renderer

## SetCurrentStack

Sets the current stack (needs to be one which is valid for the current renderer) 
Args:
- stack_name: name of the stack

## CreateMeshPrimCommand

Base class for all **Commands**.

## CreateMeshPrim

Base class for all **Commands**.

## CreateMeshPrimWithDefaultXformCommand

Base class for all **Commands**.

## CreateMeshPrimWithDefaultXform

Base class for all **Commands**.

## CreateAttributeComponentCommand

Commands class to create a attribute randomization component.

Typical usage example:

.. code-block:: python

    attribute_dict = {
        "attribute_3": {
            "name": "xformOp:rotateXYZ",
            "min": "0.0",
            "max": "360.0",
            "distribution": "uniform"
        },
        "attribute_1": {
            "name": "xformOp:translate",
            "min": "1.0",
            "max": "50.0",
            "distribution": "uniform"
        }
    }
    result, prim = omni.kit.commands.execute(
        "CreateAttributeComponentCommand",
        prim_paths=["/World/Cube"],
        custom_data = attribute_dict,
        duration=1.0,
    )

## CreateAttributeComponent

Commands class to create a attribute randomization component.

Typical usage example:

.. code-block:: python

    attribute_dict = {
        "attribute_3": {
            "name": "xformOp:rotateXYZ",
            "min": "0.0",
            "max": "360.0",
            "distribution": "uniform"
        },
        "attribute_1": {
            "name": "xformOp:translate",
            "min": "1.0",
            "max": "50.0",
            "distribution": "uniform"
        }
    }
    result, prim = omni.kit.commands.execute(
        "CreateAttributeComponentCommand",
        prim_paths=["/World/Cube"],
        custom_data = attribute_dict,
        duration=1.0,
    )

## CreateColorComponentCommand

Commands class to create a color randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateColorComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        first_color_range=(0.0, 0.0, 0.0),
        second_color_range=(1.0, 1.0, 1.0),
        roughness_range=(0.0, 1.0),
        metallic_range=(0.0, 1.0),
        duration=1.0,
        include_children=False,
    )

## CreateColorComponent

Commands class to create a color randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateColorComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        first_color_range=(0.0, 0.0, 0.0),
        second_color_range=(1.0, 1.0, 1.0),
        roughness_range=(0.0, 1.0),
        metallic_range=(0.0, 1.0),
        duration=1.0,
        include_children=False,
    )

## CreateLightComponentCommand

Commands class to create a light randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateLightComponentCommand",
        light_paths=["/World/RectLight"],
        first_color_range=(0.9, 0.9, 0.9),
        second_color_range=(1.0, 1.0, 1.0),
        intensity_range=(40000.0, 70000.0),
        temperature_range=(1500.0, 6500.0),
        enable_temperature=True,
        duration=1.0,
        include_children=False,
    )

## CreateLightComponent

Commands class to create a light randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateLightComponentCommand",
        light_paths=["/World/RectLight"],
        first_color_range=(0.9, 0.9, 0.9),
        second_color_range=(1.0, 1.0, 1.0),
        intensity_range=(40000.0, 70000.0),
        temperature_range=(1500.0, 6500.0),
        enable_temperature=True,
        duration=1.0,
        include_children=False,
    )

## CreateMaterialComponentCommand

Commands class to create a material randomization component.

Typical usage example:

.. code-block:: python

    material_list = [
        <server_path> + "/material1.mdl",
        <server_path> + "/material2.mdl",
    ]
    result, prim = omni.kit.commands.execute(
        "CreateMaterialComponentCommand",
        prim_paths=["/World/Room"],
        material_list=material_list,
        duration=1.0,
        include_children=True,
    )

## CreateMaterialComponent

Commands class to create a material randomization component.

Typical usage example:

.. code-block:: python

    material_list = [
        <server_path> + "/material1.mdl",
        <server_path> + "/material2.mdl",
    ]
    result, prim = omni.kit.commands.execute(
        "CreateMaterialComponentCommand",
        prim_paths=["/World/Room"],
        material_list=material_list,
        duration=1.0,
        include_children=True,
    )

## CreateMeshComponentCommand

Commands class to create a mesh randomization component.

Typical usage example:

.. code-block:: python

    mesh_list = [
        <server_path> + "/mesh1.mdl",
        <server_path> + "/mesh2.mdl",
    ]
    result, prim = omni.kit.commands.execute(
        "CreateMeshComponentCommand",
        mesh_list=mesh_list,
        mesh_range=[3, 5],
    )

## CreateMeshComponent

Commands class to create a mesh randomization component.

Typical usage example:

.. code-block:: python

    mesh_list = [
        <server_path> + "/mesh1.mdl",
        <server_path> + "/mesh2.mdl",
    ]
    result, prim = omni.kit.commands.execute(
        "CreateMeshComponentCommand",
        mesh_list=mesh_list,
        mesh_range=[3, 5],
    )

## CreateMovementComponentCommand

Commands class to create a movement randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateMovementComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        min_range=(0.0, 0.0, 0.0),
        max_range=(100.0, 100.0, 100.0),
        duration=1.0,
        include_children=False,
    )

## CreateMovementComponent

Commands class to create a movement randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateMovementComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        min_range=(0.0, 0.0, 0.0),
        max_range=(100.0, 100.0, 100.0),
        duration=1.0,
        include_children=False,
    )

## CreateRotationComponentCommand

Commands class to create a rotation randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateRotationComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        min_range=(0.0, 0.0, 0.0),
        max_range=(360.0, 360.0, 360.0),
        duration=1.0,
        include_children=False,
    )

## CreateRotationComponent

Commands class to create a rotation randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateRotationComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        min_range=(0.0, 0.0, 0.0),
        max_range=(360.0, 360.0, 360.0),
        duration=1.0,
        include_children=False,
    )

## CreateScaleComponentCommand

Commands class to create a scale randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateScaleComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        min_range=(1.0, 1.0, 1.0),
        max_range=(5.0, 5.0, 5.0),
        duration=1.0,
        include_children=False,
    )

## CreateScaleComponent

Commands class to create a scale randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateScaleComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        min_range=(1.0, 1.0, 1.0),
        max_range=(5.0, 5.0, 5.0),
        duration=1.0,
        include_children=False,
    )

## CreateTextureComponentCommand

Commands class to create a texture randomization component.

Typical usage example:

.. code-block:: python

    texture_list = [
        <server_path> + "/texture1.png",
        <server_path> + "/texture2.png",
    ]
    result, prim = omni.kit.commands.execute(
        "CreateTextureComponentCommand",
        prim_paths=["/World/Room"],
        enable_project_uvw=False,
        texture_list=texture_list,
        duration=1.0,
        include_children=True,
    )

## CreateTextureComponent

Commands class to create a texture randomization component.

Typical usage example:

.. code-block:: python

    texture_list = [
        <server_path> + "/texture1.png",
        <server_path> + "/texture2.png",
    ]
    result, prim = omni.kit.commands.execute(
        "CreateTextureComponentCommand",
        prim_paths=["/World/Room"],
        enable_project_uvw=False,
        texture_list=texture_list,
        duration=1.0,
        include_children=True,
    )

## CreateTransformComponentCommand

Commands class to create a transform randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateTransformComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        translate_min_range=(0.0, 0.0, 0.0),
        translate_max_range=(100.0, 100.0, 100.0),
        duration=1.0,
        include_children=False,
    )

## CreateTransformComponent

Commands class to create a transform randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateTransformComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1"],
        translate_min_range=(0.0, 0.0, 0.0),
        translate_max_range=(100.0, 100.0, 100.0),
        duration=1.0,
        include_children=False,
    )

## CreateVisibilityComponentCommand

Commands class to create a visibility randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateVisibilityComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1", "/World/Cube2", "/World/Cube3", "/World/Cube4"],
        num_visible_range=[1, 3],
        duration=1.0,
    )

## CreateVisibilityComponent

Commands class to create a visibility randomization component.

Typical usage example:

.. code-block:: python

    result, prim = omni.kit.commands.execute(
        "CreateVisibilityComponentCommand",
        prim_paths=["/World/Cube", "/World/Cube1", "/World/Cube2", "/World/Cube3", "/World/Cube4"],
        num_visible_range=[1, 3],
        duration=1.0,
    )

## ToggleExtension

Toggle extension **Command**.  Enables/disables an extension.

Args:
- ext_id(str): Extension id.
- enable(bool): Enable or disable.

## ChangeSettingCommand

Change setting **Command**.

Args:
- path: Path to the setting to change.
- value: New value to change to.
- prev: Previous value to for undo operation. If `None` current value would be saved as previous.

## ChangeSetting

Change setting **Command**.

Args:
- path: Path to the setting to change.
- value: New value to change to.
- prev: Previous value to for undo operation. If `None` current value would be saved as previous.

## CreateAndBindMdlMaterialFromLibrary

Base class for all **Commands**.

## CreateAndBindPreviewSurfaceFromLibrary

Base class for all **Commands**.

## CreateAndBindPreviewSurfaceTextureFromLibrary

Base class for all **Commands**.

