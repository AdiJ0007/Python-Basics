import re

pattern = r"[A-Z]lass"
text = """Firebird (car) redirects here. For the concept car series, see General Motors Firebird.
Pontiac Firebird

The second, third, and fourth generations of Blass
the Pontiac Firebird Trans Am
Overview Alass
Manufacturer	Pontiac (General Motors) Glass
Production	February 23, 1967 – August 30, 2002
Model years	1967 – 2002
Body and chassis
Class	Pony car
Muscle car
Layout	Front engine, rear-wheel-drive
Platform	F-body
The Pontiac Firebird is an American automobile built and produced by Pontiac from the 1967 to 2002 model years.[1] Designed as a pony car to compete with the Ford Mustang, it was introduced on February 23, 1967, five months after GM's Chevrolet division's platform-sharing Camaro.[2] This also coincided with the release of the 1967 Mercury Cougar, Ford's upscale, platform-sharing version of the Mustang.[3][4] The name "Firebird" was also previously used by GM for the General Motors Firebird series of concept cars in the 1950s.[5]
First generation (1967–1969)
See also: GM F platform § First Generation, 1967–1969

First generation
1967 Pontiac Firebird 400 coupe
Overview
Production	February 23, 1967–January 1970
Assembly	Lordstown, Ohio, United States (1967–1969)
Van Nuys, California, United States (1968–1969)
Norwood, Ohio, United States (1969)
Designer	Jack Humbert[6]
Body and chassis
Body style	2-door coupe
2-door convertible
Platform	F-body
Related	Chevrolet Camaro (first generation)
Powertrain
Engine	230 cu in (3.8 L) Pontiac SOHC I6
250 cu in (4.1 L) Pontiac SOHC I6
326 cu in (5.3 L) Pontiac V8
350 cu in (5.7 L) Pontiac V8
400 cu in (6.6 L) Pontiac V8
Transmission	2-speed automatic
3-speed Turbo-Hydramatic automatic
3-speed manual
4-speed manual
Dimensions
Wheelbase	108.1 in (2,746 mm) (1967)
Length	188.8 in (4,796 mm) (1967)
Width	72.6 in (1,844 mm) (1967)
Height	51.5 in (1,308 mm) (1967)[7]
The first generation Firebird had characteristic Coke bottle styling shared with its cousin, the Chevrolet Camaro. Announcing a Pontiac styling trend, the Firebird's bumpers were integrated into the design of the front end, giving it a more streamlined look than the Camaro. The Firebird's rear "slit" taillights were inspired by the 1966–1967 Pontiac GTO and Pontiac Grand Prix. Both a two-door hardtop and a convertible were offered through the 1969 model year. Originally, the car was a "consolation prize" for Pontiac, which had desired to produce a two-seat sports car based on its original Banshee concept car. However, GM feared this would cut into Chevrolet Corvette sales, and gave Pontiac a piece of the "pony car" market by sharing the F-body platform with Chevrolet. The listed retail price before options for the coupe was $2,666 ($24,361 in 2023 dollars[8]) and the convertible was $2,903 ($28,519 in 2023 dollars[8]).[9]
The 1967 base model Firebird came equipped with the Pontiac 230 cu in (3.8 L) SOHC inline-six. Based on the architecture of the standard Chevrolet 230 cu in (3.8 L) inline-six, it was fitted with a one-barrel Rochester carburetor and rated at 165 hp (123 kW).[2] The "Sprint" model six came with a four-barrel carburetor, developing 215 hp (160 kW).[10] Most buyers opted for one of three V8s: the 326 cu in (5.3 L) with a two-barrel carburetor producing 250 hp (186 kW); the four-barrel "HO" (high output) 326, producing 285 hp (213 kW); or the 325 hp (242 kW) 400 cu in (6.6 L) from the GTO. All 1967–1968 400 CI engines had throttle restrictors that blocked the carburetors' secondaries from fully opening.[2] A "Ram Air" option was also available, providing functional hood scoops, higher flow heads with stronger valve springs, and a hotter camshaft. Power for the Ram Air package was the same as the conventional 400 HO, but peaked at 5,200 rpm.
The 230 cu in (3.8 L) engines were subsequently enlarged for 1968 to 250 cubic inches (4.1 liters), the base version developing an increased 175 hp (130 kW) using a one-barrel carburetor, and the high-output Sprint version the same 215 hp with a four-barrel carburetor. Also for the 1968 model, the 326 cu in (5.3 L) engine was replaced by the Pontiac 350 cu in (5.7 L) V8, which actually displaced 354 cu in (5.8 L), and produced 265 hp (198 kW) with a two-barrel carburetor. An HO version of the 350 cu in (5.7 L) with a revised cam was also offered to start in that year, which developed 320 hp (239 kW). The power output of the other engines was increased marginally.[2]
There was an additional Ram Air IV option for the 400 cu in (6.6 L) V8 engines during 1969, complementing the Ram Air 400(now often colloquially but incorrectly called the "Ram Air III," a name never used by Pontiac). The Ram Air IV was rated at 345 hp (350 PS; 257 kW) at 5000 rpm and 430 lb⋅ft (583 N⋅m) of torque at 3400 rpm;[11] and 335 hp (340 PS; 250 kW) respectively. The 350 cu in (5.7 L) HO engine was revised again with a different cam and cylinder heads resulting in 325 hp (242 kW). During 1969 a special 303 cu in (5.0 L) engine was designed for Sports Car Club of America (SCCA) road racing applications that were not available in production cars.[12]
Modifications for 1968 included the addition of federally-mandated side marker lights: for the front of the car, the turn signals were made larger and extended to wrap around the front edges of the car, and on the rear, the Pontiac (V-shaped) Arrowhead logo was added to each side. The front door vent-windows was replaced with a single pane of glass and Astro Ventilation, a fresh-air-inlet system. The 1969 model received a major facelift with a new front-end design but unlike the GTO, it did not have the Endura bumper. The instrument panel and steering wheel were revised. The ignition switch was moved from the dashboard to the steering column with the introduction of GM's new locking ignition switch/steering wheel.[2]
 """
m = re.search(pattern, text)
print(m)
matches = re.finditer(pattern, text)
for i in matches:
    print(i)
    
