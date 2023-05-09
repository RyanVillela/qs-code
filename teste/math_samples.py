class MathSamples:

    @staticmethod
    def fibomacci(n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return MathSamples.fibomacci(n - 1) + MathSamples.fibomacci(n - 2)
    
    