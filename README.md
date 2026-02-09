The Design of my hackpad/macropad

<img width="866" height="583" alt="Hackpad_Assembled_Orthographic" src="https://github.com/user-attachments/assets/3032695c-6935-45ad-920d-888986f3886d" />

The CAD models of the top and bottom parts of the case

<img width="975" height="601" alt="Case" src="https://github.com/user-attachments/assets/4687990c-4c9f-4c54-8b5b-2cb8b04c4dce" />

This is the Schematic

<img width="813" height="387" alt="SCH" src="https://github.com/user-attachments/assets/c27b79bf-3afc-4d02-b230-ff715853deb1" />

This is the PCB

<img width="881" height="598" alt="PCB" src="https://github.com/user-attachments/assets/8becdaf8-2e5a-4248-bd6a-9c4ce29c6abf" />

3D Model w/ all parts of PCB

<img width="740" height="462" alt="PCB_3D" src="https://github.com/user-attachments/assets/0cfc10a0-fa29-48c5-b987-fa8d385b8cec" />

Bill of Materials (Also provided as a file in .csv format)

Item,Order Qty,Actual Usage
Seeed XIAO RP2040,1,1
MX Mechanical Switches,1 Pack (36),6
DSA Keycaps (1u),1 Pack (24),6
1N4148 Diodes,1 Pack (150),6
EC11 Rotary Encoder,1 Pack (6),1
"0.91"" OLED Display",1 Pack (5),1

----------------
The hackpad, or at least my customized version of it, contains 6 keys, a rotary encoder (knob), and a small OLED display. I plan to utilize this macropad for tasks including gaming, productivity shortcuts, and for general assist in tasks including school work, 3D modelling, and so on.
I chose this project as I wanted to challenge myself, especially since this is my first time designing a PCB, or at least my first successful PCB design. I found it very challenging through tasks like the PCB 3D model and including all the proper electronics when some required deep internet browsing. I am quite familiar with 3D modelling already, but I enjoy the process of being able to combine the new skill--designing PCBs--with my existing skills--like 3D modelling.
The way this macropad will work is through the XIAO RP2040's USB-C port, where the firmware will be flashed and each key will serve a task--like a shortcut to open Spotify--and the rotary encoder will serve as a volume control knob.

The images associated with this project are organized into different folders. Beginning to navigate the folders, you will see a "Case", "Case & PCB", and "PCB" folders, as well as this README page, and the Bill of Materials (BOM). Put simply, the "Case" folder contains a single STEP file, being of the 3D printed case itself. Inside the "PCB" folder, contains an image of the Schematic, PCB layout, a 3D generated model of the PCB, a STEP file model of the PCB itself, and another folder--containing all files necessary for ordering the PCB and for reopening the design on KiCad. Lastly, navigating on over to the "Case & PCB" folder, it contains 3 images--one of the fully assembled design but at an Orthographic view, while another image contains that same assembled design, but a top-down view, and the last image being an exploded view of the design. Alongside the images is another STEP file, and a f3z file (Fusion360 archived file), and both of these files contain the same fully assembled 3D model, just in different file formats (mentioned on Submission guidelines page)

The firmware/code file, named as "main.py", is a simple macropad setup for now, the keys are bind to buttons F13-F18, which are able to be bind using apps like AutoHotkey to control whatever I like. The code uses the rotary encoder knob to act as a simple volume control knob, and the OLED displays simple startup text for now--"Hackpad Ready"--and once volume is changed, it will momentarily display "Volume: XX" with XX being the volume on a 0-100 scale.

Thanks for checking out my macropad/hackpad!
