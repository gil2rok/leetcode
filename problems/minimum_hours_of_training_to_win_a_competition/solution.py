class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        required_energy = 0
        required_exp = 0
        
        for e in energy:
            if initialEnergy + required_energy <= e:
                required_energy += e - (initialEnergy + required_energy) + 1
            initialEnergy -= e
            
        for e in experience:
            if initialExperience + required_exp <= e:
                required_exp += e - (initialExperience + required_exp) + 1
            initialExperience += e
       
        return required_energy + required_exp
            