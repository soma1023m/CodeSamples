"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const CricketCoach_1 = require("./CricketCoach");
const GolfCoach_1 = require("./GolfCoach");
let cricketCoach = new CricketCoach_1.CricketCoach();
let golfCoach = new GolfCoach_1.GolfCoach();
;
let coach = [];
coach.push(cricketCoach);
coach.push(golfCoach);
for (let ch of coach) {
    console.log(ch.getDailyWorkOut());
}
