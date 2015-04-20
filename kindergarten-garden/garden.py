pd = {'V':'Violets',
      'R':'Radishes',
      'C':'Clover',
      'G':'Grass'
     }



class Garden:
    def __init__(self,g,students = 
                 ['Alice','Bob','Charlie','David','Eve','Fred','Ginny',
                  'Harriet','Ileana','Joseph','Kincaid','Larry']):
        self.students = sorted(students)
        # there's clearly no better way to do this. :)
        self.gl = g.split('\n')

    def plants(self,name):
        position = self.students.index(name)*2
        pl = self.gl[0][position:position+2] + self.gl[1][position:position+2]
        print(pl)
        plantList = []
        for p in pl: 
            plantList.append(pd[p])
        return plantList
