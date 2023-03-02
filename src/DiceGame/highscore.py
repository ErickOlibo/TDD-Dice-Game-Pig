class HighScore:
    
    def __init__(self, name, streak, overall_points):
        self._name = name
        self._streak = streak
        self._overallpoints = overall_points

      
    def add_streak(self, point):
        self._streak += point

    def add_overallpoints(self, value):
        self._overallpoints += value

    