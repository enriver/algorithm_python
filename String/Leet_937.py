# Reorder Data in Log Files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let=list()
        dig=list()
        
        for i in logs:
            if i.split()[1].isdigit():
                dig.append(i)
            else:
                let.append(i)
                
        let.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        
        return let+dig