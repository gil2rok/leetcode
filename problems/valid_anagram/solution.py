class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ###### SOL 1 #####
        #O(|S| * |T|)
        '''
        for s_char in s:
            if s_char in t:
                t = t.replace(s_char, '', 1)
            else:
                return False
        
        if t == '':
            return True
        else:
            return False
        '''
        
        ##### SOL 2 #####
        # O( max(|S|, |T|) ) --> linear
        # initialize dicts
        s_dict = dict.fromkeys(s, 0) #O(|S|)
        t_dict = dict.fromkeys(t, 0) #O(|T|)
        
        # insert into dicts
        for s_char in s: # O(|S|)
            s_dict[s_char] += 1
            
        for t_char in t: #O(|T|)
            t_dict[t_char] += 1
        
        # extract and compare dicts
        for c in s_dict.keys(): # O(|S|)
            
            # check if c is in both strings s, t
            try:
                t_count = t_dict[c]
                s_count = s_dict[c]
            except:
                return False
            
            # check if c has the same count in both strings s, t
            if s_count == t_count:
                del t_dict[c] # remove entry from t_dict
            else:
                return False
        
        if len(t_dict) == 0:
            return True
        else:
            return False
        
        
        
        
        