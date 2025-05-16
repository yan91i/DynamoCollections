# Room-Finish-Schedule-Generator-Dynamo-Script
【Introduction】
Room Finish Schedule Generator is a solution designed for use in the Dynamo environment. The solution is designed to calculate and add the area of the room's floor, ceiling, and walls to the Room Schedule.  Doors and windows are identified as belonging to the wall and the area is deducted. The solution also contains functions to list finish material and wall orientation. The key node in the script is "Room Finish" from Clockwork package and several customized python node. Room Finish Schedule Generator is the most coherent solution besides Roombook released by Autodesk. 

【Use Background】 
When developing a semi-automatic Quantity-Take-Off Dynamo script, there are projects that need to divide the output results by room. We tested the Roombook and Buildingbook with related functionality, but the plugins took too long to compute and the output reports were too cumbersome. The development of this script can quickly output the relevant area of the room and output it to the Room Schedule, which paved the way for SA-QTO to add a search function by room.

【Upgrade in Future】
The aspect of the script that needs to be upgraded is the recognition of the curtain facade, curve wall, and stacked wall. In addition, if you want to automatically generate parameters in Room Schedule, you can refer to the discussion in the link: "https://forum.dynamobim.com/t/dynamo-for-batch-adding-shared-parameters-to-project/5888", there is a related Dynamo script that can convert Excel data into parameters in Schedule

【Miro Link of script development whole-process】https://miro.com/app/board/uXjVOYxs4WA=/?share_link_id=389106481788

![Room Finish Script V1 0_2022-04-28_03-24-18](https://user-images.githubusercontent.com/55901325/165857709-74523795-9efe-466b-8f14-1f025954c454.png)

【Software Environment】Dynamo 2.6 (Revit 2021)

【Revit Model Samples file】: "Room Finish Example.rvt" is example with completely set Room Schedule.
![image](https://user-images.githubusercontent.com/55901325/165858330-14a6420b-4699-46b2-bbb3-a6ad65e58a36.png)
![image](https://user-images.githubusercontent.com/55901325/165858395-eb3dcbc9-bb1a-4e80-9a3d-016cb9c726f3.png)

【Script Dependencies】Clockwork 

【Script Group Color Set】 Pink - Data Input;  Blue - Data Output;  Green - Data Operation

【Revit Schedule Pre-Set】

Step 1: Create Room Schedule in Revit

Step 2: Add "Name" to schedule fields, and create 28 new Project Parameters in "Text" type with name of 
"Floor Finish Area","Floor Finish Material",
"Ceiling Finish Area","Ceiling Finish Material",
"Wall 1 Area","Wall 1 Material","Wall 1 Orientation",
"Wall 2 Area","Wall 2 Material","Wall 2 Orientation"...
(create 8 sets of numbered wall parameters)
![image](https://user-images.githubusercontent.com/55901325/165413902-ebb0efe0-2116-4fd9-a246-210f4bd19ba5.png)
![image](https://user-images.githubusercontent.com/55901325/165414123-da2dd72f-35f3-45d0-9817-d4c5d7fc2340.png)![image](https://user-images.githubusercontent.com/55901325/165414155-40d8b4ae-5e57-45bc-af74-ec23e85ff397.png)

Step 3: Run the script
