MAX_CARS = 4
MAX_CAR_COLOURS = 32
MAX_RIDE_TYPES = 3
MAX_HEAD_CARS = 3
MAX_TAIL_CARS = 1
MAX_SHOP_ITEMS = 2

class Ride:
    """The base class for rides"""
    def __init__(self):
        self.authors = []
        self.objectType = "ride"
        self.version = "1.0"
        self.id = "newride"
        self.rideTypes = ["miniatureRailway",None,None] # remember this is actually called "type"
        self.rideCategories = ["transport",None] # actually called "category"
        self.availableTrackPieces = []

        self.shopSells = [None for _ in range(MAX_SHOP_ITEMS)] # actually called "sells"
        
        self.carColours = []
        self.minCarsPerTrain = 3
        self.maxCarsPerTrain = 8
        self.zeroCars = 0 # actually called "numEmptyCars"
        self.carsPerFlatRide = 255 # 255 means N/A
        self.tabCar = 0 # offset from front
        self.defaultCar = 0
        self.headCars = [None for _ in range(MAX_HEAD_CARS)]
        self.tailCars = [None for _ in range(MAX_TAIL_CARS)]
        
        self.maxHeight = 0
        self.ratingMultiplier = {}
        
        self.flags = {}
        self.cars = [None for _ in range(MAX_CARS)]
        
        self.strings = {"name":{},"description":{},"capacity":{}}
        
    def setFlag(flag,value):
        if value != None:
            self.flags[flag] = value
        else:
            del self.flags[flag]
        # remember to update the flag buttons after running this function
        
    def setRatingModifier(modifier,value):
        if value >0:
            self.ratingMultiplier[modifier] = value
        else:
            del self.ratingMultiplier[modifier]
            
    def setHeadCar(index,value):
        if index >= 0 and index < MAX_HEAD_CARS:
            self.headCars[index] = value
        
    def setTailCar(index,value):
        if index >= 0 and index < MAX_TAIL_CARS:
            self.tailCars[index] = value
                
LANGUAGES = [
    "en-GB", # english
    "en-US", # american
    "fr-FR", # french
    "de-DE", # german
    "es-ES", # spanish
    "it-IT", # italian
    "nl-NL", # dutch
    "sv-SE", # swedish
    "ko-KR", # korean
    "zh-CN", # chinese
    "zh-TW", # taiwanese (?)
    "pt-BR", # lol i dunno
    "cs-CZ", # czech
    "ja-JP", # japanese
    "pl-PL", # polish
    "ru-RU", # russian
    ]
            
RATING_MULTIPLIERS = [

    {"Name":"excitement",
     "String":"Excitement"
     },
    {"Name":"intensity",
     "String":"Intensity"
     },
    {"Name":"nausea",
     "String":"Nausea"
     },
    ]

RIDE_CATEGORIES = [

    {"Name":"transport",
     "String":"Transport ride"
     },
    {"Name":"gentle",
     "String":"Gentle ride"
     },
    {"Name":"rollercoaster",
     "String":"Roller coaster"
     },
    {"Name":"water",
     "String":"Water ride"
     },
    {"Name":"stall",
     "String":"Stall/shop"
     },    
    ]

SHOP_TYPES = [

    {"Name":"food_stall",
     "String":"Food stall"
     },
    {"Name":"drink_stall",
     "String":"Drink stall"
     },
    {"Name":"shop",
     "String":"Shop"
     },
    {"Name":"information_kiosk",
     "String":"Information kiosk"
     },
    {"Name":"toilets",
     "String":"Toilets"
     },
    {"Name":"first_aid",
     "String":"First aid"
     },
    {"Name":"cash_machine",
     "String":"Cash machine"
     },
]

FLAT_RIDE_TYPES = [

    {"Name":"enterprise",
     "String":"HUSS enterprise"
     },
    {"Name":"maze",
     "String":"Hedge maze"
     },
    {"Name":"dodgems",
     "String":"Dodgems"
     },
    {"Name":"ferris_wheel",
     "String":"Ferris wheel"
     },
    {"Name":"twist",
     "String":"HUSS scrambler"
     },
    {"Name":"haunted_house",
     "String":"Haunted house"
     },
    {"Name":"circus",
     "String":"Circus"
     },
    {"Name":"magic_carpet",
     "String":"Magic carpet"
     },
    {"Name":"swinging_ship",
     "String":"Swinging ship"
     },
    {"Name":"swinging_inverter_ship",
     "String":"Swinging inverting ship"
     },
    {"Name":"merry_go_round",
     "String":"Merry-go-round"
     },
    {"Name":"motion_simulator",
     "String":"Motion simulator"
     },
    {"Name":"3d_cinema",
     "String":"3D cinema"
     },
    {"Name":"top_spin",
     "String":"HUSS top spin"
     },
    {"Name":"space_rings",
     "String":"Space rings"
     },
    {"Name":"spiral_slide",
     "String":"Spiral slide"
     },
    ]

TOWER_RIDE_TYPES = [

    {"Name":"launched_freefall",
     "String":"Launched freefall"
     },
    {"Name":"observation_tower",
     "String":"Observation tower"
     },
    {"Name":"roto_drop",
     "String":"Roto-drop"
     },
    {"Name":"lift",
     "String":"Elevator"
     },
    ]

TRACKED_RIDE_TYPES = [
    # Transport rides
    {"Name":"miniature_railway",
     "String":"Miniature railway"
     },
    {"Name":"monorail",
     "String":"Monorail"
     },
    {"Name":"suspended_monorail",
     "String":"Suspended monorail ride"
     },
    {"Name":"chairlift",
     "String":"Chairlift"
     },

    # Misc. tracked rides
    {"Name":"car_ride",
     "String":"Car ride"
     },
    {"Name":"ghost_train",
     "String":"Ghost train"
     },
    {"Name":"go_karts",
     "String":"Go karts"
     },
    {"Name":"mini_helicopters",
     "String":"Mini helicopters"
     },
    {"Name":"mini_golf",
     "String":"Mini golf"
     },
    {"Name":"monorail_cycles",
     "String":"Monorail cycles"
     },
    
    
    # Roller coasters (wood)
    {"Name":"wooden_rc",
     "String":"Wooden coaster"
     },
    {"Name":"wooden_wild_mouse",
     "String":"Wooden wild mouse coaster"
     },
    {"Name":"side_friction_rc",
     "String":"Side friction coaster"
     },
    {"Name":"virginia_reel",
     "String":"Virginia reel coaster"
     },
    {"Name":"reverser_rc",
     "String":"Wooden reverser coaster"
     },
    
    # Roller coasters (steel, standard)
    {"Name":"bobsleigh_rc",
     "String":"Bobsled coaster"
     },
    {"Name":"corkscrew_rc",
     "String":"Arrow corkscrew coaster"
     },
    {"Name":"multi_dimension_rc",
     "String":"Arrow multi-dimension coaster"
     },
    {"Name":"steeplechase",
     "String":"Arrow steeplechase coaster"
     },
    {"Name":"looping_rc",
     "String":"Schwarzkopf looping coaster"
     },
    {"Name":"spiral_rc",
     "String":"Schwarzkopf spiral coaster"
     },
    {"Name":"mini_rc",
     "String":"Schwarzkopf mini coaster"
     },
    {"Name":"vertical_drop_rc",
     "String":"B&M dive coaster"
     },
    {"Name":"twister_rc",
     "String":"B&M twister coaster"
     },
    {"Name":"stand_up_rc",
     "String":"TOGO standup coaster"
     },
    {"Name":"air_powered_vertical_rc",
     "String":"Air-powered vertical coaster"
     },
    {"Name":"reverse_freefall_rc",
     "String":"Reverse freefall coaster"
     },
    {"Name":"giga_rc",
     "String":"Intamin giga coaster"
     },
    {"Name":"mine_train_rc",
     "String":"Mine train coaster"
     },
    {"Name":"heartline_twister_rc",
     "String":"Heartline twister coaster"
     },
    {"Name":"mine_ride",
     "String":"Mack powered coaster"
     },
    {"Name":"steel_wild_mouse",
     "String":"Steel wild mouse coaster"
     },
    {"Name":"junior_rc",
     "String":"Junior coaster"
     },
    {"Name":"lim_launched_rc",
     "String":"Premier LIM-launched coaster"
     },
    
    # Roller coasters (inverted)
    {"Name":"inverted_impulse_rc",
     "String":"Intamin inverted impulse coaster"
     },
    {"Name":"flying_rc",
     "String":"B&M flying coaster"
     },
    {"Name":"inverted_rc",
     "String":"B&M Inverted coaster"
     },
    {"Name":"supsended_swinging_rc",
     "String":"Suspended swinging coaster"
     },
    {"Name":"compact_inverted_rc",
     "String":"Vekoma SLC coaster"
     },
    {"Name":"mini_suspended_rc",
     "String":"Mini suspended coaster"
     },
    {"Name":"inverted_hairpin_rc",
     "String":"Inverted hairpin coaster"
     },
    {"Name":"lay_down_rc",
     "String":"Vekoma lay-down coaster"
     },
    
    # Water rides
    {"Name":"water_coaster",
     "String":"Water coaster"
     },
    {"Name":"boat_hire",
     "String":"Boat hire"
     },
    {"Name":"dinghy_slide",
     "String":"Dinghy slide"
     },
    {"Name":"log_flume",
     "String":"Log flume"
     },
    {"Name":"river_rafts",
     "String":"River rafts"
     },
    {"Name":"splash_boats",
     "String":"Splash boats"
     },    
    {"Name":"submarine_ride",
     "String":"Submarine ride"
     },
    ]

RIDE_FLAGS = [
    {"Name":"noInversions",
     "String":"Disable inversions",
     "TValue":True
     },
    {"Name":"noBanking",
     "String":"Disable banked track",
     "TValue":True
     },
    {"Name":"playDepartSound",
     "String":"Chuffing on departure",
     "TValue":True
     },
    {"Name":"disableWandering",
     "String":"Disallow boat wandering",
     "TValue":True
     },
    {"Name":"playSplashSound",
     "String":"Play splash sounds on flat track",
     "TValue":True
     },
    {"Name":"playSplashSoundSlide",
     "String":"Play splash sounds on water track",
     "TValue":True
     },
    {"Name":"hasShelter",
     "String":"Peeps ride in the rain",
     "TValue":True
     },
    {"Name":"limitAirtimeBonus",
     "String":"Limit airtime bonus",
     "TValue":True
     },
    {"Name":"disableBreakdown",
     "String":"Disable breakdowns",
     "TValue":True
     },
    {"Name":"disableDoorConstruction",
     "String":"Disallow doors",
     "TValue":True
     },
    {"Name":"disableCollisionCrashes",
     "String":"Disable collision crashes",
     "TValue":True
     },
    {"Name":"disablePainting",
     "String":"Disable ride painting",
     "TValue":True
     },
    {"Name":"swingMode",
     "String":"Swing mode 1",
     "TValue":1
     },
    {"Name":"swingMode",
     "String":"Swing mode 2",
     "TValue":2
     },
    {"Name":"rotationMode",
     "String":"Rotation mode 1",
     "TValue":1
     },
    {"Name":"rotationMode",
     "String":"Rotation mode 2",
     "TValue":2
     }
]

SHOP_ITEMS = [
    {"Name":"burger",
     "String":"Burgers"
     },
    {"Name":"chips",
     "String":"French fries"
     },
    {"Name":"ice_cream",
     "String":"Icecream"
     },
    {"Name":"candyfloss",
     "String":"Cotton candy"
     },
    {"Name":"pizza",
     "String":"Pizza"
     },
    {"Name":"hot_dog",
     "String":"Hot dogs"
     },
    {"Name":"tentacle",
     "String":"Tentacles"
     },
    {"Name":"toffee_apple",
     "String":"Toffee apples"
     },
    {"Name":"doughnut",
     "String":"Donuts"
     },
    {"Name":"chicken",
     "String":"Fried chicken"
     },
    {"Name":"pretzel",
     "String":"Pretzels"
     },
    {"Name":"funnel_cake",
     "String":"Funnel cake"
     },
    {"Name":"beef_noodles",
     "String":"Beef noodles"
     },
    {"Name":"fried_rice_noodles",
     "String":"Fried rice noodles"
     },
    {"Name":"wonton_soup",
     "String":"Wonton soup"
     },
    {"Name":"meatball_soup",
     "String":"Meatball soup"
     },
    {"Name":"sub_sandwich",
     "String":"Sub sandwich"
     },
    {"Name":"cookie",
     "String":"Cookie"
     },
    {"Name":"roast_sausage",
     "String":"Roast sausage"
     },
    {"Name":"drink",
     "String":"Drinks"
     },
    {"Name":"coffee",
     "String":"Coffee"
     },
    {"Name":"lemonade",
     "String":"Lemonade"
     },
    {"Name":"chocolate",
     "String":"Hot chocolate"
     },
    {"Name":"iced_tea",
     "String":"Iced tea"
     },
    {"Name":"fruit_juice",
     "String":"Fruit juice"
     },
    {"Name":"soybean_milk",
     "String":"Soybean milk"
     },
    {"Name":"sujeonggwa",
     "String":"Sujeonggwa"
     },
    {"Name":"balloon",
     "String":"Balloons"
     },
    {"Name":"toy",
     "String":"Toys"
     },
    {"Name":"map",
     "String":"Maps"
     },
    {"Name":"photo",
     "String":"Photos"
     },
    {"Name":"umbrella",
     "String":"Umbrellas"
     },
    {"Name":"voucher",
     "String":"Vouchers"
     },
    {"Name":"hat",
     "String":"Hats"
     },
    {"Name":"tshirt",
     "String":"T-shirts"
     },
    {"Name":"sunglasses",
     "String":"Sunglasses"
     },
    ]
