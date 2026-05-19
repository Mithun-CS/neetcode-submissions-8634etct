class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position,speed), reverse =True)
        fleet_times =[]
        for pos, spd in cars:
            time_to_target = (target-pos)/spd

            if not fleet_times or time_to_target > fleet_times[-1]:
                fleet_times.append(time_to_target)

        return len(fleet_times)        