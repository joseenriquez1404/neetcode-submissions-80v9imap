class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ast = []
        for a in asteroids:
            alive = True

            while alive and ast and ast[-1] > 0 and a < 0:
                if ast[-1] < -a:
                    ast.pop()
                    continue
                elif ast[-1] == -a:
                    ast.pop()
                alive = False

            if alive:
                ast.append(a)
                    
        return ast

            
            
        
"""
El valor absoluto representa el tamaño y el signo su dirección

Condiciones:
- Siempre explota el más pequeñp
- Si son del mismo tamaño ambos explotan
- Si tienen el mismo signo nunca se van a encontrar

"""