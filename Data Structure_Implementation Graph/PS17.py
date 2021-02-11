import os 
#made this function so that we need not comment all prints
#just comment the print statement here so that no logs are printed
def Log(logString):

    #print(logString)
    return

class CorporateNetwork:

    DirectorCompany=[[],[]] # list containing companies and directors
    Edges=[] # matrix of edges/ associations
    

    # The init method or constructor  
    def __init__(self):  
        #delete outputfile if already exists
        try:
            os.remove(OUTPUT_FILE)
        except OSError as oserr:
            #if file doesnt exist
            Log(str(oserr))
         
    #_________________________________________________________
    def addCompany(self, company):
       
     
        #handle the case if the company information came more than once
        if company in self.DirectorCompany[0]:
            Log(company + " company already present") 
        else: 
            self.DirectorCompany[0].append(company)
        
        # add one more row for the new company in edges matrix
        # by appending a new rowlist with all default value of '0' 
        # to all the director columns in matrix

        tempRow = []

        #update default value only if there are already values in director 
        # column else append empty list
        if len(self.Edges) > 0:
            for i in range(len(self.Edges[0])):
                tempRow.append(0)
        Log(tempRow)
        self.Edges.append(tempRow)

        return self.DirectorCompany[0].index(company)
    #_________________________________________________________
    def addDirector(self, director):

        #check if already present if not add to DirectorCompany list
        if director in self.DirectorCompany[1]:
            Log(director + " director already present")
        else:
            self.DirectorCompany[1].append(director)

            # if new add the new director column to edges matrix also
            # add one more column by appending default value of '0' 
            # to all the company rows in matrix
            for i in range(len(self.Edges)):
                self.Edges[i].append(0)

        Log(director)
        return self.DirectorCompany[1].index(director)

    #_________________________________________________________
    def addAssociation(self, iCompany, iDirector):
        Log("add association")  
        self.Edges[iCompany][iDirector] = 1
        
    #_________________________________________________________
    def readCompanyDirfile(self, fileName):

        try:
            # Opening a file for reading
            inFile = open(fileName,"r")  
            Log("in File opened")
        except IOError as ioe:

            #handle if file is not present
            outText = "--------Input File '"'inputPS17.txt'"' Not Present----------------------------\n\n"
            objCN.writeOutputToFile(OUTPUT_FILE,outText)
            Log(ioe)
            return 0
        else:
            #read file
            try:
                contentList = inFile.readlines()

                #handle if file is empty
                if 0 == len(contentList):                    
                    outText = "--------Input File '"'inputPS17.txt'"' Empty----------------------------\n\n"
                    objCN.writeOutputToFile(OUTPUT_FILE,outText)
                    return 0
                
                lineCounter = 1
                for eachLine in contentList:
                    
                    if 0 == len(eachLine.strip()):
                        outText = "--------Parsing Input File '"'inputPS17.txt'"' ---------------------------\n\n"
                        outText = outText + "Invalid Entry at line " + str(lineCounter) +"\n"
                        outText = outText + "Format of input - Company Name / Director Name / Director Name / ... \n"
                        objCN.writeOutputToFile(OUTPUT_FILE,outText)
                        return 0

                    #line in format "companyname / direct1 / director 2"
                    Log("Line :- " + eachLine.rstrip())
                    companyInfo = eachLine.split('/')


                    #the list should contain 1 company name and atleast one director
                    if 1 == len(companyInfo) :
                        outText = "--------Parsing Input File '"'inputPS17.txt'"' ---------------------------\n\n"
                        outText = outText + "Invalid Entry at line " + str(lineCounter) + "\n"
                        outText = outText + "Format of input - Company Name / Director Name / Director Name / ... \n"
                        objCN.writeOutputToFile(OUTPUT_FILE,outText)
                        return 0

                    #first element is company name , if space or invalid string
                    if 0 == len(companyInfo[0].strip()):
                        outText = "--------Parsing Input File '"'inputPS17.txt'"' ---------------------------\n\n"
                        outText = outText + "Invalid Entry at line " + str(lineCounter) + "\n"
                        outText = outText + "Format of input - Company Name / Director Name / Director Name / ... \n"
                        objCN.writeOutputToFile(OUTPUT_FILE,outText)
                        return 0

                    companyIndex = self.addCompany(companyInfo[0].strip())
                    
                    #iterating from pos 1 for directors
                    for eachDirector in companyInfo[1:]:

                        # if entry is space or newline
                        if 0 == len(eachDirector.strip()):
                            outText = "--------Parsing Input File '"'inputPS17.txt'"' ---------------------------\n\n"
                            outText = outText + "Invalid Entry at line " + str(lineCounter) + "\n"
                            outText = outText + "Format of input - Company Name / Director Name / Director Name / ... \n"
                            objCN.writeOutputToFile(OUTPUT_FILE,outText)
                            return 0

                        directorIndex = self.addDirector(eachDirector.strip())
                        self.addAssociation(companyIndex, directorIndex)
                    
                    #incrementing the line counter
                    lineCounter = lineCounter + 1
            finally:
                inFile.close()
        return 1
#_________________________________________________________
    def writeOutputToFile(self, fileName,strText):
        try:
            # Opening a file in append mode
            outFile = open(fileName,"a")  
            Log("out File opened")
        except IOError as ioe:
            Log(ioe)
        else:
            try:
                outFile.write(strText)
            finally:
                outFile.close()
#_________________________________________________________
    def displayAll(self):
        outText = "---------Function displayAll----------\n\n"
        outText = outText + "Total no. of Companies: " + str(len(self.DirectorCompany[0])) + "\n"
        outText = outText + "Total no. of Directors: " + str(len(self.DirectorCompany[1])) + "\n"
        
        if self.DirectorCompany[0]:
            outText = outText + "\nList of Companies: \n"
            for i in self.DirectorCompany[0]:
                outText = outText + i + "\n"
                
        if self.DirectorCompany[1]:
            outText = outText + "\nList of Directors: \n"
            for i in self.DirectorCompany[1]:
                outText = outText + i + "\n"
        
        outText = outText + "--------------------------------------------\n\n"
        objCN.writeOutputToFile(OUTPUT_FILE,outText)

#_________________________________________________________
    def listCompanies(self, director):
        #get the index of the Director from list, to extract the name of companies from edge matrix
        #if director not found log
        #if found traverse through the matrix, and get the list of companies and write to file
        companies = []

        try:
            indexDirector = self.DirectorCompany[1].index(director)
        except ValueError as ve:
            Log(director + str(ve) +"\n")
        else:
            #check if there is association with company for that particular director column 
            for i in range(len(self.Edges)):
                if 1 == self.Edges[i][indexDirector]:
                    companies.append(self.DirectorCompany[0][i]) 
        return companies

#_________________________________________________________
    def displayCompanies(self, director):
        outText = "---------Function displayCompanies----------\n"

        #get the index of the Director from list, to extract the name of companies from edge matrix
        #if director not found log
        #if found traverse through the matrix, and get the list of companies and write to file

        companies = self.listCompanies(director)

        outText = outText + "Director name:" + director + "\n"
        outText = outText + "List Of Companies:\n"
        if 0 == len(companies):
            outText = outText + "\n----ERROR----\n"
            outText = outText + director +" not found \n * case sensitive \n"
            outText = outText + "No companies exist \n"
        else:
            for item in companies:
                outText = outText + item +"\n"
        outText = outText + "--------------------------------------------\n\n"

        objCN.writeOutputToFile(OUTPUT_FILE,outText)
#_________________________________________________________
    def listDirectors(self, company):
        #get the index of the company from list, to extract the name of directors from edge matrix
        #if company not found log
        #if found traverse through the matrix, and get the list of directors and write to file
        directors = []
        try:
            indexCompany = self.DirectorCompany[0].index(company)
        except ValueError as ve:
            Log(company + str(ve) +"\n")
        else:
            directors = []
            #check if there is association with director in that particular company row 
            for i in range(len(self.Edges[indexCompany])):
                if 1 == self.Edges[indexCompany][i]:
                    directors.append(self.DirectorCompany[1][i]) 
        return directors

#_________________________________________________________
    def displayDirectors(self, company):
        outText = "---------Function displayDirectors----------\n"

        #get the index of the company from list, to extract the name of directors from edge matrix
        #if company not found log
        #if found traverse through the matrix, and get the list of directors and write to file
        directors = self.listDirectors(company)
 
        outText = outText + "Company name:" + company + "\n"
        outText = outText + "List Of Directors:\n"
        if 0 == len(directors):
            outText = outText + "\n----ERROR----\n"
            outText = outText + company +" not found \n * case sensitive \n"
            outText = outText + "No directors exist \n"
        else:
            for item in directors:
                outText = outText + item +"\n"
        outText = outText + "--------------------------------------------\n\n"

        objCN.writeOutputToFile(OUTPUT_FILE,outText)


#_________________________________________________________
    def findCommonDirector(self, companyA, companyB):
        outText = "---------Function findCommonDirector--------\n"
        common_director = []           
        try:                
            CompanyA_index = self.DirectorCompany[0].index(companyA)
            CompanyB_index = self.DirectorCompany[0].index(companyB)
            
            for i in range(len(self.Edges[0])):
                is_common = self.Edges[CompanyA_index][i]*self.Edges[CompanyB_index][i]
                if is_common:
                    common_director.append(self.DirectorCompany[1][i])
                    
            outText = outText + "Company A:" + companyA + "\n"
            outText = outText + "Company B:" + companyB + "\n"
            outText = outText + "Related:" 
            if common_director:       
                outText = outText + "Yes, " + (', ').join(common_director) + "\n"
                 
            else:
                outText = outText + "No"  + "\n"
            
            outText = outText+ "--------------------------------------------\n\n"
            objCN.writeOutputToFile(OUTPUT_FILE,outText)

        except Exception as e:
           Log ("Exception" +str(e))
        finally:
            Log("Unable to check A and B are related to each other through a findCommonDirector")

#_________________________________________________________
    def traverseMatrix(self, companyA, companyB,visited):
               

        #add the current company node to visited list
        visited.append(companyA)

        #find all directors of companyA
        directors = self.listDirectors(companyA)
        for eachDirector in directors:

            #if director already traversed do not do again.
            if eachDirector in visited:
                continue
            
            #add the current director node to visited list
            visited.append(eachDirector)

            #find all companies of each director
            companies = self.listCompanies(eachDirector)
            
            #remove the current company
            companies.remove(companyA)
            for eachCompany in companies:

                if companyB == eachCompany:
                    return 1
                #company already exists
                elif eachCompany in visited:
                    continue
                # elif (len(visited) == ( len(self.DirectorCompany[0]) + len(self.DirectorCompany[1]))):
                #     return 0
                else: 
                    self.traverseMatrix(eachCompany, companyB, visited)
        return 0
#_________________________________________________________
    def findRelatedCompany(self, companyA, companyB):
        outText = "---------Function findRelatedCompany--------\n"
         #list containing nodes that are already visited.
        visited = []

        isRelated = self.traverseMatrix(companyA, companyB, visited)

        outText = outText + "Company A:" + companyA + "\n"
        outText = outText + "Company B:" + companyB + "\n"

        if True == isRelated:
            outText = outText + "Related: Yes \n"         
        else:
            outText = outText + "Related: No \n"

        outText = outText + "--------------------------------------------\n\n"
        objCN.writeOutputToFile(OUTPUT_FILE,outText)
#_________________________________________________________
    def readPromptsfile(self, fileName):
            try:
                # Opening a file for reading
                inFile = open(fileName,"r")  
                Log("in File opened")
            except IOError as ioe:
                Log(ioe)
            else:
                #read file
                try:

                    promptList = inFile.readlines()
                    for eachLine in promptList:
                        Log("Line :- " + eachLine.rstrip())
                        functionArguments = eachLine.split(':')
                        
                        if 0 == len(functionArguments):
                            Log("Empty line skip")
                        else:
                            #select which function to be called
                            functionName = functionArguments[0].strip()

                            if(1 == len(functionArguments) and "DisplayAll" == functionName):
                                self.displayAll()

                            elif (2 == len(functionArguments) and "findCompany" == functionName):
                               self.displayCompanies(functionArguments[1].strip())

                            elif (2 == len(functionArguments) and "listDirectors" == functionName):
                                self.displayDirectors(functionArguments[1].strip())

                            elif (3 == len(functionArguments) and "CommonDirector" == functionName):
                                self.findCommonDirector(functionArguments[1].strip(), functionArguments[2].strip())

                            elif (3 == len(functionArguments) and "RelatedCompany" == functionName):
                                self.findRelatedCompany(functionArguments[1].strip(), functionArguments[2].strip())

                            else:
                                Log("Invalid Input")
 
                finally:
                    inFile.close()


INPUT_FILE="inputPS17.txt"
OUTPUT_FILE="outputPS17.txt"
PROMPTS_FILE="promptsPS17.txt"

objCN = CorporateNetwork() 

# if reading input file successfull execute commands
if (objCN.readCompanyDirfile(INPUT_FILE)):

    objCN.readPromptsfile(PROMPTS_FILE)


   







