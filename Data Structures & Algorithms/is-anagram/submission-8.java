class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> gram = new HashMap<>();
        for (char c : s.toCharArray()){
            gram.merge(c, 1, Integer::sum);
        }
        for(char c: t.toCharArray()){
            if(!gram.containsKey(c)){
                return false;
            }
        gram.put(c, gram.get(c)-1);

        if(gram.get(c) == 0){
            gram.remove(c);
            }
        }
        return gram.isEmpty();
    }
}
