import { Shape } from "./Shape";
import { Circle } from "./Circle";
import { Rectangle } from "./Rectangle";
let myShape= new Shape(5,4);
console.log(myShape.getInfo())
let myCircle= new Circle(5,4,8);
console.log(myCircle.getInfo());
let myRect= new Rectangle(5,4,8,4);;
console.log(myRect.getInfo())