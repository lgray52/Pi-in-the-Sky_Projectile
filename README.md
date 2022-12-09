# Pi in the Sky Projectile
Lucy Gray Pi in the Sky Project Engineering 4


## Table of Contents
* [Planning](https://github.com/lgray52/Pi-in-the-Sky_Projectile#planning)
* [CAD](https://github.com/lgray52/Pi-in-the-Sky_Projectile#cad)
* [Code](https://github.com/lgray52/Pi-in-the-Sky_Projectile#code)

### Planning

The projectile will be launched from a [trebuchet](https://github.com/lgray52/CapstoneProject), so it needs high survivability. The goal is for Mr. Manning to be able to use the projectile to demonstrate projectile motion in his physics classes, so it also needs to be able to take measurements while it is in the air and with a high degree of accuracy. It also needs to weigh a maximum of 6.4oz or 181.44g because of the counterweight limit of the trebuchet, and ideally would be no wider than a standard-sized tennis ball, with a diameter of 6.86cm, to fit through the trebuchet's guide chute. 

<b> Preliminary Exterior Diagram </b>

<img src="images/projectile_sketch1.PNG" height="400">

<b> Preliminary Interior Diagram </b>

<img src="images/projectile_sketch2.PNG" height="400">

I still have some different ideas about how different aspects of the project will work. The main concern is survivability, and hopefully, I will be able to use a squishy 3D-printed material to minimize damage to the shell on impact. However, having an exterior that squishes might create difficulties with the wiring and circuit boards as it could damage interior circuitry. Suspending the electrics with respect to each, for example by having springs between them, could potentially protect from this damage. Depending on the level of squish, padding between different elements might be sufficient. 

<b> Problems and Solutions Brainstorming </b>

<img src="images/problems_brainstorm.PNG" height="400">


<b> Code Block Diagram </b>

<img src="images/code_diagram.PNG" height="400">

<b> Safety </b>

The projectile will experience high impact speeds, so it's important it doesn't smash into a million pieces on impact. In order to ensure this, controlled tests will be conducted by dropping/throwing it from heights and making sure the shell is thick enough not to break. The use of squishy material will also help this. The rest of the safety concerns are all trebuchet launch related - people will need to stand away from the swinging arm. 

<b> Materials </b>

I expect this project will require:

* Raspberry Pi Pico (1x)
* Altimeter (x1)
* Gyroscope (x1)
* 3D-printer material (enough for a 6.86cm diameter sphere of probably about 2.5mm thickness)
* Screws for putting the shell together
* Custom soldered circuit boards to mount electronics on

<b> Schedule </b>

* Deadline: April 1
  * CAD done by end of January
  * Code done by middle of February
  * All prints and circuit boards done by end of 1st week of March
  * Assembly and durability testing throughout March
  * Finished by April 1
* Iteration and fixes

## CAD

The primary challenge is to fit all of the electrical components into a sphere the size of a tennis ball and keep everything under the 181g weight limit while designing it to be structurally sound enough to survive repeated impacts. In the design process, I decided to make a dual-layer design with squishy TPU on the outside and rigid PLA on the inside. This way, the impact stress will be absorbed by the outer layer while the electronic components on the inside will not be squished or smashed against one another.

## Code
