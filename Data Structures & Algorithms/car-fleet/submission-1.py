class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        count = 0
        fleet = 0

        for pos, spd in cars:
            curfleet = (target - pos) / spd

            if curfleet > fleet:
                count += 1
                fleet = curfleet

        return count
            
                