class Node():
    	def __init__(self, key = None, data = None):
            self.key = key
            self.data = data
            self.child_node = {}
		
class Trie():
	def __init__(self):
		self.head = Node()
		
	def insert(self, string):
		cur_node = self.head
		
		for chr in string:
			if chr not in cur_node.child_node.keys():	
            # 노드 순차적 검색하며 없으면 노드등록
				cur_node.child_node[chr] = Node(chr)	
			cur_node = cur_node.child_node[chr]		
            # 현재노드를 다음 문자의 노드로 변경
		cur_node.data = string					
        # 마지막 노드에는 문자열 전체 저장
		
		
	def search(self, string):
		cur_node = self.head
		
		for chr in string:
			if chr not in cur_node.child_node.keys():	
            # 문자가 노드에 없으면 찾지못함
				print("Not in char")
				return False
			cur_node = cur_node.child_node[chr]		
            # 현재노드를 다음문자로 변경하며 탐색
		if cur_node.data != None:
			print ("search result : " ,string)		
            # 마지막 노드인 경우. Data는 문자열을 가진다
			return True
		else:
			print("exist : ", string)			
            # 문자가 다 저장되어있으나 마지막이 아닌경우, data는 None이기 때문에 한번더 체크
			
			
			
t = Trie()
t.insert("hello")
t.insert("byebye")

t.search("airplane")
t.search("hell")
t.search("bye")