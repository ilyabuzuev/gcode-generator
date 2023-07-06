M136 (enable build)
M73 P0
G162 X Y F2000(home XY axes maximum)
G161 Z F900(home Z axis minimum)
G92 X0 Y0 Z-5 A0 B0 (set Z to -5)
G1 Z0.0 F900(move Z to '0')
G161 Z F100(home Z axis minimum)
M132 X Y Z A B (Recall stored home offsets for XYZAB axis)
G92 X152 Y72 Z0 A0 B0
G1 X-112 Y-73 Z150 F3300.0 (move to waiting position)
G130 X20 Y20 A20 B20 (Lower stepper Vrefs while heating)
M109 S60 T0
M134 T0
M135 T0
M104 S60 T0
M133 T0
G130 X127 Y127 A127 B127 (Set Stepper motor Vref to defaults)
; Makerbot Industries
; Miracle Grue 3.9.4
; This file contains digital fabrication directives
; in G-Code format for your 3D printer
; http://www.makerbot.com/support/makerware/documentation/slicer/
; 
; Right Toolhead Weight (grams): 0.993724 
; Right Toolhead Distance (mm): 325.692 
; Duration: 491.444 seconds 
; Active extruders in print: 0 
; Chunk 0 
; Lower Position  0 
; Upper Position  0.3 
; Thickness       0.3 
; Width           2.5 
G1 X105.400 Y-74.000 Z0.270 F9000.000 (Extruder Prime Dry Move)
G1 X-112 Y-73 Z0.270 F1800.000 E25.000 (Extruder Prime Start)
G92 A0 B0 (Reset after prime)
G1 Z0.000000 F1000
G1 X-112.0 Y-73.0 Z0.0 F1000 E0.0
G92 E0
G1 X-112.000 Y-73.000 Z0.000 F1500 A-1.30000; Retract 
G1 X-112.000 Y-73.000 Z0.000 F3000; Retract 
G1 X-112.000 Y-73.000 Z0.300 F1380; Travel Move 


G1 X0 Y0 F
G1 X0 Y10 F A
G1 X4 Y0 F
G1 X4 Y10 F A
G1 X8 Y0 F
G1 X8 Y10 F A
G1 X12 Y0 F
G1 X12 Y10 F A
G1 X16 Y0 F
G1 X16 Y10 F A



; End of print 
; G1 X3.827 Y4.114 Z10.970 F1500 A325.69237; Retract 
; M127 T0 (Fan Off)
; M18 A B(Turn off A and B Steppers)
; G1 Z155 F900
; G162 X Y F2000
; M18 X Y Z(Turn off steppers after a build)
; M109 S0 T0
; M104 S0 T0
; M73 P100 (end  build progress )
; M70 P5 (We <3 Making Things!)
; M72 P1  ( Play Ta-Da song )
; M137 (build end notification)
