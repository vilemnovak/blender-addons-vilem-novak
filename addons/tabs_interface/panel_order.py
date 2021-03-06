categories = [
    # mix of editors, mainly 3d:
    'Tools',
    'Create',
    'Options',
    'Shading',
    'Relations',
    'Animation',
    'Physics',

    # cycles nodes:
    'Input',
    'Output',
    'Shader',
    'Color',
    'Pattern',
    'Textures',
    'Texture',
    'Color',
    'Vector',
    'Matte',
    'Distort',
    'Converter',
    'Script',
    'Group',
    'Layout',

    # grease p.
    'Grease Pencil',

]

spaces ={'PROPERTIES': {'WINDOW': [
    'BONE_PT_context_bone',
    'BONE_PT_curved',
    'BONE_PT_custom_props',
    'BONE_PT_deform',
    'BONE_PT_display',
    'BONE_PT_inverse_kinematics',
    'BONE_PT_relations',
    'BONE_PT_transform',
    'CYCLES_CAMERA_PT_dof',
    'CYCLES_CAMERA_PT_dof_aperture',
    'CYCLES_CAMERA_PT_dof_viewport',
    'CYCLES_LIGHT_PT_light',
    'CYCLES_LIGHT_PT_nodes',
    'CYCLES_LIGHT_PT_preview',
    'CYCLES_LIGHT_PT_spot',
    'CYCLES_MATERIAL_PT_displacement',
    'CYCLES_MATERIAL_PT_preview',
    'CYCLES_MATERIAL_PT_settings',
    'CYCLES_MATERIAL_PT_settings_surface',
    'CYCLES_MATERIAL_PT_settings_volume',
    'CYCLES_MATERIAL_PT_surface',
    'CYCLES_MATERIAL_PT_volume',
    'CYCLES_OBJECT_PT_cycles_settings',
    'CYCLES_OBJECT_PT_cycles_settings_performance',
    'CYCLES_OBJECT_PT_cycles_settings_ray_visibility',
    'CYCLES_OBJECT_PT_motion_blur',
    'CYCLES_PT_context_material',
    'CYCLES_PT_post_processing',
    'CYCLES_RENDER_PT_bake',
    'CYCLES_RENDER_PT_bake_influence',
    'CYCLES_RENDER_PT_bake_output',
    'CYCLES_RENDER_PT_bake_selected_to_active',
    'CYCLES_RENDER_PT_debug',
    'CYCLES_RENDER_PT_denoising',
    'CYCLES_RENDER_PT_film',
    'CYCLES_RENDER_PT_film_pixel_filter',
    'CYCLES_RENDER_PT_film_transparency',
    'CYCLES_RENDER_PT_filter',
    'CYCLES_RENDER_PT_hair',
    'CYCLES_RENDER_PT_light_paths',
    'CYCLES_RENDER_PT_light_paths_caustics',
    'CYCLES_RENDER_PT_light_paths_clamping',
    'CYCLES_RENDER_PT_light_paths_max_bounces',
    'CYCLES_RENDER_PT_motion_blur',
    'CYCLES_RENDER_PT_motion_blur_curve',
    'CYCLES_RENDER_PT_override',
    'CYCLES_RENDER_PT_passes',
    'CYCLES_RENDER_PT_passes_crypto',
    'CYCLES_RENDER_PT_passes_data',
    'CYCLES_RENDER_PT_passes_debug',
    'CYCLES_RENDER_PT_passes_light',
    'CYCLES_RENDER_PT_performance',
    'CYCLES_RENDER_PT_performance_acceleration_structure',
    'CYCLES_RENDER_PT_performance_final_render',
    'CYCLES_RENDER_PT_performance_threads',
    'CYCLES_RENDER_PT_performance_tiles',
    'CYCLES_RENDER_PT_performance_viewport',
    'CYCLES_RENDER_PT_sampling',
    'CYCLES_RENDER_PT_sampling_advanced',
    'CYCLES_RENDER_PT_sampling_sub_samples',
    'CYCLES_RENDER_PT_simplify',
    'CYCLES_RENDER_PT_simplify_culling',
    'CYCLES_RENDER_PT_simplify_render',
    'CYCLES_RENDER_PT_simplify_viewport',
    'CYCLES_RENDER_PT_subdivision',
    'CYCLES_RENDER_PT_volumes',
    'CYCLES_WORLD_PT_ambient_occlusion',
    'CYCLES_WORLD_PT_mist',
    'CYCLES_WORLD_PT_preview',
    'CYCLES_WORLD_PT_ray_visibility',
    'CYCLES_WORLD_PT_settings',
    'CYCLES_WORLD_PT_settings_surface',
    'CYCLES_WORLD_PT_settings_volume',
    'CYCLES_WORLD_PT_surface',
    'CYCLES_WORLD_PT_volume',
    'DATA_PT_EEVEE_light',
    'DATA_PT_EEVEE_light_distance',
    'DATA_PT_EEVEE_shadow',
    'DATA_PT_EEVEE_shadow_cascaded_shadow_map',
    'DATA_PT_EEVEE_shadow_contact',
    'DATA_PT_active_spline',
    'DATA_PT_area',
    'DATA_PT_bone_groups',
    'DATA_PT_camera',
    'DATA_PT_camera_background_image',
    'DATA_PT_camera_display',
    'DATA_PT_camera_display_composition_guides',
    'DATA_PT_camera_display_passepartout',
    'DATA_PT_camera_dof',
    'DATA_PT_camera_dof_aperture',
    'DATA_PT_camera_safe_areas',
    'DATA_PT_camera_safe_areas_center_cut',
    'DATA_PT_camera_stereoscopy',
    'DATA_PT_cone',
    'DATA_PT_context_arm',
    'DATA_PT_context_camera',
    'DATA_PT_context_curve',
    'DATA_PT_context_gpencil',
    'DATA_PT_context_lattice',
    'DATA_PT_context_light',
    'DATA_PT_context_lightprobe',
    'DATA_PT_context_mesh',
    'DATA_PT_context_metaball',
    'DATA_PT_context_speaker',
    'DATA_PT_curve_texture_space',
    'DATA_PT_custom_props_arm',
    'DATA_PT_custom_props_camera',
    'DATA_PT_custom_props_curve',
    'DATA_PT_custom_props_gpencil',
    'DATA_PT_custom_props_lattice',
    'DATA_PT_custom_props_light',
    'DATA_PT_vertex_groups',
    'DATA_PT_shape_keys',
    'DATA_PT_uv_texture',
    'DATA_PT_vertex_colors',
    'DATA_PT_face_maps',
    'DATA_PT_normals',
    'DATA_PT_texture_space',
    'DATA_PT_custom_props_metaball',
    'DATA_PT_custom_props_speaker',
    'DATA_PT_customdata',
    'DATA_PT_display',
    'DATA_PT_distance',
    'DATA_PT_empty',
    'DATA_PT_falloff_curve',
    'DATA_PT_font',
    'DATA_PT_font_transform',
    'DATA_PT_geometry_curve',
    'DATA_PT_geometry_curve_bevel',
    'DATA_PT_gpencil_canvas',
    'DATA_PT_gpencil_display',
    'DATA_PT_gpencil_layer_adjustments',
    'DATA_PT_gpencil_layer_display',
    'DATA_PT_gpencil_layer_relations',
    'DATA_PT_gpencil_layers',
    'DATA_PT_gpencil_modifiers',
    'DATA_PT_gpencil_onion_skinning',
    'DATA_PT_gpencil_onion_skinning_custom_colors',
    'DATA_PT_gpencil_onion_skinning_display',
    'DATA_PT_gpencil_strokes',
    'DATA_PT_gpencil_vertex_groups',
    'DATA_PT_iksolver_itasc',
    'DATA_PT_lattice',
    'DATA_PT_lens',
    'DATA_PT_light',
    'DATA_PT_lightprobe',
    'DATA_PT_lightprobe_display',
    'DATA_PT_lightprobe_parallax',
    'DATA_PT_lightprobe_visibility',
    'DATA_PT_mball_texture_space',
    'DATA_PT_metaball',
    'DATA_PT_metaball_element',
    'DATA_PT_motion_paths',
    'DATA_PT_motion_paths_display',
    'DATA_PT_normals_auto_smooth',
    'DATA_PT_paragraph',
    'DATA_PT_paragraph_alignment',
    'DATA_PT_paragraph_spacing',
    'DATA_PT_pathanim',
    'DATA_PT_pose_library',
    'DATA_PT_preview',
    'DATA_PT_shader_fx',
    'DATA_PT_shape_curve',
    'DATA_PT_skeleton',
    'DATA_PT_speaker',
    'DATA_PT_spot',
    'DATA_PT_text_boxes',
    'EEVEE_MATERIAL_PT_context_material',
    'EEVEE_MATERIAL_PT_surface',
    'EEVEE_MATERIAL_PT_volume',
    'EEVEE_MATERIAL_PT_settings',
    'EEVEE_WORLD_PT_mist',
    'EEVEE_WORLD_PT_surface',
    'IMAGE_PT_paint',
    'IMAGE_PT_paint_clone',
    'IMAGE_PT_paint_color',
    'IMAGE_PT_paint_curve',
    'IMAGE_PT_paint_gradient',
    'IMAGE_PT_paint_options',
    'IMAGE_PT_paint_stroke',
    'IMAGE_PT_paint_stroke_smooth_stroke',
    'IMAGE_PT_paint_swatches',
    'IMAGE_PT_tools_brush_display_custom_icon',
    'IMAGE_PT_tools_brush_display',
    'IMAGE_PT_tools_brush_display_show_brush',
    'IMAGE_PT_tools_brush_texture',
    'IMAGE_PT_tools_imagepaint_symmetry',
    'IMAGE_PT_tools_mask_texture',
    'MATERIAL_PT_viewport',
    'IMAGE_PT_uv_sculpt',
    'IMAGE_PT_uv_sculpt_curve',
    'MATERIAL_PT_custom_props',
    'MATERIAL_PT_freestyle_line',
    'MATERIAL_PT_gpencil_custom_props',
    'MATERIAL_PT_gpencil_fillcolor',
    'MATERIAL_PT_gpencil_options',
    'MATERIAL_PT_gpencil_preview',
    'MATERIAL_PT_gpencil_slots',
    'MATERIAL_PT_gpencil_strokecolor',
    'MATERIAL_PT_gpencil_surface',
    'MATERIAL_PT_preview',
    'OBJECT_PT_transform',
    'OBJECT_PT_relations',
    'OBJECT_PT_collections',
    'OBJECT_PT_context_object',
    'OBJECT_PT_instancing',
    'OBJECT_PT_motion_paths',
    'OBJECT_PT_display',
    'OBJECT_PT_custom_props',
    'OBJECT_PT_delta_transform',
    'OBJECT_PT_display_bounds',
    'OBJECT_PT_instancing_size',
    'OBJECT_PT_motion_paths_display',
    'PARTICLE_PT_boidbrain',
    'PARTICLE_PT_emission',
    'PARTICLE_PT_cache',
    'PARTICLE_PT_velocity',
    'PARTICLE_PT_rotation',
    'PARTICLE_PT_physics',
    'PARTICLE_PT_render',
    'PARTICLE_PT_draw',
    'PARTICLE_PT_children',
    'PARTICLE_PT_children_clumping',
    'PARTICLE_PT_children_clumping_noise',
    'PARTICLE_PT_children_kink',
    'PARTICLE_PT_children_parting',
    'PARTICLE_PT_children_roughness',
    'PARTICLE_PT_context_particles',
    'PARTICLE_PT_hair_shape',
    'PARTICLE_PT_field_weights',
    'PARTICLE_PT_force_fields',
    'PARTICLE_PT_vertexgroups',
    'PARTICLE_PT_textures',
    'PARTICLE_PT_custom_props',
    'PARTICLE_PT_emission_source',
    'PARTICLE_PT_force_fields_type1',
    'PARTICLE_PT_force_fields_type1_falloff',
    'PARTICLE_PT_force_fields_type2',
    'PARTICLE_PT_force_fields_type2_falloff',
    'PARTICLE_PT_hair_dynamics',
    'PARTICLE_PT_hair_dynamics_structure',
    'PARTICLE_PT_hair_dynamics_volume',
    'PARTICLE_PT_physics_boids_battle',
    'PARTICLE_PT_physics_boids_misc',
    'PARTICLE_PT_physics_boids_movement',
    'PARTICLE_PT_physics_deflection',
    'PARTICLE_PT_physics_fluid_advanced',
    'PARTICLE_PT_physics_fluid_interaction',
    'PARTICLE_PT_physics_fluid_springs',
    'PARTICLE_PT_physics_fluid_springs_advanced',
    'PARTICLE_PT_physics_fluid_springs_viscoelastic',
    'PARTICLE_PT_physics_forces',
    'PARTICLE_PT_physics_integration',
    'PARTICLE_PT_physics_relations',
    'PARTICLE_PT_render_collection',
    'PARTICLE_PT_render_collection_use_count',
    'PARTICLE_PT_render_extra',
    'PARTICLE_PT_render_line',
    'PARTICLE_PT_render_object',
    'PARTICLE_PT_render_path',
    'PARTICLE_PT_render_path_timing',
    'PARTICLE_PT_render_trails',
    'PARTICLE_PT_rotation_angular_velocity',
    'PHYSICS_PT_add',
    'PHYSICS_PT_cloth',
    'PHYSICS_PT_cloth_cache',
    'PHYSICS_PT_cloth_collision',
    'PHYSICS_PT_cloth_damping',
    'PHYSICS_PT_cloth_field_weights',
    'PHYSICS_PT_cloth_object_collision',
    'PHYSICS_PT_cloth_physical_properties',
    'PHYSICS_PT_cloth_property_weights',
    'PHYSICS_PT_cloth_self_collision',
    'PHYSICS_PT_cloth_shape',
    'PHYSICS_PT_cloth_stiffness',
    'PHYSICS_PT_collision',
    'PHYSICS_PT_collision_particle',
    'PHYSICS_PT_collision_softbody',
    'PHYSICS_PT_domain_bake',
    'PHYSICS_PT_domain_boundary',
    'PHYSICS_PT_domain_gravity',
    'PHYSICS_PT_domain_particles',
    'PHYSICS_PT_domain_viscosity',
    'PHYSICS_PT_dp_advanced_canvas',
    'PHYSICS_PT_dp_advanced_canvas_paint_dissolve',
    'PHYSICS_PT_dp_advanced_canvas_paint_dry',
    'PHYSICS_PT_dp_brush_source',
    'PHYSICS_PT_dp_brush_source_color_ramp',
    'PHYSICS_PT_dp_brush_velocity',
    'PHYSICS_PT_dp_brush_velocity_color_ramp',
    'PHYSICS_PT_dp_brush_velocity_smudge',
    'PHYSICS_PT_dp_brush_wave',
    'PHYSICS_PT_dp_cache',
    'PHYSICS_PT_dp_canvas_initial_color',
    'PHYSICS_PT_dp_canvas_output',
    'PHYSICS_PT_dp_canvas_output_bake',
    'PHYSICS_PT_dp_canvas_output_paintmaps',
    'PHYSICS_PT_dp_canvas_output_wetmaps',
    'PHYSICS_PT_dp_effects',
    'PHYSICS_PT_dp_effects_drip',
    'PHYSICS_PT_dp_effects_drip_weights',
    'PHYSICS_PT_dp_effects_shrink',
    'PHYSICS_PT_dp_effects_spread',
    'PHYSICS_PT_dynamic_paint',
    'PHYSICS_PT_dynamic_paint_settings',
    'PHYSICS_PT_field',
    'PHYSICS_PT_field_falloff',
    'PHYSICS_PT_field_falloff_angular',
    'PHYSICS_PT_field_falloff_radial',
    'PHYSICS_PT_field_settings',
    'PHYSICS_PT_field_settings_kink',
    'PHYSICS_PT_field_settings_texture_select',
    'PHYSICS_PT_fluid',
    'PHYSICS_PT_fluid_flow',
    'PHYSICS_PT_fluid_particle_cache',
    'PHYSICS_PT_fluid_settings',
    'PHYSICS_PT_rigid_body',
    'PHYSICS_PT_rigid_body_collisions',
    'PHYSICS_PT_rigid_body_collisions_collections',
    'PHYSICS_PT_rigid_body_collisions_sensitivity',
    'PHYSICS_PT_rigid_body_collisions_surface',
    'PHYSICS_PT_rigid_body_constraint',
    'PHYSICS_PT_rigid_body_constraint_limits',
    'PHYSICS_PT_rigid_body_constraint_limits_angular',
    'PHYSICS_PT_rigid_body_constraint_limits_linear',
    'PHYSICS_PT_rigid_body_constraint_motor',
    'PHYSICS_PT_rigid_body_constraint_motor_angular',
    'PHYSICS_PT_rigid_body_constraint_motor_linear',
    'PHYSICS_PT_rigid_body_constraint_objects',
    'PHYSICS_PT_rigid_body_constraint_override_iterations',
    'PHYSICS_PT_rigid_body_constraint_settings',
    'PHYSICS_PT_rigid_body_constraint_springs',
    'PHYSICS_PT_rigid_body_constraint_springs_angular',
    'PHYSICS_PT_rigid_body_constraint_springs_linear',
    'PHYSICS_PT_rigid_body_dynamics',
    'PHYSICS_PT_rigid_body_dynamics_deactivation',
    'PHYSICS_PT_rigid_body_settings',
    'PHYSICS_PT_smoke',
    'PHYSICS_PT_smoke_adaptive_domain',
    'PHYSICS_PT_smoke_behavior',
    'PHYSICS_PT_smoke_behavior_dissolve',
    'PHYSICS_PT_smoke_cache',
    'PHYSICS_PT_smoke_collections',
    'PHYSICS_PT_smoke_field_weights',
    'PHYSICS_PT_smoke_fire',
    'PHYSICS_PT_smoke_flow_texture',
    'PHYSICS_PT_smoke_highres',
    'PHYSICS_PT_smoke_settings',
    'PHYSICS_PT_smoke_settings_initial_velocity',
    'PHYSICS_PT_smoke_settings_particle_size',
    'PHYSICS_PT_smoke_viewport_display',
    'PHYSICS_PT_smoke_viewport_display_color',
    'PHYSICS_PT_smoke_viewport_display_debug',
    'PHYSICS_PT_softbody',
    'PHYSICS_PT_softbody_cache',
    'PHYSICS_PT_softbody_collision',
    'PHYSICS_PT_softbody_edge',
    'PHYSICS_PT_softbody_edge_aerodynamics',
    'PHYSICS_PT_softbody_edge_stiffness',
    'PHYSICS_PT_softbody_field_weights',
    'PHYSICS_PT_softbody_goal',
    'PHYSICS_PT_softbody_goal_settings',
    'PHYSICS_PT_softbody_goal_strengths',
    'PHYSICS_PT_softbody_object',
    'PHYSICS_PT_softbody_simulation',
    'PHYSICS_PT_softbody_solver',
    'PHYSICS_PT_softbody_solver_diagnostics',
    'PHYSICS_PT_softbody_solver_helpers',
    'RENDER_PT_eevee_sampling',
    'RENDER_PT_eevee_ambient_occlusion',
    'RENDER_PT_eevee_bloom',
    'RENDER_PT_color_management_curves',
    'RENDER_PT_context',
    'RENDER_PT_dimensions',
    'RENDER_PT_eevee_depth_of_field',
    'RENDER_PT_eevee_subsurface_scattering',
    'RENDER_PT_eevee_screen_space_reflections',
    'RENDER_PT_eevee_motion_blur',
    'RENDER_PT_eevee_volumetric',
    'RENDER_PT_eevee_hair',
    'RENDER_PT_eevee_shadows',
    'RENDER_PT_eevee_indirect_lighting',
    'RENDER_PT_eevee_film',
    'RENDER_PT_color_management',
    'RENDER_PT_eevee_film_overscan',
    'RENDER_PT_eevee_indirect_lighting_display',
    'RENDER_PT_eevee_volumetric_lighting',
    'RENDER_PT_eevee_volumetric_shadows',
    'RENDER_PT_encoding',
    'RENDER_PT_encoding_audio',
    'RENDER_PT_encoding_video',
    'RENDER_PT_frame_remapping',
    'RENDER_PT_simplify',
    'RENDER_PT_freestyle',
    'RENDER_PT_opengl_color',
    'RENDER_PT_opengl_film',
    'RENDER_PT_opengl_lighting',
    'RENDER_PT_stereoscopy',
    'RENDER_PT_opengl_options',
    'RENDER_PT_output',
    'RENDER_PT_output_views',
    'RENDER_PT_stamp',
    'RENDER_PT_post_processing',
    'RENDER_PT_simplify_greasepencil',
    'RENDER_PT_simplify_render',
    'RENDER_PT_simplify_viewport',
    'RENDER_PT_stamp_burn',
    'RENDER_PT_stamp_note',
    'SCENE_PT_scene',
    'SCENE_PT_unit',
    'SCENE_PT_physics',
    'SCENE_PT_keying_sets',
    'SCENE_PT_audio',
    'SCENE_PT_rigid_body_world',
    'SCENE_PT_custom_props',
    'SCENE_PT_keyframing_settings',
    'SCENE_PT_keying_set_paths',
    'SCENE_PT_rigid_body_cache',
    'SCENE_PT_rigid_body_field_weights',
    'SCENE_PT_rigid_body_world_settings',
    'TEXTURE_PT_blend',
    'TEXTURE_PT_clouds',
    'TEXTURE_PT_colors',
    'TEXTURE_PT_colors_ramp',
    'TEXTURE_PT_context',
    'TEXTURE_PT_custom_props',
    'TEXTURE_PT_distortednoise',
    'TEXTURE_PT_image',
    'TEXTURE_PT_image_alpha',
    'TEXTURE_PT_image_mapping',
    'TEXTURE_PT_image_mapping_crop',
    'TEXTURE_PT_image_sampling',
    'TEXTURE_PT_image_settings',
    'TEXTURE_PT_influence',
    'TEXTURE_PT_magic',
    'TEXTURE_PT_mapping',
    'TEXTURE_PT_marble',
    'TEXTURE_PT_musgrave',
    'TEXTURE_PT_node',
    'TEXTURE_PT_preview',
    'TEXTURE_PT_stucci',
    'TEXTURE_PT_voronoi',
    'TEXTURE_PT_voronoi_feature_weights',
    'TEXTURE_PT_wood',
    'VIEW3D_PT_sculpt_dyntopo',
    'TOPBAR_PT_active_tool',
    'VIEW3D_PT_sculpt_dyntopo_remesh',
    'VIEW3D_PT_sculpt_options',
    'VIEW3D_PT_sculpt_options_gravity',
    'VIEW3D_PT_sculpt_options_unified',
    'VIEW3D_PT_sculpt_symmetry',
    'VIEW3D_PT_slots_projectpaint',
    'VIEW3D_PT_stencil_projectpaint',
    'VIEW3D_PT_tools_brush',
    'VIEW3D_PT_tools_armatureedit_options',
    'VIEW3D_PT_tools_brush_clone',
    'VIEW3D_PT_tools_brush_color',
    'VIEW3D_PT_tools_brush_display',
    'VIEW3D_PT_tools_brush_display_custom_icon',
    'VIEW3D_PT_tools_brush_display_show_brush',
    'VIEW3D_PT_tools_brush_falloff',
    'VIEW3D_PT_tools_brush_falloff_frontface',
    'VIEW3D_PT_tools_brush_falloff_normal',
    'VIEW3D_PT_tools_brush_gradient',
    'VIEW3D_PT_tools_brush_options',
    'VIEW3D_PT_tools_brush_stroke',
    'VIEW3D_PT_tools_brush_stroke_smooth_stroke',
    'VIEW3D_PT_tools_brush_swatches',
    'VIEW3D_PT_tools_brush_texture',
    'VIEW3D_PT_tools_grease_pencil_brush',
    'VIEW3D_PT_tools_curveedit_options_stroke',
    'VIEW3D_PT_tools_grease_pencil_brush_option',
    'VIEW3D_PT_tools_grease_pencil_brush_random',
    'VIEW3D_PT_tools_grease_pencil_brush_settings',
    'VIEW3D_PT_tools_grease_pencil_brush_stabilizer',
    'VIEW3D_PT_tools_grease_pencil_brushcurves',
    'VIEW3D_PT_tools_grease_pencil_brushcurves_jitter',
    'VIEW3D_PT_tools_grease_pencil_brushcurves_sensitivity',
    'VIEW3D_PT_tools_grease_pencil_brushcurves_strength',
    'VIEW3D_PT_tools_grease_pencil_paint_appearance',
    'VIEW3D_PT_tools_grease_pencil_sculpt',
    'VIEW3D_PT_tools_grease_pencil_sculpt_appearance',
    'VIEW3D_PT_tools_grease_pencil_sculpt_options',
    'VIEW3D_PT_tools_grease_pencil_weight_appearance',
    'VIEW3D_PT_tools_grease_pencil_weight_paint',
    'VIEW3D_PT_tools_imagepaint_options',
    'VIEW3D_PT_tools_imagepaint_options_cavity',
    'VIEW3D_PT_tools_imagepaint_options_external',
    'VIEW3D_PT_tools_imagepaint_options_unified',
    'VIEW3D_PT_tools_imagepaint_symmetry',
    'VIEW3D_PT_tools_mask_texture',
    'VIEW3D_PT_tools_particlemode',
    'VIEW3D_PT_tools_meshedit_normal',
    'VIEW3D_PT_tools_meshedit_options',
    'VIEW3D_PT_tools_particlemode_options',
    'VIEW3D_PT_tools_particlemode_options_display',
    'VIEW3D_PT_tools_particlemode_options_shapecut',
    'VIEW3D_PT_tools_vertexpaint_options',
    'VIEW3D_PT_tools_posemode_options',
    'VIEW3D_PT_tools_vertexpaint_symmetry',
    'VIEW3D_PT_tools_weightpaint_options',
    'VIEW3D_PT_tools_weightpaint_options_unified',
    'VIEW3D_PT_tools_weightpaint_symmetry',
    'VIEWLAYER_PT_layer',
    'VIEWLAYER_PT_eevee_layer_passes',
    'VIEWLAYER_PT_freestyle',
    'VIEWLAYER_PT_freestyle_lineset',
    'VIEWLAYER_PT_freestyle_linestyle',
    'WORKSPACE_PT_addons',
    'WORKSPACE_PT_custom_props',
    'WORKSPACE_PT_main',
    'WORLD_PT_context_world',
    'WORLD_PT_viewport_display',
    'WORLD_PT_custom_props',
    'DATA_PT_custom_props_mesh']},

     'CLIP_EDITOR': {'UI': [
    'CLIP_PT_active_mask_point',
    'CLIP_PT_active_mask_spline',
    'CLIP_PT_footage',
    'CLIP_PT_grease_pencil',
    'CLIP_PT_marker',
    'CLIP_PT_mask',
    'CLIP_PT_mask_layers',
    'CLIP_PT_objects',
    'CLIP_PT_plane_track',
    'CLIP_PT_proxy',
    'CLIP_PT_stabilization',
    'CLIP_PT_track',
    'CLIP_PT_track_settings',
    'CLIP_PT_track_settings_extras',
    'CLIP_PT_tracking_camera',
    'CLIP_PT_tracking_lens']},

     'FILE_BROWSER': {},
     'IMAGE_EDITOR': {'UI': [
    'IMAGE_PT_active_mask_point',
    'IMAGE_PT_active_mask_spline',
    'IMAGE_PT_grease_pencil',
    'IMAGE_PT_image_properties',
    'IMAGE_PT_mask',
    'IMAGE_PT_mask_display',
    'IMAGE_PT_mask_layers',
    'IMAGE_PT_render_slots',
    'IMAGE_PT_sample_line',
    'IMAGE_PT_scope_sample',
    'IMAGE_PT_uv_cursor',
    'IMAGE_PT_view_histogram',
    'IMAGE_PT_view_vectorscope',
    'IMAGE_PT_view_waveform']},

     'NODE_EDITOR': {'UI': [
    'NODE_CYCLES_LIGHT_PT_light',
    'NODE_CYCLES_LIGHT_PT_spot',
    'NODE_CYCLES_MATERIAL_PT_settings',
    'NODE_CYCLES_MATERIAL_PT_settings_surface',
    'NODE_CYCLES_MATERIAL_PT_settings_volume',
    'NODE_CYCLES_WORLD_PT_ray_visibility',
    'NODE_CYCLES_WORLD_PT_settings',
    'NODE_CYCLES_WORLD_PT_settings_surface',
    'NODE_CYCLES_WORLD_PT_settings_volume',
    'NODE_DATA_PT_EEVEE_light',
    'NODE_DATA_PT_light',
    'NODE_EEVEE_MATERIAL_PT_settings',
    'NODE_MATERIAL_PT_viewport',
    'NODE_PT_active_node_color',
    'NODE_PT_active_node_generic',
    'NODE_PT_active_node_properties',
    'NODE_PT_backdrop',
    'NODE_PT_grease_pencil',
    'NODE_PT_grease_pencil_tools',
    'NODE_PT_quality',
    'NODE_PT_texture_mapping',
    'NODE_WORLD_PT_viewport_display']},

     'SEQUENCE_EDITOR': {'UI': [
    'SEQUENCER_PT_annotation_onion',
    'SEQUENCER_PT_custom_props',
    'SEQUENCER_PT_edit',
    'SEQUENCER_PT_effect',
    'SEQUENCER_PT_filter',
    'SEQUENCER_PT_grease_pencil',
    'SEQUENCER_PT_grease_pencil_tools',
    'SEQUENCER_PT_input',
    'SEQUENCER_PT_mask',
    'SEQUENCER_PT_modifiers',
    'SEQUENCER_PT_preview',
    'SEQUENCER_PT_proxy_settings',
    'SEQUENCER_PT_scene',
    'SEQUENCER_PT_sound',
    'SEQUENCER_PT_strip_proxy',
    'SEQUENCER_PT_view',
    'SEQUENCER_PT_view_safe_areas']},

     'TEXT_EDITOR': {'UI': [
    'TEXT_PT_find',
    'TEXT_PT_properties']},

     'VIEW_3D': {'UI': [
    'VIEW3D_PT_annotation_onion',
    'VIEW3D_PT_blenderkit_downloads',
    'VIEW3D_PT_blenderkit_model_properties',
    'VIEW3D_PT_blenderkit_unified',
    'VIEW3D_PT_context_properties',
    'VIEW3D_PT_grease_pencil',
    'VIEW3D_PT_print3d_mesh',
    'VIEW3D_PT_print3d_object',
    'VIEW3D_PT_quad_view',
    'VIEW3D_PT_tools_looptools',
    'VIEW3D_PT_view3d_cursor',
    'VIEW3D_PT_view3d_lock',
    'VIEW3D_PT_view3d_properties',
    'VIEW3D_PT_view3d_stereo']}}