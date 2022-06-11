import { Coach } from "./Coach";
import { CricketCoach } from "./CricketCoach";
import { GolfCoach } from "./GolfCoach";


let cricketCoach= new CricketCoach();

let golfCoach= new GolfCoach();;

let coach:Coach[]=[];

coach.push(cricketCoach);
coach.push(golfCoach);

for(let ch of coach ){
    console.log(ch.getDailyWorkOut());
}
    