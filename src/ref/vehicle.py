
class Car:
    """The base class for cars"""
    def __init__(self):
        self.rotationFrameMast = 31
        self.spacing = 200000
        self.mass = 600
        self.tabOffset = 0 # unknown
        self.num_seats = 0 # this is calculated by the animation
        self.spriteWidth = 0 # unknown
        self.spriteHeightNegative = 0 # unknown
        self.spriteHeightPositive = 0 # unknown
        self.animation = 0 # animation type
        self.baseNumFrames # unknown
        self.spinningInertia = 0
        self.spinningFriction = 0
        self.frictionSoundId = 255 # the running sound
        self.logFlumeReverserVehicleType = 0 #unknown
        self.soundRange = 255 # the scream sounds or whistle/bell
        self.doubleSoundFrequency = 0 # unknown
        self.poweredAcceleration = 0
        self.poweredMaxSpeed = 0
        self.carVisual = 0
        self.effectVisual = 1
        self.drawOrder = 5
        self.numVerticalFramesOverride = 0
        self.loadingPositions = [] # this is calculated by the animation
        self.loadingWaypoints = [] # unknown
        
        self.flags = {}
        
    def setFlag(flag,value):
        if value != None:
            self.flags[flag] = value
        else:
            del self.flags[flag]
        # remember to update the flag buttons after running this function
        
FRICTION_SOUNDS = [
    {"String":"Large wooden coaster",
     "Value":54
     },
    {"String":"Small wooden coaster",
     "Value":1
     },
    {"String":"Standard steel coaster",
     "Value":2
     },
    {"String":"Modern steel coaster",
     "Value":57
     },
    {"String":"Waterslide",
     "Value":32
     },
    {"String":"Railway train",
     "Value":31
     },
    {"String":"Petrol engine",
     "Value":21
     },
    {"String":"No running sound",
     "Value":255
     }
    ]
        
SOUND_RANGE_SOUNDS = [
    {"String":"Screams type 1",
     "Value":0
     },
    {"String":"Screams type 2",
     "Value":1
     },
    {"String":"Screams type 3",
     "Value":2
     },
    {"String":"Steam whistle",
     "Value":3
     },
    {"String":"Tram bell",
     "Value":4
     },
    {"String":"No additional sound",
     "Value":255
     }
    ]        
VEHICLE_FLAGS = [
    {"Name":"VEHICLE_ENTRY_FLAG_POWERED_RIDE_UNRESTRICTED_GRAVITY",
     "String":"Vehicle does not brake on downhills"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_NO_UPSTOP_WHEELS",
     "String":"Vehicle flies off hill crests"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_NO_UPSTOP_BOBSLEIGH",
     "String":"Vehicle flies off hill crests (bobsled)"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_MINI_GOLF",
     "String":"Mini golf"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_4",
     "String":"Flag 4"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_5",
     "String":"Flag 5"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_HAS_INVERTED_SPRITE_SET",
     "String":"Vehicle can travel inverted indefinitely"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_DODGEM_INUSE_LIGHTS",
     "String":"Vehicle has \"in use\" lights"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_ALLOW_DOORS_DEPRECATED",
     "String":"Vehicle opens doors"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_2",
     "String":"Vehicle has 3rd color swatch"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_10",
     "String":"Flag 10"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_11",
     "String":"Flag 11"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_OVERRIDE_NUM_VERTICAL_FRAMES",
     "String":"Vehicle has custom number of vertical frames"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_13",
     "String":"Flag 13"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_SPINNING_ADDITIONAL_FRAMES",
     "String":"Vehicle has extra spinning frames"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_LIFT",
     "String":"Vehicle is an elevator car"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_ENABLE_ADDITIONAL_COLOUR_1",
     "String":"Vehicle has 2nd color swatch"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_SWINGING",
     "String":"Vehicle swings in curves"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_SPINNING",
     "String":"Vehicle spins"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_POWERED",
     "String":"Vehicle is powered"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_RIDERS_SCREAM",
     "String":"Riders scream"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_21",
     "String":"Flag 21"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_BOAT_HIRE_COLLISION_DETECTION",
     "String":"Vehicle operates out of a boat hire"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_VEHICLE_ANIMATION",
     "String":"Vehicle is animated"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_RIDER_ANIMATION",
     "String":"Vehicle riders are animated"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_25",
     "String":"Flag 25"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_SLIDE_SWING",
     "String":"Slide Swing"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_CHAIRLIFT",
     "String":"Vehicle is a chairlift car"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_WATER_RIDE",
     "String":"Vehicle is propelled by moving water"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_GO_KART",
     "String":"Vehicle is a go-kart"
     },
    {"Name":"VEHICLE_ENTRY_FLAG_DODGEM_CAR_PLACEMENT",
     "String":"Vehicle uses dodgem placement"
     },
    {"Name":"",
     "String":""
     },
    ]

SPRITE_FLAGS = [
    {"Name":"flat",
     "String":"Flat track"
     },
    {"Name":"flatBanked",
     "String":"Flat banked track"
     },
    {"Name":"gentleSlopes",
     "String":"Gentle slopes"
     },
    {"Name":"steepSlopes",
     "String":"Steep slopes",
     "Dependencies":["gentleSlopes"]
     },
    {"Name":"verticalSlopes",
     "String":"Vertical slopes and loops",
     "Dependencies":["steepSlopes","gentleSlopes"]
     },
    {"Name":"diagonalSlopes",
     "String":"Diagonal slopes"
     },
    {"Name":"inlineTwists",
     "String":"Inline twists",
     "Dependencies":["flatBanked"]
     },
    {"Name":"flatToGentleSlopeBankedTransitions",
     "String":""
     },
    {"Name":"diagonalGentleSlopeBankedTransitions",
     "String":"Diagonal bank transition slope transitions"
     },
    {"Name":"gentleSlopeBankedTransitions",
     "String":"Bank transition slope transitions",
     "Dependencies":["diagonalSlopes"]
     },
    {"Name":"gentleSlopeBankedTurns",
     "String":"Sloped banked turns"
     },
    {"Name":"flatToGentleSlopeWhileBankedTransitions",
     "String":"Banked slope transitions"
     },
    {"Name":"corkscrews",
     "String":"Corkscrews",
     "Excludes":["curvedLiftHill"]
     },
    {"Name":"curvedLiftHill",
     "String":"Curved lift hill",
     "Excludes":["corkscrews"]
     },
    {"Name":"restraintAnimation",
     "String":"Animated restraints"
     },
    {"Name":"VEHICLE_SPRITE_FLAG_15", # something to do with submarine ride
     "String":"FLAG_15"
     },
    ]