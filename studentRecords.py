class StudentFileReader:
    def __init__(self, _inputSrc):
        self._inputSrc = _inputSrc
        self._inputFile = None


    def open(self):
        self._inputFile = open(self._inputSrc, "r")

    def close(self):
        self._inputFile.close()
        self._inputFile = None

    def fetchAll(self):
        theRecords = []
        student = self.fetchRecord()
        while student != None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords

    def fetchRecord(self):
        line = self._inputFile.readline()
        if line == "" :
            return None
        
        
        idNum = int(line)
        firstName = self._inputFile.readline().rstrip()
        lastName = self._inputFile.readline().rstrip()
        classCode = int( self._inputFile.readline().rstrip() )
        gpa = float(self._inputFile.readline())
        student = StudentRecord(idNum, firstName, lastName, classCode, gpa)
        
        return student

class StudentRecord:
    def __init__( self, idNum, firstName, lastName, classCode, gpa ):
        self.idNum = idNum
        self.firstName = firstName
        self.lastName = lastName
        self.classCode = classCode
        self.gpa = gpa
    
      
s = StudentFileReader("studentRecord.txt")
s.open()

records  = s.fetchAll()

for r in records:
    print(f"The id number is {r.idNum}")
    print(f"The first Name is {r.firstName}")
    print(f"The last name is {r.lastName}")
    print(f"The class code is {r.classCode}")
    print(f"The gpa is {r.gpa}")


