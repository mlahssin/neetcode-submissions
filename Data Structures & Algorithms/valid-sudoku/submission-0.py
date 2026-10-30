class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        carre_hash_set = {}
        carre_col = 3

        carres = [{} for i in range(9)] 
        index = 0

        for x in range (9):
            hash_set_raw = {}
            hash_set_col = {}

            for y in range(9):
                index = (x // 3) * 3 + y // 3
                # print("index", index)
                raw_elt = board[x][y]
                col_elt = board[y][x]
                if raw_elt not in carres[index]:
                    carres[index][raw_elt] = 1
                else:
                    carres[index][raw_elt] += 1
                    
                
                if raw_elt not in hash_set_raw:
                    hash_set_raw[raw_elt] = 1
                else:
                    hash_set_raw[raw_elt] += 1
            
                if col_elt not in hash_set_col:
                    hash_set_col[col_elt] = 1
                else:
                    hash_set_col[col_elt] += 1
                
                if col_elt != "." and hash_set_col[col_elt] > 1:
                    print("cp")
                    return False

                if raw_elt != "." and hash_set_raw[raw_elt] > 1:
                    print("tp")
                    return False

                if raw_elt != "." and carres[index][raw_elt] > 1:
                    print(carres[index])
                    
                    print("zip")
                    return False
                
        
        return True
        

        
                

        
        
        