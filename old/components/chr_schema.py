from typing import List
from components.component import Component
from components.tab import Tab
from components.field_group import FieldGroup
from components.field import Field

EXAMPLE_SCHEMA = {
    "name": None,
    "type": "chr",
    "tabs": {
        "name": None,
        "groups": {
            "name": None,
            "fields": {
                "In-File-Name": {
                    "in_game_name": None,
                    "data_type": None,
                    "parent": None,
                    "value": None
                }
            }
        }
    }
}

def process_fields(field_stack, group: FieldGroup):
        while field_stack:
            field_obj = field_stack.pop()
            group.fields[field_obj.in_file_name] = field_obj

'''
TO-DO:
- Assign Correct Data types
- Modularize and refine repetitive function logic
- Testing
'''

class ChrSchema:
    @staticmethod
    def _main_tab() -> Tab:
        main_tab = Tab(name="Main")
        main_properties_group = FieldGroup(name="Main Properties")
        fields: List[Field] = [
            Field(in_file_name="Name", in_game_name="Profile Name", data_type="string"),
            Field(in_file_name="MaxHealth", in_game_name="Health", data_type="integer"), #revise
            Field(in_file_name="MinRespawnDelay", in_game_name="Min Respawn Delay", data_type="float"),
            Field(in_file_name="MaxRespawnDelay", in_game_name="Max Respawn Delay", data_type="float"),
            Field(in_file_name="RespawnAnimationDuration", in_game_name="Respawn Animation Duration", data_type="float"),
            Field(in_file_name="HeadshotOnly", in_game_name="Headshot Only", data_type="boolean"),
            Field(in_file_name="CameraOffset", in_game_name="Camera Height Offset", data_type="vector"),
            Field(in_file_name="HideThirdPersonCamera", in_game_name="Hide Third Person Camera", data_type="boolean"), #revise
            Field(in_file_name="ThirdPersonCamera", in_game_name="Third Person Camera", data_type="boolean"),
            Field(in_file_name="TPSArmLength", in_game_name="TPS Arm Length", data_type="float"), #revise
            Field(in_file_name="TPSOffsetMin", in_game_name="TPS Offset Min", data_type="float"), #revise
            Field(in_file_name="TPSOffsetMax", in_game_name="TPS Offset Max", data_type="float"), #revise
        ]
        fields.reverse()
        for field_obj in fields:
            main_properties_group.fields[field_obj.in_file_name] = field_obj
        main_tab.groups[main_properties_group.name] = main_properties_group
        return main_tab

    @staticmethod
    def _move_tab() -> Tab:
        move_tab = Tab(name="Move")
        movement_properties_group = FieldGroup(name="Movement Properties")
        fields: List[Field] = [
            Field(in_file_name="isFlyer", in_game_name="Flies", data_type="boolean"),
            Field(in_file_name="FlightObeysPitch", in_game_name="Fligh Obeys Pitch", data_type="boolean"),
            Field(in_file_name="FlightVelocityUp", in_game_name="Flight Velocity Up", data_type="float"),
            Field(in_file_name="FlightVelocityDown", in_game_name="FlightVelocityUp", data_type="float"),
            Field(in_file_name="FlightAccelUp", in_game_name="Flight Accel Up", data_type="float"),
            Field(in_file_name="FlightVelocityDown", in_game_name="Flight Velocity Down", data_type="float"),
            Field(in_file_name="FlightAccelDown", in_game_name="Flight Accel Down", data_type="float"),
            Field(in_file_name="UseAerialFriction", in_game_name="Use Flight Vertical Friction", data_type="boolean"),
            Field(in_file_name="AerialVerticalTurningFriction", in_game_name="Flight Vertical Turning Friction", data_type="float"),
            Field(in_file_name="AerialVerticalBreakingFriction", in_game_name="Flight Breaking Friction", data_type="float"),
            Field(in_file_name="HasJetpack", in_game_name="Has Jetpack", data_type="boolean"),
            Field(in_file_name="MaxSpeed", in_game_name="Run Speed", data_type="float"),
            Field(in_file_name="ForwardSpeedBias", in_game_name="Forward Speed Bias", data_type="float"),
            Field(in_file_name="StrafeSpeedMult", in_game_name="Strafe Speed Multiplier", data_type="float"),
            Field(in_file_name="BackSpeedMult", in_game_name="Back Speed Multiplier", data_type="float"),
            Field(in_file_name="Acceleration", in_game_name="Walking Acceleration", data_type="float"),
            Field(in_file_name="CrouchingAcceleration", in_game_name="Crouching Acceleration", data_type="float"),
            Field(in_file_name="Friction", in_game_name="Scaling Friction", data_type="float"),
            Field(in_file_name="BrakingFriction", in_game_name="Let Off Friction", data_type="float"),
            Field(in_file_name="BrakingDeceleration", in_game_name="Flat Friction", data_type="float"),
            Field(in_file_name="StepUpHeight", in_game_name="Step Up Height", data_type="integer"), #revise
            Field(in_file_name="isFlyOnJumpAndCrouch", in_game_name="Fly On Jump And Crouch", data_type="boolean"),
            Field(in_file_name="JumpVelocityMin", in_game_name="Jump Velocity Min", data_type="float"),
            Field(in_file_name="JumpVelocityMax", in_game_name="Jump Velocity Max", data_type="float"),
            Field(in_file_name="AerialFriction", in_game_name="Aerial Friction", data_type="float"), #revise
            Field(in_file_name="Gravity", in_game_name="Gravity Scale", data_type="float"),
            Field(in_file_name="TerminalVelocity", in_game_name="Terminal Velocity", data_type="float"), #revise
            Field(in_file_name="DragCoefficient", in_game_name="Drag Coefficient", data_type="integer"), #revise
            Field(in_file_name="AirControl", in_game_name="Air Control Factor", data_type="integer"), #revise
            Field(in_file_name="AllowBufferedJumps", in_game_name="Allow Buffered Jumps", data_type="boolean"),
            Field(in_file_name="CanPogoJump", in_game_name="Can Pogo Jump", data_type="boolean"),
            Field(in_file_name="CanJumpFromCrouch", in_game_name="Can Jump From Crouch", data_type="boolean"),
            Field(in_file_name="AirJumpCount", in_game_name="Aerial Jump Count", data_type="integer"), #revise
            Field(in_file_name="CanCrouch", in_game_name="Can Crouch", data_type="boolean"),
            Field(in_file_name="MaxCrouchSpeed", in_game_name="Crouch Speed", data_type="float"),
            Field(in_file_name="CrouchHeightModifier", in_game_name="Crouch Height Multiplier", data_type="float"),
            Field(in_file_name="CrouchAnimationSpeed", in_game_name="Crouch Animation Rate", data_type="integer"), #revise
            Field(in_file_name="CanCrouchInAir", in_game_name="Can Crouch In Air", data_type="boolean"),
            Field(in_file_name="BounceOffWalls", in_game_name="Bounce Off Walls", data_type="boolean"),
            Field(in_file_name="JumpSpeedPenaltyDuration", in_game_name="Landing Speed Penalty Time", data_type="float"), #revise
            Field(in_file_name="JumpSpeedPenaltyPercent", in_game_name="Landing Speed Penalty", data_type="integer"), #revise
            Field(in_file_name="EnableQuakeMovement", in_game_name="Enable Quake/Source Movement", data_type="boolean"), 
            Field(in_file_name="JumpSkipsFriction", in_game_name="Jump Skips Friction", data_type="boolean"), #revise
            Field(in_file_name="ContinousGroundFriction", in_game_name="Continuous Ground Friction", data_type="float"), #revise
            Field(in_file_name="ContinuousAirFriction", in_game_name="Continuous Air Friction", data_type="boolean"), #revise
            Field(in_file_name="ScaledGroundAcceleration", in_game_name="Scaled Ground Acceleration", data_type="float"),
            Field(in_file_name="ScaledAirAcceleration", in_game_name="Scaled Air Acceleration", data_type="float"),
            Field(in_file_name="Max Air Speed", in_game_name="Max Air Speed", data_type="float"), #revise
            Field(in_file_name="Stop Speed Threshold", in_game_name="StopSpeedThreshold", data_type="float"), #revise
            Field(in_file_name="StopSpeed", in_game_name="Stop Speed", data_type="float"), #revise
            Field(in_file_name="ClampVelocityToInputSpeed", in_game_name="Clamp Velocity To Input Speed", data_type="boolean"),
            Field(in_file_name="EnableQuakeJump", in_game_name="Enable Quake Ramp Jump", data_type="boolean"),
            Field(in_file_name="KtJump", in_game_name="KtJump", data_type="float"), #revise
            Field(in_file_name="MovementPhysicsTickEnabled", in_game_name="Fixed Movement Tick", data_type="boolean"),
            Field(in_file_name="MovementPhysicsTickInterval", in_game_name="Tick Interval", data_type="float") #revise
        ]
        fields.reverse()
        for field_obj in fields:
            movement_properties_group.fields[field_obj.in_file_name] = field_obj
        move_tab.groups[movement_properties_group.name] = movement_properties_group
        return move_tab
        
    @staticmethod
    def _boxes_tab() -> Tab: #revise
        boxes_tab = Tab(name="Boxes")
        bounding_box_properties = FieldGroup(name="Bounding Box Properties")
        fields: List[Field] = [
            Field(in_file_name="CharacterModel", in_game_name="Character Model", data_type=None), #revise
            Field(in_file_name="CharacterSkin", in_game_name="Character Skin", data_type=None), #revise
            Field(in_file_name="MeshHitDetection", in_game_name="Per Mesh Hit Detection", data_type="boolean"), #revise
        ]
        fields.reverse()
        process_fields(field_stack=fields, group=bounding_box_properties)
        boxes_tab.groups[bounding_box_properties.name] = bounding_box_properties

        main_bounding_box = FieldGroup(name="Main Bounding Box")
        fields: List[Field] = [
            Field(in_file_name="MainBBType", in_game_name="Bounding Box Type", data_type=None), #revise
            Field(in_file_name="MainBBHide", in_game_name="Hide Bounding Box", data_type="boolean"), #revise
            Field(in_file_name="MainBBHasHead", in_game_name="Has Head", data_type="boolean"), #revise
            Field(in_file_name="MainBBHeight", in_game_name="Body Height", data_type="float"), #revise
            Field(in_file_name="MainBBRadius", in_game_name="Body Radius", data_type="float"), #revise
            Field(in_file_name="MainBBHeadOffset", in_game_name="Head Offset", data_type="float"), #revise
            Field(in_file_name="MainBBHeadRadius", in_game_name="Head Radius", data_type="float"), #revise
        ]
        fields.reverse()
        process_fields(field_stack=fields, group=main_bounding_box)
        boxes_tab.groups[main_bounding_box.name] = main_bounding_box

        projectile_bounding_box = FieldGroup(name="Projectile Bounding Box")
        fields: List[Field] = [
            Field(in_file_name="ProjBBType", in_game_name="Projectile Bounding Box Type", data_type=None), #revise
            Field(in_file_name="ProjBBHide", in_game_name="Hide Bounding Box", data_type="boolean"), #revise
            Field(in_file_name="ProjBBHasHead", in_game_name="Has Head", data_type="boolean"), #revise
            Field(in_file_name="ProjBBHeight", in_game_name="Body Height", data_type="float"), #revise
            Field(in_file_name="ProjBBRadius", in_game_name="Body Radius", data_type="float"), #revise
            Field(in_file_name="ProjBBOffset", in_game_name="Head Offset", data_type="float"), #revise
            Field(in_file_name="ProjBBHeadRadisu", in_game_name="Head Radius", data_type="float"), #revise
        ]
        fields.reverse()
        process_fields(field_stack=fields, group=projectile_bounding_box)
        boxes_tab.groups[projectile_bounding_box.name] = projectile_bounding_box
        return boxes_tab

    @staticmethod
    def _abilities_tab() -> Tab:
        abilities_tab = Tab(name="Abilities")
        abilities_group = FieldGroup(name="Abilities")
        fields: List[Field] = [
            Field(in_file_name="AbilityGlobalCooldown", in_game_name="Global Cooldown", data_type="float"), #revise
            Field(in_file_name="BlockAbilityOnStartDuration", in_game_name="Block Ability For Duration On Challenge Start", data_type="float"), #revise
        ]
        fields.reverse()
        process_fields(field_stack=fields, group=abilities_group)
        abilities_tab.groups[abilities_group.name] = abilities_group
        return abilities_tab

    @staticmethod
    def _spawn_tab() -> Tab:
        spawn_tab = Tab(name="Spawn")
        spawn_rules_group = FieldGroup(name="Spawn Rules")
        fields: List[Field] = [
            Field(in_file_name="SpawnOffsetMin", in_game_name="Spawn Offset Minimum", data_type="vector"),
            Field(in_file_name="SpawnOffsetMax", in_game_name="Spawn Offset Maximum", data_type="vector"),
            Field(in_file_name="BlockedSpawnRadius", in_game_name="Blocked Self Spawn Radius", data_type="float"), #revise
            Field(in_file_name="BlockSpawnFOV", in_game_name="Block Other Spawn FOV", data_type="float"),
            Field(in_file_name="InvertBlockSpawn", in_game_name="Invert Block Other Spawn POV Logic", data_type="boolean"), #revise
            Field(in_file_name="BlockSpawnDistance", in_game_name="Block Other Spawn Distance", data_type="float"), #revise
        ]
        fields.reverse()
        process_fields(field_stack=fields, group=spawn_rules_group)
        spawn_tab.groups[spawn_rules_group.name] = spawn_rules_group

        playback_on_spawn_group = FieldGroup(name="Playback On Spawn")
        fields: List[Field] = [
            Field(in_file_name="Playback.ProfileName", in_game_name="Profile Name", data_type=None), #revise, not in file
            Field(in_file_name="PlaybackOptions.OverrideMovement", in_game_name="Override Movement", data_type="boolean"),
            Field(in_file_name="PlaybackOptions.OverrideRotation", in_game_name="Override Rotation", data_type="boolean"),
            Field(in_file_name="PlaybackOptions.OverrideWeapons", in_game_name="Override Weapon Input", data_type="boolean"),
            Field(in_file_name="PlaybackOptions.OverrideAbilities", in_game_name="Override Ability Input", data_type="boolean"),
            Field(in_file_name="PlaybackOptions.LoopUponCompletion", in_game_name="Loop Upon Completion", data_type="boolean"),
            Field(in_file_name="PlaybackOptions.PlaybackMode", in_game_name="Playback Mode", data_type=None), #revise
            Field(in_file_name="PlaybackOptions.BreakToInputMode", in_game_name="Break To Input Mode", data_type="boolean"), # not visible in-game
            Field(in_file_name="PlaybackOptions.OverrideDodgeTime", in_game_name="Override Dodge Time", data_type="boolean"), # not visible in-game
        ]
        fields.reverse()
        process_fields(field_stack=fields, group=playback_on_spawn_group)
        spawn_tab.groups[playback_on_spawn_group.name] = playback_on_spawn_group
        return spawn_tab

    @staticmethod
    def _effects_tab() -> Tab:
        effects_tab = Tab(name="Effects")
        field_group = FieldGroup() # no groups, so just defaults to name 'Default'
        fields: List[Field] = [
            Field(in_file_name="DamageKnockbackFactor", in_game_name="Damage Knockback Factor", data_type=None),
            Field(in_file_name="RespawnInvincible", in_game_name="Respawn Invincibility Timer", data_type=None),
            Field(in_file_name="BlockSelfDamage", in_game_name="Block Self Damage", data_type=None),
            Field(in_file_name="BlockTeamDamage", in_game_name="Block Team Damage", data_type=None),
            Field(in_file_name="InvinciblePlayers", in_game_name="Invincible Players", data_type=None),
            Field(in_file_name="InvincibleBots", in_game_name="Invincible Bots", data_type=None),
            Field(in_file_name="DisableCharacterCollision", in_game_name="Disable Character Collision", data_type=None),
            Field(in_file_name="HealthRegainedonKill", in_game_name="Health Regained on Kill", data_type=None),
            Field(in_file_name="HealthRegenPerSec", in_game_name="Health Regen Per Sec", data_type=None),
            Field(in_file_name="HealthRegenDelay", in_game_name="Health Regen Delay", data_type=None),
            Field(in_file_name="AmmoRegainedOnKill", in_game_name="Ammo Awarded On Death", data_type=None),
            Field(in_file_name="ViewBobTime", in_game_name="Landing View Bob Time", data_type=None),
            Field(in_file_name="ViewBobAngleAdjustment", in_game_name="Landing Angle Adjustment", data_type=None),
            Field(in_file_name="ViewBobCameraZOffset", in_game_name="Landing Camera Z Offset", data_type=None),
            Field(in_file_name="ViewBobAffectsShots", in_game_name="Landing Affects Shots", data_type=None),
            Field(in_file_name="LifeStealPercent", in_game_name="Lifesteal", data_type=None),
        ]
        fields.reverse()
        process_fields(field_stack=fields, group=field_group)
        effects_tab.groups[field_group.name] = field_group
        return effects_tab

    @staticmethod
    def _jetpack_tab() -> Tab:
        jetpack_tab = Tab(name="Jetpack")
        field_group = FieldGroup(name="Jetpack") # temp
        # finish later to double check in UI
        fields: List[Field] = [
            Field(in_file_name="JetpackActivationDelay", in_game_name="Jetpack Activation Delay", data_type=None),
            Field(in_file_name="JetpackFullFuelTime", in_game_name="Full Fuel Tank Time", data_type=None),
            Field(in_file_name="JetpackFuelIncPerSec", in_game_name="Fuel Regen Rate", data_type=None),
            Field(in_file_name="JetpackFuelRegeneration", in_game_name="Fuel Regens In Air", data_type=None),
            Field(in_file_name="JetpackThrust", in_game_name="Thrust", data_type=None),
            Field(in_file_name="JetpackMaxZVelocity", in_game_name="Max Z Velocity", data_type=None),
            Field(in_file_name="JetpackAirControlWithThrust", in_game_name="Air Control With Thrust", data_type=None),
        ]
        fields.reverse()
        process_fields(field_stack=fields, group=field_group)
        jetpack_tab.groups[field_group.name] = field_group
        return jetpack_tab

    @staticmethod
    def chr_schema() -> Component:
        chr_comp = Component()
        tabs: List[Tab] = [] # this could be more efficient, but I think this is easier to maintain and more readable
        tabs.append(ChrSchema._main_tab())
        tabs.append(ChrSchema._move_tab())
        tabs.append(ChrSchema._boxes_tab())
        tabs.append(ChrSchema._abilities_tab())
        tabs.append(ChrSchema._spawn_tab())
        tabs.append(ChrSchema._effects_tab())
        tabs.append(ChrSchema._jetpack_tab())

        while tabs: # might revise stacks since it is LIFO, and could insert out of order
            tab_obj = tabs.pop()
            chr_comp.tabs[tab_obj.name] = tab_obj
        return chr_comp
        
        